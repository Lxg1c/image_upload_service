# Используем официальный образ Python
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir fastapi uvicorn

# Открываем порт для приложения
EXPOSE 8000

# Запускаем FastAPI через Uvicorn
CMD ["uvicorn", "your_script:app", "--host", "0.0.0.0", "--port", "8000"]
