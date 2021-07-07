import requests
from bs4 import BeautifulSoup
import fake_useragent

user_ag = fake_useragent.UserAgent().random
header = {
    'user-agent': user_ag
}

def get_html(url):
    r = requests.get(url, headers=header)
    return r.text

def get_info(request, message_text):
    temps = []
    info = ''
    soup = BeautifulSoup(request, 'html.parser')
    weather = soup.find('div', {'id':'archiveString'})
    for i in weather:
        try:
            temp = i.find('span', class_='t_0')
            temps.append(temp.text)
        except:
            temp = ''
        try:
            information = i.find('a', class_='ArchiveStrLink').text
            info += information
        except:
            information = ''
            
    if '+' in temps[1]:
        return f'Today in {message_text} {temps[0]}\n{info}'
    else:
        return f'Today in {message_text} {temps[0]}\nIt feels like {temps[1]}\n{info}'

def get_weather(message_text):
    url = f'https://rp5.ru/Weather_in_{message_text}'
    response = get_info(get_html(url), message_text)
    return response


def choice_city(message, bot):
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