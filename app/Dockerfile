# Используем базовый образ Python
FROM python:3.11

# Устанавливаем переменную окружения для Python, чтобы вывод был направлен прямо в терминал без буферизации
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в /code
WORKDIR /app

# Копируем зависимости в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в контейнер
COPY . /app/