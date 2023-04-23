import telegram
import logging
import random

import updater as updater
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler
from telegram.ext import Application, MessageHandler, filters, Updater, CommandHandler
import os
from PIL import Image
import random

# инициализируем логгер
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# задаем токен бота, полученный от BotFather
TOKEN = '6245333260:AAGy8x5K7OipL43Wk5uWEXV54B5Q6wKub9o'

dispatcher = Application.builder().token(TOKEN).build()

# создаем словарь марок автомобилей и соответствующих им фотографий
car_images = {
    'Audi': ['audi1.png', 'audi2.png'],
    'BMW': ['bmw1.png', 'bmw2.png', 'bmw3.png', 'bmw4.png', 'bmw5.png'],
    'Mercedes': ['mercedes1.png', 'mercedes2.png', 'mercedes3.png', 'mercedes4.png', 'mercedes5.png'],
    'Lada': ['lada1.png', 'lada2.png', 'lada3.png'],
    'Volvo': ['volvo1.png', 'volvo2.png'],
    'Skoda': ['skoda1.png', 'skoda2.png', 'skoda3.png'],
    'ГАЗ': ['gaz1.jpeg'],
    'Chevrolet': ['chevrolet1.png'],
    'Ford': ['ford1.png'],
    'Haval': ['haval1.png'],
    'Land Rover': ['lr1.png'],
    'Mazda': ['mazda1.png', 'mazda2.png'],
    'Toyota': ['t1.png', 't2.png']
}
car_brands = list(car_images.keys())
button_list = car_brands


async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Привет! Я бот-тестер знания марок автомобилей. Я буду отправлять вам фотографии автомобилей, а вы должны будете угадать марку. Для начала игры отправьте команду /play.")


async def play(update, context):
    # выбираем случайную марку автомобиля и ее фотографию
    car_brand = random.choice(car_brands)
    car_image = car_images[car_brand]
    car_i_g = random.choice(car_image)
    # photo_url = random.choice(car_brand[car_brand])
    print(car_i_g)
    # сохраняем выбранную марку и ее фотографию в контексте
    context.user_data['car_brand'] = car_brand
    context.user_data['car_image'] = car_image

    keyboard = []
    for i in range(0, len(car_brands), 2):
        row = []
        row.append(InlineKeyboardButton(car_brands[i], callback_data=car_brands[i]))
        if i + 1 < len(car_brands):
            row.append(InlineKeyboardButton(car_brands[i + 1], callback_data=car_brands[i + 1]))
        keyboard.append(row)
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(car_i_g, caption='Угадайте, какой марки этот автомобиль?',
                                     reply_markup=reply_markup)


async def answer(update, context):
    print('ожидание ответа')
    # получаем ответ пользователя
    user_answer = update.message.text
    # получаем сохраненную марку автомобиля

    car_brand = context.user_data['car_brand']

    if user_answer.lower() == car_brand.lower():
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Правильно! Вы угадали марку автомобиля.")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Неправильно! Попробуйте еще раз.")

    # МААААКС короче по идеи вот так получать  нажатие от кнопки, но оно не работет резберись
    # query = update.callback_data
    # query.answer()
    # print(query.data)


def main() -> None:
    start_handler = CommandHandler('start', start)
    play_handler = CommandHandler('play', play)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(play_handler)
    answer_handler = MessageHandler(filters.TEXT, answer)
    dispatcher.add_handler(answer_handler)
    dispatcher.run_polling()


if __name__ == '__main__':
    main()
