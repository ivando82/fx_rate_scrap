import requests
from bs4 import BeautifulSoup
import pyodbc
import datetime
from datetime import date




SLAT_url = 'https://www.slatinska-banka.hr/tecajna-lista/'

SLAT_page = requests.get(SLAT_url)

SLAT_soup = BeautifulSoup(SLAT_page.text, 'html.parser')


SLAT_table = SLAT_soup.find('table')

#print(SLAT_table)

SLAT_AUD = SLAT_table.find_all('tr')[1]

SLAT_AUD_jedinica = SLAT_AUD.find_all('td')[3].text
SLAT_AUD_kod = SLAT_AUD.find_all('td')[1].text
SLAT_AUD_kupovni = SLAT_AUD.find_all('td')[5].text
SLAT_AUD_srednji = SLAT_AUD.find_all('td')[6].text
SLAT_AUD_prodajni = SLAT_AUD.find_all('td')[7].text

print(SLAT_AUD_jedinica, SLAT_AUD_kod, SLAT_AUD_kupovni, SLAT_AUD_srednji, SLAT_AUD_prodajni)


SLAT_CAD = SLAT_table.find_all('tr')[2]

SLAT_CAD_jedinica = SLAT_CAD.find_all('td')[3].text
SLAT_CAD_kod = SLAT_CAD.find_all('td')[1].text
SLAT_CAD_kupovni = SLAT_CAD.find_all('td')[5].text
SLAT_CAD_srednji = SLAT_CAD.find_all('td')[6].text
SLAT_CAD_prodajni = SLAT_CAD.find_all('td')[7].text

print(SLAT_CAD_jedinica, SLAT_CAD_kod, SLAT_CAD_kupovni, SLAT_CAD_srednji, SLAT_CAD_prodajni)


SLAT_CZK = SLAT_table.find_all('tr')[3]

SLAT_CZK_jedinica = SLAT_CZK.find_all('td')[3].text
SLAT_CZK_kod = SLAT_CZK.find_all('td')[1].text
SLAT_CZK_kupovni = SLAT_CZK.find_all('td')[5].text
SLAT_CZK_srednji = SLAT_CZK.find_all('td')[6].text
SLAT_CZK_prodajni = SLAT_CZK.find_all('td')[7].text

print(SLAT_CZK_jedinica, SLAT_CZK_kod, SLAT_CZK_kupovni, SLAT_CZK_srednji, SLAT_CZK_prodajni)


SLAT_DKK = SLAT_table.find_all('tr')[4]

SLAT_DKK_jedinica = SLAT_DKK.find_all('td')[3].text
SLAT_DKK_kod = SLAT_DKK.find_all('td')[1].text
SLAT_DKK_kupovni = SLAT_DKK.find_all('td')[5].text
SLAT_DKK_srednji = SLAT_DKK.find_all('td')[6].text
SLAT_DKK_prodajni = SLAT_DKK.find_all('td')[7].text

print(SLAT_DKK_jedinica, SLAT_DKK_kod, SLAT_DKK_kupovni, SLAT_DKK_srednji, SLAT_DKK_prodajni)


SLAT_HUF = SLAT_table.find_all('tr')[5]

SLAT_HUF_jedinica = SLAT_HUF.find_all('td')[3].text
SLAT_HUF_kod = SLAT_HUF.find_all('td')[1].text
SLAT_HUF_kupovni = SLAT_HUF.find_all('td')[5].text
SLAT_HUF_srednji = SLAT_HUF.find_all('td')[6].text
SLAT_HUF_prodajni = SLAT_HUF.find_all('td')[7].text

print(SLAT_HUF_jedinica, SLAT_HUF_kod, SLAT_HUF_kupovni, SLAT_HUF_srednji, SLAT_HUF_prodajni)


SLAT_JPY = SLAT_table.find_all('tr')[6]

SLAT_JPY_jedinica = SLAT_JPY.find_all('td')[3].text
SLAT_JPY_kod = SLAT_JPY.find_all('td')[1].text
SLAT_JPY_kupovni = SLAT_JPY.find_all('td')[5].text
SLAT_JPY_srednji = SLAT_JPY.find_all('td')[6].text
SLAT_JPY_prodajni = SLAT_JPY.find_all('td')[7].text

