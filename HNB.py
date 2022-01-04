import requests
from bs4 import BeautifulSoup
import pyodbc
import datetime





HNB_AUD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=AUD&format=xml').text

HNB_AUD_data = BeautifulSoup(HNB_AUD_xml, 'lxml')

AUD_jedinica = HNB_AUD_data.find('jedinica').text
AUD_kod = HNB_AUD_data.find('valuta').text
AUD_kupovni = HNB_AUD_data.find('kupovni_tecaj').text
AUD_srednji = HNB_AUD_data.find('srednji_tecaj').text
AUD_prodajni = HNB_AUD_data.find('prodajni_tecaj').text

print(AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni)

HNB_CAD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CAD&format=xml').text

HNB_CAD_data = BeautifulSoup(HNB_CAD_xml, 'lxml')

CAD_jedinica = HNB_CAD_data.find('jedinica').text
CAD_kod = HNB_CAD_data.find('valuta').text
CAD_kupovni = HNB_CAD_data.find('kupovni_tecaj').text
CAD_srednji = HNB_CAD_data.find('srednji_tecaj').text
CAD_prodajni = HNB_CAD_data.find('prodajni_tecaj').text

print(CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni)

HNB_CZK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CZK&format=xml').text

HNB_CZK_data = BeautifulSoup(HNB_CZK_xml, 'lxml')

CZK_jedinica = HNB_CZK_data.find('jedinica').text
CZK_kod = HNB_CZK_data.find('valuta').text
CZK_kupovni = HNB_CZK_data.find('kupovni_tecaj').text
CZK_srednji = HNB_CZK_data.find('srednji_tecaj').text
CZK_prodajni = HNB_CZK_data.find('prodajni_tecaj').text

print(CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni)

HNB_DKK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=DKK&format=xml').text

HNB_DKK_data = BeautifulSoup(HNB_DKK_xml, 'lxml')

DKK_jedinica = HNB_DKK_data.find('jedinica').text
DKK_kod = HNB_DKK_data.find('valuta').text
DKK_kupovni = HNB_DKK_data.find('kupovni_tecaj').text
DKK_srednji = HNB_DKK_data.find('srednji_tecaj').text
DKK_prodajni = HNB_DKK_data.find('prodajni_tecaj').text

print(DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni)

HNB_HUF_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=HUF&format=xml').text

HNB_HUF_data = BeautifulSoup(HNB_HUF_xml, 'lxml')

HUF_jedinica = HNB_HUF_data.find('jedinica').text
HUF_kod = HNB_HUF_data.find('valuta').text
HUF_kupovni = HNB_HUF_data.find('kupovni_tecaj').text
HUF_srednji = HNB_HUF_data.find('srednji_tecaj').text
HUF_prodajni = HNB_HUF_data.find('prodajni_tecaj').text

print(HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni)

HNB_JPY_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=JPY&format=xml').text

HNB_JPY_data = BeautifulSoup(HNB_JPY_xml, 'lxml')

JPY_jedinica = HNB_JPY_data.find('jedinica').text
JPY_kod = HNB_JPY_data.find('valuta').text
JPY_kupovni = HNB_JPY_data.find('kupovni_tecaj').text
JPY_srednji = HNB_JPY_data.find('srednji_tecaj').text
JPY_prodajni = HNB_JPY_data.find('prodajni_tecaj').text

print(JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni)

HNB_NOK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=NOK&format=xml').text

HNB_NOK_data = BeautifulSoup(HNB_NOK_xml, 'lxml')

NOK_jedinica = HNB_NOK_data.find('jedinica').text
NOK_kod = HNB_NOK_data.find('valuta').text
NOK_kupovni = HNB_NOK_data.find('kupovni_tecaj').text
NOK_srednji = HNB_NOK_data.find('srednji_tecaj').text
NOK_prodajni = HNB_NOK_data.find('prodajni_tecaj').text

print(NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni)

HNB_SEK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=SEK&format=xml').text

HNB_SEK_data = BeautifulSoup(HNB_SEK_xml, 'lxml')

SEK_jedinica = HNB_SEK_data.find('jedinica').text
SEK_kod = HNB_SEK_data.find('valuta').text
SEK_kupovni = HNB_SEK_data.find('kupovni_tecaj').text
SEK_srednji = HNB_SEK_data.find('srednji_tecaj').text
SEK_prodajni = HNB_SEK_data.find('prodajni_tecaj').text

print(SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni)

HNB_CHF_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CHF&format=xml').text

HNB_CHF_data = BeautifulSoup(HNB_CHF_xml, 'lxml')

CHF_jedinica = HNB_CHF_data.find('jedinica').text
CHF_kod = HNB_CHF_data.find('valuta').text
CHF_kupovni = HNB_CHF_data.find('kupovni_tecaj').text
CHF_srednji = HNB_CHF_data.find('srednji_tecaj').text
CHF_prodajni = HNB_CHF_data.find('prodajni_tecaj').text

