### Задача 1
Реализовать с помощью математического языка LaTeX нижеприведенную формулу:
Прислать код на LaTeX и картинку-результат, где, помимо формулы, будет указано ФИО студента.

```bash
\textbf{ФИО: Прилепский Владислав Валерьевич}
\int_x^\infty \frac{dt}{t(t^2 - 1) \log t} = \int_x^\infty \frac{1}{t \log t}\left( \sum_m t^{-2m} \right) dt = \sum_m \int_x^\infty \frac{t^{-2m}}{t \log t} dt \overset{u = t^{-2m}}{=} -\sum_m \mathrm{li}(x^{-2m})
```
![Снимок экрана 2024-11-22 в 14 42 39](https://github.com/user-attachments/assets/0cd04f08-dbf0-429f-8c9f-cb49f356c74d)

### Задача 2
На языке PlantUML реализовать диаграмму на рисунке ниже. Прислать текст на PlantUML и картинку-результат, в которой ФИО студента заменены Вашими собственными. Обратите внимание на оформление, желательно придерживаться именно его, то есть без стандартного желтого цвета и проч. Чтобы много не писать используйте псевдонимы с помощью ключевого слова "as".
```bash
@startuml
skinparam lifelineStrategy nosolid
actor "Студент Прилепский В.В" as S
database Piazza as P
actor Преподаватель as T

T -> P : Публикация задачи
activate P
P --> T : Задача опубликована
deactivate P
...
S -> P : Поиск задач
activate P
P --> S : Получение задачи
deactivate P
...
S -> P : Публикация решения
activate P
P --> S : Решение опубликовано
deactivate P
...
T -> P : Поиск решений
activate P
P --> T : Решение найдено
T -> P : Публикация оценки
P --> T : Оценка опубликована
deactivate P
...
S -> P : Проверка оценки
activate P
P --> S : Оценка получена
deactivate P
@enduml
```
![Снимок экрана 2024-11-22 в 14 47 33](https://github.com/user-attachments/assets/b63e96d0-ef98-4010-8270-8cb4d0f23f2e)

### Задача 3

Описать какой-либо алгоритм сортировки с помощью noweb. Язык реализации не важен. Прислать nw-файл, pdf-файл и файл с исходным кодом. В начале pdf-файла должно быть указано ваше авторство. Добавьте, например, где-то в своем тексте сноску: \footnote{Разработал Фамилия И.О.) Дополнительное задание: сравните "грамотное программирование" с Jupyter-блокнотами (см.
https://github.com/norvig/pytudes/blob/master/ipynb/BASIC.ipynb), опишите сходные черты, различия, перспективы того и другого.

nw файл (sorting_algorithm.nw):
```bash
\documentclass{article}
\usepackage{amsmath}
\begin{document}

\title{Сортировка пузырьком}
\author{Прилепский Владислав Валерьевич}
\date{\today}
\maketitle

\section*{Описание}
Алгоритм сортировки пузырьком состоит из многократного прохода по списку, во время которого соседние элементы сравниваются и меняются местами, если они стоят в неправильном порядке. Процесс продолжается до тех пор, пока список не будет полностью отсортирован.

\section*{Исходный код}
\begin{verbatim}
<<*>>=
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
@
\end{verbatim}

\footnote{Разработал Прилепский Владислав Валерьевич.}

\end{document}
```

исходный код:
```bash
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Проход по массиву, уменьшая зону проверки на каждом шаге
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
pdf-файл:
[code2pdf_674084bca0a59.pdf](https://github.com/user-attachments/files/17870833/code2pdf_674084bca0a59.pdf)








