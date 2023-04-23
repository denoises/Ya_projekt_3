





# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot

# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot

# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot

# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot
# МАКС БОТ В ТГ НАЗЫВАЕТСЯ Test_knowledge_of_car_brands_Bot




# Импортируем необходимые классы.
import logging
import telegram
import random
from telegram.ext import Application, MessageHandler, filters, Updater, CommandHandler

BOT_TOKEN = '6245333260:AAGy8x5K7OipL43Wk5uWEXV54B5Q6wKub9o'

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

# Список марок автомобилей
brands = ['BMW', 'Audi', 'Mercedes-Benz', 'Toyota', 'Honda', 'Ford']

# Список изображений автомобилей
images = ['https://example.com/image1.jpg', 'https://example.com/image2.jpg', 'https://example.com/image3.jpg']


def start(update, context):
    """Обработчик команды /start"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет! Я бот для тестов по угадыванию марок автомобилей. Что ты хочешь сделать?")


def full_car_test(update, context):
    """Обработчик команды /full_car_test"""
    brand = random.choice(brands)
    image = random.choice(images)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image,
                           caption="Угадай, какая марка автомобиля на картинке? Выбери вариант ответа ниже.")
    keyboard = [[brand, random.choice(brands), random.choice(brands), random.choice(brands)]]
    random.shuffle(keyboard)
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Выбери вариант ответа:", reply_markup=reply_markup)


def part_car_test(update, context):
    """Обработчик команды /part_car_test"""
    brand = random.choice(brands)
    part = random.choice(['фары', 'бампер'])
    image_url = f'https://example.com/{brand}_{part}.jpg'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url,
                           caption=f"Угадай, какая марка автомобиля по {part}?")
    keyboard = [[brand, random.choice(brands), random.choice(brands), random.choice(brands)]]
    random.shuffle(keyboard)
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Выбери вариант ответа:", reply_markup=reply_markup)


def check_answer(update, context):
    """Обработчик сообщений с ответом"""
    user_answer = update.message.text
    correct_answer = context.user_data['correct_answer']
    if user_answer == correct_answer:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Правильно!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Неправильно. Попроб...уй еще раз.")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Выбери вариант ответа:",
                                 reply_markup=context.user_data['reply_markup'])


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('full_car_test', full_car_test))
    application.add_handler(CommandHandler('part_car_test', part_car_test))

    # Добавляем обработчик сообщений с ответом
    text_handler = MessageHandler(filters.TEXT, check_answer)

    # # Запускаем бота
    application.add_handler(text_handler)
    application.run_polling()

if __name__ == '__main__':
    main()
