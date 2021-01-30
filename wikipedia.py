from bs4 import BeautifulSoup
import requests


while True:
    source = requests.get('https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona').text
    soup = BeautifulSoup(source, 'lxml')

    header = soup.find(id='firstHeading')
    category = soup.find(id='mw-normal-catlinks')

    print(header.get_text())
    print(category.get_text())

    odp = input("Chcesz o tym poczytać? ")

    if odp=="n":
        continue
    else:
        for paragraph in soup.find_all('p'):
            print(paragraph.get_text())
        wait= input('...')