print(SLAT_JPY_jedinica, SLAT_JPY_kod, SLAT_JPY_kupovni, SLAT_JPY_srednji, SLAT_JPY_prodajni)


SLAT_NOK = SLAT_table.find_all('tr')[7]

SLAT_NOK_jedinica = SLAT_NOK.find_all('td')[3].text
SLAT_NOK_kod = SLAT_NOK.find_all('td')[1].text
SLAT_NOK_kupovni = SLAT_NOK.find_all('td')[5].text
SLAT_NOK_srednji = SLAT_NOK.find_all('td')[6].text
SLAT_NOK_prodajni = SLAT_NOK.find_all('td')[7].text

print(SLAT_NOK_jedinica, SLAT_NOK_kod, SLAT_NOK_kupovni, SLAT_NOK_srednji, SLAT_NOK_prodajni)



SLAT_SEK = SLAT_table.find_all('tr')[8]

SLAT_SEK_jedinica = SLAT_SEK.find_all('td')[3].text
SLAT_SEK_kod = SLAT_SEK.find_all('td')[1].text
SLAT_SEK_kupovni = SLAT_SEK.find_all('td')[5].text
SLAT_SEK_srednji = SLAT_SEK.find_all('td')[6].text
SLAT_SEK_prodajni = SLAT_SEK.find_all('td')[7].text

print(SLAT_SEK_jedinica, SLAT_SEK_kod, SLAT_SEK_kupovni, SLAT_SEK_srednji, SLAT_SEK_prodajni)


SLAT_CHF = SLAT_table.find_all('tr')[9]

SLAT_CHF_jedinica = SLAT_CHF.find_all('td')[3].text
SLAT_CHF_kod = SLAT_CHF.find_all('td')[1].text
SLAT_CHF_kupovni = SLAT_CHF.find_all('td')[5].text
SLAT_CHF_srednji = SLAT_CHF.find_all('td')[6].text
SLAT_CHF_prodajni = SLAT_CHF.find_all('td')[7].text

print(SLAT_CHF_jedinica, SLAT_CHF_kod, SLAT_CHF_kupovni, SLAT_CHF_srednji, SLAT_CHF_prodajni)


SLAT_GBP = SLAT_table.find_all('tr')[10]

SLAT_GBP_jedinica = SLAT_GBP.find_all('td')[3].text
SLAT_GBP_kod = SLAT_GBP.find_all('td')[1].text
SLAT_GBP_kupovni = SLAT_GBP.find_all('td')[5].text
SLAT_GBP_srednji = SLAT_GBP.find_all('td')[6].text
SLAT_GBP_prodajni = SLAT_GBP.find_all('td')[7].text

print(SLAT_GBP_jedinica, SLAT_GBP_kod, SLAT_GBP_kupovni, SLAT_GBP_srednji, SLAT_GBP_prodajni)


SLAT_USD = SLAT_table.find_all('tr')[11]

SLAT_USD_jedinica = SLAT_USD.find_all('td')[3].text
SLAT_USD_kod = SLAT_USD.find_all('td')[1].text
SLAT_USD_kupovni = SLAT_USD.find_all('td')[5].text
SLAT_USD_srednji = SLAT_USD.find_all('td')[6].text
SLAT_USD_prodajni = SLAT_USD.find_all('td')[7].text

print(SLAT_USD_jedinica, SLAT_USD_kod, SLAT_USD_kupovni, SLAT_USD_srednji, SLAT_USD_prodajni)


SLAT_BAM = SLAT_table.find_all('tr')[12]

SLAT_BAM_jedinica = SLAT_BAM.find_all('td')[3].text
SLAT_BAM_kod = SLAT_BAM.find_all('td')[1].text
SLAT_BAM_kupovni = SLAT_BAM.find_all('td')[5].text
SLAT_BAM_srednji = SLAT_BAM.find_all('td')[6].text
SLAT_BAM_prodajni = SLAT_BAM.find_all('td')[7].text

print(SLAT_BAM_jedinica, SLAT_BAM_kod, SLAT_BAM_kupovni, SLAT_BAM_srednji, SLAT_BAM_prodajni)


