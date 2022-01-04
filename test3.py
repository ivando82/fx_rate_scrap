import requests
from bs4 import BeautifulSoup
import pyodbc
import datetime



url = 'https://www.addiko.hr/izracuni/tecajna-lista/'

ADDIKO_page = requests.get(url)

ADIDIKO_soup = BeautifulSoup(ADDIKO_page.text, 'html.parser')


ADDIKO_table = ADIDIKO_soup.find('table')

#print(table)

AUD = ADDIKO_table.find_all('tr')[1]

AUD_jedinica = AUD.find_all('td')[3].text
AUD_kod = AUD.find_all('td')[2].text
AUD_kupovni = AUD.find_all('td')[4].text
AUD_srednji = AUD.find_all('td')[5].text
AUD_prodajni = AUD.find_all('td')[6].text

print(AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni)