## Описание проекта.
Учебный проект по теме API. Проект позволяет бекенду взаимодействовать с фронтендом. В проекте реализованы таблицы: Постов, Комментариев, Подписок и Групп. Проект написан с использованием языка программирования Python, фреймворка Django REST framework. Для аутентификации использовался JWT, для реализации использовались Djoser и Simple JWT.


## Запуск проекта

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:monemonic/api_final_yatube.git
cd kittygram
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
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

## Дорожная карта проекта

- [x] Создание API View-функций и API View-классов, добавление вьюсетов и роутеров.
- [x] Добавление сериализаторов, регулярных выражений аутентификации с помощью JWT. 
- [x] Добавление проверки прав с помощью Permission.
- [x] Добавление пагинации, фильтрации и сортировки.

Project Link: [https://github.com/monemonic/api_final_yatube](https://github.com/monemonic/api_final_yatube)