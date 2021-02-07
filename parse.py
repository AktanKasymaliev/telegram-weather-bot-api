import requests
from bs4 import BeautifulSoup
import fake_useragent

user_ag = fake_useragent.UserAgent().random
header = {
    'user-agent': user_ag
}
# можно созадть списов регионов по которым будет происходить поиск или просто зпмена урла на другой
Url = 'https://ru.meteotrend.com/forecast/kg/bishkek/'

list_day = []
Desc = []
r = requests.get(Url, headers=header).text
soup = BeautifulSoup(r, 'html.parser')
blocks = soup.find_all('div', class_='lf2')[:2]
for i in blocks:
    list_ = i.text.split(' ')[3].split('\xa0')[1].split('...')
    Desc.append(i.text.split(' ')[-1].split('C')[-1])
    list_day.append(list_)
tellingDay = f'Днем {Desc[0]}: {list_day[0][0]} и {list_day[0][1]} Градусов по C'
telling_night = f'Вечером {Desc[1]}: {list_day[1][0]} и {list_day[1][1]} Градусов по C'
print(tellingDay, telling_night, sep='\n')