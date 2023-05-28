import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

url = 'https://news.ycombinator.com/'
payloads = {'p': 1}
h = {'Accept-Language': 'en-US'}

file = open('hacker_news.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['Title', 'Score', 'Time'])

while payloads['p'] < 50:
    response = requests.get(url, params=payloads, headers=h)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    item_soup = soup.find_all('tr', class_='athing')
    item_soup2 = soup.find_all('td', class_='subtext')

    for item, item2 in zip(item_soup, item_soup2):
        title = item.find('span', class_='titleline').text
        score = item2.find('span', class_='score').text
        time = item2.find('span', class_='age').text
        csv_obj.writerow([title, score, time])

    payloads['p'] += 1
    sleep(randint(5, 15))

file.close()