import telebot 
from telebot import types
from parse import *
from config import TOKEN, load_config

token = load_config(TOKEN, "token", default="notoken")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    bt1 = types.KeyboardButton('Bishkek')
    bt2 = types.KeyboardButton('Talas')
    bt3 = types.KeyboardButton('Issyk-Kul')
    bt4 = types.KeyboardButton('Naryn')
    bt5 = types.KeyboardButton('Osh')
    bt6 = types.KeyboardButton('Batken')
    bt7 = types.KeyboardButton('Jalal-Abad')
    other = types.KeyboardButton('Other')
    markup.add(bt1, bt2, bt3, bt4, bt5, bt6, bt7, other)
    bot.send_message(message.chat.id, 'Hello!\nChoose the one variant of them', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def reply_mess(message):
    choice_city(message, bot)


bot.polling()