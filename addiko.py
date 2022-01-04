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

CAD = ADDIKO_table.find_all('tr')[2]

CAD_jedinica = CAD.find_all('td')[3].text
CAD_kod = CAD.find_all('td')[2].text
CAD_kupovni = CAD.find_all('td')[4].text
CAD_srednji = CAD.find_all('td')[5].text
CAD_prodajni = CAD.find_all('td')[6].text

print(CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni)

CZK = ADDIKO_table.find_all('tr')[3]

CZK_jedinica = CZK.find_all('td')[3].text
CZK_kod = CZK.find_all('td')[2].text
CZK_kupovni = CZK.find_all('td')[4].text
CZK_srednji = CZK.find_all('td')[5].text
CZK_prodajni = CZK.find_all('td')[6].text

print(CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni)

DKK = ADDIKO_table.find_all('tr')[4]

DKK_jedinica = DKK.find_all('td')[3].text
DKK_kod = DKK.find_all('td')[2].text
DKK_kupovni = DKK.find_all('td')[4].text
DKK_srednji = DKK.find_all('td')[5].text
DKK_prodajni = DKK.find_all('td')[6].text

print(DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni)

HUF = ADDIKO_table.find_all('tr')[5]

HUF_jedinica = HUF.find_all('td')[3].text
HUF_kod = HUF.find_all('td')[2].text
HUF_kupovni = HUF.find_all('td')[4].text
HUF_srednji = HUF.find_all('td')[5].text
HUF_prodajni = HUF.find_all('td')[6].text

print(HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni)

JPY = ADDIKO_table.find_all('tr')[6]

JPY_jedinica = JPY.find_all('td')[3].text
JPY_kod = JPY.find_all('td')[2].text
JPY_kupovni = JPY.find_all('td')[4].text
JPY_srednji = JPY.find_all('td')[5].text
JPY_prodajni = JPY.find_all('td')[6].text

print(JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni)

NOK = ADDIKO_table.find_all('tr')[7]

NOK_jedinica = NOK.find_all('td')[3].text
NOK_kod = NOK.find_all('td')[2].text
NOK_kupovni = NOK.find_all('td')[4].text
NOK_srednji = NOK.find_all('td')[5].text
NOK_prodajni = NOK.find_all('td')[6].text

print(NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni)

SEK = ADDIKO_table.find_all('tr')[8]

SEK_jedinica = SEK.find_all('td')[3].text
SEK_kod = SEK.find_all('td')[2].text
SEK_kupovni = SEK.find_all('td')[4].text
SEK_srednji = SEK.find_all('td')[5].text
SEK_prodajni = SEK.find_all('td')[6].text

print(SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni)

CHF = ADDIKO_table.find_all('tr')[9]

CHF_jedinica = CHF.find_all('td')[3].text
CHF_kod = CHF.find_all('td')[2].text
CHF_kupovni = CHF.find_all('td')[4].text
CHF_srednji = CHF.find_all('td')[5].text
CHF_prodajni = CHF.find_all('td')[6].text

print(CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni)

GBP = ADDIKO_table.find_all('tr')[10]

GBP_jedinica = GBP.find_all('td')[3].text
GBP_kod = GBP.find_all('td')[2].text
GBP_kupovni = GBP.find_all('td')[4].text
GBP_srednji = GBP.find_all('td')[5].text
GBP_prodajni = GBP.find_all('td')[6].text

print(GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni)

USD = ADDIKO_table.find_all('tr')[11]

USD_jedinica = USD.find_all('td')[3].text
USD_kod = USD.find_all('td')[2].text
USD_kupovni = USD.find_all('td')[4].text
USD_srednji = USD.find_all('td')[5].text
USD_prodajni = USD.find_all('td')[6].text

print(USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni)

EUR = ADDIKO_table.find_all('tr')[12]

EUR_jedinica = EUR.find_all('td')[3].text
EUR_kod = EUR.find_all('td')[2].text
EUR_kupovni = EUR.find_all('td')[4].text
EUR_srednji = EUR.find_all('td')[5].text
EUR_prodajni = EUR.find_all('td')[6].text

print(EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni)

PLN = ADDIKO_table.find_all('tr')[13]

PLN_jedinica = PLN.find_all('td')[3].text
PLN_kod = PLN.find_all('td')[2].text
PLN_kupovni = PLN.find_all('td')[4].text
PLN_srednji = PLN.find_all('td')[5].text
PLN_prodajni = PLN.find_all('td')[6].text

print(PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni)

BAM = ADDIKO_table.find_all('tr')[14]

BAM_jedinica = BAM.find_all('td')[3].text
BAM_kod = BAM.find_all('td')[2].text
BAM_kupovni = BAM.find_all('td')[4].text
BAM_srednji = BAM.find_all('td')[5].text
BAM_prodajni = BAM.find_all('td')[6].text

print(BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni)




AR_bank_id = '79A59AAFF950430B83A2AB8D55A23F9C'

bank = 'ADDIKO'


timeStamp = str(datetime.datetime.now())[0:-3]

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=B2ANALIZA;'
                      'Database=FX_RATES_TEST;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (EUR_jedinica, EUR_kod, EUR_kupovni.replace(',','.'), EUR_srednji.replace(',','.'), EUR_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (AUD_jedinica, AUD_kod, AUD_kupovni.replace(',','.'), AUD_srednji.replace(',','.'), AUD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CAD_jedinica, CAD_kod, CAD_kupovni.replace(',','.'), CAD_srednji.replace(',','.'), CAD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CZK_jedinica, CZK_kod, CZK_kupovni.replace(',','.'), CZK_srednji.replace(',','.'), CZK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (DKK_jedinica, DKK_kod, DKK_kupovni.replace(',','.'), DKK_srednji.replace(',','.'), DKK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HUF_jedinica, HUF_kod, HUF_kupovni.replace(',','.'), HUF_srednji.replace(',','.'), HUF_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (JPY_jedinica, JPY_kod, JPY_kupovni.replace(',','.'), JPY_srednji.replace(',','.'), JPY_prodajni.replace(',','.'), timeStamp, AR_bank_id,bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (NOK_jedinica, NOK_kod, NOK_kupovni.replace(',','.'), NOK_srednji.replace(',','.'), NOK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SEK_jedinica, SEK_kod, SEK_kupovni.replace(',','.'), SEK_srednji.replace(',','.'), SEK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CHF_jedinica, CHF_kod, CHF_kupovni.replace(',','.'), CHF_srednji.replace(',','.'), CHF_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (GBP_jedinica, GBP_kod, GBP_kupovni.replace(',','.'), GBP_srednji.replace(',','.'), GBP_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (USD_jedinica, USD_kod, USD_kupovni.replace(',','.'), USD_srednji.replace(',','.'), USD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (PLN_jedinica, PLN_kod, PLN_kupovni.replace(',','.'), PLN_srednji.replace(',','.'), PLN_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ADDIKO
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (BAM_jedinica, BAM_kod, BAM_kupovni.replace(',','.'), BAM_srednji.replace(',','.'), BAM_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

conn.commit()
