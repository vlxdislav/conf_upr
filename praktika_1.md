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
