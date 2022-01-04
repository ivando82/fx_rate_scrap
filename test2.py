import requests
from bs4 import BeautifulSoup
import pyodbc
import datetime




HNB_AUD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=AUD&format=xml').text

HNB_AUD_data = BeautifulSoup(HNB_AUD_xml, 'lxml')

HNB_AUD_kod = HNB_AUD_data.find('valuta').text
HNB_AUD_jedinica = HNB_AUD_data.find('jedinica').text
HNB_AUD_kupovni = HNB_AUD_data.find('kupovni_tecaj').text
HNB_AUD_srednji = HNB_AUD_data.find('srednji_tecaj').text
HNB_AUD_prodajni = HNB_AUD_data.find('prodajni_tecaj').text

# print(AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni)

HNB_CAD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CAD&format=xml').text

HNB_CAD_data = BeautifulSoup(HNB_CAD_xml, 'lxml')

HNB_CAD_jedinica = HNB_CAD_data.find('jedinica').text
HNB_CAD_kod = HNB_CAD_data.find('valuta').text
HNB_CAD_kupovni = HNB_CAD_data.find('kupovni_tecaj').text
HNB_CAD_srednji = HNB_CAD_data.find('srednji_tecaj').text
HNB_CAD_prodajni = HNB_CAD_data.find('prodajni_tecaj').text

# print(CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni)

HNB_CZK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CZK&format=xml').text

HNB_CZK_data = BeautifulSoup(HNB_CZK_xml, 'lxml')

HNB_CZK_jedinica = HNB_CZK_data.find('jedinica').text
HNB_CZK_kod = HNB_CZK_data.find('valuta').text
HNB_CZK_kupovni = HNB_CZK_data.find('kupovni_tecaj').text
HNB_CZK_srednji = HNB_CZK_data.find('srednji_tecaj').text
HNB_CZK_prodajni = HNB_CZK_data.find('prodajni_tecaj').text

# print(CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni)

HNB_DKK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=DKK&format=xml').text

HNB_DKK_data = BeautifulSoup(HNB_DKK_xml, 'lxml')

HNB_DKK_jedinica = HNB_DKK_data.find('jedinica').text
HNB_DKK_kod = HNB_DKK_data.find('valuta').text
HNB_DKK_kupovni = HNB_DKK_data.find('kupovni_tecaj').text
HNB_DKK_srednji = HNB_DKK_data.find('srednji_tecaj').text
HNB_DKK_prodajni = HNB_DKK_data.find('prodajni_tecaj').text

# print(DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni)

HNB_HUF_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=HUF&format=xml').text

HNB_HUF_data = BeautifulSoup(HNB_HUF_xml, 'lxml')

HNB_HUF_jedinica = HNB_HUF_data.find('jedinica').text
HNB_HUF_kod = HNB_HUF_data.find('valuta').text
HNB_HUF_kupovni = HNB_HUF_data.find('kupovni_tecaj').text
HNB_HUF_srednji = HNB_HUF_data.find('srednji_tecaj').text
HNB_HUF_prodajni = HNB_HUF_data.find('prodajni_tecaj').text

# print(HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni)

HNB_JPY_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=JPY&format=xml').text

HNB_JPY_data = BeautifulSoup(HNB_JPY_xml, 'lxml')

HNB_JPY_jedinica = HNB_JPY_data.find('jedinica').text
HNB_JPY_kod = HNB_JPY_data.find('valuta').text
HNB_JPY_kupovni = HNB_JPY_data.find('kupovni_tecaj').text
HNB_JPY_srednji = HNB_JPY_data.find('srednji_tecaj').text
HNB_JPY_prodajni = HNB_JPY_data.find('prodajni_tecaj').text

# print(JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni)

HNB_NOK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=NOK&format=xml').text

HNB_NOK_data = BeautifulSoup(HNB_NOK_xml, 'lxml')

