### Задача 1
Написать программу на Питоне, которая транслирует граф зависимостей civgraph в makefile в духе примера выше. Для мало знакомых с Питоном используется упрощенный вариант civgraph: civgraph.json.

Пример:

> make mathematics
mining
bronze_working
sailing
astrology
celestial_navigation
pottery
writing
code_of_laws
foreign_trade
currency
irrigation
masonry
early_empire
mysticism
drama_poetry
mathematics

```bash
import json

# Загрузка графа из JSON-файла
def load_graph(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Генерация Makefile на основе графа зависимостей
def create_makefile(graph, target):
    processed = set()  # Для отслеживания обработанных технологий
    tasks = []

    # Вспомогательная функция для обработки зависимостей
    def process(technology):
        if technology not in processed:
            processed.add(technology)
            for prerequisite in graph.get(technology, []):
                process(prerequisite)
            tasks.append(technology)

    # Запуск обработки с целевой технологии
    process(target)

    # Вывод списка технологий в порядке выполнения
    for tech in tasks:
        print(tech)

if __name__ == "__main__":
    # Загружаем граф зависимостей
    graph = load_graph("civgraph.json")

    # Получаем целевую технологию от пользователя
    target_tech = input("Введите целевую технологию: ")

    # Создаем Makefile
    create_makefile(graph, target_tech)
```
Вывод
```bash
> python3 civ_to_make.py
Enter the target technology: mathematics
mining
bronze_working
sailing
astrology
celestial_navigation
pottery
writing
code_of_laws
currency
irrigation
masonry
early_empire
mysticism
drama_poetry
mathematics
```

### Задача 2
Реализовать вариант трансляции, при котором повторный запуск make не выводит для civgraph на экран уже выполненные "задачи".

```bash
import json

# Загрузка графа из JSON-файла
def load_graph(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Генерация Makefile на основе графа зависимостей
def create_makefile(graph, target, output_file="Makefile"):
    visited = set()
    rules = []

    # Рекурсивная функция для генерации правил
    def generate_rules(technology):
        if technology in visited:
            return
        visited.add(technology)

        dependencies = graph.get(technology, [])
        for prerequisite in dependencies:
            generate_rules(prerequisite)

        # Формируем правило для текущей технологии
        rule = f"{technology}.done: {' '.join([f'{dep}.done' for dep in dependencies])}\n"
        rule += f"\t@echo \"Processing {technology}\" && touch {technology}.done\n"
        rules.append(rule)

    # Генерируем правила, начиная с целевой технологии
    generate_rules(target)

    # Записываем правила в Makefile
    with open(output_file, "w") as file:
        file.write("all: " + f"{target}.done\n\n")
        file.write("\n".join(rules))
    print(f"Makefile создан в файле {output_file}")

if __name__ == "__main__":
    # Загружаем граф зависимостей
    graph = load_graph("civgraph.json")

    # Получаем целевую технологию от пользователя
    target_tech = input("Введите целевую технологию: ")

    # Создаем Makefile
    create_makefile(graph, target_tech)
```

### Задача 3
Добавить цель clean, не забыв и про "животное".

```bash
import json
import os

COMPLETED_TASKS_FILE = "completed_tasks.txt"

def load_completed_tasks():
    if os.path.exists(COMPLETED_TASKS_FILE):
        with open(COMPLETED_TASKS_FILE, 'r') as f:
            return set(f.read().splitlines())
    return set()

def save_completed_tasks(completed_tasks):
    with open(COMPLETED_TASKS_FILE, 'w') as f:
        f.write('\n'.join(completed_tasks))

def clean():
    if os.path.exists(COMPLETED_TASKS_FILE):
        os.remove(COMPLETED_TASKS_FILE)
        print("Cleaned completed tasks.")

def generate_makefile(civgraph, target):
    visited = set()
    result = []
    completed_tasks = load_completed_tasks()

    def visit(tech):
        if tech in visited or tech in completed_tasks:
            return
        visited.add(tech)
        for dep in civgraph.get(tech, []):
            visit(dep)
        result.append(tech)

    visit(target)

    for task in result:
        if task not in completed_tasks:
            print(task)
            completed_tasks.add(task)

    save_completed_tasks(completed_tasks)

if __name__ == '__main__':
    civgraph = load_civgraph('civgraph.json')
    action = input('Enter action (make/clean): ')

    if action == 'clean':
        clean()
    else:
        target = input('Enter the target technology: ')
        generate_makefile(civgraph, target)
```


### Задача 4
Написать makefile для следующего скрипта сборки:

gcc prog.c data.c -o prog
dir /B > files.lst
7z a distr.zip *.*

Вместо gcc можно использовать другой компилятор командной строки, но на вход ему должны подаваться два модуля: prog и data. Если используете не Windows, то исправьте вызовы команд на их эквиваленты из вашей ОС. В makefile должны быть, как минимум, следующие задачи: all, clean, archive. Обязательно покажите на примере, что уже сделанные подзадачи у вас не перестраиваются.
```bash


# Переменные
CC = gcc
CFLAGS = -Wall -O2
TARGET = prog
MODULES = prog.c data.c
ARCHIVE = distr.zip

# Задача по умолчанию
all: $(TARGET)

# Компиляция программы
$(TARGET): $(MODULES)
	$(CC) $(CFLAGS) -o $@ $^

# Генерация списка файлов
files.lst: 
	ls > files.lst  # Используйте "dir /B > files.lst" для Windows

# Создание архива
archive: $(TARGET) files.lst
	7z a $(ARCHIVE) *.*

# Очистка
clean:
	rm -f $(TARGET) files.lst $(ARCHIVE) # Используйте "del" для Windows

# Уточнение, какие задачи являются файлами
.PHONY: all clean archive
```
