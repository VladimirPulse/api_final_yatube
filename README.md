# api_final_yatube
api_final_yatube — это ресурс на котором вы найдете творчество, разнообразие и свободу взглядов и самовыражений. А также сообщество людей, для которых нет грани между ведением публикаций и дружбой в социальных сетях.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ваш-аккаунт-на-гитхабе/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Пример запросов:

На эндпоинт POST-зарос:

``` 
http://127.0.0.1:8000/api/v1/posts/
```

Данные на отправку:

```
{
    "text": "Пост зарегистрированного пользователя."
}
```

Получен ответ:

```
{
    "id": 7,
    "author": "regular_user",
    "text": "Пост зарегистрированного пользователя.",
    "pub_date": "2024-01-14T18:16:43.100751Z",
    "image": null,
    "group": null
}
```
На эндпоинт GET-зарос:

``` 
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Получен ответ:

```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
