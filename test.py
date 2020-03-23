import requests
import re
from bs4 import BeautifulSoup as bs
from lxml import html

#user
USER ='B10632020'
PASSWORD ='tap776unn'
LOGIN_URL = 'https://moodle.ntust.edu.tw/login/index.php'


session_requests = requests.session()
result = session_requests.get(LOGIN_URL)
tree = html.fromstring(result.text)
token = list(set(tree.xpath('//input[@name="logintoken"]/@value')))[0] #get token

payload = {
    'username' : USER,
    'password' : PASSWORD,
    'logintoken': token
}

result = session_requests.post(LOGIN_URL,data=payload)
report1=session_requests.get('https://moodle.ntust.edu.tw/calendar/view.php?time=1&course=1')
soup = bs(report1.text, "html.parser")
events = soup.find_all('div',class_ = 'event')

for event in events:
    title = event.find('h3').text
    name = event.find('div',class_='course').text
    nameary = name.split(' ') 
    date = event.find('span',class_ = 'date').text
    print('----------------------------')
    print(nameary[1])
    print(title)
    print(date)

