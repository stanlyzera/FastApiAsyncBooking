# Booking сервис отелей

## Технический стек

![](https://img.shields.io/badge/-Python-386e9d?style=for-the-badge&logo=Python&logoColor=ffd241&) ![](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![](https://img.shields.io/badge/-sqlalchemy-4479A7?style=for-the-badge&amp;&amp;logoColor=ffffff) ![](https://img.shields.io/badge/-Postgresql-%232c3e50?style=for-the-badge&logo=Postgresql) ![](https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![](https://img.shields.io/badge/-Celery-386e9d?style=for-the-badge&logoColor=ffd241&)

### **Описание**

Booking сервис решает задачу бронирования номеров отеля для проживания. Каждый зарегистрированный пользователь может:
- Зарегистрироваться;
- Посмотреть список доступных отелей/комнат;
- Забронировать комнату;

---
### Запуск через Docker compose
Необходимо создать два индентичных файла .env и .env-non-dev и заполнить их своими переменными окружениями индентично файлу env-example.txt! Для запуска всех сервисов (БД, Redis, веб-сервер (FastAPI), Celery) необходимо использовать файл docker-compose.yml и команды из директории, где располагаются docker файлы!
```
docker compose build
docker compose up
```
Прежде чем тестировать API, следует выполнить ниже указанные действия!
---

### **Примеры запросов к API**
1. **Регистрация пользователя:**
```
POST /auth/register/
{
  "email": "user@example.com",
  "password": "string"
}
```
2. **Логин:**
```
POST /auth/login/
{
  "email": "user@example.com",
  "password": "string"
}
```

3. **Загрузка тестовых данных в базу данных:**
```
POST /import/{table_name}
1) Выбор hotels/bookings/rooms
2) Загрузка соответствующего файла из папки csv-data
Выполнять загрузку следует в следующем порядке hotels-rooms-bookings
```

4. **Бронирование:**
```
POST /bookings
parameters:
1) room_id
2) date_from
3) date_to
```

5. **Получение своих бронирований:**
```
GET /v1/bookings

```

---

Для детальной информации об API и его возможностях обратитесь к документации по **localhost:7777/docs**
