# :poop: Интернет-маркетплейс на Django
> Проект создается в целях изучения Django для портфолио :shipit:

## :white_circle: Стек проекта: 
- Python (Django, Django REST)
- HTML5
- CSS (Bootstrap 5, UIkit)
- NGNIX, Gunicorn

## :memo: [Changelog](https://github.com/Re-Gelu/Sample_shop/blob/master/changelog.txt)

## :closed_lock_with_key: Админка

- Логин: *admin*
- Пароль: *1234*

> Либо `$ python manage.py createsuperuser --username admin --email admin@email.com`

## :white_circle: Авто-заполнение магазина для быстрого тестирования

```
.../db_auto_fill/7/Categories/
```
```
.../db_auto_fill/10/Subcategories/
```
```
.../db_auto_fill/300/Products/
```

> Необходимы права администратора

## :whale: Работа с Docker

- rm containers

  ```
  $ docker-compose down -v
  ```

- Dev
  ```
  $ docker-compose -f docker-compose.yml up -d --build
  ```

- Prod
  ```
  $ docker-compose -f docker-compose.prod.yml up -d --build
  $ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
  $ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
  ```
  
## :camera: Скрины проекта

![Изображение №1](https://user-images.githubusercontent.com/75813517/188868325-ccd04c10-ce03-4f4e-953d-585486d8c895.png)
![Изображение №2](https://user-images.githubusercontent.com/75813517/188868290-8b498777-60ec-4122-b541-f212753966cc.png)
![Изображение №3](https://user-images.githubusercontent.com/75813517/188868272-d8536fb7-d3bc-4877-baf1-665ba7183fcd.png)
![Изображение №4](https://user-images.githubusercontent.com/75813517/188868235-59a80095-d2be-474e-849c-b36b1562ce31.png)
![Изображение №5](https://user-images.githubusercontent.com/75813517/188868163-d8e8793e-85f7-467a-9378-000430b886c1.png)