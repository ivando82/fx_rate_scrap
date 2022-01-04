import datetime
import time
import requests
from json import loads
import objectpath
import pyodbc

# Get data from URL
data_as_text = requests.get("https://local.erstebank.hr/rproxy/webdocapi/fx/current").text

# Turn to dictionary
data_dictionary = loads(data_as_text)

#print(data_dictionary)

tree_obj = objectpath.Tree(data_dictionary)


AUD_jedinica = tuple(tree_obj.execute('$..amount'))[0]
AUD_kod = tuple(tree_obj.execute('$..name'))[0]
AUD_kupovni = tuple(tree_obj.execute('$..buy'))[0]
AUD_srednji = tuple(tree_obj.execute('$..mid'))[0]
AUD_prodajni = tuple(tree_obj.execute('$..sell'))[0]

print(AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni)

CAD_jedinica = tuple(tree_obj.execute('$..amount'))[1]
CAD_kod = tuple(tree_obj.execute('$..name'))[1]
CAD_kupovni = tuple(tree_obj.execute('$..buy'))[1]
CAD_srednji = tuple(tree_obj.execute('$..mid'))[1]
CAD_prodajni = tuple(tree_obj.execute('$..sell'))[1]

print(CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni)

CZK_jedinica = tuple(tree_obj.execute('$..amount'))[2]
CZK_kod = tuple(tree_obj.execute('$..name'))[2]
CZK_kupovni = tuple(tree_obj.execute('$..buy'))[2]
CZK_srednji = tuple(tree_obj.execute('$..mid'))[2]
CZK_prodajni = tuple(tree_obj.execute('$..sell'))[2]

print(CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni)

DKK_jedinica = tuple(tree_obj.execute('$..amount'))[3]
DKK_kod = tuple(tree_obj.execute('$..name'))[3]
DKK_kupovni = tuple(tree_obj.execute('$..buy'))[3]
DKK_srednji = tuple(tree_obj.execute('$..mid'))[3]
DKK_prodajni = tuple(tree_obj.execute('$..sell'))[3]

print(DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni)

HUF_jedinica = tuple(tree_obj.execute('$..amount'))[4]
HUF_kod = tuple(tree_obj.execute('$..name'))[4]
HUF_kupovni = tuple(tree_obj.execute('$..buy'))[4]
HUF_srednji = tuple(tree_obj.execute('$..mid'))[4]
HUF_prodajni = tuple(tree_obj.execute('$..sell'))[4]

print(HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni)

JPY_jedinica = tuple(tree_obj.execute('$..amount'))[5]
JPY_kod = tuple(tree_obj.execute('$..name'))[5]
JPY_kupovni = tuple(tree_obj.execute('$..buy'))[5]
JPY_srednji = tuple(tree_obj.execute('$..mid'))[5]
JPY_prodajni = tuple(tree_obj.execute('$..sell'))[5]

print(JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni)

NOK_jedinica = tuple(tree_obj.execute('$..amount'))[6]
NOK_kod = tuple(tree_obj.execute('$..name'))[6]
NOK_kupovni = tuple(tree_obj.execute('$..buy'))[6]
NOK_srednji = tuple(tree_obj.execute('$..mid'))[6]
NOK_prodajni = tuple(tree_obj.execute('$..sell'))[6]

print(NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni)

SEK_jedinica = tuple(tree_obj.execute('$..amount'))[7]
SEK_kod = tuple(tree_obj.execute('$..name'))[7]
SEK_kupovni = tuple(tree_obj.execute('$..buy'))[7]
SEK_srednji = tuple(tree_obj.execute('$..mid'))[7]
SEK_prodajni = tuple(tree_obj.execute('$..sell'))[7]

print(SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni)

CHF_jedinica = tuple(tree_obj.execute('$..amount'))[8]
CHF_kod = tuple(tree_obj.execute('$..name'))[8]
CHF_kupovni = tuple(tree_obj.execute('$..buy'))[8]
CHF_srednji = tuple(tree_obj.execute('$..mid'))[8]
CHF_prodajni = tuple(tree_obj.execute('$..sell'))[8]

print(CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni)

GBP_jedinica = tuple(tree_obj.execute('$..amount'))[9]
GBP_kod = tuple(tree_obj.execute('$..name'))[9]
GBP_kupovni = tuple(tree_obj.execute('$..buy'))[9]
GBP_srednji = tuple(tree_obj.execute('$..mid'))[9]
GBP_prodajni = tuple(tree_obj.execute('$..sell'))[9]

print(GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni)

USD_jedinica = tuple(tree_obj.execute('$..amount'))[10]
USD_kod = tuple(tree_obj.execute('$..name'))[10]
USD_kupovni = tuple(tree_obj.execute('$..buy'))[10]
USD_srednji = tuple(tree_obj.execute('$..mid'))[10]
USD_prodajni = tuple(tree_obj.execute('$..sell'))[10]

print(USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni)

BAM_jedinica = tuple(tree_obj.execute('$..amount'))[11]
BAM_kod = tuple(tree_obj.execute('$..name'))[11]
BAM_kupovni = tuple(tree_obj.execute('$..buy'))[11]
BAM_srednji = tuple(tree_obj.execute('$..mid'))[11]
BAM_prodajni = tuple(tree_obj.execute('$..sell'))[11]

print(BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni)

EUR_jedinica = tuple(tree_obj.execute('$..amount'))[12]
EUR_kod = tuple(tree_obj.execute('$..name'))[12]
EUR_kupovni = tuple(tree_obj.execute('$..buy'))[12]
EUR_srednji = tuple(tree_obj.execute('$..mid'))[12]
EUR_prodajni = tuple(tree_obj.execute('$..sell'))[12]

print(EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni)

PLN_jedinica = tuple(tree_obj.execute('$..amount'))[13]
PLN_kod = tuple(tree_obj.execute('$..name'))[13]
PLN_kupovni = tuple(tree_obj.execute('$..buy'))[13]
PLN_srednji = tuple(tree_obj.execute('$..mid'))[13]
PLN_prodajni = tuple(tree_obj.execute('$..sell'))[13]

print(PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni)



AR_bank_id = 'F56523DACD1A471A816C2FD187D7DC37'
bank = 'ERSTE'

timeStamp = str(datetime.datetime.now())[0:-3]

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=B2ANALIZA;'
                      'Database=FX_RATES_TEST;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni, timeStamp, AR_bank_id,bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.ERSTE
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni, timeStamp, AR_bank_id, bank)
)



conn.commit()

