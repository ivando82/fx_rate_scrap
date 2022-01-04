import requests
from bs4 import BeautifulSoup
import pyodbc
import datetime
from json import loads
import objectpath
import time
import traceback
import sys


try:
    ADDIKO_url = 'https://www.addiko.hr/izracuni/tecajna-lista/'

    ADDIKO_page = requests.get(ADDIKO_url)

    ADDIKO_soup = BeautifulSoup(ADDIKO_page.text, 'html.parser')


    ADDIKO_table = ADDIKO_soup.find('table')

    ##print(table)

    ADDIKO_AUD = ADDIKO_table.find_all('tr')[1]

    ADDIKO_AUD_jedinica = ADDIKO_AUD.find_all('td')[3].text
    ADDIKO_AUD_kod = ADDIKO_AUD.find_all('td')[2].text
    ADDIKO_AUD_kupovni = ADDIKO_AUD.find_all('td')[4].text
    ADDIKO_AUD_srednji = ADDIKO_AUD.find_all('td')[5].text
    ADDIKO_AUD_prodajni = ADDIKO_AUD.find_all('td')[6].text

    #print(ADDIKO_AUD_jedinica, ADDIKO_AUD_kod, ADDIKO_AUD_kupovni, ADDIKO_AUD_srednji, ADDIKO_AUD_prodajni)

    ADDIKO_CAD = ADDIKO_table.find_all('tr')[2]

    ADDIKO_CAD_jedinica = ADDIKO_CAD.find_all('td')[3].text
    ADDIKO_CAD_kod = ADDIKO_CAD.find_all('td')[2].text
    ADDIKO_CAD_kupovni = ADDIKO_CAD.find_all('td')[4].text
    ADDIKO_CAD_srednji = ADDIKO_CAD.find_all('td')[5].text
    ADDIKO_CAD_prodajni = ADDIKO_CAD.find_all('td')[6].text

    #print(ADDIKO_CAD_jedinica, ADDIKO_CAD_kod, ADDIKO_CAD_kupovni, ADDIKO_CAD_srednji, ADDIKO_CAD_prodajni)

    ADDIKO_CZK = ADDIKO_table.find_all('tr')[3]

    ADDIKO_CZK_jedinica = ADDIKO_CZK.find_all('td')[3].text
    ADDIKO_CZK_kod = ADDIKO_CZK.find_all('td')[2].text
    ADDIKO_CZK_kupovni = ADDIKO_CZK.find_all('td')[4].text
    ADDIKO_CZK_srednji = ADDIKO_CZK.find_all('td')[5].text
    ADDIKO_CZK_prodajni = ADDIKO_CZK.find_all('td')[6].text

    #print(ADDIKO_CZK_jedinica, ADDIKO_CZK_kod, ADDIKO_CZK_kupovni, ADDIKO_CZK_srednji, ADDIKO_CZK_prodajni)

    ADDIKO_DKK = ADDIKO_table.find_all('tr')[4]

    ADDIKO_DKK_jedinica = ADDIKO_DKK.find_all('td')[3].text
    ADDIKO_DKK_kod = ADDIKO_DKK.find_all('td')[2].text
    ADDIKO_DKK_kupovni = ADDIKO_DKK.find_all('td')[4].text
    ADDIKO_DKK_srednji = ADDIKO_DKK.find_all('td')[5].text
    ADDIKO_DKK_prodajni = ADDIKO_DKK.find_all('td')[6].text

    #print(ADDIKO_DKK_jedinica, ADDIKO_DKK_kod, ADDIKO_DKK_kupovni, ADDIKO_DKK_srednji, ADDIKO_DKK_prodajni)

    ADDIKO_HUF = ADDIKO_table.find_all('tr')[5]

    ADDIKO_HUF_jedinica = ADDIKO_HUF.find_all('td')[3].text
    ADDIKO_HUF_kod = ADDIKO_HUF.find_all('td')[2].text
    ADDIKO_HUF_kupovni = ADDIKO_HUF.find_all('td')[4].text
    ADDIKO_HUF_srednji = ADDIKO_HUF.find_all('td')[5].text
    ADDIKO_HUF_prodajni = ADDIKO_HUF.find_all('td')[6].text

    #print(ADDIKO_HUF_jedinica, ADDIKO_HUF_kod, ADDIKO_HUF_kupovni, ADDIKO_HUF_srednji, ADDIKO_HUF_prodajni)

    ADDIKO_JPY = ADDIKO_table.find_all('tr')[6]

    ADDIKO_JPY_jedinica = ADDIKO_JPY.find_all('td')[3].text
    ADDIKO_JPY_kod = ADDIKO_JPY.find_all('td')[2].text
    ADDIKO_JPY_kupovni = ADDIKO_JPY.find_all('td')[4].text
    ADDIKO_JPY_srednji = ADDIKO_JPY.find_all('td')[5].text
    ADDIKO_JPY_prodajni = ADDIKO_JPY.find_all('td')[6].text

    #print(ADDIKO_JPY_jedinica, ADDIKO_JPY_kod, ADDIKO_JPY_kupovni, ADDIKO_JPY_srednji, ADDIKO_JPY_prodajni)

    ADDIKO_NOK = ADDIKO_table.find_all('tr')[7]

    ADDIKO_NOK_jedinica = ADDIKO_NOK.find_all('td')[3].text
    ADDIKO_NOK_kod = ADDIKO_NOK.find_all('td')[2].text
    ADDIKO_NOK_kupovni = ADDIKO_NOK.find_all('td')[4].text
    ADDIKO_NOK_srednji = ADDIKO_NOK.find_all('td')[5].text
    ADDIKO_NOK_prodajni = ADDIKO_NOK.find_all('td')[6].text

    #print(ADDIKO_NOK_jedinica, ADDIKO_NOK_kod, ADDIKO_NOK_kupovni, ADDIKO_NOK_srednji, ADDIKO_NOK_prodajni)

    ADDIKO_SEK = ADDIKO_table.find_all('tr')[8]

    ADDIKO_SEK_jedinica = ADDIKO_SEK.find_all('td')[3].text
    ADDIKO_SEK_kod = ADDIKO_SEK.find_all('td')[2].text
    ADDIKO_SEK_kupovni = ADDIKO_SEK.find_all('td')[4].text
    ADDIKO_SEK_srednji = ADDIKO_SEK.find_all('td')[5].text
    ADDIKO_SEK_prodajni = ADDIKO_SEK.find_all('td')[6].text

    #print(ADDIKO_SEK_jedinica, ADDIKO_SEK_kod, ADDIKO_SEK_kupovni, ADDIKO_SEK_srednji, ADDIKO_SEK_prodajni)

    ADDIKO_CHF = ADDIKO_table.find_all('tr')[9]

    ADDIKO_CHF_jedinica = ADDIKO_CHF.find_all('td')[3].text
    ADDIKO_CHF_kod = ADDIKO_CHF.find_all('td')[2].text
    ADDIKO_CHF_kupovni = ADDIKO_CHF.find_all('td')[4].text
    ADDIKO_CHF_srednji = ADDIKO_CHF.find_all('td')[5].text
    ADDIKO_CHF_prodajni = ADDIKO_CHF.find_all('td')[6].text

    #print(ADDIKO_CHF_jedinica, ADDIKO_CHF_kod, ADDIKO_CHF_kupovni, ADDIKO_CHF_srednji, ADDIKO_CHF_prodajni)

    ADDIKO_GBP = ADDIKO_table.find_all('tr')[10]

    ADDIKO_GBP_jedinica = ADDIKO_GBP.find_all('td')[3].text
    ADDIKO_GBP_kod = ADDIKO_GBP.find_all('td')[2].text
    ADDIKO_GBP_kupovni = ADDIKO_GBP.find_all('td')[4].text
    ADDIKO_GBP_srednji = ADDIKO_GBP.find_all('td')[5].text
    ADDIKO_GBP_prodajni = ADDIKO_GBP.find_all('td')[6].text

    #print(ADDIKO_GBP_jedinica, ADDIKO_GBP_kod, ADDIKO_GBP_kupovni, ADDIKO_GBP_srednji, ADDIKO_GBP_prodajni)

    ADDIKO_USD = ADDIKO_table.find_all('tr')[11]

    ADDIKO_USD_jedinica = ADDIKO_USD.find_all('td')[3].text
    ADDIKO_USD_kod = ADDIKO_USD.find_all('td')[2].text
    ADDIKO_USD_kupovni = ADDIKO_USD.find_all('td')[4].text
    ADDIKO_USD_srednji = ADDIKO_USD.find_all('td')[5].text
    ADDIKO_USD_prodajni = ADDIKO_USD.find_all('td')[6].text

    #print(ADDIKO_USD_jedinica, ADDIKO_USD_kod, ADDIKO_USD_kupovni, ADDIKO_USD_srednji, ADDIKO_USD_prodajni)

    ADDIKO_EUR = ADDIKO_table.find_all('tr')[12]

    ADDIKO_EUR_jedinica = ADDIKO_EUR.find_all('td')[3].text
    ADDIKO_EUR_kod = ADDIKO_EUR.find_all('td')[2].text
    ADDIKO_EUR_kupovni = ADDIKO_EUR.find_all('td')[4].text
    ADDIKO_EUR_srednji = ADDIKO_EUR.find_all('td')[5].text
    ADDIKO_EUR_prodajni = ADDIKO_EUR.find_all('td')[6].text

    #print(ADDIKO_EUR_jedinica, ADDIKO_EUR_kod, ADDIKO_EUR_kupovni, ADDIKO_EUR_srednji, ADDIKO_EUR_prodajni)

    ADDIKO_PLN = ADDIKO_table.find_all('tr')[13]

    ADDIKO_PLN_jedinica = ADDIKO_PLN.find_all('td')[3].text
    ADDIKO_PLN_kod = ADDIKO_PLN.find_all('td')[2].text
    ADDIKO_PLN_kupovni = ADDIKO_PLN.find_all('td')[4].text
    ADDIKO_PLN_srednji = ADDIKO_PLN.find_all('td')[5].text
    ADDIKO_PLN_prodajni = ADDIKO_PLN.find_all('td')[6].text

    #print(ADDIKO_PLN_jedinica, ADDIKO_PLN_kod, ADDIKO_PLN_kupovni, ADDIKO_PLN_srednji, ADDIKO_PLN_prodajni)

    ADDIKO_BAM = ADDIKO_table.find_all('tr')[14]

    ADDIKO_BAM_jedinica = ADDIKO_BAM.find_all('td')[3].text
    ADDIKO_BAM_kod = ADDIKO_BAM.find_all('td')[2].text
    ADDIKO_BAM_kupovni = ADDIKO_BAM.find_all('td')[4].text
    ADDIKO_BAM_srednji = ADDIKO_BAM.find_all('td')[5].text
    ADDIKO_BAM_prodajni = ADDIKO_BAM.find_all('td')[6].text

    #print(ADDIKO_BAM_jedinica, ADDIKO_BAM_kod, ADDIKO_BAM_kupovni, ADDIKO_BAM_srednji, ADDIKO_BAM_prodajni)




    ADDIKO_AR_bank_id = '79A59AAFF950430B83A2AB8D55A23F9C'

    ADDIKO_bank = 'ADDIKO'


    timeStamp = str(datetime.datetime.now())[0:-3]

    ADDIKO_conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=B2ANALIZA;'
                          'Database=FX_RATES_CHECK;'
                          'Trusted_Connection=no;'
                          'UID=kpitest;'
                          'PWD=Logitech2020!;' )

    ADDIKO_cursor = ADDIKO_conn.cursor()

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_EUR_jedinica, ADDIKO_EUR_kod, ADDIKO_EUR_kupovni.replace(',','.'), ADDIKO_EUR_srednji.replace(',','.'), ADDIKO_EUR_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_AUD_jedinica, ADDIKO_AUD_kod, ADDIKO_AUD_kupovni.replace(',','.'), ADDIKO_AUD_srednji.replace(',','.'), ADDIKO_AUD_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_CAD_jedinica, ADDIKO_CAD_kod, ADDIKO_CAD_kupovni.replace(',','.'), ADDIKO_CAD_srednji.replace(',','.'), ADDIKO_CAD_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_CZK_jedinica, ADDIKO_CZK_kod, ADDIKO_CZK_kupovni.replace(',','.'), ADDIKO_CZK_srednji.replace(',','.'), ADDIKO_CZK_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_DKK_jedinica, ADDIKO_DKK_kod, ADDIKO_DKK_kupovni.replace(',','.'), ADDIKO_DKK_srednji.replace(',','.'), ADDIKO_DKK_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_HUF_jedinica, ADDIKO_HUF_kod, ADDIKO_HUF_kupovni.replace(',','.'), ADDIKO_HUF_srednji.replace(',','.'), ADDIKO_HUF_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_JPY_jedinica, ADDIKO_JPY_kod, ADDIKO_JPY_kupovni.replace(',','.'), ADDIKO_JPY_srednji.replace(',','.'), ADDIKO_JPY_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id,ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_NOK_jedinica, ADDIKO_NOK_kod, ADDIKO_NOK_kupovni.replace(',','.'), ADDIKO_NOK_srednji.replace(',','.'), ADDIKO_NOK_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_SEK_jedinica, ADDIKO_SEK_kod, ADDIKO_SEK_kupovni.replace(',','.'), ADDIKO_SEK_srednji.replace(',','.'), ADDIKO_SEK_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_CHF_jedinica, ADDIKO_CHF_kod, ADDIKO_CHF_kupovni.replace(',','.'), ADDIKO_CHF_srednji.replace(',','.'), ADDIKO_CHF_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_GBP_jedinica, ADDIKO_GBP_kod, ADDIKO_GBP_kupovni.replace(',','.'), ADDIKO_GBP_srednji.replace(',','.'), ADDIKO_GBP_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_USD_jedinica, ADDIKO_USD_kod, ADDIKO_USD_kupovni.replace(',','.'), ADDIKO_USD_srednji.replace(',','.'), ADDIKO_USD_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_PLN_jedinica, ADDIKO_PLN_kod, ADDIKO_PLN_kupovni.replace(',','.'), ADDIKO_PLN_srednji.replace(',','.'), ADDIKO_PLN_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (ADDIKO_BAM_jedinica, ADDIKO_BAM_kod, ADDIKO_BAM_kupovni.replace(',','.'), ADDIKO_BAM_srednji.replace(',','.'), ADDIKO_BAM_prodajni.replace(',','.'), timeStamp, ADDIKO_AR_bank_id, ADDIKO_bank)
    )

    ADDIKO_conn.commit()

