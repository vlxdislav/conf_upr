## Задача 1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
```bash
pip show matplotlib

Name: matplotlib
Version: 3.7.2
Summary: Python plotting package
Home-page: https://matplotlib.org
Author: John D. Hunter, Michael Droettboom
Author-email: matplotlib-users@python.org
License: PSF
Location: /Users/prilepskyv/anaconda3/lib/python3.11/site-packages
Requires: contourpy, cycler, fonttools, kiwisolver, numpy, packaging, pillow, pyparsing, python-dateutil
Required-by: seaborn
```
Установка без использования pip, 
```bash
pip install git+https://github.com/matplotlib/matplotlib.git
cd matplotlib
python setup.py install
```
## Задача 2
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
```bash
>npm show express

express@4.21.0 | MIT | deps: 31 | versions: 279
Fast, unopinionated, minimalist web framework
http://expressjs.com/

keywords: express, framework, sinatra, web, http, rest, restful, router, app, api

dist
.tarball: https://registry.npmjs.org/express/-/express-4.21.0.tgz
.shasum: d57cb706d49623d4ac27833f1cbc466b668eb915
.integrity: sha512-VqcNGcj/Id5ZT1LZ/cfihi3ttTn+NJmkli2eZADigjq29qTlWi/hAQ43t/VLPq8+UX06FCEx3ByOYet6ZFblng==
.unpackedSize: 220.8 kB

dependencies:
accepts: ~1.3.8      cookie: 0.6.0        encodeurl: ~2.0.0    finalhandler: 1.3.1  methods: ~1.1.2      proxy-addr: ~2.0.7   safe-buffer: 5.2.1   type-is: ~1.6.18     
body-parser: 1.20.3  debug: 2.6.9         escape-html: ~1.0.3  fresh: 0.5.2         on-finished: 2.4.1   qs: 6.13.0           send: 0.19.0         utils-merge: 1.0.1   
content-type: ~1.0.4 depd: 2.0.0          etag: ~1.8.1         http-errors: 2.0.0   parseurl: ~1.3.3     range-parser: ~1.2.1 statuses: 2.0.1      vary: ~1.1.2         
(...and 7 more.)

maintainers:
- wesleytodd <wes@wesleytodd.com>
- dougwilson <doug@somethingdoug.com>
- linusu <linus@folkdatorn.se>
- sheplu <jean.burellier@gmail.com>
- blakeembrey <hello@blakeembrey.com>
- ulisesgascon <ulisesgascondev@gmail.com>
- mikeal <mikeal.rogers@gmail.com>

dist-tags:
latest: 4.21.0  next: 5.0.0     

published 3 weeks ago by wesleytodd <wes@wesleytodd.com>
```

Установка без npm
```bash
git clone https://github.com/expressjs/express.git
cd express
```
## Задача 3
Сформировать graphviz-код и получить изображения зависимостей matplotlib, express
```bash
pipdeptree --packages matplotlib --graph-output dot > matplotlib_deps.dot
```
![image](https://github.com/user-attachments/assets/7a2c4c7a-74d9-4ed3-acd3-734d63041cd8)



## Задача 4
Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.
```bash
include "globals.mzn";  % Подключение библиотеки глобальных ограничений
% Модель для задачи о счастливых билетах с уникальными цифрами

% Билет состоит из 6 цифр от 0 до 9
array[1..6] of var 0..9: digits;

% Условие: все цифры билета должны быть различными
constraint all_different(digits);

% Условие счастливого билета: сумма первых трех цифр равна сумме последних трех
constraint
  digits[1] + digits[2] + digits[3] = digits[4] + digits[5] + digits[6];

% Минимизируем сумму первых трех цифр
var int: sum_digits = digits[1] + digits[2] + digits[3];
solve minimize sum_digits;

output ["Digits: \(digits)\n", "Sum of first three digits: \(sum(digits[1..3]))\n", "Sum of last three digits: \(sum(digits[4..6]))\n"];

```

```bash

% Выводим решение
Running untitled_model.mzn
874msec

Digits: [8, 1, 0, 4, 3, 2]
Sum of first three digits: 9
Sum of last three digits: 9
----------
Digits: [6, 2, 0, 4, 3, 1]
Sum of first three digits: 8
Sum of last three digits: 8
----------
==========
Finished in 874msec.

];
```