HNB_NOK_jedinica = HNB_NOK_data.find('jedinica').text
HNB_NOK_kod = HNB_NOK_data.find('valuta').text
HNB_NOK_kupovni = HNB_NOK_data.find('kupovni_tecaj').text
HNB_NOK_srednji = HNB_NOK_data.find('srednji_tecaj').text
HNB_NOK_prodajni = HNB_NOK_data.find('prodajni_tecaj').text

# print(NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni)

HNB_SEK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=SEK&format=xml').text

HNB_SEK_data = BeautifulSoup(HNB_SEK_xml, 'lxml')

HNB_SEK_jedinica = HNB_SEK_data.find('jedinica').text
HNB_SEK_kod = HNB_SEK_data.find('valuta').text
HNB_SEK_kupovni = HNB_SEK_data.find('kupovni_tecaj').text
HNB_SEK_srednji = HNB_SEK_data.find('srednji_tecaj').text
HNB_SEK_prodajni = HNB_SEK_data.find('prodajni_tecaj').text

# print(SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni)

HNB_CHF_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CHF&format=xml').text

HNB_CHF_data = BeautifulSoup(HNB_CHF_xml, 'lxml')

HNB_CHF_jedinica = HNB_CHF_data.find('jedinica').text
HNB_CHF_kod = HNB_CHF_data.find('valuta').text
HNB_CHF_kupovni = HNB_CHF_data.find('kupovni_tecaj').text
HNB_CHF_srednji = HNB_CHF_data.find('srednji_tecaj').text
HNB_CHF_prodajni = HNB_CHF_data.find('prodajni_tecaj').text

# print(CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni)

HNB_GBP_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=GBP&format=xml').text

HNB_GBP_data = BeautifulSoup(HNB_GBP_xml, 'lxml')

HNB_GBP_jedinica = HNB_GBP_data.find('jedinica').text
HNB_GBP_kod = HNB_GBP_data.find('valuta').text
HNB_GBP_kupovni = HNB_GBP_data.find('kupovni_tecaj').text
HNB_GBP_srednji = HNB_GBP_data.find('srednji_tecaj').text
HNB_GBP_prodajni = HNB_GBP_data.find('prodajni_tecaj').text

# print(GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni)

HNB_USD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=USD&format=xml').text

HNB_USD_data = BeautifulSoup(HNB_USD_xml, 'lxml')

HNB_USD_jedinica = HNB_USD_data.find('jedinica').text
HNB_USD_kod = HNB_USD_data.find('valuta').text
HNB_USD_kupovni = HNB_USD_data.find('kupovni_tecaj').text
HNB_USD_srednji = HNB_USD_data.find('srednji_tecaj').text
HNB_USD_prodajni = HNB_USD_data.find('prodajni_tecaj').text

# print(USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni)

HNB_BAM_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=BAM&format=xml').text

HNB_BAM_data = BeautifulSoup(HNB_BAM_xml, 'lxml')

HNB_BAM_jedinica = HNB_BAM_data.find('jedinica').text
HNB_BAM_kod = HNB_BAM_data.find('valuta').text
HNB_BAM_kupovni = HNB_BAM_data.find('kupovni_tecaj').text
HNB_BAM_srednji = HNB_BAM_data.find('srednji_tecaj').text
HNB_BAM_prodajni = HNB_BAM_data.find('prodajni_tecaj').text

# print(BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni)

HNB_EUR_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=EUR&format=xml').text

HNB_EUR_data = BeautifulSoup(HNB_EUR_xml, 'lxml')

HNB_EUR_jedinica = HNB_EUR_data.find('jedinica').text
HNB_EUR_kod = HNB_EUR_data.find('valuta').text
HNB_EUR_kupovni = HNB_EUR_data.find('kupovni_tecaj').text
HNB_EUR_srednji = HNB_EUR_data.find('srednji_tecaj').text
HNB_EUR_prodajni = HNB_EUR_data.find('prodajni_tecaj').text

