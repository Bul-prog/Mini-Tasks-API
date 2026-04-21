# Mini Tasks API (FastAPI)

## REST API для управления списком задач.

## Технологии
- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

## Структура проекта
app/
 ├── main.py        # точка входа
 ├── controller.py  # HTTP endpoints
 ├── service.py     # бизнес-логика
 ├── dto.py         # модели и валидация

## Установка и запуск
1. Клонировать репозиторий
```bash
git clone <your-repo-url>
cd <project-folder>
```

2. Создать виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

3. Установить зависимости
```bash
pip install -r requirements.txt
```

4. Запустить сервер
```bash
uvicorn main:app --reload
```

## Документация API

После запуска доступно:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

## Эндпоинты
- Создать задачу
```text
POST /tasks

{
  "title": "Купить молоко",
  "description": "2 литра",
  "status": "new"
}
```

- Получить список задач
```text
GET /tasks
```

- Получить задачу по ID
```text
GET /tasks/{id}
```

### Особенности
- Данные хранятся в памяти (без базы данных)
- Валидация через Pydantic
