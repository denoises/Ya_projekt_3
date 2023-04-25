import telegram
import logging
import random

import updater as updater
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler
from telegram.ext import Application, MessageHandler, filters, Updater, CommandHandler
import os
from PIL import Image
import random

# небольшая переменная для подсчета, не надо создавать для нее файл, тк она обнуляется
scor = 0
# инициализируем логгер
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# задаем токен бота, полученный от BotFather
TOKEN = '6245333260:AAGy8x5K7OipL43Wk5uWEXV54B5Q6wKub9o'

dispatcher = Application.builder().token(TOKEN).read_timeout(100).write_timeout(100).build()

# создаем словарь марок автомобилей и соответствующих им фотографий
car_images = {
    'Audi': ['audi1.png', 'audi2.png'],
    'BMW': ['bmw1.png', 'bmw2.png', 'bmw3.png', 'bmw4.png', 'bmw5.png'],
    'Mercedes': ['mercedes1.png', 'mercedes2.png', 'mercedes3.png', 'mercedes4.png', 'mercedes5.png'],
    'Lada': ['lada1.png', 'lada2.png', 'lada3.png', 'lada4.png', 'lada5.png'],
    'Volvo': ['volvo1.png', 'volvo2.png'],
    'Skoda': ['skoda1.png', 'skoda2.png', 'skoda3.png'],
    'ГАЗ': ['gaz1.jpeg'],
    'Chevrolet': ['chevrolet1.png'],
    'Ford': ['ford1.png'],
    'Haval': ['haval1.png'],
    'Land Rover': ['lr1.png'],
    'Mazda': ['mazda1.png', 'mazda2.png'],
    'Toyota': ['t1.png', 't2.png'],
    'Fiat': ['fiat1.png', 'fiat2.png'],
    'Geely': ['geely1.png'],
    'Lexus': ['lexus1.png', 'lexus2.png', 'lexus3.png'],
    'Volkswagen': ['volkswagen1.png', 'volkswagen2.png', 'volkswagen3.png', 'volkswagen4.png', 'volkswagen5.png',
                   'volkswagen6.png'],
    'Hyundai': ['hyundai1.png', 'hyundai2.png', 'hyundai3.png'],
    'Infiniti': ['infiniti1.png', 'infiniti2.png'],
    'Honda': ['honda1.png', 'honda2.png'],
    'Jaguar': ['jaguar1.png', 'jaguar2.png'],
    'УАЗ': ['yaz1.png', 'yaz2.png', 'yaz3.png'],
    'Citroen': ['Citroen.png'],
    'Renault': ['renault1.png', 'renault2.png', 'renault3.png'],
    'Opel': ['opel.png', 'opel2.png', 'ope3.png'],
    'KIA': ['kia1.png', 'kia2.png', 'kia3.png', 'kia4.png', 'kia5.png', 'kia6.png'],
    'Nissan': ['nissan1.png', 'nissan2.png', 'nissan3.png']

}
car_brands = list(car_images.keys())
button_list = car_brands


async def start(update, context):
    global scor
    scor = 0
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
    print(context)
    context.user_data['car_brand'] = car_brand
    context.user_data['car_image'] = car_image

    keyboard = []
    for i in range(0, len(car_brands), 2):
        row = []
        row.append(InlineKeyboardButton(car_brands[i], callback_data=car_brands[i]))
        if i + 1 < len(car_brands):
            row.append(InlineKeyboardButton(car_brands[i + 1], callback_data=car_brands[i + 1]))
        keyboard.append(row)
    random.shuffle(keyboard)
    keyboard = keyboard[:3]
    try:
        keyboard[0][random.randint(0, 1)] = InlineKeyboardButton(context.user_data['car_brand'],
                                                                 callback_data=context.user_data['car_brand'])
    except Exception:
        keyboard[0][0] = InlineKeyboardButton(context.user_data['car_brand'],
                                              callback_data=context.user_data['car_brand'])
    random.shuffle(keyboard)
    markup = ReplyKeyboardMarkup(keyboard)
    try:
        await update.message.reply_photo(car_i_g, caption='Угадайте, какой марки этот автомобиль?',
                                         reply_markup=markup)
    except Exception:
        print('отсылается дольше обычного, возможна ошибка сети')


async def answer(update, context):
    global scor
    print('ожидание ответа')
    # получаем ответ пользователя
    user_answer = update.message.text
    # получаем сохраненную марку автомобиля
    try:
        car_brand = context.user_data['car_brand']

        if user_answer.lower() == car_brand.lower():
            scor += 1
            if scor > 1:
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text=f"Правильно! {scor} верно подряд, так держать!"
                                                    " Для следующего /play")
            else:
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text=f"Правильно! Для следующего вопроса /play")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Неправильно! Попробуйте еще раз.")
            scor = 0
    except Exception:
        print('лишнее сообщение:', update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Напишите /start')


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
