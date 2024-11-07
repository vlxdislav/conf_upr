### Задача 1
На сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing-git/ (цвета могут отличаться, есть команды undo/redo) с помощью команд эмулятора git получить следующее состояние проекта (сливаем master с first, перебазируем second на master): см. картинку ниже. Прислать свою картинку.

![Снимок экрана 2024-11-07 в 16 51 05](https://github.com/user-attachments/assets/f36bd087-38a0-435a-8893-d90228b6275b)


### Задача 2
```bash
prilepskyv@mac Conf % mkdir my_project
prilepskyv@mac Conf % cd my_project
prilepskyv@mac my_project % git init
Initialized empty Git repository in /Users/prilepskyv/Desktop/conf/my_project/.git/
prilepskyv@mac my_project % git config --global user.name "coder1"
prilepskyv@mac my_project % git config --global user.email "coder1@example.com"
prilepskyv@mac my_project % echo "print('Hello, World!')" > prog.py
prilepskyv@mac my_project % git add prog.py
prilepskyv@mac my_project % git commit -m "Добавлен файл prog.py с Hello World"
[master (root-commit) 41a5434] Добавлен файл prog.py с Hello World
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py
prilepskyv@mac my_project % git status
On branch master
nothing to commit, working tree clean
prilepskyv@mac my_project % git log
commit 41a5434626a03f41c0ca8827a8fdc54100e57373 (HEAD -> master)
Author: coder1 <coder1@example.com>
Date:   Thu Nov 7 17:01:38 2024 +0300

    Добавлен файл prog.py с Hello World
```

### Задача 3
```
prilepskyv@mac my_project % mkdir server.git
prilepskyv@mac my_project % cd server.git
prilepskyv@mac server.git % git init --bare

Initialized empty Git repository in /Users/prilepskyv/Desktop/conf/my_project/server.git/
prilepskyv@mac server.git % cd /Users/prilepskyv/Desktop/conf/my_project

prilepskyv@mac my_project % git remote add server /Users/prilepskyv/Desktop/conf/my_project/server.git
prilepskyv@mac my_project % git push server master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 272 bytes | 272.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To /Users/prilepskyv/Desktop/conf/my_project/server.git
 * [new branch]      master -> master

prilepskyv@mac my_project % git remote -v
server	/Users/prilepskyv/Desktop/conf/my_project/server.git (fetch)
server	/Users/prilepskyv/Desktop/conf/my_project/server.git (push)

prilepskyv@mac my_project % mkdir my_project_coder2
prilepskyv@mac my_project % git clone /Users/prilepskyv/Desktop/conf/my_project/server.git
Cloning into 'server'...
done.

prilepskyv@mac my_project % git config user.name "coder2"
prilepskyv@mac my_project % git config user.email "coder2@example.com"

prilepskyv@mac my_project % echo "# Программа, которая выводит 'Hello, World!'" > readme.md
prilepskyv@mac my_project % git add readme.md

prilepskyv@mac my_project % git commit -m "Добавлен файл readme.md с описанием программы"
[master db107e0] Добавлен файл readme.md с описанием программы
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md
prilepskyv@mac my_project % git push server master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 396 bytes | 198.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To /Users/prilepskyv/Desktop/conf/my_project/server.git
   41a5434..db107e0  master -> master

prilepskyv@mac my_project % git pull server master
From /Users/prilepskyv/Desktop/conf/my_project/server
 * branch            master     -> FETCH_HEAD
Already up to date.
prilepskyv@mac my_project % echo "Автор: Coder1" >> readme.md
prilepskyv@mac my_project % git add readme.md
prilepskyv@mac my_project % git commit -m "Добавлена информация о Coder1 в разделах об авторах"
[master b724fed] Добавлена информация о Coder1 в разделах об авторах
 1 file changed, 1 insertion(+)
prilepskyv@mac my_project % git push server master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 419 bytes | 209.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To /Users/prilepskyv/Desktop/conf/my_project/server.git
   db107e0..b724fed  master -> master
prilepskyv@mac my_project % 

prilepskyv@mac my_project % cd my_project_coder2
prilepskyv@mac my_project_coder2 % git pull server master
From /Users/prilepskyv/Desktop/conf/my_project/server
 * branch            master     -> FETCH_HEAD
Already up to date.

prilepskyv@mac my_project_coder2 % cd -
~/Desktop/conf/my_project
prilepskyv@mac my_project % git add readme.md
prilepskyv@mac my_project % git commit -m "Исправленый конфликты в разделах об авторах" 
[master 926d600] Исправленый конфликты в разделах об авторах
 1 file changed, 1 insertion(+), 1 deletion(-)
prilepskyv@mac my_project % git push server master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 369 bytes | 369.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
To /Users/prilepskyv/Desktop/conf/my_project/server.git
   b724fed..926d600  master -> master
prilepskyv@mac my_project % git log   
commit 926d600a387176e7ea95f87e8d0a79ea2b04eb20 (HEAD -> master, server/master)
Author: coder2 <coder2@example.com>
Date:   Thu Nov 7 17:48:46 2024 +0300

    Исправленый конфликты в разделах об авторах

commit b724fedb5ac7f21fafd21b9abcf7dc5d85986927
Author: coder2 <coder2@example.com>
Date:   Thu Nov 7 17:43:28 2024 +0300

    Добавлена информация о Coder1 в разделах об авторах

commit db107e09e4075a1daad14e2895d315a6aaf28c14
Author: coder2 <coder2@example.com>
Date:   Thu Nov 7 17:35:01 2024 +0300

    Добавлен файл readme.md с описанием программы

commit 41a5434626a03f41c0ca8827a8fdc54100e57373
Author: coder1 <coder1@example.com>
Date:   Thu Nov 7 17:01:38 2024 +0300

    Добавлен файл prog.py с Hello World
```
### Задача 4
Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file- р". Идеальное решение не использовать иных сторонних команд и библиотек для работы с git.

```bash

```
