# Weather-Query-App
Тестовое задание для СМД-БАЙ ГРУПП.

## Install
```bash
git clone https://github.com/qwissx/Weather-Query-App.git
```

## Run
Скопировать .env.example файл в .env находящийся в корневом каталоге и вставить свой API ключ с сайта OpenWeatherMap.

Затем необходимо создать образ приложения.
```bash
docker build -f docker/Dockerfile -t weather .
```

После чего запустить контейнер с Postgres (предварительно установив образ postgres:latest).
```bash
docker run --name main \
  -e POSTGRES_USER=main \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=main \
  -p 5432:5432 \
  -d postgres:latest
```

Запускаем контейнер python приложения.
```bash 
docker run --env-file .env --name test -p 8000:8000 weather
```

Загружаем миграции базы данных.
```bash 
docker exec -it test alembic upgrade head
```

Теперь приложения будет доступно по адресу http://localhost:8000/docs.

## Test

Для проверки работоспособности приложения стоит придерживаться следующего плана:

1. Сделать запрос на http://localhost:8000/weather/test
2. Сделать запрос с несколькими городами.
3. Сделать запрос на http://localhost:8000/weather где отобразяться все запросы

