import os
import zipfile
import argparse

def extract_virtual_fs(archive_path):
    temp_fs_path = '/tmp/virtual_fs'
    if os.path.exists(temp_fs_path):
        os.system(f'rm -rf {temp_fs_path}')  # Очистка старого содержимого
    os.makedirs(temp_fs_path, exist_ok=True)  # Создание нового каталога
    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(temp_fs_path)  # Извлечение файлов
    else:
        # Если это не архив, просто копируем файл
        os.system(f'cp {archive_path} {temp_fs_path}')
    os.chdir(temp_fs_path)  # Меняем текущую директорию на временную файловую систему

def ls_command():
    try:
        items = os.listdir(os.getcwd())
        return '\n'.join(items) if items else ''
    except Exception as e:
        return f"ls: {e}"

def cd_command(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        return f"cd: no such file or directory: {path}"
    except NotADirectoryError:
        return f"cd: not a directory: {path}"
    return ""

def tail_command(filename, lines=10):
    try:
        with open(filename, 'r') as file:
            content = file.readlines()
            # Вывод последних строк
            return ''.join(content[-lines:]) if len(content) >= lines else ''.join(content)
    except FileNotFoundError:
        return f"tail: cannot open '{filename}' for reading: No such file"
    except Exception as e:
        return f"tail: {e}"


def uname_command():
    return os.uname().sysname

def echo_command(*args):
    return ' '.join(args)

def execute_script(script_path):
    if not os.path.exists(script_path):
        print(f"Error: Script file '{script_path}' not found.")  # Вывод ошибки, если скрипт не найден
        return
    try:
        with open(script_path, 'r') as script:
            commands = script.readlines()
        for command in commands:
            command = command.strip()
            if command:
                print(process_command(command))
    except Exception as e:
        print(f"Error reading script '{script_path}': {e}")

def process_command(input_command):
    args = input_command.split()
    if not args:
        return ""

    command = args[0]
    if command == 'ls':
        return ls_command()
    elif command == 'cd':
        if len(args) > 1:
            return cd_command(args[1])
        return "cd: missing operand"
    elif command == 'exit':
        exit(0)
    elif command == 'tail':
        if len(args) > 1:
            try:
                # Проверка на параметр -n
                if args[1].startswith('-n'):
                    lines = int(args[2])  # Читаем количество строк
                    filename = args[3]  # Читаем имя файла
                    return tail_command(filename, lines)
                else:
                    filename = args[1]
                    return tail_command(filename, 10)  # По умолчанию 10 строк
            except (IndexError, ValueError):
                return "tail: invalid arguments"
        return "tail: missing file operand"
    elif command == 'uname':
        return uname_command()
    elif command == 'echo':
        return echo_command(*args[1:])
    else:
        return f"Unknown command: {command}"

def main():
    parser = argparse.ArgumentParser(description="Shell Emulator")
    parser.add_argument('--user', required=True, help="User name for prompt")
    parser.add_argument('--host', required=True, help="Host name for prompt")
    parser.add_argument('--vfs', required=True, help="Path to the virtual file system archive (ZIP)")
    parser.add_argument('--start-script', help="Path to the startup script", default=None)

    args = parser.parse_args()

    extract_virtual_fs(args.vfs)  # Извлекаем файловую систему

    if args.start_script:
        execute_script(args.start_script)  # Выполняем стартовый скрипт, если он указан

    while True:
        try:
            prompt = f"{args.user}@{args.host}:{os.getcwd()}$ "
            user_input = input(prompt)  # Ввод пользователя
            output = process_command(user_input)  # Обработка команды
            if output:
                print(output)  # Печать вывода команды
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except EOFError:
            print("Exiting.")
            break

if __name__ == '__main__':
    main()
