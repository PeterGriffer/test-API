# Movie Collection API

REST API для управления коллекцией фильмов, реализованный на Python. Проект выполнен в рамках практической работы № 5 по дисциплине «Проектирование и разработка программных интерфейсов приложений в WEB».

В качестве альтернативы стеку MEAN (Node.js + Express + AngularJS) выбран современный Python-стек: **FastAPI + MongoDB**.

## Стек технологий

*   **Python 3.10+** — язык программирования
*   **FastAPI** — веб-фреймворк для создания REST API (аналог Express)
*   **Uvicorn** — ASGI-сервер для запуска приложения
*   **MongoDB (Atlas)** — облачная NoSQL база данных
*   **PyMongo** — драйвер для работы с MongoDB
*   **Jinja2** — шаблонизатор для рендеринга HTML-страниц
*   **Bootstrap 5** — CSS-фреймворк для оформления интерфейса
*   **Fetch API (JS)** — для взаимодействия клиентской части с сервером

## Структура проекта

```text
testAPI-python/
├── app/
│   ├── __init__.py
│   ├── main.py               # Точка входа, запуск сервера и подключение роутов
│   ├── database.py           # Подключение к MongoDB
│   ├── models/
│   │   └── movie.py          # Pydantic-модель фильма
│   ├── services/
│   │   └── movie_service.py  # Бизнес-логика (CRUD)
│   ├── routes/
│   │   └── movie_routes.py   # Маршруты API
│   └── templates/
│       └── index.html        # UI (интерфейс)
├── static/
│   └── js/
│       └── app.js            # Клиентская логика (JS)
├── .env                      # Переменные окружения (не загружается в Git)
├── .gitignore                # Исключения для Git
├── Procfile                  # Файл для деплоя на Render/Heroku
├── requirements.txt          # Зависимости проекта
└── README.md                 # Описание проекта