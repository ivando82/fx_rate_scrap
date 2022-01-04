import requests
from bs4 import BeautifulSoup
import pyodbc
import datetime



RBA_url = 'https://www.rba.hr/aktualna-tecajna-lista/'

RBA_page = requests.get(RBA_url)

RBA_soup = BeautifulSoup(RBA_page.text, 'html.parser')


RBA_table = RBA_soup.find('table', class_ = 'stdtbl tecaj datagrid')

for tecaj in RBA_table.find_all('tbody'):
    EUR = tecaj.find_all('tr')[0]
    EUR_jedinica = EUR.find_all('td')[0].text
    EUR_kod = EUR.find_all('td')[1].text
    EUR_kupovni = EUR.find_all('td')[2].text
    EUR_srednji = EUR.find_all('td')[3].text
    EUR_prodajni = EUR.find_all('td')[4].text

for tecaj in RBA_table.find_all('tbody'):
    USD = tecaj.find_all('tr')[1]
    USD_jedinica = USD.find_all('td')[0].text
    USD_kod = USD.find_all('td')[1].text
    USD_kupovni = USD.find_all('td')[2].text
    USD_srednji = USD.find_all('td')[3].text
    USD_prodajni = USD.find_all('td')[4].text

for tecaj in RBA_table.find_all('tbody'):
    CHF = tecaj.find_all('tr')[2]
    CHF_jedinica = CHF.find_all('td')[0].text
    CHF_kod = CHF.find_all('td')[1].text
    CHF_kupovni = CHF.find_all('td')[2].text
    CHF_srednji = CHF.find_all('td')[3].text
    CHF_prodajni = CHF.find_all('td')[4].text

for tecaj in RBA_table.find_all('tbody'):
    GBP = tecaj.find_all('tr')[3]
    GBP_jedinica = GBP.find_all('td')[0].text
    GBP_kod = GBP.find_all('td')[1].text
    GBP_kupovni = GBP.find_all('td')[2].text
    GBP_srednji = GBP.find_all('td')[3].text
    GBP_prodajni = GBP.find_all('td')[4].text

for tecaj in RBA_table.find_all('tbody'):
    AUD = tecaj.find_all('tr')[4]
    AUD_jedinica = AUD.find_all('td')[0].text
    AUD_kod = AUD.find_all('td')[1].text
    AUD_kupovni = AUD.find_all('td')[2].text
    AUD_srednji = AUD.find_all('td')[3].text
    AUD_prodajni = AUD.find_all('td')[4].text


for tecaj in RBA_table.find_all('tbody'):
    JPY = tecaj.find_all('tr')[5]
    JPY_jedinica = JPY.find_all('td')[0].text
    JPY_kod = JPY.find_all('td')[1].text
    JPY_kupovni = JPY.find_all('td')[2].text
    JPY_srednji = JPY.find_all('td')[3].text
    JPY_prodajni = JPY.find_all('td')[4].text

for tecaj in RBA_table.find_all('tbody'):
    BAM = tecaj.find_all('tr')[6]
    BAM_jedinica = BAM.find_all('td')[0].text
    BAM_kod = BAM.find_all('td')[1].text
    BAM_kupovni = BAM.find_all('td')[2].text
    BAM_srednji = BAM.find_all('td')[3].text
    BAM_prodajni = BAM.find_all('td')[4].text