SLAT_EUR = SLAT_table.find_all('tr')[13]

SLAT_EUR_jedinica = SLAT_EUR.find_all('td')[3].text
SLAT_EUR_kod = SLAT_EUR.find_all('td')[1].text
SLAT_EUR_kupovni = SLAT_EUR.find_all('td')[5].text
SLAT_EUR_srednji = SLAT_EUR.find_all('td')[6].text
SLAT_EUR_prodajni = SLAT_EUR.find_all('td')[7].text

print(SLAT_EUR_jedinica, SLAT_EUR_kod, SLAT_EUR_kupovni, SLAT_EUR_srednji, SLAT_EUR_prodajni)


SLAT_PLN = SLAT_table.find_all('tr')[14]

SLAT_PLN_jedinica = SLAT_PLN.find_all('td')[3].text
SLAT_PLN_kod = SLAT_PLN.find_all('td')[1].text
SLAT_PLN_kupovni = SLAT_PLN.find_all('td')[5].text
SLAT_PLN_srednji = SLAT_PLN.find_all('td')[6].text
SLAT_PLN_prodajni = SLAT_PLN.find_all('td')[7].text

print(SLAT_PLN_jedinica, SLAT_PLN_kod, SLAT_PLN_kupovni, SLAT_PLN_srednji, SLAT_PLN_prodajni)

SLAT_AR_bank_id = '8DA47BCFD91D4566A759E9FC1E4F8427'

SLAT_bank = 'SLAT'

timeStamp = str(datetime.datetime.now())[0:-3]

SLAT_conn = pyodbc.connect('Driver={SQL Server};'
                             'Server=B2ANALIZA;'
                             'Database=FX_RATES_CHECK;'
                             'Trusted_Connection=no;'
                             'UID=kpitest;'
                             'PWD=Logitech2020!;')

SLAT_cursor = SLAT_conn.cursor()

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_EUR_jedinica, SLAT_EUR_kod, SLAT_EUR_kupovni, SLAT_EUR_srednji,
     SLAT_EUR_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_AUD_jedinica, SLAT_AUD_kod, SLAT_AUD_kupovni, SLAT_AUD_srednji,
     SLAT_AUD_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_CAD_jedinica, SLAT_CAD_kod, SLAT_CAD_kupovni, SLAT_CAD_srednji,
     SLAT_CAD_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_CZK_jedinica, SLAT_CZK_kod, SLAT_CZK_kupovni, SLAT_CZK_srednji,
     SLAT_CZK_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_DKK_jedinica, SLAT_DKK_kod, SLAT_DKK_kupovni, SLAT_DKK_srednji,
     SLAT_DKK_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_HUF_jedinica, SLAT_HUF_kod, SLAT_HUF_kupovni, SLAT_HUF_srednji,
     SLAT_HUF_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_JPY_jedinica, SLAT_JPY_kod, SLAT_JPY_kupovni, SLAT_JPY_srednji,
     SLAT_JPY_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_NOK_jedinica, SLAT_NOK_kod, SLAT_NOK_kupovni, SLAT_NOK_srednji,
     SLAT_NOK_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_SEK_jedinica, SLAT_SEK_kod, SLAT_SEK_kupovni, SLAT_SEK_srednji,
     SLAT_SEK_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_CHF_jedinica, SLAT_CHF_kod, SLAT_CHF_kupovni, SLAT_CHF_srednji,
     SLAT_CHF_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_GBP_jedinica, SLAT_GBP_kod, SLAT_GBP_kupovni, SLAT_GBP_srednji,
     SLAT_GBP_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_USD_jedinica, SLAT_USD_kod, SLAT_USD_kupovni, SLAT_USD_srednji,
     SLAT_USD_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_PLN_jedinica, SLAT_PLN_kod, SLAT_PLN_kupovni, SLAT_PLN_srednji,
     SLAT_PLN_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SLAT_BAM_jedinica, SLAT_BAM_kod, SLAT_BAM_kupovni, SLAT_BAM_srednji,
     SLAT_BAM_prodajni, timeStamp, SLAT_AR_bank_id, SLAT_bank)
)

SLAT_conn.commit()

