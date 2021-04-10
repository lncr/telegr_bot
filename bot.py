import telebot
from telebot import types

import requests
from bs4 import BeautifulSoup


bot = telebot.TeleBot('1691093213:AAHU8Z1GDZQZSJZD8YktOt3ofKTbGFpPdvQ')


@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_more = types.InlineKeyboardButton(text = 'гороскоп на сегодня', callback_data= 'h')
    markup_inline.add(item_more)
    bot.send_message(message.chat.id, 'Добро пожаловать!',
        reply_markup=markup_inline
    )

@bot.callback_query_handler(func = lambda call: True)
def hello(call):
    if call.data == 'h':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)

        aries = types.KeyboardButton('aries')
        taurus = types.KeyboardButton('taurus')
        gemini = types.KeyboardButton('gemini')
        cancer = types.KeyboardButton('cancer')
        leo = types.KeyboardButton('leo')
        virgo = types.KeyboardButton('virgo')
        libra = types.KeyboardButton('libra')
        scorpio = types.KeyboardButton('scorpio')
        sagittarius = types.KeyboardButton('sagittarius')
        capricorn = types.KeyboardButton('capricorn')
        aquarius = types.KeyboardButton('aquarius')
        pisces = types.KeyboardButton('pisces')

        markup_reply.add(aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces)
    bot.send_message(call.message.chat.id, 'Что вас интересует?',
        reply_markup=markup_reply    
    )

@bot.message_handler(content_types = ['text'])
def t(message):
    txt = message.text
    if txt in ['aries', 'taurus', 'gemini', ]:
        bot.send_message(message.chat.id, zp(txt))


def zp(sign):
    url = f'https://horo.mail.ru/prediction/{sign}/today/'

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")

    zs = []
    for zs in soup.find_all('div', {'class': 'article__item'}):
        zs.append(zs.get_text())

    return zs

bot.polling()