except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    error = (''.join('!! ' + line for line in lines))
    ErrortimeStamp = str(datetime.datetime.now())[0:-3]
    error_conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=B2ANALIZA;'
                                'Database=FX_RATES_CHECK;'
                                'Trusted_Connection=no;'
                                'UID=kpitest;'
                                'PWD=Logitech2020!;')

    error_cursor = error_conn.cursor()
    error_cursor.execute(
        '''
                INSERT INTO FX_RATES_CHECK.dbo.errorlog
                (bank, error, date)
                VALUES (?, ?, ?)
                ''',
        ('ADDIKO', error, ErrortimeStamp))
    error_conn.commit()

######################################################################################################################################################################
######################################################################################################################################################################
                                                    #PBZ


try:
   PBZ_xml = requests.get('https://www.pbz.hr/Downloads/PBZteclist.xml').text

   PBZ_data = BeautifulSoup(PBZ_xml, 'xml')

   PBZ_AUD_jedinica = PBZ_data.find_all('Unit')[0].text
   PBZ_AUD_kod = PBZ_data.find_all('Name')[0].text
   PBZ_AUD_kupovni = PBZ_data.find_all('BuyRateForeign')[0].text
   PBZ_AUD_srednji = PBZ_data.find_all('MeanRate')[0].text
   PBZ_AUD_prodajni = PBZ_data.find_all('SellRateForeign')[0].text

   #print(PBZ_AUD_jedinica, PBZ_AUD_kod, PBZ_AUD_kupovni, PBZ_AUD_srednji, PBZ_AUD_prodajni)

   PBZ_CAD_jedinica = PBZ_data.find_all('Unit')[1].text
   PBZ_CAD_kod = PBZ_data.find_all('Name')[1].text
   PBZ_CAD_kupovni = PBZ_data.find_all('BuyRateForeign')[1].text
   PBZ_CAD_srednji = PBZ_data.find_all('MeanRate')[1].text
   PBZ_CAD_prodajni = PBZ_data.find_all('SellRateForeign')[1].text

   #print(PBZ_CAD_jedinica, PBZ_CAD_kod, PBZ_CAD_kupovni, PBZ_CAD_srednji, PBZ_CAD_prodajni)

   PBZ_CZK_jedinica = PBZ_data.find_all('Unit')[2].text
   PBZ_CZK_kod = PBZ_data.find_all('Name')[2].text
   PBZ_CZK_kupovni = PBZ_data.find_all('BuyRateForeign')[2].text
   PBZ_CZK_srednji = PBZ_data.find_all('MeanRate')[2].text
   PBZ_CZK_prodajni = PBZ_data.find_all('SellRateForeign')[2].text

   #print(PBZ_CZK_jedinica, PBZ_CZK_kod, PBZ_CZK_kupovni, PBZ_CZK_srednji, PBZ_CZK_prodajni)


   PBZ_DKK_jedinica = PBZ_data.find_all('Unit')[3].text
   PBZ_DKK_kod = PBZ_data.find_all('Name')[3].text
   PBZ_DKK_kupovni = PBZ_data.find_all('BuyRateForeign')[3].text
   PBZ_DKK_srednji = PBZ_data.find_all('MeanRate')[3].text
   PBZ_DKK_prodajni = PBZ_data.find_all('SellRateForeign')[3].text

   #print(PBZ_DKK_jedinica, PBZ_DKK_kod, PBZ_DKK_kupovni, PBZ_DKK_srednji, PBZ_DKK_prodajni)

   PBZ_HUF_jedinica = PBZ_data.find_all('Unit')[4].text
   PBZ_HUF_kod = PBZ_data.find_all('Name')[4].text
   PBZ_HUF_kupovni = PBZ_data.find_all('BuyRateForeign')[4].text
   PBZ_HUF_srednji = PBZ_data.find_all('MeanRate')[4].text
   PBZ_HUF_prodajni = PBZ_data.find_all('SellRateForeign')[4].text

   #print(PBZ_HUF_jedinica, PBZ_HUF_kod, PBZ_HUF_kupovni, PBZ_HUF_srednji, PBZ_HUF_prodajni)

   PBZ_JPY_jedinica = PBZ_data.find_all('Unit')[5].text
   PBZ_JPY_kod = PBZ_data.find_all('Name')[5].text
   PBZ_JPY_kupovni = PBZ_data.find_all('BuyRateForeign')[5].text
   PBZ_JPY_srednji = PBZ_data.find_all('MeanRate')[5].text
   PBZ_JPY_prodajni = PBZ_data.find_all('SellRateForeign')[5].text

   #print(PBZ_JPY_jedinica, PBZ_JPY_kod, PBZ_JPY_kupovni, PBZ_JPY_srednji, PBZ_JPY_prodajni)

   PBZ_NOK_jedinica = PBZ_data.find_all('Unit')[6].text
   PBZ_NOK_kod = PBZ_data.find_all('Name')[6].text
   PBZ_NOK_kupovni = PBZ_data.find_all('BuyRateForeign')[6].text
   PBZ_NOK_srednji = PBZ_data.find_all('MeanRate')[6].text
   PBZ_NOK_prodajni = PBZ_data.find_all('SellRateForeign')[6].text

   #print(PBZ_NOK_jedinica, PBZ_NOK_kod, PBZ_NOK_kupovni, PBZ_NOK_srednji, PBZ_NOK_prodajni)

   PBZ_SEK_jedinica = PBZ_data.find_all('Unit')[7].text
   PBZ_SEK_kod = PBZ_data.find_all('Name')[7].text
   PBZ_SEK_kupovni = PBZ_data.find_all('BuyRateForeign')[7].text
   PBZ_SEK_srednji = PBZ_data.find_all('MeanRate')[7].text
   PBZ_SEK_prodajni = PBZ_data.find_all('SellRateForeign')[7].text

   #print(PBZ_SEK_jedinica, PBZ_SEK_kod, PBZ_SEK_kupovni, PBZ_SEK_srednji, PBZ_SEK_prodajni)

   PBZ_CHF_jedinica = PBZ_data.find_all('Unit')[8].text
   PBZ_CHF_kod = PBZ_data.find_all('Name')[8].text
   PBZ_CHF_kupovni = PBZ_data.find_all('BuyRateForeign')[8].text
   PBZ_CHF_srednji = PBZ_data.find_all('MeanRate')[8].text
   PBZ_CHF_prodajni = PBZ_data.find_all('SellRateForeign')[8].text

   #print(PBZ_CHF_jedinica, PBZ_CHF_kod, PBZ_CHF_kupovni, PBZ_CHF_srednji, PBZ_CHF_prodajni)

   PBZ_GBP_jedinica = PBZ_data.find_all('Unit')[9].text
   PBZ_GBP_kod = PBZ_data.find_all('Name')[9].text
   PBZ_GBP_kupovni = PBZ_data.find_all('BuyRateForeign')[9].text
   PBZ_GBP_srednji = PBZ_data.find_all('MeanRate')[9].text
   PBZ_GBP_prodajni = PBZ_data.find_all('SellRateForeign')[9].text

   #print(PBZ_GBP_jedinica, PBZ_GBP_kod, PBZ_GBP_kupovni, PBZ_GBP_srednji, PBZ_GBP_prodajni)

   PBZ_USD_jedinica = PBZ_data.find_all('Unit')[10].text
   PBZ_USD_kod = PBZ_data.find_all('Name')[10].text
   PBZ_USD_kupovni = PBZ_data.find_all('BuyRateForeign')[10].text
   PBZ_USD_srednji = PBZ_data.find_all('MeanRate')[10].text
   PBZ_USD_prodajni = PBZ_data.find_all('SellRateForeign')[10].text

   #print(PBZ_USD_jedinica, PBZ_USD_kod, PBZ_USD_kupovni, PBZ_USD_srednji, PBZ_USD_prodajni)

   PBZ_BAM_jedinica = PBZ_data.find_all('Unit')[11].text
   PBZ_BAM_kod = PBZ_data.find_all('Name')[11].text
   PBZ_BAM_kupovni = PBZ_data.find_all('BuyRateForeign')[11].text
   PBZ_BAM_srednji = PBZ_data.find_all('MeanRate')[11].text
   PBZ_BAM_prodajni = PBZ_data.find_all('SellRateForeign')[11].text

   #print(PBZ_BAM_jedinica, PBZ_BAM_kod, PBZ_BAM_kupovni, PBZ_BAM_srednji, PBZ_BAM_prodajni)

   PBZ_EUR_jedinica = PBZ_data.find_all('Unit')[12].text
   PBZ_EUR_kod = PBZ_data.find_all('Name')[12].text
   PBZ_EUR_kupovni = PBZ_data.find_all('BuyRateForeign')[12].text
   PBZ_EUR_srednji = PBZ_data.find_all('MeanRate')[12].text
   PBZ_EUR_prodajni = PBZ_data.find_all('SellRateForeign')[12].text

   #print(PBZ_EUR_jedinica, PBZ_EUR_kod, PBZ_EUR_kupovni, PBZ_EUR_srednji, PBZ_EUR_prodajni)

   PBZ_PLN_jedinica = PBZ_data.find_all('Unit')[13].text
   PBZ_PLN_kod = PBZ_data.find_all('Name')[13].text
   PBZ_PLN_kupovni = PBZ_data.find_all('BuyRateForeign')[13].text
   PBZ_PLN_srednji = PBZ_data.find_all('MeanRate')[13].text
   PBZ_PLN_prodajni = PBZ_data.find_all('SellRateForeign')[13].text

   #print(PBZ_PLN_jedinica, PBZ_PLN_kod, PBZ_PLN_kupovni, PBZ_PLN_srednji, PBZ_PLN_prodajni)


   PBZ_AR_bank_id = '610CCE1C353044FCABCB0362192998DF'

   PBZ_bank = 'PBZ'


   timeStamp = str(datetime.datetime.now())[0:-3]

   PBZ_conn = pyodbc.connect('Driver={SQL Server};'
                         'Server=B2ANALIZA;'
                         'Database=FX_RATES_CHECK;'
                         'Trusted_Connection=no;'
                         'UID=kpitest;'
                         'PWD=Logitech2020!;' )

   PBZ_cursor = PBZ_conn.cursor()

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_EUR_jedinica, PBZ_EUR_kod, PBZ_EUR_kupovni.replace(',','.'), PBZ_EUR_srednji.replace(',','.'), PBZ_EUR_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_AUD_jedinica, PBZ_AUD_kod, PBZ_AUD_kupovni.replace(',','.'), PBZ_AUD_srednji.replace(',','.'), PBZ_AUD_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_CAD_jedinica, PBZ_CAD_kod, PBZ_CAD_kupovni.replace(',','.'), PBZ_CAD_srednji.replace(',','.'), PBZ_CAD_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_CZK_jedinica, PBZ_CZK_kod, PBZ_CZK_kupovni.replace(',','.'), PBZ_CZK_srednji.replace(',','.'), PBZ_CZK_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_DKK_jedinica, PBZ_DKK_kod, PBZ_DKK_kupovni.replace(',','.'), PBZ_DKK_srednji.replace(',','.'), PBZ_DKK_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_HUF_jedinica, PBZ_HUF_kod, PBZ_HUF_kupovni.replace(',','.'), PBZ_HUF_srednji.replace(',','.'), PBZ_HUF_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_JPY_jedinica, PBZ_JPY_kod, PBZ_JPY_kupovni.replace(',','.'), PBZ_JPY_srednji.replace(',','.'), PBZ_JPY_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id,PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_NOK_jedinica, PBZ_NOK_kod, PBZ_NOK_kupovni.replace(',','.'), PBZ_NOK_srednji.replace(',','.'), PBZ_NOK_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_SEK_jedinica, PBZ_SEK_kod, PBZ_SEK_kupovni.replace(',','.'), PBZ_SEK_srednji.replace(',','.'), PBZ_SEK_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_CHF_jedinica, PBZ_CHF_kod, PBZ_CHF_kupovni.replace(',','.'), PBZ_CHF_srednji.replace(',','.'), PBZ_CHF_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_GBP_jedinica, PBZ_GBP_kod, PBZ_GBP_kupovni.replace(',','.'), PBZ_GBP_srednji.replace(',','.'), PBZ_GBP_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_USD_jedinica, PBZ_USD_kod, PBZ_USD_kupovni.replace(',','.'), PBZ_USD_srednji.replace(',','.'), PBZ_USD_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_PLN_jedinica, PBZ_PLN_kod, PBZ_PLN_kupovni.replace(',','.'), PBZ_PLN_srednji.replace(',','.'), PBZ_PLN_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (PBZ_BAM_jedinica, PBZ_BAM_kod, PBZ_BAM_kupovni.replace(',','.'), PBZ_BAM_srednji.replace(',','.'), PBZ_BAM_prodajni.replace(',','.'), timeStamp, PBZ_AR_bank_id, PBZ_bank)
   )

   PBZ_conn.commit()