for tecaj in RBA_table.find_all('tbody'):
    CAD = tecaj.find_all('tr')[7]
    CAD_jedinica = CAD.find_all('td')[0].text
    CAD_kod = CAD.find_all('td')[1].text
    CAD_kupovni = CAD.find_all('td')[2].text
    CAD_srednji = CAD.find_all('td')[3].text
    CAD_prodajni = CAD.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        CZK = tecaj.find_all('tr')[8]
        CZK_jedinica = CZK.find_all('td')[0].text
        CZK_kod = CZK.find_all('td')[1].text
        CZK_kupovni = CZK.find_all('td')[2].text
        CZK_srednji = CZK.find_all('td')[3].text
        CZK_prodajni = CZK.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        DKK = tecaj.find_all('tr')[9]
        DKK_jedinica = DKK.find_all('td')[0].text
        DKK_kod = DKK.find_all('td')[1].text
        DKK_kupovni = DKK.find_all('td')[2].text
        DKK_srednji = DKK.find_all('td')[3].text
        DKK_prodajni = DKK.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        HUF = tecaj.find_all('tr')[10]
        HUF_jedinica = HUF.find_all('td')[0].text
        HUF_kod = HUF.find_all('td')[1].text
        HUF_kupovni = HUF.find_all('td')[2].text
        HUF_srednji = HUF.find_all('td')[3].text
        HUF_prodajni = HUF.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        NOK = tecaj.find_all('tr')[11]
        NOK_jedinica = NOK.find_all('td')[0].text
        NOK_kod = NOK.find_all('td')[1].text
        NOK_kupovni = NOK.find_all('td')[2].text
        NOK_srednji = NOK.find_all('td')[3].text
        NOK_prodajni = NOK.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        PLN = tecaj.find_all('tr')[12]
        PLN_jedinica = PLN.find_all('td')[0].text
        PLN_kod = PLN.find_all('td')[1].text
        PLN_kupovni = PLN.find_all('td')[2].text
        PLN_srednji = PLN.find_all('td')[3].text
        PLN_prodajni = PLN.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        SEK = tecaj.find_all('tr')[13]
        SEK_jedinica = SEK.find_all('td')[0].text
        SEK_kod = SEK.find_all('td')[1].text
        SEK_kupovni = SEK.find_all('td')[2].text
        SEK_srednji = SEK.find_all('td')[3].text
        SEK_prodajni = SEK.find_all('td')[4].text




AR_bank_id = '1B27B838E50641D081216A2C57133275'

bank = 'RBA'


timeStamp = str(datetime.datetime.now())[0:-3]

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=B2ANALIZA;'
                      'Database=FX_RATES_TEST;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (EUR_jedinica, EUR_kod, EUR_kupovni.replace(',','.'), EUR_srednji.replace(',','.'), EUR_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (AUD_jedinica, AUD_kod, AUD_kupovni.replace(',','.'), AUD_srednji.replace(',','.'), AUD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CAD_jedinica, CAD_kod, CAD_kupovni.replace(',','.'), CAD_srednji.replace(',','.'), CAD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CZK_jedinica, CZK_kod, CZK_kupovni.replace(',','.'), CZK_srednji.replace(',','.'), CZK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (DKK_jedinica, DKK_kod, DKK_kupovni.replace(',','.'), DKK_srednji.replace(',','.'), DKK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HUF_jedinica, HUF_kod, HUF_kupovni.replace(',','.'), HUF_srednji.replace(',','.'), HUF_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (JPY_jedinica, JPY_kod, JPY_kupovni.replace(',','.'), JPY_srednji.replace(',','.'), JPY_prodajni.replace(',','.'), timeStamp, AR_bank_id,bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (NOK_jedinica, NOK_kod, NOK_kupovni.replace(',','.'), NOK_srednji.replace(',','.'), NOK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SEK_jedinica, SEK_kod, SEK_kupovni.replace(',','.'), SEK_srednji.replace(',','.'), SEK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CHF_jedinica, CHF_kod, CHF_kupovni.replace(',','.'), CHF_srednji.replace(',','.'), CHF_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (GBP_jedinica, GBP_kod, GBP_kupovni.replace(',','.'), GBP_srednji.replace(',','.'), GBP_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (USD_jedinica, USD_kod, USD_kupovni.replace(',','.'), USD_srednji.replace(',','.'), USD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (PLN_jedinica, PLN_kod, PLN_kupovni.replace(',','.'), PLN_srednji.replace(',','.'), PLN_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.RBA
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (BAM_jedinica, BAM_kod, BAM_kupovni.replace(',','.'), BAM_srednji.replace(',','.'), BAM_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

conn.commit()





