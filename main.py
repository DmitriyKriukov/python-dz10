import telebot
from config import TOKEN
import random

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcom(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = telebot.types.KeyboardButton('Знак зодиака')
    item_2 = telebot.types.KeyboardButton('Угадайка')
    markup.add(item_1, item_2)
    bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def f(mess):
    if mess.text == 'Знак зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item_1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')
        item_2 = telebot.types.InlineKeyboardButton('Телец', callback_data='Телец')
        item_3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='Близнецы')
        item_4 = telebot.types.InlineKeyboardButton('Рак', callback_data='Рак')
        item_5 = telebot.types.InlineKeyboardButton('Лев', callback_data='Лев')
        item_6 = telebot.types.InlineKeyboardButton('Дева', callback_data='Дева')
        item_7 = telebot.types.InlineKeyboardButton('Весы', callback_data='Весы')
        item_8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='Скорпион')
        item_9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='Стрелец')
        item_10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='Козерог')
        item_11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='Водолей')
        item_12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='Рыбы')
        markup.add(item_1, item_2, item_3, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11,
                   item_12)
        bot.send_message(mess.chat.id, 'Отлично, нажимай!', reply_markup=markup)
    elif mess.text == 'Угадайка':
        msg = bot.send_message(mess.chat.id, 'Я загадал число от 1 до 5, попробуй угадать')
        bot.register_next_step_handler(msg, num_rnd)
    else:
        with open('sticker.txt', 'r', encoding='utf-8') as file:
            sticker = file.read().split('\n')
        bot.send_sticker(mess.chat.id, random.choice(sticker))


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    dikt_znak = znak_har()
    if call.data == 'Овен':
        bot.send_message(call.message.chat.id, dikt_znak['Овен'])
    elif call.data == 'Телец':
        bot.send_message(call.message.chat.id, dikt_znak['Телец'])
    elif call.data == 'Близнецы':
        bot.send_message(call.message.chat.id, dikt_znak['Близнецы'])
    elif call.data == 'Рак':
        bot.send_message(call.message.chat.id, dikt_znak['Рак'])
    elif call.data == 'Лев':
        bot.send_message(call.message.chat.id, dikt_znak['Лев'])
    elif call.data == 'Дева':
        bot.send_message(call.message.chat.id, dikt_znak['Дева'])
    elif call.data == 'Весы':
        bot.send_message(call.message.chat.id, dikt_znak['Весы'])
    elif call.data == 'Скорпион':
        bot.send_message(call.message.chat.id, dikt_znak['Скорпион'])
    elif call.data == 'Стрелец':
        bot.send_message(call.message.chat.id, dikt_znak['Стрелец'])
    elif call.data == 'Козерог':
        bot.send_message(call.message.chat.id, dikt_znak['Козерог'])
    elif call.data == 'Водолей':
        bot.send_message(call.message.chat.id, dikt_znak['Водолей'])
    elif call.data == 'Рыбы':
        bot.send_message(call.message.chat.id, dikt_znak['Рыбы'])

def znak_har():
    dict = {}
    with open('zodiak.txt', 'r', encoding='utf-8') as file:
        for i in range(1, 13):
            str1 = file.readline().split(' ', 1)
            dict[str1[0]] = str1[1]
    return dict

def num_rnd(message):
    x = random.randint(1, 5)
    if message.text == str(x):
        bot.send_message(message.chat.id, f'Угадал, мое число {x}')
    else:
        bot.send_message(message.chat.id, f'Не угадал, мое число {x}')

bot.polling(none_stop=True)