except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    error = (''.join('!! ' + line for line in lines))
    ErrortimeStamp = str(datetime.datetime.now())[0:-3]
    error_conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=B2ANALIZA;'
                                'Database=FX_RATES_CHECK;'
                                'Trusted_Connection=no;'
                                'UID=kpitest;'
                                'PWD=Logitech2020!;')

    error_cursor = error_conn.cursor()
    error_cursor.execute(
        '''
                INSERT INTO FX_RATES_CHECK.dbo.errorlog
                (bank, error, date)
                VALUES (?, ?, ?)
                ''',
        ('PBZ', error, ErrortimeStamp))
    error_conn.commit()

######################################################################################################################################################################
######################################################################################################################################################################
                                                            #ERSTE

try:

   ERSTE_data_as_text = requests.get("https://local.erstebank.hr/rproxy/webdocapi/fx/current").text

   # Turn to dictionary
   ERSTE_data_dictionary = loads(ERSTE_data_as_text)

   ##print(data_dictionary)

   ERSTE_tree_obj = objectpath.Tree(ERSTE_data_dictionary)


   ERSTE_AUD_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[0]
   ERSTE_AUD_kod = tuple(ERSTE_tree_obj.execute('$..name'))[0]
   ERSTE_AUD_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[0]
   ERSTE_AUD_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[0]
   ERSTE_AUD_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[0]

   #print(ERSTE_AUD_jedinica, ERSTE_AUD_kod, ERSTE_AUD_kupovni, ERSTE_AUD_srednji, ERSTE_AUD_prodajni)

   ERSTE_CAD_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[1]
   ERSTE_CAD_kod = tuple(ERSTE_tree_obj.execute('$..name'))[1]
   ERSTE_CAD_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[1]
   ERSTE_CAD_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[1]
   ERSTE_CAD_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[1]

   #print(ERSTE_CAD_jedinica, ERSTE_CAD_kod, ERSTE_CAD_kupovni, ERSTE_CAD_srednji, ERSTE_CAD_prodajni)

   ERSTE_CZK_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[2]
   ERSTE_CZK_kod = tuple(ERSTE_tree_obj.execute('$..name'))[2]
   ERSTE_CZK_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[2]
   ERSTE_CZK_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[2]
   ERSTE_CZK_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[2]

   #print(ERSTE_CZK_jedinica, ERSTE_CZK_kod, ERSTE_CZK_kupovni, ERSTE_CZK_srednji, ERSTE_CZK_prodajni)

   ERSTE_DKK_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[3]
   ERSTE_DKK_kod = tuple(ERSTE_tree_obj.execute('$..name'))[3]
   ERSTE_DKK_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[3]
   ERSTE_DKK_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[3]
   ERSTE_DKK_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[3]

   #print(ERSTE_DKK_jedinica, ERSTE_DKK_kod, ERSTE_DKK_kupovni, ERSTE_DKK_srednji, ERSTE_DKK_prodajni)

   ERSTE_HUF_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[4]
   ERSTE_HUF_kod = tuple(ERSTE_tree_obj.execute('$..name'))[4]
   ERSTE_HUF_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[4]
   ERSTE_HUF_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[4]
   ERSTE_HUF_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[4]

   #print(ERSTE_HUF_jedinica, ERSTE_HUF_kod, ERSTE_HUF_kupovni, ERSTE_HUF_srednji, ERSTE_HUF_prodajni)

   ERSTE_JPY_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[5]
   ERSTE_JPY_kod = tuple(ERSTE_tree_obj.execute('$..name'))[5]
   ERSTE_JPY_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[5]
   ERSTE_JPY_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[5]
   ERSTE_JPY_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[5]

   #print(ERSTE_JPY_jedinica, ERSTE_JPY_kod, ERSTE_JPY_kupovni, ERSTE_JPY_srednji, ERSTE_JPY_prodajni)

   ERSTE_NOK_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[6]
   ERSTE_NOK_kod = tuple(ERSTE_tree_obj.execute('$..name'))[6]
   ERSTE_NOK_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[6]
   ERSTE_NOK_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[6]
   ERSTE_NOK_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[6]

   #print(ERSTE_NOK_jedinica, ERSTE_NOK_kod, ERSTE_NOK_kupovni, ERSTE_NOK_srednji, ERSTE_NOK_prodajni)

   ERSTE_SEK_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[7]
   ERSTE_SEK_kod = tuple(ERSTE_tree_obj.execute('$..name'))[7]
   ERSTE_SEK_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[7]
   ERSTE_SEK_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[7]
   ERSTE_SEK_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[7]

   #print(ERSTE_SEK_jedinica, ERSTE_SEK_kod, ERSTE_SEK_kupovni, ERSTE_SEK_srednji, ERSTE_SEK_prodajni)

   ERSTE_CHF_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[8]
   ERSTE_CHF_kod = tuple(ERSTE_tree_obj.execute('$..name'))[8]
   ERSTE_CHF_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[8]
   ERSTE_CHF_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[8]
   ERSTE_CHF_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[8]

   #print(ERSTE_CHF_jedinica, ERSTE_CHF_kod, ERSTE_CHF_kupovni, ERSTE_CHF_srednji, ERSTE_CHF_prodajni)

   ERSTE_GBP_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[9]
   ERSTE_GBP_kod = tuple(ERSTE_tree_obj.execute('$..name'))[9]
   ERSTE_GBP_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[9]
   ERSTE_GBP_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[9]
   ERSTE_GBP_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[9]

   #print(ERSTE_GBP_jedinica, ERSTE_GBP_kod, ERSTE_GBP_kupovni, ERSTE_GBP_srednji, ERSTE_GBP_prodajni)

   ERSTE_USD_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[10]
   ERSTE_USD_kod = tuple(ERSTE_tree_obj.execute('$..name'))[10]
   ERSTE_USD_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[10]
   ERSTE_USD_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[10]
   ERSTE_USD_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[10]

   #print(ERSTE_USD_jedinica, ERSTE_USD_kod, ERSTE_USD_kupovni, ERSTE_USD_srednji, ERSTE_USD_prodajni)

   ERSTE_BAM_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[11]
   ERSTE_BAM_kod = tuple(ERSTE_tree_obj.execute('$..name'))[11]
   ERSTE_BAM_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[11]
   ERSTE_BAM_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[11]
   ERSTE_BAM_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[11]

   #print(ERSTE_BAM_jedinica, ERSTE_BAM_kod, ERSTE_BAM_kupovni, ERSTE_BAM_srednji, ERSTE_BAM_prodajni)

   ERSTE_EUR_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[12]
   ERSTE_EUR_kod = tuple(ERSTE_tree_obj.execute('$..name'))[12]
   ERSTE_EUR_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[12]
   ERSTE_EUR_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[12]
   ERSTE_EUR_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[12]

   #print(ERSTE_EUR_jedinica, ERSTE_EUR_kod, ERSTE_EUR_kupovni, ERSTE_EUR_srednji, ERSTE_EUR_prodajni)

   ERSTE_PLN_jedinica = tuple(ERSTE_tree_obj.execute('$..amount'))[13]
   ERSTE_PLN_kod = tuple(ERSTE_tree_obj.execute('$..name'))[13]
   ERSTE_PLN_kupovni = tuple(ERSTE_tree_obj.execute('$..buy'))[13]
   ERSTE_PLN_srednji = tuple(ERSTE_tree_obj.execute('$..mid'))[13]
   ERSTE_PLN_prodajni = tuple(ERSTE_tree_obj.execute('$..sell'))[13]

   #print(ERSTE_PLN_jedinica, ERSTE_PLN_kod, ERSTE_PLN_kupovni, ERSTE_PLN_srednji, ERSTE_PLN_prodajni)



   ERSTE_AR_bank_id = 'F56523DACD1A471A816C2FD187D7DC37'
   ERSTE_bank = 'ERSTE'

   timeStamp = str(datetime.datetime.now())[0:-3]

   ERSTE_conn = pyodbc.connect('Driver={SQL Server};'
                         'Server=B2ANALIZA;'
                         'Database=FX_RATES_CHECK;'
                         'Trusted_Connection=no;'
                         'UID=kpitest;'
                         'PWD=Logitech2020!;' )

   ERSTE_cursor = ERSTE_conn.cursor()

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_EUR_jedinica, ERSTE_EUR_kod, ERSTE_EUR_kupovni, ERSTE_EUR_srednji, ERSTE_EUR_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_AUD_jedinica, ERSTE_AUD_kod, ERSTE_AUD_kupovni, ERSTE_AUD_srednji, ERSTE_AUD_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_CAD_jedinica, ERSTE_CAD_kod, ERSTE_CAD_kupovni, ERSTE_CAD_srednji, ERSTE_CAD_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_CZK_jedinica, ERSTE_CZK_kod, ERSTE_CZK_kupovni, ERSTE_CZK_srednji, ERSTE_CZK_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_DKK_jedinica, ERSTE_DKK_kod, ERSTE_DKK_kupovni, ERSTE_DKK_srednji, ERSTE_DKK_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_HUF_jedinica, ERSTE_HUF_kod, ERSTE_HUF_kupovni, ERSTE_HUF_srednji, ERSTE_HUF_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_JPY_jedinica, ERSTE_JPY_kod, ERSTE_JPY_kupovni, ERSTE_JPY_srednji, ERSTE_JPY_prodajni, timeStamp, ERSTE_AR_bank_id,ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_NOK_jedinica, ERSTE_NOK_kod, ERSTE_NOK_kupovni, ERSTE_NOK_srednji, ERSTE_NOK_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_SEK_jedinica, ERSTE_SEK_kod, ERSTE_SEK_kupovni, ERSTE_SEK_srednji, ERSTE_SEK_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_CHF_jedinica, ERSTE_CHF_kod, ERSTE_CHF_kupovni, ERSTE_CHF_srednji, ERSTE_CHF_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_GBP_jedinica, ERSTE_GBP_kod, ERSTE_GBP_kupovni, ERSTE_GBP_srednji, ERSTE_GBP_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_USD_jedinica, ERSTE_USD_kod, ERSTE_USD_kupovni, ERSTE_USD_srednji, ERSTE_USD_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_PLN_jedinica, ERSTE_PLN_kod, ERSTE_PLN_kupovni, ERSTE_PLN_srednji, ERSTE_PLN_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )

   ERSTE_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (ERSTE_BAM_jedinica, ERSTE_BAM_kod, ERSTE_BAM_kupovni, ERSTE_BAM_srednji, ERSTE_BAM_prodajni, timeStamp, ERSTE_AR_bank_id, ERSTE_bank)
   )


   ERSTE_conn.commit()

