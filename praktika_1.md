# Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (понадобится grep).
## Код
```bash
grep '.*' /etc/passwd | cut -d: -f1 | sort
```

```bash
_amavisd
_analyticsd
_appinstalld
_appleevents
_applepay
_appowner
_appserver
_appstore
_ard
_assetcache
_astris
_atsserver
_avbdeviced
_calendar
_captiveagent
_ces
_clamav
_cmiodalassistants
_coreaudiod
_coremediaiod
_coreml
_ctkd
_cvmsroot
_cvs
_cyrus
_datadetectors
```

# Задача 2
Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:
## Код
```bash
awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 5
```

```bash
258 divert
255 #
253-254 #
240 pfsync
```
# Задача 3
Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):
## Код
```bash
#!/bin/bash

text=$*
length=${#text}

for i in $(seq 1 $((length + 2))); do
    line+="-"
done

echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"
```
```bash
./banner.sh "Hello, World"
+--------------+
| Hello, World |
+--------------+
```

# Задача 4
Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).
## Код
```bash
#!/bin/bash

file="$1"

id=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)

```
```bash
grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | grep -vE '\b(int|void|return|if|else|for|while|include|stdio)\b' | sort | uniq
apple
door
hi
mirea
phone
table
```

# Задача 5
Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).
## Код
```bash
#!/bin/bash

file=$1

chmod 755 "./$file"

sudo cp "$file" /usr/local/bin/
```

```bash
./task.sh banner.sh

ls /usr/local/bin
VBoxAudioTest	VBoxDTrace	VirtualBox	banner.sh	vboxwebsrv
VBoxAutostart	VBoxHeadless	VirtualBoxVM	code
VBoxBalloonCtrl	VBoxManage	apm		vbox-img
VBoxBugReport	VBoxVRDP	atom		vboximg-mount
```
# Задача 6
Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.
## Код
```bash
#!/bin/bash
# Проход по всем файлам с расширениями .c, .js, .py
for file in $(find . -type f \( -name "*.c" -o -name "*.js" -o -name "*.py" \)); do
    # Чтение первой строки файла
    first_line=$(head -n 1 "$file")
    
    # Проверка, начинается ли строка с комментария (для C, JS и Python)
    if [[ "$file" == *.c || "$file" == *.js ]]; then
        if [[ "$first_line" =~ ^(//|/\*) ]]; then
            echo "Файл $file содержит комментарий в первой строке."
        else
            echo "Файл $file не содержит комментарий в первой строке."
        fi
    elif [[ "$file" == *.py ]]; then
        if [[ "$first_line" =~ ^# ]]; then
            echo "Файл $file содержит комментарий в первой строке."
        else
            echo "Файл $file не содержит комментарий в первой строке."
        fi
    fi
done
```
Файл hi.c :
```bash
//комментарий
123
123
```

Файл hi.js :
```bash
//комментарий
123
123
```
Файл hi.py :
```bash
#комментарий 
123
123
```



```bash
./check_comments.sh
Файл ./hi.py содержит комментарий в первой строке.
Файл ./hi.c содержит комментарий в первой строке.
Файл ./hi.js содержит комментарий в первой строке.
```

# Задача 7
Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).
## Код
```bash
#!/bin/bash

# Путь для поиска
directory="$1"

if [[ -z "$directory" ]]; then
    echo "Использование: $0 <путь_к_каталогу>"
    exit 1
fi

# Находим дубликаты
find "$directory" -type f -exec shasum {} \; | sort | awk '{
    if ($1 in seen) {
        print $1 " " seen[$1] ", " $2
    } else {
        seen[$1] = $2
    }
}'
```

```bash
./find_duplicates.sh ~/Desktop/conf

487b6170c18fa66126f0865a3e4203254b984ce3 /Users/prilepskyv/Desktop/conf/hi.c, /Users/prilepskyv/Desktop/conf/hi copy.c
91f2c8f9b4a56e485b4bc6c16723f9faf5d7d9b9 /Users/prilepskyv/Desktop/conf/hello.c, /Users/prilepskyv/Desktop/conf/hello copy.c
```
# Задача 8
Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.

## Код 
```bash
#!/bin/bash

# Проверка наличия аргументов
if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <путь_к_каталогу> <расширение>"
    exit 1
fi

directory="$1"
extension="$2"

# Поиск файлов с заданным расширением
files=$(find "$directory" -type f -name "*.$extension")

# Проверка на наличие найденных файлов
if [ -z "$files" ]; then
    echo "Файлы с расширением .$extension не найдены в $directory."
    exit 1
fi

# Создание имени архива
archive_name="archive.tar.gz"

# Архивирование найденных файлов
tar -czf "$archive_name" -C "$directory" $(basename $files)

echo "Архив создан: $archive_name"

```

```bash
./archive_files.sh ~/Desktop/conf c 
Архив создан: archive.tar.gz
```

# Задача 9
Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.
## Код
```bash
#!/bin/bash

# Проверка наличия аргументов
if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <входной_файл> <выходной_файл>"
    exit 1
fi

input_file="$1"
output_file="$2"

# Замена 4 пробелов на символ табуляции и запись в выходной файл
sed 's/    /\t/g' "$input_file" > "$output_file"

echo "Заменено в файле $input_file и записано в $output_file."

```
```bash
./replace_spaces.sh input.txt output.txt
Заменено в файле input.txt и записано в output.txt.
```
intpu.txt
```bash
   //123
        //123
        //123
            //123
```
output.txt
```bash
	//123
		//123
		//123
			//123
```


# Задача 10
Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром.
## Код
```bash
#!/bin/bash

# Проверка наличия аргумента
if [ "$#" -ne 1 ]; then
    echo "Использование: $0 <путь_к_каталогу>"
    exit 1
fi

directory="$1"

# Проверка, существует ли директория
if [ ! -d "$directory" ]; then
    echo "Ошибка: Директория $directory не найдена."
    exit 1
fi

# Поиск и вывод пустых текстовых файлов
find "$directory" -type f -name "*.txt" -size 0 | while read -r file; do
    echo "$file"
done
```
```bash
./find_empty_files.sh ~/Desktop/conf 
/Users/prilepskyv/Desktop/conf/file.txt
```
