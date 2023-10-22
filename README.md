Тестовый DRF проект

Задача - реализовать REST API сервис со следующими эндпоинтами:
<ul>
  <li>GET /city/ — получение всех городов из базы</li>
  <li>GET /city/city_id/street/ — получение всех улиц города</li>
  <li>POST /shop/ — создание магазина</li>
  <li>GET /shop/?street=&city=&open=0 - Фильтрация</li>
</ul>

<h2>Стек</h2>
<ul>
  <li>Django</li>
  <li>Djangorestframework</li>
  <li>PostgreSQL</li>
</ul>
</hr>

<h2>Установка</h2>
<code>pip install -r requirements.txt</code><br>
В файле .env вписываем данные для соединения с БД
<br><br>Запускаем сервер командой<br> <code>python manage.py runserver</code>