except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    error = (''.join('!! ' + line for line in lines))
    ErrortimeStamp = str(datetime.datetime.now())[0:-3]
    error_conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=B2ANALIZA;'
                                'Database=FX_RATES_CHECK;'
                                'Trusted_Connection=no;'
                                'UID=kpitest;'
                                'PWD=Logitech2020!;')

    error_cursor = error_conn.cursor()
    error_cursor.execute(
        '''
                INSERT INTO FX_RATES_CHECK.dbo.errorlog
                (bank, error, date)
                VALUES (?, ?, ?)
                ''',
        ('ERSTE', error, ErrortimeStamp))
    error_conn.commit()


######################################################################################################################################################################
######################################################################################################################################################################
                                                    #SBER

try:

    SBER_ms = datetime.datetime.now()
    ##print(time.mktime(ms.timetuple()) * 1000)

    SBER_unix = time.mktime(SBER_ms.timetuple()) * 1000

    ##print(type(unix))

    SBER_unix_int = int(SBER_unix)

    SBER_unix_string = str(SBER_unix_int)

    ##print(unix_string)

    #datestr = 'https://www.sberbank.hr/umbraco/api/ExchangeRates/GetRates?dateString=' + unix_string

    ##print(datestr)


    SBER_url = 'https://www.sberbank.hr/umbraco/api/ExchangeRates/GetRates?dateString=' + SBER_unix_string

    SBER_data = requests.get(SBER_url).json()


    SBER_jsondata = loads(SBER_data)

    ##print(jsondata)

    #data_dict = json.dumps(jsondata)

    ##print(type(data_dict))


    SBER_tree_obj = objectpath.Tree(SBER_jsondata)



    SBER_EUR_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[0]
    SBER_EUR_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[0]
    SBER_EUR_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[0]
    SBER_EUR_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[0]
    SBER_EUR_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[0]

    ##print(SBER_EUR_jedinica, SBER_EUR_kod, SBER_EUR_kupovni, SBER_EUR_srednji, SBER_EUR_prodajni)

    SBER_AUD_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[1]
    SBER_AUD_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[1]
    SBER_AUD_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[1]
    SBER_AUD_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[1]
    SBER_AUD_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[1]

    SBER_CAD_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[2]
    SBER_CAD_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[2]
    SBER_CAD_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[2]
    SBER_CAD_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[2]
    SBER_CAD_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[2]

    #print(SBER_CAD_jedinica, SBER_CAD_kod, SBER_CAD_kupovni, SBER_CAD_srednji, SBER_CAD_prodajni)

    SBER_CZK_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[3]
    SBER_CZK_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[3]
    SBER_CZK_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[3]
    SBER_CZK_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[3]
    SBER_CZK_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[3]

    #print(SBER_CZK_jedinica, SBER_CZK_kod, SBER_CZK_kupovni, SBER_CZK_srednji, SBER_CZK_prodajni)

    SBER_DKK_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[4]
    SBER_DKK_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[4]
    SBER_DKK_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[4]
    SBER_DKK_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[4]
    SBER_DKK_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[4]

    #print(SBER_DKK_jedinica, SBER_DKK_kod, SBER_DKK_kupovni, SBER_DKK_srednji, SBER_DKK_prodajni)

    SBER_HUF_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[5]
    SBER_HUF_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[5]
    SBER_HUF_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[5]
    SBER_HUF_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[5]
    SBER_HUF_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[5]

    #print(SBER_HUF_jedinica, SBER_HUF_kod, SBER_HUF_kupovni, SBER_HUF_srednji, SBER_HUF_prodajni)


    SBER_JPY_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[6]
    SBER_JPY_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[6]
    SBER_JPY_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[6]
    SBER_JPY_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[6]
    SBER_JPY_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[6]

    #print(SBER_JPY_jedinica, SBER_JPY_kod, SBER_JPY_kupovni, SBER_JPY_srednji, SBER_JPY_prodajni)

    SBER_NOK_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[7]
    SBER_NOK_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[7]
    SBER_NOK_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[7]
    SBER_NOK_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[7]
    SBER_NOK_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[7]

    #print(SBER_NOK_jedinica, SBER_NOK_kod, SBER_NOK_kupovni, SBER_NOK_srednji, SBER_NOK_prodajni)

    SBER_SEK_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[8]
    SBER_SEK_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[8]
    SBER_SEK_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[8]
    SBER_SEK_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[8]
    SBER_SEK_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[8]

    #print(SBER_SEK_jedinica, SBER_SEK_kod, SBER_SEK_kupovni, SBER_SEK_srednji, SBER_SEK_prodajni)

    SBER_CHF_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[9]
    SBER_CHF_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[9]
    SBER_CHF_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[9]
    SBER_CHF_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[9]
    SBER_CHF_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[9]

    #print(SBER_CHF_jedinica, SBER_CHF_kod, SBER_CHF_kupovni, SBER_CHF_srednji, SBER_CHF_prodajni)

    SBER_GBP_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[10]
    SBER_GBP_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[10]
    SBER_GBP_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[10]
    SBER_GBP_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[10]
    SBER_GBP_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[10]

    #print(SBER_GBP_jedinica, SBER_GBP_kod, SBER_GBP_kupovni, SBER_GBP_srednji, SBER_GBP_prodajni)

    SBER_USD_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[11]
    SBER_USD_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[11]
    SBER_USD_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[11]
    SBER_USD_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[11]
    SBER_USD_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[11]

    #print(SBER_USD_jedinica, SBER_USD_kod, SBER_USD_kupovni, SBER_USD_srednji, SBER_USD_prodajni)

    SBER_PLN_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[12]
    SBER_PLN_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[12]
    SBER_PLN_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[12]
    SBER_PLN_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[12]
    SBER_PLN_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[12]

    #print(SBER_PLN_jedinica, SBER_PLN_kod, SBER_PLN_kupovni, SBER_PLN_srednji, SBER_PLN_prodajni)

    SBER_BAM_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[13]
    SBER_BAM_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[13]
    SBER_BAM_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[13]
    SBER_BAM_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[13]
    SBER_BAM_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[13]

    #print(SBER_BAM_jedinica, SBER_BAM_kod, SBER_BAM_kupovni, SBER_BAM_srednji, SBER_BAM_prodajni)

    SBER_RUB_jedinica = tuple(SBER_tree_obj.execute('$..Unit'))[14]
    SBER_RUB_kod = tuple(SBER_tree_obj.execute('$..CurrencyCode'))[14]
    SBER_RUB_kupovni = tuple(SBER_tree_obj.execute('$..NonCashBuyValue'))[14]
    SBER_RUB_srednji = tuple(SBER_tree_obj.execute('$..CashMiddleValue'))[14]
    SBER_RUB_prodajni = tuple(SBER_tree_obj.execute('$..NonCashSellValue'))[14]

    #print(SBER_RUB_jedinica, SBER_RUB_kod, SBER_RUB_kupovni, SBER_RUB_srednji, SBER_RUB_prodajni)



    SBER_AR_bank_id = '096CF0C2A88A4837BFA3714CD2BD625A'
    SBER_bank = 'SBER'

    timeStamp = str(datetime.datetime.now())[0:-3]

    SBER_conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=B2ANALIZA;'
                          'Database=FX_RATES_CHECK;'
                          'Trusted_Connection=no;'
                          'UID=kpitest;'
                          'PWD=Logitech2020!;' )

    SBER_cursor = SBER_conn.cursor()

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_EUR_jedinica, SBER_EUR_kod, SBER_EUR_kupovni, SBER_EUR_srednji, SBER_EUR_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_AUD_jedinica, SBER_AUD_kod, SBER_AUD_kupovni, SBER_AUD_srednji, SBER_AUD_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_CAD_jedinica, SBER_CAD_kod, SBER_CAD_kupovni, SBER_CAD_srednji, SBER_CAD_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_CZK_jedinica, SBER_CZK_kod, SBER_CZK_kupovni, SBER_CZK_srednji, SBER_CZK_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_DKK_jedinica, SBER_DKK_kod, SBER_DKK_kupovni, SBER_DKK_srednji, SBER_DKK_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_HUF_jedinica, SBER_HUF_kod, SBER_HUF_kupovni, SBER_HUF_srednji, SBER_HUF_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_JPY_jedinica, SBER_JPY_kod, SBER_JPY_kupovni, SBER_JPY_srednji, SBER_JPY_prodajni, timeStamp, SBER_AR_bank_id,SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_NOK_jedinica, SBER_NOK_kod, SBER_NOK_kupovni, SBER_NOK_srednji, SBER_NOK_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_SEK_jedinica, SBER_SEK_kod, SBER_SEK_kupovni, SBER_SEK_srednji, SBER_SEK_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_CHF_jedinica, SBER_CHF_kod, SBER_CHF_kupovni, SBER_CHF_srednji, SBER_CHF_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_GBP_jedinica, SBER_GBP_kod, SBER_GBP_kupovni, SBER_GBP_srednji, SBER_GBP_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_USD_jedinica, SBER_USD_kod, SBER_USD_kupovni, SBER_USD_srednji, SBER_USD_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_PLN_jedinica, SBER_PLN_kod, SBER_PLN_kupovni, SBER_PLN_srednji, SBER_PLN_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    SBER_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (SBER_BAM_jedinica, SBER_BAM_kod, SBER_BAM_kupovni, SBER_BAM_srednji, SBER_BAM_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    )

    #SBER_cursor.execute(
    #    '''
    #    INSERT INTO FX_RATES_CHECK.dbo.allbanks
    #    (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
    #    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    #    ''',
    #    (SBER_RUB_jedinica, SBER_RUB_kod, SBER_RUB_kupovni, SBER_RUB_srednji, SBER_RUB_prodajni, timeStamp, SBER_AR_bank_id, SBER_bank)
    #)

    SBER_conn.commit()

except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    error = (''.join('!! ' + line for line in lines))
    ErrortimeStamp = str(datetime.datetime.now())[0:-3]
    error_conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=B2ANALIZA;'
                                'Database=FX_RATES_CHECK;'
                                'Trusted_Connection=no;'
                                'UID=kpitest;'
                                'PWD=Logitech2020!;')

    error_cursor = error_conn.cursor()
    error_cursor.execute(
        '''
                INSERT INTO FX_RATES_CHECK.dbo.errorlog
                (bank, error, date)
                VALUES (?, ?, ?)
                ''',
        ('SBER', error, ErrortimeStamp))
    error_conn.commit()

######################################################################################################################################################################
######################################################################################################################################################################
                                                    #OTP


