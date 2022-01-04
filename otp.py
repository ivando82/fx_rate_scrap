import requests
import objectpath
import pyodbc
import datetime


OTP_query_data = {
    "q1": "latest",
    "q2": "OTP",
    "q3": '',
    "q4": 'DISPLAY'
}

OTP_response = requests.post('https://www.otpbanka.hr/otp/ajax/exchange', data = OTP_query_data)

OTP_data = OTP_response.json()

#print(data)

OTP_tree_obj = objectpath.Tree(OTP_data)

AUD_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[0]
AUD_kod = tuple(OTP_tree_obj.execute('$..currency'))[0]
AUD_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[0]
AUD_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[0]
AUD_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[0]

print(AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni)

CAD_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[1]
CAD_kod = tuple(OTP_tree_obj.execute('$..currency'))[1]
CAD_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[1]
CAD_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[1]
CAD_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[1]

print(CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni)

CZK_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[2]
CZK_kod = tuple(OTP_tree_obj.execute('$..currency'))[2]
CZK_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[2]
CZK_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[2]
CZK_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[2]

print(CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni)

DKK_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[3]
DKK_kod = tuple(OTP_tree_obj.execute('$..currency'))[3]
DKK_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[3]
DKK_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[3]
DKK_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[3]

print(DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni)

HUF_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[4]
HUF_kod = tuple(OTP_tree_obj.execute('$..currency'))[4]
HUF_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[4]
HUF_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[4]
HUF_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[4]

print(HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni)

JPY_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[5]
JPY_kod = tuple(OTP_tree_obj.execute('$..currency'))[5]
JPY_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[5]
JPY_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[5]
JPY_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[5]

print(JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni)

NOK_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[6]
NOK_kod = tuple(OTP_tree_obj.execute('$..currency'))[6]
NOK_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[6]
NOK_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[6]
NOK_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[6]

print(NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni)

SEK_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[7]
SEK_kod = tuple(OTP_tree_obj.execute('$..currency'))[7]
SEK_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[7]
SEK_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[7]
SEK_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[7]

print(SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni)

CHF_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[8]
CHF_kod = tuple(OTP_tree_obj.execute('$..currency'))[8]
CHF_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[8]
CHF_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[8]
CHF_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[8]

print(CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni)

GBP_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[9]
GBP_kod = tuple(OTP_tree_obj.execute('$..currency'))[9]
GBP_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[9]
GBP_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[9]
GBP_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[9]

print(GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni)

USD_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[10]
USD_kod = tuple(OTP_tree_obj.execute('$..currency'))[10]
USD_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[10]
USD_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[10]
USD_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[10]

print(USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni)

BAM_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[11]
BAM_kod = tuple(OTP_tree_obj.execute('$..currency'))[11]
BAM_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[11]
BAM_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[11]
BAM_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[11]

print(BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni)

EUR_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[12]
EUR_kod = tuple(OTP_tree_obj.execute('$..currency'))[12]
EUR_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[12]
EUR_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[12]
EUR_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[12]

print(EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni)

PLN_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[13]
PLN_kod = tuple(OTP_tree_obj.execute('$..currency'))[13]
PLN_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[13]
PLN_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[13]
PLN_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[13]

print(PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni)



AR_bank_id = '9CBA76D0CA0F40C08ED811B299CE1A77'
bank = 'OTP'

timeStamp = str(datetime.datetime.now())[0:-3]

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=B2ANALIZA;'
                      'Database=FX_RATES_TEST;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (EUR_jedinica, EUR_kod, EUR_kupovni.replace(',','.'), EUR_srednji.replace(',','.'), EUR_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (AUD_jedinica, AUD_kod, AUD_kupovni.replace(',','.'), AUD_srednji.replace(',','.'), AUD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CAD_jedinica, CAD_kod, CAD_kupovni.replace(',','.'), CAD_srednji.replace(',','.'), CAD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CZK_jedinica, CZK_kod, CZK_kupovni.replace(',','.'), CZK_srednji.replace(',','.'), CZK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (DKK_jedinica, DKK_kod, DKK_kupovni.replace(',','.'), DKK_srednji.replace(',','.'), DKK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (HUF_jedinica, HUF_kod, HUF_kupovni.replace(',','.'), HUF_srednji.replace(',','.'), HUF_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (JPY_jedinica, JPY_kod, JPY_kupovni.replace(',','.'), JPY_srednji.replace(',','.'), JPY_prodajni.replace(',','.'), timeStamp, AR_bank_id,bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (NOK_jedinica, NOK_kod, NOK_kupovni.replace(',','.'), NOK_srednji.replace(',','.'), NOK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (SEK_jedinica, SEK_kod, SEK_kupovni.replace(',','.'), SEK_srednji.replace(',','.'), SEK_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (CHF_jedinica, CHF_kod, CHF_kupovni.replace(',','.'), CHF_srednji.replace(',','.'), CHF_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (GBP_jedinica, GBP_kod, GBP_kupovni.replace(',','.'), GBP_srednji.replace(',','.'), GBP_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (USD_jedinica, USD_kod, USD_kupovni.replace(',','.'), USD_srednji.replace(',','.'), USD_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (PLN_jedinica, PLN_kod, PLN_kupovni.replace(',','.'), PLN_srednji.replace(',','.'), PLN_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)

cursor.execute(
    '''
    INSERT INTO FX_RATES_TEST.dbo.OTP
    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    (BAM_jedinica, BAM_kod, BAM_kupovni.replace(',','.'), BAM_srednji.replace(',','.'), BAM_prodajni.replace(',','.'), timeStamp, AR_bank_id, bank)
)



conn.commit()