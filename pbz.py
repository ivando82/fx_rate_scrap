import requests
from bs4 import BeautifulSoup
import pyodbc
import datetime





PBZ_xml = requests.get('https://www.pbz.hr/Downloads/PBZteclist.xml').text

PBZ_data = BeautifulSoup(PBZ_xml, 'xml')

AUD_jedinica = PBZ_data.find_all('Unit')[0].text
AUD_kod = PBZ_data.find_all('Name')[0].text
AUD_kupovni = PBZ_data.find_all('BuyRateForeign')[0].text
AUD_srednji = PBZ_data.find_all('MeanRate')[0].text
AUD_prodajni = PBZ_data.find_all('SellRateForeign')[0].text

print(AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni)

CAD_jedinica = PBZ_data.find_all('Unit')[1].text
CAD_kod = PBZ_data.find_all('Name')[1].text
CAD_kupovni = PBZ_data.find_all('BuyRateForeign')[1].text
CAD_srednji = PBZ_data.find_all('MeanRate')[1].text
CAD_prodajni = PBZ_data.find_all('SellRateForeign')[1].text

print(CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni)

CZK_jedinica = PBZ_data.find_all('Unit')[2].text
CZK_kod = PBZ_data.find_all('Name')[2].text
CZK_kupovni = PBZ_data.find_all('BuyRateForeign')[2].text
CZK_srednji = PBZ_data.find_all('MeanRate')[2].text
CZK_prodajni = PBZ_data.find_all('SellRateForeign')[2].text

print(CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni)


DKK_jedinica = PBZ_data.find_all('Unit')[3].text
DKK_kod = PBZ_data.find_all('Name')[3].text
DKK_kupovni = PBZ_data.find_all('BuyRateForeign')[3].text
DKK_srednji = PBZ_data.find_all('MeanRate')[3].text
DKK_prodajni = PBZ_data.find_all('SellRateForeign')[3].text

print(DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni)

HUF_jedinica = PBZ_data.find_all('Unit')[4].text
HUF_kod = PBZ_data.find_all('Name')[4].text
HUF_kupovni = PBZ_data.find_all('BuyRateForeign')[4].text
HUF_srednji = PBZ_data.find_all('MeanRate')[4].text
HUF_prodajni = PBZ_data.find_all('SellRateForeign')[4].text

print(HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni)

JPY_jedinica = PBZ_data.find_all('Unit')[5].text
JPY_kod = PBZ_data.find_all('Name')[5].text
JPY_kupovni = PBZ_data.find_all('BuyRateForeign')[5].text
JPY_srednji = PBZ_data.find_all('MeanRate')[5].text
JPY_prodajni = PBZ_data.find_all('SellRateForeign')[5].text

print(JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni)

NOK_jedinica = PBZ_data.find_all('Unit')[6].text
NOK_kod = PBZ_data.find_all('Name')[6].text
NOK_kupovni = PBZ_data.find_all('BuyRateForeign')[6].text
NOK_srednji = PBZ_data.find_all('MeanRate')[6].text
NOK_prodajni = PBZ_data.find_all('SellRateForeign')[6].text

print(NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni)

SEK_jedinica = PBZ_data.find_all('Unit')[7].text
SEK_kod = PBZ_data.find_all('Name')[7].text
SEK_kupovni = PBZ_data.find_all('BuyRateForeign')[7].text
SEK_srednji = PBZ_data.find_all('MeanRate')[7].text
SEK_prodajni = PBZ_data.find_all('SellRateForeign')[7].text

print(SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni)

CHF_jedinica = PBZ_data.find_all('Unit')[8].text
CHF_kod = PBZ_data.find_all('Name')[8].text
CHF_kupovni = PBZ_data.find_all('BuyRateForeign')[8].text
CHF_srednji = PBZ_data.find_all('MeanRate')[8].text
CHF_prodajni = PBZ_data.find_all('SellRateForeign')[8].text

print(CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni)

