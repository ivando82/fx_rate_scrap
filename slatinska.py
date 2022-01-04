import requests
from bs4 import BeautifulSoup
import pyodbc
import datetime
from datetime import date




url = 'https://www.slatinska-banka.hr/tecajna-lista/'

SLAT_page = requests.get(url)

ADIDIKO_soup = BeautifulSoup(SLAT_page.text, 'html.parser')


SLAT_table = ADIDIKO_soup.find('table')

#print(SLAT_table)

AUD = SLAT_table.find_all('tr')[1]

AUD_jedinica = AUD.find_all('td')[3].text
AUD_kod = AUD.find_all('td')[1].text
AUD_kupovni = AUD.find_all('td')[5].text
AUD_srednji = AUD.find_all('td')[6].text
AUD_prodajni = AUD.find_all('td')[7].text

print(AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni)


CAD = SLAT_table.find_all('tr')[2]

CAD_jedinica = CAD.find_all('td')[3].text
CAD_kod = CAD.find_all('td')[1].text
CAD_kupovni = CAD.find_all('td')[5].text
CAD_srednji = CAD.find_all('td')[6].text
CAD_prodajni = CAD.find_all('td')[7].text

print(CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni)


CZK = SLAT_table.find_all('tr')[3]

CZK_jedinica = CZK.find_all('td')[3].text
CZK_kod = CZK.find_all('td')[1].text
CZK_kupovni = CZK.find_all('td')[5].text
CZK_srednji = CZK.find_all('td')[6].text
CZK_prodajni = CZK.find_all('td')[7].text

print(CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni)


DKK = SLAT_table.find_all('tr')[4]

DKK_jedinica = DKK.find_all('td')[3].text
DKK_kod = DKK.find_all('td')[1].text
DKK_kupovni = DKK.find_all('td')[5].text
DKK_srednji = DKK.find_all('td')[6].text
DKK_prodajni = DKK.find_all('td')[7].text

print(DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni)


HUF = SLAT_table.find_all('tr')[5]

HUF_jedinica = HUF.find_all('td')[3].text
HUF_kod = HUF.find_all('td')[1].text
HUF_kupovni = HUF.find_all('td')[5].text
HUF_srednji = HUF.find_all('td')[6].text
HUF_prodajni = HUF.find_all('td')[7].text

print(HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni)


JPY = SLAT_table.find_all('tr')[6]

JPY_jedinica = JPY.find_all('td')[3].text
JPY_kod = JPY.find_all('td')[1].text
JPY_kupovni = JPY.find_all('td')[5].text
JPY_srednji = JPY.find_all('td')[6].text
JPY_prodajni = JPY.find_all('td')[7].text

print(JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni)


NOK = SLAT_table.find_all('tr')[7]

NOK_jedinica = NOK.find_all('td')[3].text
NOK_kod = NOK.find_all('td')[1].text
NOK_kupovni = NOK.find_all('td')[5].text
NOK_srednji = NOK.find_all('td')[6].text
NOK_prodajni = NOK.find_all('td')[7].text

print(NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni)



SEK = SLAT_table.find_all('tr')[8]

SEK_jedinica = SEK.find_all('td')[3].text
SEK_kod = SEK.find_all('td')[1].text
SEK_kupovni = SEK.find_all('td')[5].text
SEK_srednji = SEK.find_all('td')[6].text
SEK_prodajni = SEK.find_all('td')[7].text

print(SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni)


CHF = SLAT_table.find_all('tr')[9]

CHF_jedinica = CHF.find_all('td')[3].text
CHF_kod = CHF.find_all('td')[1].text
CHF_kupovni = CHF.find_all('td')[5].text
CHF_srednji = CHF.find_all('td')[6].text
CHF_prodajni = CHF.find_all('td')[7].text

print(CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni)


GBP = SLAT_table.find_all('tr')[10]

GBP_jedinica = GBP.find_all('td')[3].text
GBP_kod = GBP.find_all('td')[1].text
GBP_kupovni = GBP.find_all('td')[5].text
GBP_srednji = GBP.find_all('td')[6].text
GBP_prodajni = GBP.find_all('td')[7].text