try:

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

    OTP_AUD_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[0]
    OTP_AUD_kod = tuple(OTP_tree_obj.execute('$..currency'))[0]
    OTP_AUD_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[0]
    OTP_AUD_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[0]
    OTP_AUD_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[0]

    #print(OTP_AUD_jedinica, OTP_AUD_kod, OTP_AUD_kupovni, OTP_AUD_srednji, OTP_AUD_prodajni)

    OTP_CAD_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[1]
    OTP_CAD_kod = tuple(OTP_tree_obj.execute('$..currency'))[1]
    OTP_CAD_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[1]
    OTP_CAD_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[1]
    OTP_CAD_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[1]

    #print(OTP_CAD_jedinica, OTP_CAD_kod, OTP_CAD_kupovni, OTP_CAD_srednji, OTP_CAD_prodajni)

    OTP_CZK_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[2]
    OTP_CZK_kod = tuple(OTP_tree_obj.execute('$..currency'))[2]
    OTP_CZK_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[2]
    OTP_CZK_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[2]
    OTP_CZK_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[2]

    #print(OTP_CZK_jedinica, OTP_CZK_kod, OTP_CZK_kupovni, OTP_CZK_srednji, OTP_CZK_prodajni)

    OTP_DKK_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[3]
    OTP_DKK_kod = tuple(OTP_tree_obj.execute('$..currency'))[3]
    OTP_DKK_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[3]
    OTP_DKK_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[3]
    OTP_DKK_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[3]

    #print(OTP_DKK_jedinica, OTP_DKK_kod, OTP_DKK_kupovni, OTP_DKK_srednji, OTP_DKK_prodajni)

    OTP_HUF_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[4]
    OTP_HUF_kod = tuple(OTP_tree_obj.execute('$..currency'))[4]
    OTP_HUF_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[4]
    OTP_HUF_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[4]
    OTP_HUF_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[4]

    #print(OTP_HUF_jedinica, OTP_HUF_kod, OTP_HUF_kupovni, OTP_HUF_srednji, OTP_HUF_prodajni)

    OTP_JPY_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[5]
    OTP_JPY_kod = tuple(OTP_tree_obj.execute('$..currency'))[5]
    OTP_JPY_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[5]
    OTP_JPY_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[5]
    OTP_JPY_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[5]

    #print(OTP_JPY_jedinica, OTP_JPY_kod, OTP_JPY_kupovni, OTP_JPY_srednji, OTP_JPY_prodajni)

    OTP_NOK_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[6]
    OTP_NOK_kod = tuple(OTP_tree_obj.execute('$..currency'))[6]
    OTP_NOK_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[6]
    OTP_NOK_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[6]
    OTP_NOK_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[6]

    #print(OTP_NOK_jedinica, OTP_NOK_kod, OTP_NOK_kupovni, OTP_NOK_srednji, OTP_NOK_prodajni)

    OTP_SEK_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[7]
    OTP_SEK_kod = tuple(OTP_tree_obj.execute('$..currency'))[7]
    OTP_SEK_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[7]
    OTP_SEK_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[7]
    OTP_SEK_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[7]

    #print(OTP_SEK_jedinica, OTP_SEK_kod, OTP_SEK_kupovni, OTP_SEK_srednji, OTP_SEK_prodajni)

    OTP_CHF_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[8]
    OTP_CHF_kod = tuple(OTP_tree_obj.execute('$..currency'))[8]
    OTP_CHF_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[8]
    OTP_CHF_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[8]
    OTP_CHF_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[8]

    #print(OTP_CHF_jedinica, OTP_CHF_kod, OTP_CHF_kupovni, OTP_CHF_srednji, OTP_CHF_prodajni)

    OTP_GBP_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[9]
    OTP_GBP_kod = tuple(OTP_tree_obj.execute('$..currency'))[9]
    OTP_GBP_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[9]
    OTP_GBP_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[9]
    OTP_GBP_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[9]

    #print(OTP_GBP_jedinica, OTP_GBP_kod, OTP_GBP_kupovni, OTP_GBP_srednji, OTP_GBP_prodajni)

    OTP_USD_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[10]
    OTP_USD_kod = tuple(OTP_tree_obj.execute('$..currency'))[10]
    OTP_USD_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[10]
    OTP_USD_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[10]
    OTP_USD_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[10]

    #print(OTP_USD_jedinica, OTP_USD_kod, OTP_USD_kupovni, OTP_USD_srednji, OTP_USD_prodajni)

    OTP_BAM_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[11]
    OTP_BAM_kod = tuple(OTP_tree_obj.execute('$..currency'))[11]
    OTP_BAM_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[11]
    OTP_BAM_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[11]
    OTP_BAM_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[11]

    #print(OTP_BAM_jedinica, OTP_BAM_kod, OTP_BAM_kupovni, OTP_BAM_srednji, OTP_BAM_prodajni)

    OTP_EUR_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[12]
    OTP_EUR_kod = tuple(OTP_tree_obj.execute('$..currency'))[12]
    OTP_EUR_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[12]
    OTP_EUR_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[12]
    OTP_EUR_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[12]

    #print(OTP_EUR_jedinica, OTP_EUR_kod, OTP_EUR_kupovni, OTP_EUR_srednji, OTP_EUR_prodajni)

    OTP_PLN_jedinica = tuple(OTP_tree_obj.execute('$..unit'))[13]
    OTP_PLN_kod = tuple(OTP_tree_obj.execute('$..currency'))[13]
    OTP_PLN_kupovni = tuple(OTP_tree_obj.execute('$..foreignCurrencyBuy'))[13]
    OTP_PLN_srednji = tuple(OTP_tree_obj.execute('$..cashMiddle'))[13]
    OTP_PLN_prodajni = tuple(OTP_tree_obj.execute('$..foreignCurrencySell'))[13]

    #print(OTP_PLN_jedinica, OTP_PLN_kod, OTP_PLN_kupovni, OTP_PLN_srednji, OTP_PLN_prodajni)



    OTP_AR_bank_id = '9CBA76D0CA0F40C08ED811B299CE1A77'
    OTP_bank = 'OTP'

    timeStamp = str(datetime.datetime.now())[0:-3]

    OTP_conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=B2ANALIZA;'
                          'Database=FX_RATES_CHECK;'
                          'Trusted_Connection=no;'
                          'UID=kpitest;'
                          'PWD=Logitech2020!;' )

    OTP_cursor = OTP_conn.cursor()

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_EUR_jedinica, OTP_EUR_kod, OTP_EUR_kupovni.replace(',','.'), OTP_EUR_srednji.replace(',','.'), OTP_EUR_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_AUD_jedinica, OTP_AUD_kod, OTP_AUD_kupovni.replace(',','.'), OTP_AUD_srednji.replace(',','.'), OTP_AUD_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_CAD_jedinica, OTP_CAD_kod, OTP_CAD_kupovni.replace(',','.'), OTP_CAD_srednji.replace(',','.'), OTP_CAD_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_CZK_jedinica, OTP_CZK_kod, OTP_CZK_kupovni.replace(',','.'), OTP_CZK_srednji.replace(',','.'), OTP_CZK_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_DKK_jedinica, OTP_DKK_kod, OTP_DKK_kupovni.replace(',','.'), OTP_DKK_srednji.replace(',','.'), OTP_DKK_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_HUF_jedinica, OTP_HUF_kod, OTP_HUF_kupovni.replace(',','.'), OTP_HUF_srednji.replace(',','.'), OTP_HUF_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_JPY_jedinica, OTP_JPY_kod, OTP_JPY_kupovni.replace(',','.'), OTP_JPY_srednji.replace(',','.'), OTP_JPY_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id,OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_NOK_jedinica, OTP_NOK_kod, OTP_NOK_kupovni.replace(',','.'), OTP_NOK_srednji.replace(',','.'), OTP_NOK_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_SEK_jedinica, OTP_SEK_kod, OTP_SEK_kupovni.replace(',','.'), OTP_SEK_srednji.replace(',','.'), OTP_SEK_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_CHF_jedinica, OTP_CHF_kod, OTP_CHF_kupovni.replace(',','.'), OTP_CHF_srednji.replace(',','.'), OTP_CHF_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_GBP_jedinica, OTP_GBP_kod, OTP_GBP_kupovni.replace(',','.'), OTP_GBP_srednji.replace(',','.'), OTP_GBP_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_USD_jedinica, OTP_USD_kod, OTP_USD_kupovni.replace(',','.'), OTP_USD_srednji.replace(',','.'), OTP_USD_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_PLN_jedinica, OTP_PLN_kod, OTP_PLN_kupovni.replace(',','.'), OTP_PLN_srednji.replace(',','.'), OTP_PLN_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )

    OTP_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (OTP_BAM_jedinica, OTP_BAM_kod, OTP_BAM_kupovni.replace(',','.'), OTP_BAM_srednji.replace(',','.'), OTP_BAM_prodajni.replace(',','.'), timeStamp, OTP_AR_bank_id, OTP_bank)
    )



    OTP_conn.commit()

except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    error = (''.join('!! ' + line for line in lines))
    ErrortimeStamp = str(datetime.datetime.now())[0:-3]
    error_conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=B2ANALIZA;'
                                'Database=FX_RATES_CHECK;'
                                'Trusted_Connection=no;'
                                'UID=kpitest;'
                                'PWD=Logitech2020!;')

    error_cursor = error_conn.cursor()
    error_cursor.execute(
        '''
                INSERT INTO FX_RATES_CHECK.dbo.errorlog
                (bank, error, date)
                VALUES (?, ?, ?)
                ''',
        ('OTP', error, ErrortimeStamp))
    error_conn.commit()

######################################################################################################################################################################
######################################################################################################################################################################
                                                    #RBA


