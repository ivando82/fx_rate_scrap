import datetime
import time
import requests
from json import loads
import json
import objectpath
import pyodbc


ms = datetime.datetime.now()
#print(time.mktime(ms.timetuple()) * 1000)

unix = time.mktime(ms.timetuple()) * 1000

#print(type(unix))

unix_int = int(unix)

unix_string = str(unix_int)

#print(unix_string)

#datestr = 'https://www.sberbank.hr/umbraco/api/ExchangeRates/GetRates?dateString=' + unix_string

#print(datestr)


url = 'https://www.sberbank.hr/umbraco/api/ExchangeRates/GetRates?dateString=' + unix_string

data = requests.get(url).json()


jsondata = loads(data)

#print(jsondata)

#data_dict = json.dumps(jsondata)

#print(type(data_dict))


tree_obj = objectpath.Tree(jsondata)



EUR_jedinica = tuple(tree_obj.execute('$..Unit'))[0]
EUR_kod = tuple(tree_obj.execute('$..CurrencyCode'))[0]
EUR_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[0]
EUR_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[0]
EUR_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[0]

#print(EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni)

AUD_jedinica = tuple(tree_obj.execute('$..Unit'))[1]
AUD_kod = tuple(tree_obj.execute('$..CurrencyCode'))[1]
AUD_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[1]
AUD_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[1]
AUD_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[1]

CAD_jedinica = tuple(tree_obj.execute('$..Unit'))[2]
CAD_kod = tuple(tree_obj.execute('$..CurrencyCode'))[2]
CAD_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[2]
CAD_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[2]
CAD_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[2]

print(CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni)

CZK_jedinica = tuple(tree_obj.execute('$..Unit'))[3]
CZK_kod = tuple(tree_obj.execute('$..CurrencyCode'))[3]
CZK_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[3]
CZK_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[3]
CZK_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[3]

print(CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni)

DKK_jedinica = tuple(tree_obj.execute('$..Unit'))[4]
DKK_kod = tuple(tree_obj.execute('$..CurrencyCode'))[4]
DKK_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[4]
DKK_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[4]
DKK_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[4]

print(DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni)

HUF_jedinica = tuple(tree_obj.execute('$..Unit'))[5]
HUF_kod = tuple(tree_obj.execute('$..CurrencyCode'))[5]
HUF_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[5]
HUF_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[5]
HUF_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[5]

print(HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni)


JPY_jedinica = tuple(tree_obj.execute('$..Unit'))[6]
JPY_kod = tuple(tree_obj.execute('$..CurrencyCode'))[6]
JPY_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[6]
JPY_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[6]
JPY_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[6]

print(JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni)

NOK_jedinica = tuple(tree_obj.execute('$..Unit'))[7]
NOK_kod = tuple(tree_obj.execute('$..CurrencyCode'))[7]
NOK_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[7]
NOK_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[7]
NOK_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[7]

print(NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni)

SEK_jedinica = tuple(tree_obj.execute('$..Unit'))[8]
SEK_kod = tuple(tree_obj.execute('$..CurrencyCode'))[8]
SEK_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[8]
SEK_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[8]
SEK_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[8]

print(SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni)

CHF_jedinica = tuple(tree_obj.execute('$..Unit'))[9]
CHF_kod = tuple(tree_obj.execute('$..CurrencyCode'))[9]
CHF_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[9]
CHF_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[9]
CHF_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[9]

print(CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni)

GBP_jedinica = tuple(tree_obj.execute('$..Unit'))[10]
GBP_kod = tuple(tree_obj.execute('$..CurrencyCode'))[10]
GBP_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[10]
GBP_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[10]
GBP_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[10]

print(GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni)

USD_jedinica = tuple(tree_obj.execute('$..Unit'))[11]
USD_kod = tuple(tree_obj.execute('$..CurrencyCode'))[11]
USD_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[11]
USD_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[11]
USD_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[11]

print(USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni)

PLN_jedinica = tuple(tree_obj.execute('$..Unit'))[12]
PLN_kod = tuple(tree_obj.execute('$..CurrencyCode'))[12]
PLN_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[12]
PLN_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[12]
PLN_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[12]

print(PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni)

BAM_jedinica = tuple(tree_obj.execute('$..Unit'))[13]
BAM_kod = tuple(tree_obj.execute('$..CurrencyCode'))[13]
BAM_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[13]
BAM_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[13]
BAM_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[13]

print(BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni)

RUB_jedinica = tuple(tree_obj.execute('$..Unit'))[14]
RUB_kod = tuple(tree_obj.execute('$..CurrencyCode'))[14]
RUB_kupovni = tuple(tree_obj.execute('$..NonCashBuyValue'))[14]
RUB_srednji = tuple(tree_obj.execute('$..CashMiddleValue'))[14]
RUB_prodajni = tuple(tree_obj.execute('$..NonCashSellValue'))[14]

print(RUB_jedinica, RUB_kod, RUB_kupovni, RUB_srednji, RUB_prodajni)



AR_bank_id = '096CF0C2A88A4837BFA3714CD2BD625A'
bank = 'SBER'

timeStamp = str(datetime.datetime.now())[0:-3]

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=B2ANALIZA;'
                      'Database=FX_RATES_TEST;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni, timeStamp, AR_bank_id,bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni, timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.SBER
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (RUB_jedinica, RUB_kod, RUB_kupovni, RUB_srednji, RUB_prodajni, timeStamp, AR_bank_id, bank)
)

conn.commit()