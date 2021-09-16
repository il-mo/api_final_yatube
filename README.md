### Описание:
API для работы с проектом Yatube.


### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/il-mo/api_final_yatube.git
```

```
cd yatube_api
```

2. Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

3. Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Выполнить миграции:

```
python manage.py migrate
```

5. Запустить проект:

```
python manage.py runserver
```

### Примеры запросов:
Пример POST-запроса с токеном user: добавление нового поста.

POST .../api/v1/posts/
```
{
    "text": "Взяла старуха крылышко, по коробу поскребла, по сусеку помела и наскребла муки горсти две.",
    "group": 1
} 
```
Пример ответа:
```
{
    "id": 1,
    "text": "Взяла старуха крылышко, по коробу поскребла, по сусеку помела и наскребла муки горсти две.",
    "author": "user",
    "image": null,
    "group": 1,
    "pub_date": "2021-09-01T08:47:11.084589Z"
} 
```
Пример POST-запроса с токеном user: отправляем новый комментарий к посту с id=1.

POST .../api/v1/posts/1/comments/
```
{
    "text": "Текст комментария",
} 
```
Пример ответа:
```
{
    "id": 3,
    "author": "user",
    "post": 1,
    "text": "тест тест",
    "created": "2021-09-01T10:14:51.388932Z"
} 
```
Пример GET-запроса с токеном user: получаем информацию о группе.

GET .../api/v1/groups/2/

Пример ответа:
```
{
    "id": 2,
    "title": "Все о книгах",
    "slug": "books",
    "description": "Посты о книгах"
} 
```