try:

    RBA_url = 'https://www.rba.hr/aktualna-tecajna-lista/'

    RBA_page = requests.get(RBA_url)

    RBA_soup = BeautifulSoup(RBA_page.text, 'html.parser')


    RBA_table = RBA_soup.find('table', class_ = 'stdtbl tecaj datagrid')

    for tecaj in RBA_table.find_all('tbody'):
        RBA_EUR = tecaj.find_all('tr')[0]
        RBA_EUR_jedinica = RBA_EUR.find_all('td')[0].text
        RBA_EUR_kod = RBA_EUR.find_all('td')[1].text
        RBA_EUR_kupovni = RBA_EUR.find_all('td')[2].text
        RBA_EUR_srednji = RBA_EUR.find_all('td')[3].text
        RBA_EUR_prodajni = RBA_EUR.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_USD = tecaj.find_all('tr')[1]
        RBA_USD_jedinica = RBA_USD.find_all('td')[0].text
        RBA_USD_kod = RBA_USD.find_all('td')[1].text
        RBA_USD_kupovni = RBA_USD.find_all('td')[2].text
        RBA_USD_srednji = RBA_USD.find_all('td')[3].text
        RBA_USD_prodajni = RBA_USD.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_CHF = tecaj.find_all('tr')[2]
        RBA_CHF_jedinica = RBA_CHF.find_all('td')[0].text
        RBA_CHF_kod = RBA_CHF.find_all('td')[1].text
        RBA_CHF_kupovni = RBA_CHF.find_all('td')[2].text
        RBA_CHF_srednji = RBA_CHF.find_all('td')[3].text
        RBA_CHF_prodajni = RBA_CHF.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_GBP = tecaj.find_all('tr')[3]
        RBA_GBP_jedinica = RBA_GBP.find_all('td')[0].text
        RBA_GBP_kod = RBA_GBP.find_all('td')[1].text
        RBA_GBP_kupovni = RBA_GBP.find_all('td')[2].text
        RBA_GBP_srednji = RBA_GBP.find_all('td')[3].text
        RBA_GBP_prodajni = RBA_GBP.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_AUD = tecaj.find_all('tr')[4]
        RBA_AUD_jedinica = RBA_AUD.find_all('td')[0].text
        RBA_AUD_kod = RBA_AUD.find_all('td')[1].text
        RBA_AUD_kupovni = RBA_AUD.find_all('td')[2].text
        RBA_AUD_srednji = RBA_AUD.find_all('td')[3].text
        RBA_AUD_prodajni = RBA_AUD.find_all('td')[4].text


    for tecaj in RBA_table.find_all('tbody'):
        RBA_JPY = tecaj.find_all('tr')[5]
        RBA_JPY_jedinica = RBA_JPY.find_all('td')[0].text
        RBA_JPY_kod = RBA_JPY.find_all('td')[1].text
        RBA_JPY_kupovni = RBA_JPY.find_all('td')[2].text
        RBA_JPY_srednji = RBA_JPY.find_all('td')[3].text
        RBA_JPY_prodajni = RBA_JPY.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_BAM = tecaj.find_all('tr')[6]
        RBA_BAM_jedinica = RBA_BAM.find_all('td')[0].text
        RBA_BAM_kod = RBA_BAM.find_all('td')[1].text
        RBA_BAM_kupovni = RBA_BAM.find_all('td')[2].text
        RBA_BAM_srednji = RBA_BAM.find_all('td')[3].text
        RBA_BAM_prodajni = RBA_BAM.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_CAD = tecaj.find_all('tr')[7]
        RBA_CAD_jedinica = RBA_CAD.find_all('td')[0].text
        RBA_CAD_kod = RBA_CAD.find_all('td')[1].text
        RBA_CAD_kupovni = RBA_CAD.find_all('td')[2].text
        RBA_CAD_srednji = RBA_CAD.find_all('td')[3].text
        RBA_CAD_prodajni = RBA_CAD.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_CZK = tecaj.find_all('tr')[8]
        RBA_CZK_jedinica = RBA_CZK.find_all('td')[0].text
        RBA_CZK_kod = RBA_CZK.find_all('td')[1].text
        RBA_CZK_kupovni = RBA_CZK.find_all('td')[2].text
        RBA_CZK_srednji = RBA_CZK.find_all('td')[3].text
        RBA_CZK_prodajni = RBA_CZK.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_DKK = tecaj.find_all('tr')[9]
        RBA_DKK_jedinica = RBA_DKK.find_all('td')[0].text
        RBA_DKK_kod = RBA_DKK.find_all('td')[1].text
        RBA_DKK_kupovni = RBA_DKK.find_all('td')[2].text
        RBA_DKK_srednji = RBA_DKK.find_all('td')[3].text
        RBA_DKK_prodajni = RBA_DKK.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_HUF = tecaj.find_all('tr')[10]
        RBA_HUF_jedinica = RBA_HUF.find_all('td')[0].text
        RBA_HUF_kod = RBA_HUF.find_all('td')[1].text
        RBA_HUF_kupovni = RBA_HUF.find_all('td')[2].text
        RBA_HUF_srednji = RBA_HUF.find_all('td')[3].text
        RBA_HUF_prodajni = RBA_HUF.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_NOK = tecaj.find_all('tr')[11]
        RBA_NOK_jedinica = RBA_NOK.find_all('td')[0].text
        RBA_NOK_kod = RBA_NOK.find_all('td')[1].text
        RBA_NOK_kupovni = RBA_NOK.find_all('td')[2].text
        RBA_NOK_srednji = RBA_NOK.find_all('td')[3].text
        RBA_NOK_prodajni = RBA_NOK.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_PLN = tecaj.find_all('tr')[12]
        RBA_PLN_jedinica = RBA_PLN.find_all('td')[0].text
        RBA_PLN_kod = RBA_PLN.find_all('td')[1].text
        RBA_PLN_kupovni = RBA_PLN.find_all('td')[2].text
        RBA_PLN_srednji = RBA_PLN.find_all('td')[3].text
        RBA_PLN_prodajni = RBA_PLN.find_all('td')[4].text

    for tecaj in RBA_table.find_all('tbody'):
        RBA_SEK = tecaj.find_all('tr')[13]
        RBA_SEK_jedinica = RBA_SEK.find_all('td')[0].text
        RBA_SEK_kod = RBA_SEK.find_all('td')[1].text
        RBA_SEK_kupovni = RBA_SEK.find_all('td')[2].text
        RBA_SEK_srednji = RBA_SEK.find_all('td')[3].text
        RBA_SEK_prodajni = RBA_SEK.find_all('td')[4].text




    RBA_AR_bank_id = '1B27B838E50641D081216A2C57133275'

    RBA_bank = 'RBA'


    timeStamp = str(datetime.datetime.now())[0:-3]

    RBA_conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=B2ANALIZA;'
                          'Database=FX_RATES_CHECK;'
                          'Trusted_Connection=no;'
                          'UID=kpitest;'
                          'PWD=Logitech2020!;' )

    RBA_cursor = RBA_conn.cursor()

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_EUR_jedinica, RBA_EUR_kod, RBA_EUR_kupovni.replace(',','.'), RBA_EUR_srednji.replace(',','.'), RBA_EUR_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_AUD_jedinica, RBA_AUD_kod, RBA_AUD_kupovni.replace(',','.'), RBA_AUD_srednji.replace(',','.'), RBA_AUD_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_CAD_jedinica, RBA_CAD_kod, RBA_CAD_kupovni.replace(',','.'), RBA_CAD_srednji.replace(',','.'), RBA_CAD_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_CZK_jedinica, RBA_CZK_kod, RBA_CZK_kupovni.replace(',','.'), RBA_CZK_srednji.replace(',','.'), RBA_CZK_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_DKK_jedinica, RBA_DKK_kod, RBA_DKK_kupovni.replace(',','.'), RBA_DKK_srednji.replace(',','.'), RBA_DKK_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_HUF_jedinica, RBA_HUF_kod, RBA_HUF_kupovni.replace(',','.'), RBA_HUF_srednji.replace(',','.'), RBA_HUF_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_JPY_jedinica, RBA_JPY_kod, RBA_JPY_kupovni.replace(',','.'), RBA_JPY_srednji.replace(',','.'), RBA_JPY_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id,RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_NOK_jedinica, RBA_NOK_kod, RBA_NOK_kupovni.replace(',','.'), RBA_NOK_srednji.replace(',','.'), RBA_NOK_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_SEK_jedinica, RBA_SEK_kod, RBA_SEK_kupovni.replace(',','.'), RBA_SEK_srednji.replace(',','.'), RBA_SEK_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_CHF_jedinica, RBA_CHF_kod, RBA_CHF_kupovni.replace(',','.'), RBA_CHF_srednji.replace(',','.'), RBA_CHF_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_GBP_jedinica, RBA_GBP_kod, RBA_GBP_kupovni.replace(',','.'), RBA_GBP_srednji.replace(',','.'), RBA_GBP_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_USD_jedinica, RBA_USD_kod, RBA_USD_kupovni.replace(',','.'), RBA_USD_srednji.replace(',','.'), RBA_USD_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_PLN_jedinica, RBA_PLN_kod, RBA_PLN_kupovni.replace(',','.'), RBA_PLN_srednji.replace(',','.'), RBA_PLN_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (RBA_BAM_jedinica, RBA_BAM_kod, RBA_BAM_kupovni.replace(',','.'), RBA_BAM_srednji.replace(',','.'), RBA_BAM_prodajni.replace(',','.'), timeStamp, RBA_AR_bank_id, RBA_bank)
    )

    RBA_conn.commit()


except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    error = (''.join('!! ' + line for line in lines))
    ErrortimeStamp = str(datetime.datetime.now())[0:-3]
    error_conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=B2ANALIZA;'
                                'Database=FX_RATES_CHECK;'
                                'Trusted_Connection=no;'
                                'UID=kpitest;'
                                'PWD=Logitech2020!;')

    error_cursor = error_conn.cursor()
    error_cursor.execute(
        '''
                INSERT INTO FX_RATES_CHECK.dbo.errorlog
                (bank, error, date)
                VALUES (?, ?, ?)
                ''',
        ('RBA', error, ErrortimeStamp))
    error_conn.commit()


######################################################################################################################################################################
######################################################################################################################################################################
                                                    #HNB


