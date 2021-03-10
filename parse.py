import requests
from bs4 import BeautifulSoup
import fake_useragent

user_ag = fake_useragent.UserAgent().random
header = {
    'user-agent': user_ag
}
# # можно созадть списов регионов по которым будет происходить поиск или просто зпмена урла на другой
# Url = 'https://rp5.ru/Weather_in_Bishkek'

def BishkekWeather():
    Url = 'https://rp5.ru/Weather_in_Bishkek'
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
    return f'Today in Bishkek {temps[0]}\n{info}'


def TalasWeather():
    Url = 'https://rp5.ru/Weather_in_Talas'
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
    return f'Today in Talas {temps[0]}\n{info}'


def IKWeather():
    Url = 'https://rp5.ru/Weather_in_Issyk-Kul'
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
    return f'Today in Issyk-Kul {temps[0]}\n{info}'


def OshWeather():
    Url = 'https://rp5.ru/Weather_in_Osh'
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
    return f'Today in Osh {temps[0]}\n{info}'

def BatkenWeather():
    Url = 'https://rp5.ru/Weather_in_Batken'
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
    return f'Today in Batken {temps[0]}\n{info}'

def JalalAbadWeather():
    Url = 'https://rp5.ru/Weather_in_Jalal-Abad'
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
    return f'Today in Jalal-Abad {temps[0]}\n{info}'

def NarynWeather():
    Url = 'https://rp5.ru/Weather_in_Naryn'
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
    return f'Today in Naryn {temps[0]}\n{info}'