# print(EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni)

HNB_PLN_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=PLN&format=xml').text

HNB_PLN_data = BeautifulSoup(HNB_PLN_xml, 'lxml')

HNB_PLN_jedinica = HNB_PLN_data.find('jedinica').text
HNB_PLN_kod = HNB_PLN_data.find('valuta').text
HNB_PLN_kupovni = HNB_PLN_data.find('kupovni_tecaj').text
HNB_PLN_srednji = HNB_PLN_data.find('srednji_tecaj').text
HNB_PLN_prodajni = HNB_PLN_data.find('prodajni_tecaj').text

# print(PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni)


HNB_AR_bank_id = '7E878B242D824F58AB91B6D304824475'

HNB_bank = 'HNB'

timeStamp = str(datetime.datetime.now())[0:-3]

HNB_conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=B2ANALIZA;'
                          'Database=FX_RATES_CHECK;'
                          'Trusted_Connection=no;'
                          'UID=kpitest;'
                          'PWD=Logitech2020!;')

HNB_cursor = HNB_conn.cursor()

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_EUR_jedinica, HNB_EUR_kod, HNB_EUR_kupovni.replace(',', '.'), HNB_EUR_srednji.replace(',', '.'),
     HNB_EUR_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_AUD_jedinica, HNB_AUD_kod, HNB_AUD_kupovni.replace(',', '.'), HNB_AUD_srednji.replace(',', '.'),
     HNB_AUD_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_CAD_jedinica, HNB_CAD_kod, HNB_CAD_kupovni.replace(',', '.'), HNB_CAD_srednji.replace(',', '.'),
     HNB_CAD_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_CZK_jedinica, HNB_CZK_kod, HNB_CZK_kupovni.replace(',', '.'), HNB_CZK_srednji.replace(',', '.'),
     HNB_CZK_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_DKK_jedinica, HNB_DKK_kod, HNB_DKK_kupovni.replace(',', '.'), HNB_DKK_srednji.replace(',', '.'),
     HNB_DKK_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_HUF_jedinica, HNB_HUF_kod, HNB_HUF_kupovni.replace(',', '.'), HNB_HUF_srednji.replace(',', '.'),
     HNB_HUF_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_JPY_jedinica, HNB_JPY_kod, HNB_JPY_kupovni.replace(',', '.'), HNB_JPY_srednji.replace(',', '.'),
     HNB_JPY_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_NOK_jedinica, HNB_NOK_kod, HNB_NOK_kupovni.replace(',', '.'), HNB_NOK_srednji.replace(',', '.'),
     HNB_NOK_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_SEK_jedinica, HNB_SEK_kod, HNB_SEK_kupovni.replace(',', '.'), HNB_SEK_srednji.replace(',', '.'),
     HNB_SEK_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_CHF_jedinica, HNB_CHF_kod, HNB_CHF_kupovni.replace(',', '.'), HNB_CHF_srednji.replace(',', '.'),
     HNB_CHF_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_GBP_jedinica, HNB_GBP_kod, HNB_GBP_kupovni.replace(',', '.'), HNB_GBP_srednji.replace(',', '.'),
     HNB_GBP_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_USD_jedinica, HNB_USD_kod, HNB_USD_kupovni.replace(',', '.'), HNB_USD_srednji.replace(',', '.'),
     HNB_USD_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_PLN_jedinica, HNB_PLN_kod, HNB_PLN_kupovni.replace(',', '.'), HNB_PLN_srednji.replace(',', '.'),
     HNB_PLN_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_cursor.execute(
    '''
    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HNB_BAM_jedinica, HNB_BAM_kod, HNB_BAM_kupovni.replace(',', '.'), HNB_BAM_srednji.replace(',', '.'),
     HNB_BAM_prodajni.replace(',', '.'), timeStamp, HNB_AR_bank_id, HNB_bank)
)

HNB_conn.commit()