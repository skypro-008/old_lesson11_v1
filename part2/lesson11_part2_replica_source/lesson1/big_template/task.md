# Большая шаблонизация

У вас есть код шаблонизации на Jinja2.
Нужно внимательно рассматривать контекст и добавлять недостающие теги и элементы Jinja2 в шаблон.
Отрендерить шаблон.

Список пропущенных тегов и элементов:
- {{
- %}
- if
- else
- endif
- {%

---
**ВАЖНО!**
Роут должен быть `/prizes`.
---

Данные:

```python
    prices = [1300, 400, 100]
    user = {
        "blocked": False
    }
    prize_name = "Flight Ticket"
```

Список пропущенных тегов и элементов:
- {{
- %}
- if
- else
- {%
- endif


HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% if user.blocked %}
You have been blocked at __ user.blocked_at }} for {{ user.unblock_period }}.
{% else %}
Choose your prize:
{% for p in prices __
<div class="card">
    <div class="prize">
        <div class="
      {% __ p > 1000 %}
        expensive_price
      {% elif p < 500 %}
        normal_price
      {% __ %}
        default_price
      {% endif %}">
            {{ prize_name }}
        </div>
    </div>
</div>
__ endfor %}
{% __ %}
</body>
</html>
```

---
**ВАЖНО!**
Если у вас ошибка и тест не проходит, но вы уверены, что сделали все корректно откройте HTML файл и нажмите `Ctrl + Alt + L`
для авто форматирования шаблонизированного HTML файла.
---
