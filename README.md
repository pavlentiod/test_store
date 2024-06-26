# Инструкция по запуску приложения

## Описание проекта

Приложение представляет собой REST API для управления продуктами на торговой площадке. Оно позволяет пользователям добавлять, обновлять, удалять и получать информацию о продуктах, а также получать информацию о категориях и фильтровать продукты по различным параметрам. Приложение реализовано с использованием FastAPI и запускается в контейнере с помощью Docker Compose.

### Используемые технологии

Для разработки данного приложения использованы следующие технологии и библиотеки:

Основной стек: FastAPI + PostgreSQL(SQLAlchemy)

- **Python**: Версия 3.11, основной язык программирования проекта.
- **FastAPI**: Версия 0.111.0, фреймворк для создания веб-приложений и API.
- **SQLAlchemy**: Версия 2.0.27 (с экстрами "all"), библиотека ORM для работы с базами данных.
- **asyncpg**: Версия 0.29.0, драйвер для PostgreSQL для асинхронной работы.
- **Alembic**: Версия 1.13.1, инструмент для управления миграциями базы данных.
- **python-multipart**: Версия 0.0.9, библиотека для работы с загрузкой файлов.
- **pathlib**: Версия 1.0.1, библиотека для работы с путями файловой системы.
- **pydantic-settings**: Версия 2.3.3, библиотека для управления настройками конфигурации.
- **gunicorn**: Версия 22.0.0, WSGI HTTP сервер для запуска Python приложений.


## Требования

Перед началом работы убедитесь, что у вас установлены следующие инструменты:
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Шаги по запуску проекта

### 1. Клонирование репозитория

Склонируйте репозиторий проекта с GitHub на свой локальный компьютер:

```bash
git clone https://github.com/pavlentiod/test_store.git
```

Перейдите в директорию проекта:

```bash
cd test_store
```

### 2. Сборка и запуск контейнеров

Для сборки и запуска контейнеров используйте Docker Compose. Выполните следующую команду:

```bash
docker-compose up --build
```

Эта команда скачает необходимые образы, соберет контейнеры и запустит их. Также при запуске база данных будет заполнена тестовыми данными.

### 3. Проверка работы приложения

После успешного запуска контейнеров, ваше приложение будет доступно по адресу [http://localhost:8001](http://localhost:8001).

### 4. Тестирование API

API документация доступна по адресу [http://localhost:8001/docs](http://localhost:8001/docs). Вы можете использовать её для тестирования конечных точек вашего API.

