# Почти готово

У вас есть:
- HTML верстка шаблонизированный при помощи jinja2.
- Готовый роут /books с пропущенным return

Вам надо:
1. Установить Flask
1. Вставить пропущенный стейтмент после ключевого слова return (отрендерить шаблон и передать данные из файла books.json)
1. Посмотреть на результат в браузере по роуту /books

python view method:
```python
@app.route('/books')
def books():
    with open('books.json') as f:
        data = json.load(f)
        return ???
```

html (скопировать БЕЗ изменений)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% for book in books %}
<ul>
    <li>Title: {{ book.title }}</li>
    <li>Year: {{ book.year }}</li>
    <li>Author: {{ book.author }}</li>
</ul>
{% endfor %}
</body>
</html>
```

Данные (файл books.json):
```json
[
    {
        "title":"Harry Potter",
        "year": 1996,
        "author": "Джоан Роалинг"
    },
    {
        "title":"Король Артур",
        "year": 1485,
        "author": "Томас Мэлори"
    }
]
```

---
**ВАЖНО!**
Если у вас ошибка и тест не проходит,
но вы уверены, что сделали все корректно
откройте HTML файл и нажмите `Ctrl + Alt + L`
для авто форматирования шаблонизированного
HTML файла.
---
