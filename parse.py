import requests
from bs4 import BeautifulSoup
import fake_useragent

user_ag = fake_useragent.UserAgent().random
header = {
    'user-agent': user_ag
}

def get_weather(message_text):
    Url = f'https://rp5.ru/Weather_in_{message_text}'
    temps = []
    info = ''
    r = requests.get(Url, headers=header).text
    soup = BeautifulSoup(r, 'html.parser')
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