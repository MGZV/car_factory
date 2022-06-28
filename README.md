# Автомобильный завод

---
Это приложение позволяет хранить стоимость деталей и рассчитать стоимость
автомобилей.

---

# Установка

Необходимо клонировать приложение. Создать виртуальное окружение.

Выполнить:
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # создать суперюзера
python manage.py runserver
```
Перейти в браузере по адресу
```
http://127.0.0.1:8000/
```
