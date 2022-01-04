import pandas as pd

from selenium import webdriver

from bs4 import BeautifulSoup

url= 'https://www.erstebank.hr/hr/tecajna-lista'

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Load the web page
driver.get(url)
# Wait for the page to fully load
driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, 'lxml')

tables = soup.find_all('table')

print(tables)





driver.close()





