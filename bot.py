import telebot 
from telebot import types
import requests
from bs4 import BeautifulSoup
import fake_useragent
from parse import *


TOKEN = '1653612500:AAE-EPc2EVFkD47xS-hjh4dU1gxFdB8wdcA'

bot = telebot.TeleBot(TOKEN)


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
    if message.text == 'Bishkek':
        bot.send_message(message.chat.id, get_weather(message_text=message.text))
    if message.text == 'Talas':
        bot.send_message(message.chat.id, get_weather(message_text=message.text))
    if message.text == 'Issyk-Kul':
        bot.send_message(message.chat.id, get_weather(message_text=message.text))
    if message.text == 'Naryn':
        bot.send_message(message.chat.id, get_weather(message_text=message.text))
    if message.text == 'Osh':
        bot.send_message(message.chat.id, get_weather(message_text=message.text))
    if message.text == 'Batken':
        bot.send_message(message.chat.id, get_weather(message_text=message.text))
    if message.text == 'Jalal-Abad':
        bot.send_message(message.chat.id, get_weather(message_text=message.text))
    if message.text == 'Other':
        bot.send_message(message.chat.id, 'Ok, tell me, wich city do you want?\nWithout mistake please!')
    else:
        try:
            bot.send_message(message.chat.id, get_weather(message_text=message.text))
        except:
            bot.send_message(message.chat.id, "Such city doesn't found with us\nOr retype please correctly")
        else:
            bot.send_message(message.chat.id, "We found this city!")



    
    







































bot.polling()