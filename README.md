# REST-сервис на DRF для управления виртуальными машинами(VPS)

## Модель VPS включает в себя следующие параметры:
```
uid — уникальный идентификатор сервера
cpu — количество ядер процессора
ram — объем оперативной памяти  
hdd — объем хранилища
status — текущий статус сервера (запущено, завершено, остановлено)
```

## Установка

1. Склонируйте репозиторий:
```
git clone https://github.com/tonboek/vps_manager.git
```
2. Создание виртуального окружения
```
python -m venv venv
```
3. Активация виртуального окружения
```
venv\Scripts\activate
```
4. Установка зависимостей проекта
```
pip install -r requirements.txt
```
5. Применение миграции
```
python manage.py migrate
```
6. Запуск сервера
```
python manage.py runserver
```

## Для работы с сервисом после запуска сервера:
```
http://127.0.0.1:8000/vps
```
## Admin:
```
http://127.0.0.1:8000/admin
```
