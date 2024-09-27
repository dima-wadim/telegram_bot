# telegram_bot
### Создание простого чат-бота для Телеграм на Python (тестовое задание)
Инструкция по подключению и запуску бота (README.md):
Создайте файл .env: Сохраните токен бота в переменной TELEGRAM_TOKEN.
Установите зависимости: pip install -r requirements.txt
Запустите бота: python bot.py
Встретившиеся проблемы и решения:
Получение курса валют: Для получения актуального курса рекомендуется использовать специализированные API, такие как exchangerate-api.com.
Асинхронность: Использование aiohttp позволяет выполнять запросы к API асинхронно, не блокируя основной поток.
Размещение бота: Для постоянной работы бота его необходимо разместить на сервере. Бесплатный вариант - Heroku.
Дополнительные возможности:
Сохранение данных пользователей: Использование базы данных для хранения информации о пользователях.
Расширение функционала: Добавление команд для получения информации о погоде, новостях и т.д.
Интерактивность: Создание кнопок, меню и других элементов для удобного взаимодействия с ботом.
Примечание:

Замените https://api.exchangerate-api.com/v4/latest/USD на адрес API, который вы будете использовать.
Подробную документацию по Telebot можно найти на официальном сайте: [неправильный URL удален]
Для более сложных ботов рекомендуется использовать фреймворки для веб-разработки, такие как Flask или Django.
Важно:

Безопасность: Никогда не публикуйте свой токен бота в открытом доступе.
Лимиты API: Учтите лимиты на количество запросов к API, чтобы избежать блокировки.
Дополнительные советы:

Структурируйте код: Используйте функции и классы для разделения логики бота.
Пишите комментарии: Объясняйте каждый участок кода, чтобы его было легче понимать.
Тестируйте код: Проверяйте работу бота на разных устройствах и с различными запросами.
Следуя этим рекомендациям, вы сможете создать своего собственного чат-бота в Telegram.

(Инструкция по запуску)
Требования:
Python 3.x
Аккаунт в Telegram
Токен бота от BotFather
Установка и запуск:
Создать виртуальное окружение (рекомендуется):

python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
Клонировать проект:
git clone <git@github.com:dima-wadim/telegram_bot.git>
cd telegram_bot
Установить зависимости:

pip install -r requirements.txt

Настроить бота:
В файле config.py укажите ваш токен бота (переменная TOKEN).
При необходимости замените API_URL на другой источник курса валют.
Запуск бота:

python bot.py
Настройка в Telegram:
Создайте бота через BotFather и получите токен.
Добавьте токен в config.py.
Запустите бота с помощью команды /start.
Проблемы и их решение:
Выбор API для курса валют: Некоторые API требуют ключи или ограничены по количеству запросов. Был выбран Open Exchange Rates API, так как он предлагает базовые функции бесплатно.

Обработка ошибок: Возможны ошибки сети или недоступность API. В код добавлена обработка исключений, чтобы бот мог отвечать пользователю, даже если данные о курсе временно недоступны.

Работа с Telegram API: Библиотека python-telegram-bot значительно упрощает работу с Telegram API, но требует знания основ асинхронного программирования.
