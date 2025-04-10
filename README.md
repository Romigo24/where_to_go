# Куда пойти - глазами Артёма (бэкенд)

Бэкенд для сайта о самых интересных местах Москвы, сайт доступен по адресу: [https://romigo939.pythonanywhere.com](https://romigo939.pythonanywhere.com)

### Описание 
Этот проект является бэкенд-частью для фронтенда, который отображает Карту москвы с с метками интересных мест. Бэкенд предоставляет данные о локациях в формате JSON, которые используются фронтендом для отображения информации на карте.

### Как запустить проект
1. Установите зависимости:

Убедитесь, что у вас установлен Python 3.9 или выше. Затем установите зависимости командой:
```
pip install -r requirements.txt
```

2. Настройте переменные окружения:

В корневой директоррии проекта создайте файл .env в котором будут прописаны переменные окружения:
```
# Ключ для защиты данных Django (обязательный, должен быть уникальным)
SECRET_KEY=your_secret_key_here

# Режим разработки: True для разработки, False для продакшена
DEBUG=True

# Допустимые адреса для доступа к сайту (через запятую, например: 'localhost,127.0.0.1')  
ALLOWED_HOSTS=your_host_here  

# Ссылка для подключения к БД (пример для SQLite)  
DATABASE_URL=sqlite:///db.sqlite3
```

3. Применените миграции командой:

```
python manage.py migrate
```
4. Создайте суперпользователя командой:
```
python manage.py createsuperuser
```
5. Запустите сервер разработки командой:
```
python manage.py runserver
```
Сервер будет доступен по адресу [ http://127.0.0.1:8000/]( http://127.0.0.1:8000/)

6. Загрузите тестовые данные: Используйте админку Django для добавления локаций и изображений. Перейдите по адресу [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) и войдите с учётными данными суперпользователя.
