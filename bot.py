import telebot 
from telebot import types
import requests
from bs4 import BeautifulSoup
import fake_useragent


TOKEN = '1653612500:AAE-EPc2EVFkD47xS-hjh4dU1gxFdB8wdcA'
Url = 'https://ru.meteotrend.com/forecast/kg/bishkek/'

bot = telebot.TeleBot(TOKEN)


user_ag = fake_useragent.UserAgent().random
header = {
    'user-agent': user_ag
}
# можно созадть списов регионов по которым будет происходить поиск или просто зпмена урла на другой

list_day = []
Desc = []
r = requests.get(Url, headers=header).text
soup = BeautifulSoup(r, 'html.parser')
blocks = soup.find_all('div', class_='lf2')[:2]
for i in blocks:
    list_ = i.text.split(' ')[3].split('\xa0')[1].split('...')
    Desc.append(i.text.split(' ')[-1].split('C')[-1])
    list_day.append(list_)


telling_night = f'Днем {Desc[0]}: {list_day[0][0]} и {list_day[0][1]} Градусов по C'
tellingDay = f'Вечером {Desc[1]}: {list_day[1][0]} и {list_day[1][1]} Градусов по C'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    bt1 = types.KeyboardButton('Бишкек')
    bt2 = types.KeyboardButton('Кашка-суу')
    markup.add(bt1, bt2)
    bot.send_message(message.chat.id, 'Hello!\nChoose the variante', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def reply_mess(message):
    if message.text == 'Бишкек':
        bot.send_message(message.chat.id, f'{telling_night}\n{tellingDay}')
    
    







































bot.polling()