### Задача 1
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
```bash
local groupPrefix = "ИКБО-";
local groupYear = "20";
local groupCount = 24;

local generateGroups(count) = [
  groupPrefix + std.extVar("groupNumber") + "-" + groupYear for groupNumber in std.range(1, count)
];

local students = [
  { age: 19, group: "ИКБО-4-20", name: "Иванов И.И." },
  { age: 18, group: "ИКБО-5-20", name: "Петров П.П." },
  { age: 18, group: "ИКБО-5-20", name: "Сидоров С.С." },
  { age: 20, group: "ИКБО-6-20", name: "Алексеев А.А." } // четвертый студент
];

{
  groups: generateGroups(groupCount),
  students: students,
  subject: "Конфигурационное управление"
}

```

### Задача 2
Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
```bash
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сидоров С.С."
    },
    <добавьте ваши данные в качестве четвертого студента>
  ],
  "subject": "Конфигурационное управление"
} 
```

```bash
let Group = Text
let Student = { age : Natural, group : Group, name : Text }

let groupPrefix = "ИКБО-"
let groupYear = "20"
let groupCount = 24

let generateGroups : List Group =
      List.map (λ(i : Natural) → groupPrefix ++ Natural/show i ++ "-" ++ groupYear) (List.range 1 groupCount)

let students : List Student =
      [ { age = 19, group = "ИКБО-4-20", name = "Иванов И.И." }
      , { age = 18, group = "ИКБО-5-20", name = "Петров П.П." }
      , { age = 18, group = "ИКБО-5-20", name = "Сидоров С.С." }
      , { age = 20, group = "ИКБО-6-20", name = "Алексеев А.А." }  -- четвертый студент
      ]

let config =
      { groups = generateGroups
      , students = students
      , subject = "Конфигурационное управление"
      }

in  config


```

### Задача 3
Язык нулей и единиц.

10
100
11
101101
000

```bash
BNF = '''
E = 10 | 100 | 11 | 101101 | 000
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```

### Задача 4
Язык правильно расставленных скобок двух видов.

(({((()))}))
{}
{()}
()
{}

```bash
BNF = '''
E = "()" | "{}" | E E | "(" E ")" | "{" E "}"
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```

Задача 5
Язык выражений алгебры логики.
```bash
BNF = '''
E = "~" E | E "&" E | E "|" E | "(" E ")" | "x" | "y"
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
