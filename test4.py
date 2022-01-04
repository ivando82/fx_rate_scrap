from bs4 import BeautifulSoup
import requests
url = 'https://www.simplilearn.com/resources'
result = requests.get(url)
web_page = result.content
soup = BeautifulSoup(web_page, 'html.parser')
article = soup.findAll(class_='contentBySegment') #that gives me bs4.element.ResultSet

print(article)