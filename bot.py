import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN, API_URL

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Обработчик команды /start
async def start(update: Update, context):
    await update.message.reply_text('Добрый день. Как вас зовут?')

# Обработчик сообщения с именем пользователя
async def handle_name(update: Update, context):
    user_name = update.message.text
    dollar_rate = get_dollar_rate()
    if dollar_rate:
        await update.message.reply_text(f'Рад знакомству, {user_name}! Курс доллара сегодня {dollar_rate}р')
    else:
        await update.message.reply_text('Не удалось получить курс доллара. Попробуйте позже.')

# Функция для получения курса доллара
def get_dollar_rate():
    try:
        response = requests.get(API_URL)
        data = response.json()
        # В зависимости от API может потребоваться изменение пути к курсу
        return data['rates']['RUB']
    except Exception as e:
        logger.error(f"Ошибка при получении курса доллара: {e}")
        return None

def main():
    # Создание объекта приложения
    application = Application.builder().token(TOKEN).build()

    # Добавление обработчиков команд и сообщений
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
