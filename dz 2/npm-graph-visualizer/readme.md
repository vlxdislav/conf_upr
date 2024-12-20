 # npm-graph-visualizer

Инструмент командной строки для визуализации зависимостей npm-пакетов с использованием Graphviz.


## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/yourusername/npm-graph-visualizer.git
   cd npm-graph-visualizer
	2	Установите зависимости:  npm install  
	3	Установите Graphviz:
	•	macOS: brew install graphviz  
	•	Ubuntu: sudo apt-get install graphviz  
	•	Windows: Скачайте и установите с Graphviz Download
Использование
Для визуализации зависимостей npm-пакета выполните следующую команду:

node index.js <graphvizPath> <packageName> <outputFilePath> <maxDepth>
	•	<graphvizPath>: Путь к исполняемому файлу Graphviz (необязательно, если Graphviz находится в вашем PATH).
	•	<packageName>: Имя анализируемого npm-пакета.
	•	<outputFilePath>: Путь к файлу, в который будет сохранен код Graphviz.
	•	<maxDepth>: Максимальная глубина анализа зависимостей.
Пример:

node index.js /usr/local/bin/dot express output.dot 2
Функции
	•	Визуализация зависимостей npm-пакетов.
	•	Поддержка транзитивных зависимостей.
	•	Генерация кода Graphviz.
	•	Автоматическое создание PNG-изображения из кода Graphviz.
Пример
Для следующего кода Graphviz в output.dot:

digraph G {
  "express";
  "express" -> "accepts";
  "express" -> "array-flatten";
}
Выполнение команды:

dot -Tpng output.dot -o output.png
Создаст изображение output.png, которое визуализирует зависимости.
Тестирование
Для запуска тестов используйте следующую команду:

npm test