GBP_jedinica = PBZ_data.find_all('Unit')[9].text
GBP_kod = PBZ_data.find_all('Name')[9].text
GBP_kupovni = PBZ_data.find_all('BuyRateForeign')[9].text
GBP_srednji = PBZ_data.find_all('MeanRate')[9].text
GBP_prodajni = PBZ_data.find_all('SellRateForeign')[9].text

print(GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni)

USD_jedinica = PBZ_data.find_all('Unit')[10].text
USD_kod = PBZ_data.find_all('Name')[10].text
USD_kupovni = PBZ_data.find_all('BuyRateForeign')[10].text
USD_srednji = PBZ_data.find_all('MeanRate')[10].text
USD_prodajni = PBZ_data.find_all('SellRateForeign')[10].text

print(USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni)

BAM_jedinica = PBZ_data.find_all('Unit')[11].text
BAM_kod = PBZ_data.find_all('Name')[11].text
BAM_kupovni = PBZ_data.find_all('BuyRateForeign')[11].text
BAM_srednji = PBZ_data.find_all('MeanRate')[11].text
BAM_prodajni = PBZ_data.find_all('SellRateForeign')[11].text

print(BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni)

EUR_jedinica = PBZ_data.find_all('Unit')[12].text
EUR_kod = PBZ_data.find_all('Name')[12].text
EUR_kupovni = PBZ_data.find_all('BuyRateForeign')[12].text
EUR_srednji = PBZ_data.find_all('MeanRate')[12].text
EUR_prodajni = PBZ_data.find_all('SellRateForeign')[12].text

print(EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni)

PLN_jedinica = PBZ_data.find_all('Unit')[13].text
PLN_kod = PBZ_data.find_all('Name')[13].text
PLN_kupovni = PBZ_data.find_all('BuyRateForeign')[13].text
PLN_srednji = PBZ_data.find_all('MeanRate')[13].text
PLN_prodajni = PBZ_data.find_all('SellRateForeign')[13].text

print(PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni)


AR_bank_id = '610CCE1C353044FCABCB0362192998DF'

bank = 'PBZ'


timeStamp = str(datetime.datetime.now())[0:-3]

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=B2ANALIZA;'
                      'Database=FX_RATES_TEST;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (EUR_jedinica, EUR_kod, EUR_kupovni.replace(',','.'), EUR_srednji.replace(',','.'), EUR_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (AUD_jedinica, AUD_kod, AUD_kupovni.replace(',','.'), AUD_srednji.replace(',','.'), AUD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CAD_jedinica, CAD_kod, CAD_kupovni.replace(',','.'), CAD_srednji.replace(',','.'), CAD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CZK_jedinica, CZK_kod, CZK_kupovni.replace(',','.'), CZK_srednji.replace(',','.'), CZK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (DKK_jedinica, DKK_kod, DKK_kupovni.replace(',','.'), DKK_srednji.replace(',','.'), DKK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HUF_jedinica, HUF_kod, HUF_kupovni.replace(',','.'), HUF_srednji.replace(',','.'), HUF_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (JPY_jedinica, JPY_kod, JPY_kupovni.replace(',','.'), JPY_srednji.replace(',','.'), JPY_prodajni.replace(',','.'), timeStamp, AR_bank_id,bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (NOK_jedinica, NOK_kod, NOK_kupovni.replace(',','.'), NOK_srednji.replace(',','.'), NOK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SEK_jedinica, SEK_kod, SEK_kupovni.replace(',','.'), SEK_srednji.replace(',','.'), SEK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CHF_jedinica, CHF_kod, CHF_kupovni.replace(',','.'), CHF_srednji.replace(',','.'), CHF_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (GBP_jedinica, GBP_kod, GBP_kupovni.replace(',','.'), GBP_srednji.replace(',','.'), GBP_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (USD_jedinica, USD_kod, USD_kupovni.replace(',','.'), USD_srednji.replace(',','.'), USD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (PLN_jedinica, PLN_kod, PLN_kupovni.replace(',','.'), PLN_srednji.replace(',','.'), PLN_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.PBZ
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (BAM_jedinica, BAM_kod, BAM_kupovni.replace(',','.'), BAM_srednji.replace(',','.'), BAM_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

conn.commit()



