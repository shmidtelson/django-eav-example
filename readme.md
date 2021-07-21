## Информация
frontend - папка с vue.js

db.sqlite3 - база  с уже добавленными данными

CATEGORY_ALL_ID в settings, категория "все", для уучастия в выборках

Роуты фронта в `frontend.src.routes`

## Установка
* `pipenv install`
* Настроить в `settings.CORS_ALLOWED_ORIGINS` урл фронта
* Настроить в `frontend.src.api.API_URL` из бэкенда
* Запустить фронт `cd frontend && yarn run serve`
## Данные
* Вход в админ панель admin:admin
## Разработка
* `cd frontend && yarn run build:watch`
