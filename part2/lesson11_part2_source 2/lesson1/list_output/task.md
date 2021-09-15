#  Вывод списка

Дан список пользователей в формате list словарей в Python.
Вам надо создать метод представления и шаблонизировать HTML верстку при помощи Jinja2 чтобы отрендерить этот шаблон и вывести этот список в заданном виде.

---
**ВАЖНО!**
Роут должен быть `/phones`.
---

Данные:
```python
    phones = [
        {
            "name": "Ivan",
            "mail": "ivan@mail.ru",
            "phone": "89991234567"
        },
        {
            "name": "Maxim",
            "mail": "maxim@mail.ru",
            "phone": "89991234567"
        },
        {
            "name": "Peter",
            "mail": "maxim@mail.ru",
            "phone": "89991234567"
        }
    ]
```

HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Title</title>
</head>
<body>
<ul>
   <li>Ivan</li>
   <li>ivan@mail.ru</li>
   <li>89991234567</li>
</ul>
<ul>
   <li>Maxim</li>
   <li>maxim@mail.ru</li>
   <li>89991234567</li>
</ul>
<ul>
   <li>Peter</li>
   <li>maxim@mail.ru</li>
   <li>89991234567</li>
</ul>
</body>
</html>
```

---
**ВАЖНО!**
Если у вас ошибка и тест не проходит, 
но вы уверены, что сделали все корректно 
откройте HTML файл и нажмите `Ctrl + Alt + L` 
для авто форматирования шаблонизированного 
HTML файла.
---