print(CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni)

HNB_GBP_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=GBP&format=xml').text

HNB_GBP_data = BeautifulSoup(HNB_GBP_xml, 'lxml')

GBP_jedinica = HNB_GBP_data.find('jedinica').text
GBP_kod = HNB_GBP_data.find('valuta').text
GBP_kupovni = HNB_GBP_data.find('kupovni_tecaj').text
GBP_srednji = HNB_GBP_data.find('srednji_tecaj').text
GBP_prodajni = HNB_GBP_data.find('prodajni_tecaj').text

print(GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni)

HNB_USD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=USD&format=xml').text

HNB_USD_data = BeautifulSoup(HNB_USD_xml, 'lxml')

USD_jedinica = HNB_USD_data.find('jedinica').text
USD_kod = HNB_USD_data.find('valuta').text
USD_kupovni = HNB_USD_data.find('kupovni_tecaj').text
USD_srednji = HNB_USD_data.find('srednji_tecaj').text
USD_prodajni = HNB_USD_data.find('prodajni_tecaj').text

print(USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni)

HNB_BAM_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=BAM&format=xml').text

HNB_BAM_data = BeautifulSoup(HNB_BAM_xml, 'lxml')

BAM_jedinica = HNB_BAM_data.find('jedinica').text
BAM_kod = HNB_BAM_data.find('valuta').text
BAM_kupovni = HNB_BAM_data.find('kupovni_tecaj').text
BAM_srednji = HNB_BAM_data.find('srednji_tecaj').text
BAM_prodajni = HNB_BAM_data.find('prodajni_tecaj').text

print(BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni)

HNB_EUR_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=EUR&format=xml').text

HNB_EUR_data = BeautifulSoup(HNB_EUR_xml, 'lxml')

EUR_jedinica = HNB_EUR_data.find('jedinica').text
EUR_kod = HNB_EUR_data.find('valuta').text
EUR_kupovni = HNB_EUR_data.find('kupovni_tecaj').text
EUR_srednji = HNB_EUR_data.find('srednji_tecaj').text
EUR_prodajni = HNB_EUR_data.find('prodajni_tecaj').text

print(EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni)

HNB_PLN_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=PLN&format=xml').text

HNB_PLN_data = BeautifulSoup(HNB_PLN_xml, 'lxml')

PLN_jedinica = HNB_PLN_data.find('jedinica').text
PLN_kod = HNB_PLN_data.find('valuta').text
PLN_kupovni = HNB_PLN_data.find('kupovni_tecaj').text
PLN_srednji = HNB_PLN_data.find('srednji_tecaj').text
PLN_prodajni = HNB_PLN_data.find('prodajni_tecaj').text

print(PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni)


AR_bank_id = '7E878B242D824F58AB91B6D304824475'

bank = 'HNB'


timeStamp = str(datetime.datetime.now())[0:-3]

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=B2ANALIZA;'
                      'Database=FX_RATES_TEST;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (EUR_jedinica, EUR_kod, EUR_kupovni.replace(',','.'), EUR_srednji.replace(',','.'), EUR_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (AUD_jedinica, AUD_kod, AUD_kupovni.replace(',','.'), AUD_srednji.replace(',','.'), AUD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CAD_jedinica, CAD_kod, CAD_kupovni.replace(',','.'), CAD_srednji.replace(',','.'), CAD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CZK_jedinica, CZK_kod, CZK_kupovni.replace(',','.'), CZK_srednji.replace(',','.'), CZK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (DKK_jedinica, DKK_kod, DKK_kupovni.replace(',','.'), DKK_srednji.replace(',','.'), DKK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HUF_jedinica, HUF_kod, HUF_kupovni.replace(',','.'), HUF_srednji.replace(',','.'), HUF_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (JPY_jedinica, JPY_kod, JPY_kupovni.replace(',','.'), JPY_srednji.replace(',','.'), JPY_prodajni.replace(',','.'), timeStamp, AR_bank_id,bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (NOK_jedinica, NOK_kod, NOK_kupovni.replace(',','.'), NOK_srednji.replace(',','.'), NOK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SEK_jedinica, SEK_kod, SEK_kupovni.replace(',','.'), SEK_srednji.replace(',','.'), SEK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CHF_jedinica, CHF_kod, CHF_kupovni.replace(',','.'), CHF_srednji.replace(',','.'), CHF_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (GBP_jedinica, GBP_kod, GBP_kupovni.replace(',','.'), GBP_srednji.replace(',','.'), GBP_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (USD_jedinica, USD_kod, USD_kupovni.replace(',','.'), USD_srednji.replace(',','.'), USD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (PLN_jedinica, PLN_kod, PLN_kupovni.replace(',','.'), PLN_srednji.replace(',','.'), PLN_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.HNB
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (BAM_jedinica, BAM_kod, BAM_kupovni.replace(',','.'), BAM_srednji.replace(',','.'), BAM_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

conn.commit()