try:

    HNB_AUD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=AUD&format=xml').text

    HNB_AUD_data = BeautifulSoup(HNB_AUD_xml, 'lxml')

    HNB_AUD_kod = HNB_AUD_data.find('valuta').text
    HNB_AUD_jedinica = HNB_AUD_data.find('jedinica').text
    HNB_AUD_kupovni = HNB_AUD_data.find('kupovni_tecaj').text
    HNB_AUD_srednji = HNB_AUD_data.find('srednji_tecaj').text
    HNB_AUD_prodajni = HNB_AUD_data.find('prodajni_tecaj').text

    #print(AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni)

    HNB_CAD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CAD&format=xml').text

    HNB_CAD_data = BeautifulSoup(HNB_CAD_xml, 'lxml')

    HNB_CAD_jedinica = HNB_CAD_data.find('jedinica').text
    HNB_CAD_kod = HNB_CAD_data.find('valuta').text
    HNB_CAD_kupovni = HNB_CAD_data.find('kupovni_tecaj').text
    HNB_CAD_srednji = HNB_CAD_data.find('srednji_tecaj').text
    HNB_CAD_prodajni = HNB_CAD_data.find('prodajni_tecaj').text

    #print(CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni)

    HNB_CZK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CZK&format=xml').text

    HNB_CZK_data = BeautifulSoup(HNB_CZK_xml, 'lxml')

    HNB_CZK_jedinica = HNB_CZK_data.find('jedinica').text
    HNB_CZK_kod = HNB_CZK_data.find('valuta').text
    HNB_CZK_kupovni = HNB_CZK_data.find('kupovni_tecaj').text
    HNB_CZK_srednji = HNB_CZK_data.find('srednji_tecaj').text
    HNB_CZK_prodajni = HNB_CZK_data.find('prodajni_tecaj').text

    #print(CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni)

    HNB_DKK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=DKK&format=xml').text

    HNB_DKK_data = BeautifulSoup(HNB_DKK_xml, 'lxml')

    HNB_DKK_jedinica = HNB_DKK_data.find('jedinica').text
    HNB_DKK_kod = HNB_DKK_data.find('valuta').text
    HNB_DKK_kupovni = HNB_DKK_data.find('kupovni_tecaj').text
    HNB_DKK_srednji = HNB_DKK_data.find('srednji_tecaj').text
    HNB_DKK_prodajni = HNB_DKK_data.find('prodajni_tecaj').text

    #print(DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni)

    HNB_HUF_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=HUF&format=xml').text

    HNB_HUF_data = BeautifulSoup(HNB_HUF_xml, 'lxml')

    HNB_HUF_jedinica = HNB_HUF_data.find('jedinica').text
    HNB_HUF_kod = HNB_HUF_data.find('valuta').text
    HNB_HUF_kupovni = HNB_HUF_data.find('kupovni_tecaj').text
    HNB_HUF_srednji = HNB_HUF_data.find('srednji_tecaj').text
    HNB_HUF_prodajni = HNB_HUF_data.find('prodajni_tecaj').text

    #print(HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni)

    HNB_JPY_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=JPY&format=xml').text

    HNB_JPY_data = BeautifulSoup(HNB_JPY_xml, 'lxml')

    HNB_JPY_jedinica = HNB_JPY_data.find('jedinica').text
    HNB_JPY_kod = HNB_JPY_data.find('valuta').text
    HNB_JPY_kupovni = HNB_JPY_data.find('kupovni_tecaj').text
    HNB_JPY_srednji = HNB_JPY_data.find('srednji_tecaj').text
    HNB_JPY_prodajni = HNB_JPY_data.find('prodajni_tecaj').text

    #print(JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni)

    HNB_NOK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=NOK&format=xml').text

    HNB_NOK_data = BeautifulSoup(HNB_NOK_xml, 'lxml')

    HNB_NOK_jedinica = HNB_NOK_data.find('jedinica').text
    HNB_NOK_kod = HNB_NOK_data.find('valuta').text
    HNB_NOK_kupovni = HNB_NOK_data.find('kupovni_tecaj').text
    HNB_NOK_srednji = HNB_NOK_data.find('srednji_tecaj').text
    HNB_NOK_prodajni = HNB_NOK_data.find('prodajni_tecaj').text

    #print(NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni)

    HNB_SEK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=SEK&format=xml').text

    HNB_SEK_data = BeautifulSoup(HNB_SEK_xml, 'lxml')

    HNB_SEK_jedinica = HNB_SEK_data.find('jedinica').text
    HNB_SEK_kod = HNB_SEK_data.find('valuta').text
    HNB_SEK_kupovni = HNB_SEK_data.find('kupovni_tecaj').text
    HNB_SEK_srednji = HNB_SEK_data.find('srednji_tecaj').text
    HNB_SEK_prodajni = HNB_SEK_data.find('prodajni_tecaj').text

    #print(SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni)

    HNB_CHF_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CHF&format=xml').text

    HNB_CHF_data = BeautifulSoup(HNB_CHF_xml, 'lxml')

    HNB_CHF_jedinica = HNB_CHF_data.find('jedinica').text
    HNB_CHF_kod = HNB_CHF_data.find('valuta').text
    HNB_CHF_kupovni = HNB_CHF_data.find('kupovni_tecaj').text
    HNB_CHF_srednji = HNB_CHF_data.find('srednji_tecaj').text
    HNB_CHF_prodajni = HNB_CHF_data.find('prodajni_tecaj').text

    #print(CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni)

    HNB_GBP_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=GBP&format=xml').text

    HNB_GBP_data = BeautifulSoup(HNB_GBP_xml, 'lxml')

    HNB_GBP_jedinica = HNB_GBP_data.find('jedinica').text
    HNB_GBP_kod = HNB_GBP_data.find('valuta').text
    HNB_GBP_kupovni = HNB_GBP_data.find('kupovni_tecaj').text
    HNB_GBP_srednji = HNB_GBP_data.find('srednji_tecaj').text
    HNB_GBP_prodajni = HNB_GBP_data.find('prodajni_tecaj').text

    #print(GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni)

    HNB_USD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=USD&format=xml').text

    HNB_USD_data = BeautifulSoup(HNB_USD_xml, 'lxml')

    HNB_USD_jedinica = HNB_USD_data.find('jedinica').text
    HNB_USD_kod = HNB_USD_data.find('valuta').text
    HNB_USD_kupovni = HNB_USD_data.find('kupovni_tecaj').text
    HNB_USD_srednji = HNB_USD_data.find('srednji_tecaj').text
    HNB_USD_prodajni = HNB_USD_data.find('prodajni_tecaj').text

    #print(USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni)

    HNB_BAM_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=BAM&format=xml').text

    HNB_BAM_data = BeautifulSoup(HNB_BAM_xml, 'lxml')

    HNB_BAM_jedinica = HNB_BAM_data.find('jedinica').text
    HNB_BAM_kod = HNB_BAM_data.find('valuta').text
    HNB_BAM_kupovni = HNB_BAM_data.find('kupovni_tecaj').text
    HNB_BAM_srednji = HNB_BAM_data.find('srednji_tecaj').text
    HNB_BAM_prodajni = HNB_BAM_data.find('prodajni_tecaj').text

    #print(BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni)

    HNB_EUR_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=EUR&format=xml').text

    HNB_EUR_data = BeautifulSoup(HNB_EUR_xml, 'lxml')

    HNB_EUR_jedinica = HNB_EUR_data.find('jedinica').text
    HNB_EUR_kod = HNB_EUR_data.find('valuta').text
    HNB_EUR_kupovni = HNB_EUR_data.find('kupovni_tecaj').text
    HNB_EUR_srednji = HNB_EUR_data.find('srednji_tecaj').text
    HNB_EUR_prodajni = HNB_EUR_data.find('prodajni_tecaj').text

    #print(EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni)

    HNB_PLN_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=PLN&format=xml').text

    HNB_PLN_data = BeautifulSoup(HNB_PLN_xml, 'lxml')

    HNB_PLN_jedinica = HNB_PLN_data.find('jedinica').text
    HNB_PLN_kod = HNB_PLN_data.find('valuta').text
    HNB_PLN_kupovni = HNB_PLN_data.find('kupovni_tecaj').text
    HNB_PLN_srednji = HNB_PLN_data.find('srednji_tecaj').text
    HNB_PLN_prodajni = HNB_PLN_data.find('prodajni_tecaj').text

    #print(PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni)


    HNB_AR_bank_id = '7E878B242D824F58AB91B6D304824475'

    HNB_bank = 'HNB'


    timeStamp = str(datetime.datetime.now())[0:-3]

    HNB_conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=B2ANALIZA;'
                          'Database=FX_RATES_CHECK;'
                          'Trusted_Connection=no;'
                          'UID=kpitest;'
                          'PWD=Logitech2020!;' )

    HNB_cursor = HNB_conn.cursor()


    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_EUR_jedinica, HNB_EUR_kod, HNB_EUR_kupovni.replace(',','.'), HNB_EUR_srednji.replace(',','.'), HNB_EUR_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_AUD_jedinica, HNB_AUD_kod, HNB_AUD_kupovni.replace(',','.'), HNB_AUD_srednji.replace(',','.'), HNB_AUD_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_CAD_jedinica, HNB_CAD_kod, HNB_CAD_kupovni.replace(',','.'), HNB_CAD_srednji.replace(',','.'), HNB_CAD_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_CZK_jedinica, HNB_CZK_kod, HNB_CZK_kupovni.replace(',','.'), HNB_CZK_srednji.replace(',','.'), HNB_CZK_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_DKK_jedinica, HNB_DKK_kod, HNB_DKK_kupovni.replace(',','.'), HNB_DKK_srednji.replace(',','.'), HNB_DKK_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_HUF_jedinica, HNB_HUF_kod, HNB_HUF_kupovni.replace(',','.'), HNB_HUF_srednji.replace(',','.'), HNB_HUF_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_JPY_jedinica, HNB_JPY_kod, HNB_JPY_kupovni.replace(',','.'), HNB_JPY_srednji.replace(',','.'), HNB_JPY_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id,HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_NOK_jedinica, HNB_NOK_kod, HNB_NOK_kupovni.replace(',','.'), HNB_NOK_srednji.replace(',','.'), HNB_NOK_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_SEK_jedinica, HNB_SEK_kod, HNB_SEK_kupovni.replace(',','.'), HNB_SEK_srednji.replace(',','.'), HNB_SEK_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_CHF_jedinica, HNB_CHF_kod, HNB_CHF_kupovni.replace(',','.'), HNB_CHF_srednji.replace(',','.'), HNB_CHF_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_GBP_jedinica, HNB_GBP_kod, HNB_GBP_kupovni.replace(',','.'), HNB_GBP_srednji.replace(',','.'), HNB_GBP_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_USD_jedinica, HNB_USD_kod, HNB_USD_kupovni.replace(',','.'), HNB_USD_srednji.replace(',','.'), HNB_USD_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_PLN_jedinica, HNB_PLN_kod, HNB_PLN_kupovni.replace(',','.'), HNB_PLN_srednji.replace(',','.'), HNB_PLN_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_cursor.execute(
        '''
        INSERT INTO FX_RATES_CHECK.dbo.allbanks
        (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (HNB_BAM_jedinica, HNB_BAM_kod, HNB_BAM_kupovni.replace(',','.'), HNB_BAM_srednji.replace(',','.'), HNB_BAM_prodajni.replace(',','.'), timeStamp, HNB_AR_bank_id, HNB_bank)
    )

    HNB_conn.commit()

except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    error = (''.join('!! ' + line for line in lines))
    ErrortimeStamp = str(datetime.datetime.now())[0:-3]
    error_conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=B2ANALIZA;'
                                'Database=FX_RATES_CHECK;'
                                'Trusted_Connection=no;'
                                'UID=kpitest;'
                                'PWD=Logitech2020!;')

    error_cursor = error_conn.cursor()
    error_cursor.execute(
        '''
                INSERT INTO FX_RATES_CHECK.dbo.errorlog
                (bank, error, date)
                VALUES (?, ?, ?)
                ''',
        ('HNB', error, ErrortimeStamp))
    error_conn.commit()

######################################################################################################################################################################
######################################################################################################################################################################
                                                    #HNB_B2P



try:

   HNB_B2P_AUD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=AUD&format=xml').text

   HNB_B2P_AUD_data = BeautifulSoup(HNB_B2P_AUD_xml, 'lxml')

   HNB_B2P_AUD_kod = HNB_B2P_AUD_data.find('valuta').text
   HNB_B2P_AUD_jedinica = HNB_B2P_AUD_data.find('jedinica').text
   HNB_B2P_AUD_kupovni = HNB_B2P_AUD_data.find('kupovni_tecaj').text
   HNB_B2P_AUD_srednji = HNB_B2P_AUD_data.find('srednji_tecaj').text
   HNB_B2P_AUD_prodajni = HNB_B2P_AUD_data.find('prodajni_tecaj').text

   #print(AUD_jedinica, AUD_kod, AUD_kupovni, AUD_srednji, AUD_prodajni)

   HNB_B2P_CAD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CAD&format=xml').text

   HNB_B2P_CAD_data = BeautifulSoup(HNB_B2P_CAD_xml, 'lxml')

   HNB_B2P_CAD_jedinica = HNB_B2P_CAD_data.find('jedinica').text
   HNB_B2P_CAD_kod = HNB_B2P_CAD_data.find('valuta').text
   HNB_B2P_CAD_kupovni = HNB_B2P_CAD_data.find('kupovni_tecaj').text
   HNB_B2P_CAD_srednji = HNB_B2P_CAD_data.find('srednji_tecaj').text
   HNB_B2P_CAD_prodajni = HNB_B2P_CAD_data.find('prodajni_tecaj').text

   #print(CAD_jedinica, CAD_kod, CAD_kupovni, CAD_srednji, CAD_prodajni)

   HNB_B2P_CZK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CZK&format=xml').text

   HNB_B2P_CZK_data = BeautifulSoup(HNB_B2P_CZK_xml, 'lxml')

   HNB_B2P_CZK_jedinica = HNB_B2P_CZK_data.find('jedinica').text
   HNB_B2P_CZK_kod = HNB_B2P_CZK_data.find('valuta').text
   HNB_B2P_CZK_kupovni = HNB_B2P_CZK_data.find('kupovni_tecaj').text
   HNB_B2P_CZK_srednji = HNB_B2P_CZK_data.find('srednji_tecaj').text
   HNB_B2P_CZK_prodajni = HNB_B2P_CZK_data.find('prodajni_tecaj').text

   #print(CZK_jedinica, CZK_kod, CZK_kupovni, CZK_srednji, CZK_prodajni)

   HNB_B2P_DKK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=DKK&format=xml').text

   HNB_B2P_DKK_data = BeautifulSoup(HNB_B2P_DKK_xml, 'lxml')

   HNB_B2P_DKK_jedinica = HNB_B2P_DKK_data.find('jedinica').text
   HNB_B2P_DKK_kod = HNB_B2P_DKK_data.find('valuta').text
   HNB_B2P_DKK_kupovni = HNB_B2P_DKK_data.find('kupovni_tecaj').text
   HNB_B2P_DKK_srednji = HNB_B2P_DKK_data.find('srednji_tecaj').text
   HNB_B2P_DKK_prodajni = HNB_B2P_DKK_data.find('prodajni_tecaj').text

   #print(DKK_jedinica, DKK_kod, DKK_kupovni, DKK_srednji, DKK_prodajni)

   HNB_B2P_HUF_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=HUF&format=xml').text

   HNB_B2P_HUF_data = BeautifulSoup(HNB_B2P_HUF_xml, 'lxml')

   HNB_B2P_HUF_jedinica = HNB_B2P_HUF_data.find('jedinica').text
   HNB_B2P_HUF_kod = HNB_B2P_HUF_data.find('valuta').text
   HNB_B2P_HUF_kupovni = HNB_B2P_HUF_data.find('kupovni_tecaj').text
   HNB_B2P_HUF_srednji = HNB_B2P_HUF_data.find('srednji_tecaj').text
   HNB_B2P_HUF_prodajni = HNB_B2P_HUF_data.find('prodajni_tecaj').text

   #print(HUF_jedinica, HUF_kod, HUF_kupovni, HUF_srednji, HUF_prodajni)

   HNB_B2P_JPY_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=JPY&format=xml').text

   HNB_B2P_JPY_data = BeautifulSoup(HNB_B2P_JPY_xml, 'lxml')

   HNB_B2P_JPY_jedinica = HNB_B2P_JPY_data.find('jedinica').text
   HNB_B2P_JPY_kod = HNB_B2P_JPY_data.find('valuta').text
   HNB_B2P_JPY_kupovni = HNB_B2P_JPY_data.find('kupovni_tecaj').text
   HNB_B2P_JPY_srednji = HNB_B2P_JPY_data.find('srednji_tecaj').text
   HNB_B2P_JPY_prodajni = HNB_B2P_JPY_data.find('prodajni_tecaj').text

   #print(JPY_jedinica, JPY_kod, JPY_kupovni, JPY_srednji, JPY_prodajni)

   HNB_B2P_NOK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=NOK&format=xml').text

   HNB_B2P_NOK_data = BeautifulSoup(HNB_B2P_NOK_xml, 'lxml')

   HNB_B2P_NOK_jedinica = HNB_B2P_NOK_data.find('jedinica').text
   HNB_B2P_NOK_kod = HNB_B2P_NOK_data.find('valuta').text
   HNB_B2P_NOK_kupovni = HNB_B2P_NOK_data.find('kupovni_tecaj').text
   HNB_B2P_NOK_srednji = HNB_B2P_NOK_data.find('srednji_tecaj').text
   HNB_B2P_NOK_prodajni = HNB_B2P_NOK_data.find('prodajni_tecaj').text

   #print(NOK_jedinica, NOK_kod, NOK_kupovni, NOK_srednji, NOK_prodajni)

   HNB_B2P_SEK_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=SEK&format=xml').text

   HNB_B2P_SEK_data = BeautifulSoup(HNB_B2P_SEK_xml, 'lxml')

   HNB_B2P_SEK_jedinica = HNB_B2P_SEK_data.find('jedinica').text
   HNB_B2P_SEK_kod = HNB_B2P_SEK_data.find('valuta').text
   HNB_B2P_SEK_kupovni = HNB_B2P_SEK_data.find('kupovni_tecaj').text
   HNB_B2P_SEK_srednji = HNB_B2P_SEK_data.find('srednji_tecaj').text
   HNB_B2P_SEK_prodajni = HNB_B2P_SEK_data.find('prodajni_tecaj').text

   #print(SEK_jedinica, SEK_kod, SEK_kupovni, SEK_srednji, SEK_prodajni)

   HNB_B2P_CHF_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=CHF&format=xml').text

   HNB_B2P_CHF_data = BeautifulSoup(HNB_B2P_CHF_xml, 'lxml')

   HNB_B2P_CHF_jedinica = HNB_B2P_CHF_data.find('jedinica').text
   HNB_B2P_CHF_kod = HNB_B2P_CHF_data.find('valuta').text
   HNB_B2P_CHF_kupovni = HNB_B2P_CHF_data.find('kupovni_tecaj').text
   HNB_B2P_CHF_srednji = HNB_B2P_CHF_data.find('srednji_tecaj').text
   HNB_B2P_CHF_prodajni = HNB_B2P_CHF_data.find('prodajni_tecaj').text

   #print(CHF_jedinica, CHF_kod, CHF_kupovni, CHF_srednji, CHF_prodajni)

   HNB_B2P_GBP_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=GBP&format=xml').text

   HNB_B2P_GBP_data = BeautifulSoup(HNB_B2P_GBP_xml, 'lxml')

   HNB_B2P_GBP_jedinica = HNB_B2P_GBP_data.find('jedinica').text
   HNB_B2P_GBP_kod = HNB_B2P_GBP_data.find('valuta').text
   HNB_B2P_GBP_kupovni = HNB_B2P_GBP_data.find('kupovni_tecaj').text
   HNB_B2P_GBP_srednji = HNB_B2P_GBP_data.find('srednji_tecaj').text
   HNB_B2P_GBP_prodajni = HNB_B2P_GBP_data.find('prodajni_tecaj').text

   #print(GBP_jedinica, GBP_kod, GBP_kupovni, GBP_srednji, GBP_prodajni)

   HNB_B2P_USD_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=USD&format=xml').text

   HNB_B2P_USD_data = BeautifulSoup(HNB_B2P_USD_xml, 'lxml')

   HNB_B2P_USD_jedinica = HNB_B2P_USD_data.find('jedinica').text
   HNB_B2P_USD_kod = HNB_B2P_USD_data.find('valuta').text
   HNB_B2P_USD_kupovni = HNB_B2P_USD_data.find('kupovni_tecaj').text
   HNB_B2P_USD_srednji = HNB_B2P_USD_data.find('srednji_tecaj').text
   HNB_B2P_USD_prodajni = HNB_B2P_USD_data.find('prodajni_tecaj').text

   #print(USD_jedinica, USD_kod, USD_kupovni, USD_srednji, USD_prodajni)

   HNB_B2P_BAM_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=BAM&format=xml').text

   HNB_B2P_BAM_data = BeautifulSoup(HNB_B2P_BAM_xml, 'lxml')

   HNB_B2P_BAM_jedinica = HNB_B2P_BAM_data.find('jedinica').text
   HNB_B2P_BAM_kod = HNB_B2P_BAM_data.find('valuta').text
   HNB_B2P_BAM_kupovni = HNB_B2P_BAM_data.find('kupovni_tecaj').text
   HNB_B2P_BAM_srednji = HNB_B2P_BAM_data.find('srednji_tecaj').text
   HNB_B2P_BAM_prodajni = HNB_B2P_BAM_data.find('prodajni_tecaj').text

   #print(BAM_jedinica, BAM_kod, BAM_kupovni, BAM_srednji, BAM_prodajni)

   HNB_B2P_EUR_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=EUR&format=xml').text

   HNB_B2P_EUR_data = BeautifulSoup(HNB_B2P_EUR_xml, 'lxml')

   HNB_B2P_EUR_jedinica = HNB_B2P_EUR_data.find('jedinica').text
   HNB_B2P_EUR_kod = HNB_B2P_EUR_data.find('valuta').text
   HNB_B2P_EUR_kupovni = HNB_B2P_EUR_data.find('kupovni_tecaj').text
   HNB_B2P_EUR_srednji = HNB_B2P_EUR_data.find('srednji_tecaj').text
   HNB_B2P_EUR_prodajni = HNB_B2P_EUR_data.find('prodajni_tecaj').text

   #print(EUR_jedinica, EUR_kod, EUR_kupovni, EUR_srednji, EUR_prodajni)

   HNB_B2P_PLN_xml = requests.get('https://api.hnb.hr/tecajn/v1?valuta=PLN&format=xml').text

   HNB_B2P_PLN_data = BeautifulSoup(HNB_B2P_PLN_xml, 'lxml')

   HNB_B2P_PLN_jedinica = HNB_B2P_PLN_data.find('jedinica').text
   HNB_B2P_PLN_kod = HNB_B2P_PLN_data.find('valuta').text
   HNB_B2P_PLN_kupovni = HNB_B2P_PLN_data.find('kupovni_tecaj').text
   HNB_B2P_PLN_srednji = HNB_B2P_PLN_data.find('srednji_tecaj').text
   HNB_B2P_PLN_prodajni = HNB_B2P_PLN_data.find('prodajni_tecaj').text

   #print(PLN_jedinica, PLN_kod, PLN_kupovni, PLN_srednji, PLN_prodajni)


   HNB_B2P_AR_bank_id = 'DB257CE7750E45ECADE94C368EEB5EF5'

   HNB_B2P_bank = 'HNB_B2P'


   timeStamp = str(datetime.datetime.now())[0:-3]

   HNB_B2P_conn = pyodbc.connect('Driver={SQL Server};'
                         'Server=B2ANALIZA;'
                         'Database=FX_RATES_CHECK;'
                         'Trusted_Connection=no;'
                         'UID=kpitest;'
                         'PWD=Logitech2020!;' )

   HNB_B2P_cursor = HNB_B2P_conn.cursor()


   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_EUR_jedinica, HNB_B2P_EUR_kod, HNB_B2P_EUR_kupovni.replace(',','.'), HNB_B2P_EUR_srednji.replace(',','.'), HNB_B2P_EUR_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_AUD_jedinica, HNB_B2P_AUD_kod, HNB_B2P_AUD_kupovni.replace(',','.'), HNB_B2P_AUD_srednji.replace(',','.'), HNB_B2P_AUD_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_CAD_jedinica, HNB_B2P_CAD_kod, HNB_B2P_CAD_kupovni.replace(',','.'), HNB_B2P_CAD_srednji.replace(',','.'), HNB_B2P_CAD_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_CZK_jedinica, HNB_B2P_CZK_kod, HNB_B2P_CZK_kupovni.replace(',','.'), HNB_B2P_CZK_srednji.replace(',','.'), HNB_B2P_CZK_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_DKK_jedinica, HNB_B2P_DKK_kod, HNB_B2P_DKK_kupovni.replace(',','.'), HNB_B2P_DKK_srednji.replace(',','.'), HNB_B2P_DKK_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_HUF_jedinica, HNB_B2P_HUF_kod, HNB_B2P_HUF_kupovni.replace(',','.'), HNB_B2P_HUF_srednji.replace(',','.'), HNB_B2P_HUF_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_JPY_jedinica, HNB_B2P_JPY_kod, HNB_B2P_JPY_kupovni.replace(',','.'), HNB_B2P_JPY_srednji.replace(',','.'), HNB_B2P_JPY_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id,HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_NOK_jedinica, HNB_B2P_NOK_kod, HNB_B2P_NOK_kupovni.replace(',','.'), HNB_B2P_NOK_srednji.replace(',','.'), HNB_B2P_NOK_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_SEK_jedinica, HNB_B2P_SEK_kod, HNB_B2P_SEK_kupovni.replace(',','.'), HNB_B2P_SEK_srednji.replace(',','.'), HNB_B2P_SEK_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_CHF_jedinica, HNB_B2P_CHF_kod, HNB_B2P_CHF_kupovni.replace(',','.'), HNB_B2P_CHF_srednji.replace(',','.'), HNB_B2P_CHF_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_GBP_jedinica, HNB_B2P_GBP_kod, HNB_B2P_GBP_kupovni.replace(',','.'), HNB_B2P_GBP_srednji.replace(',','.'), HNB_B2P_GBP_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_USD_jedinica, HNB_B2P_USD_kod, HNB_B2P_USD_kupovni.replace(',','.'), HNB_B2P_USD_srednji.replace(',','.'), HNB_B2P_USD_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_PLN_jedinica, HNB_B2P_PLN_kod, HNB_B2P_PLN_kupovni.replace(',','.'), HNB_B2P_PLN_srednji.replace(',','.'), HNB_B2P_PLN_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_cursor.execute(
       '''
       INSERT INTO FX_RATES_CHECK.dbo.allbanks
       (jedinica, kod, kupovni, srednji, prodajni, date, bank_id, bank)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       ''',
       (HNB_B2P_BAM_jedinica, HNB_B2P_BAM_kod, HNB_B2P_BAM_kupovni.replace(',','.'), HNB_B2P_BAM_srednji.replace(',','.'), HNB_B2P_BAM_prodajni.replace(',','.'), timeStamp, HNB_B2P_AR_bank_id, HNB_B2P_bank)
   )

   HNB_B2P_conn.commit()

except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    error = (''.join('!! ' + line for line in lines))
    ErrortimeStamp = str(datetime.datetime.now())[0:-3]
    error_conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=B2ANALIZA;'
                                'Database=FX_RATES_CHECK;'
                                'Trusted_Connection=no;'
                                'UID=kpitest;'
                                'PWD=Logitech2020!;')

    error_cursor = error_conn.cursor()
    error_cursor.execute(
        '''
                INSERT INTO FX_RATES_CHECK.dbo.errorlog
                (bank, error, date)
                VALUES (?, ?, ?)
                ''',
        ('HNB_B2P', error, ErrortimeStamp))
    error_conn.commit()


######################################################################################################################################################################
######################################################################################################################################################################
                                                    #SLATINSKA


try:
    SLAT_url = 'https://www.slatinska-banka.hr/tecajna-lista/'

    SLAT_page = requests.get(SLAT_url)

    SLAT_soup = BeautifulSoup(SLAT_page.text, 'html.parser')

    SLAT_table = SLAT_soup.find('table')

    # print(SLAT_table)

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

except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    error = (''.join('!! ' + line for line in lines))
    ErrortimeStamp = str(datetime.datetime.now())[0:-3]
    error_conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=B2ANALIZA;'
                                'Database=FX_RATES_CHECK;'
                                'Trusted_Connection=no;'
                                'UID=kpitest;'
                                'PWD=Logitech2020!;')

    error_cursor = error_conn.cursor()
    error_cursor.execute(
        '''
                INSERT INTO FX_RATES_CHECK.dbo.errorlog
                (bank, error, date)
                VALUES (?, ?, ?)
                ''',
        ('SLAT', error, ErrortimeStamp))
    error_conn.commit()