print(GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni)


USD = SLAT_table.find_all('tr')[11]

USD_jedinica = USD.find_all('td')[3].text
USD_kod = USD.find_all('td')[1].text
USD_kupovni = USD.find_all('td')[5].text
USD_srednji = USD.find_all('td')[6].text
USD_prodajni = USD.find_all('td')[7].text

print(USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni)


BAM = SLAT_table.find_all('tr')[12]

BAM_jedinica = BAM.find_all('td')[3].text
BAM_kod = BAM.find_all('td')[1].text
BAM_kupovni = BAM.find_all('td')[5].text
BAM_srednji = BAM.find_all('td')[6].text
BAM_prodajni = BAM.find_all('td')[7].text

print(BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni)


EUR = SLAT_table.find_all('tr')[13]

EUR_jedinica = EUR.find_all('td')[3].text
EUR_kod = EUR.find_all('td')[1].text
EUR_kupovni = EUR.find_all('td')[5].text
EUR_srednji = EUR.find_all('td')[6].text
EUR_prodajni = EUR.find_all('td')[7].text

print(EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni)


PLN = SLAT_table.find_all('tr')[14]

PLN_jedinica = PLN.find_all('td')[3].text
PLN_kod = PLN.find_all('td')[1].text
PLN_kupovni = PLN.find_all('td')[5].text
PLN_srednji = PLN.find_all('td')[6].text
PLN_prodajni = PLN.find_all('td')[7].text

print(PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni)


HUF_srednji = (float(HUF_srednji) / float(HUF_jedinica))
HUF_kupovni = (float(HUF_kupovni) / float(HUF_jedinica))
HUF_prodajni = (float(HUF_prodajni) / float(HUF_jedinica))


JPY_srednji = (float(JPY_srednji) / float(JPY_jedinica))
JPY_kupovni = (float(JPY_kupovni) / float(JPY_jedinica))
JPY_prodajni = (float(JPY_prodajni) / float(JPY_jedinica))



acBbank = 'Slatinska Banka D.D.'

anUserIns = 1
anUserChg = 1

timeStamp = str(datetime.datetime.now())[0:-3]

#print(timeStamp)

today = str(datetime.datetime.today()).split()[0]


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=10.7.1.36;'
                      'Database=B2Kapital_HR;'
                      'Trusted_Connection=no;'
                       'UID=fximport;'
                       'PWD=Z750eFP2207#;')

cursor = conn.cursor()

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, EUR_kod, today, EUR_srednji, timeStamp, anUserIns, timeStamp, anUserChg, EUR_kupovni, EUR_prodajni)
      )

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, AUD_kod, today, AUD_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  AUD_kupovni, AUD_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, CAD_kod, today, CAD_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  CAD_kupovni, CAD_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, CZK_kod, today, CZK_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  CZK_kupovni, CZK_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, DKK_kod, today, DKK_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  DKK_kupovni, DKK_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, HUF_kod, today, HUF_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  HUF_kupovni, HUF_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, JPY_kod, today, JPY_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  JPY_kupovni, JPY_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, NOK_kod, today, NOK_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  NOK_kupovni, NOK_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, SEK_kod, today, SEK_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  SEK_kupovni, SEK_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, CHF_kod, today, CHF_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  CHF_kupovni, CHF_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, GBP_kod, today, GBP_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  GBP_kupovni, GBP_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, USD_kod, today, USD_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  USD_kupovni, USD_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, PLN_kod, today, PLN_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  PLN_kupovni, PLN_prodajni)
)

cursor.execute(
    '''
    INSERT INTO B2Kapital_HR.dbo.tHE_SetFXRate
    (AcBank, AcCurrency, adDate, anFXRate, adTimeIns, anUserIns, adTimeChg, AnUserChg, anFXRateBuy, anFxRateSale)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (acBbank, BAM_kod, today, BAM_srednji, timeStamp, anUserIns, timeStamp, anUserChg,  BAM_kupovni, BAM_prodajni)
)

conn.commit()
