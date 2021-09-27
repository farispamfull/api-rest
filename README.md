# api-rest
Проект по управлению студентами, лекциями, успеваемостью и оценками.

Характерные особенности:

Проект на полную аутентификацию пользователь с собственными представлениями, некоторой кастомизацией jwt и backend аутентификацией Django. Гибкая реализация передача permissions на уровне модели и на уровне экземпляра модели с помощью django-guardian и django admin.


## Процесс регистрации 
1. Пользователь отправляет запрос с параметрами  `email`,`username`,`password` на `/auth/register/`.
2. Сервер отправляет письмо с ссылкой на подтверждение электронной почты на адрес `email` 
3. Пользователь переходит по ссылке и если она действительная сервер вернет ответ Successfully activated
4. Далее пользователь отправляет запрос с параметрами `email`,`password` на `auth/signup/` в ответе на запрос ему приходит `token` (JWT-токен).

## Доступные endpoint

*Prefix* `auth/`

`register/`

`activate-email/<uidb64>/<token>/`

`signup/`

`token/refresh/`

`change_password/`

`password_reset/`

`password_reset/confirm/`

*Prefix* `api/`

`/users/profiles` (доступ staff)

`/users/profiles/me` (доступ request.user)




# TODO
* документация
* permissions/admin permissions
* добавить модели оценки
* celery + redis
* docker-compose
