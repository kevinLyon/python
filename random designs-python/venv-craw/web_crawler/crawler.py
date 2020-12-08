import re

import requests
from bs4 import BeautifulSoup

#re = \(?0?([1-9]{2})[ \-\.\)]{0,2}(9[ \-\.]?\d{4})[ \-\.]?(\d{4})
#soup.prettify() faz o parsing do html
dominio = 'aHR0cHM6Ly9kamFuZ28tYW51bmNpb3Muc29seWQuY29tLmJyCg==' 
url = 'aHR0cHM6Ly9kamFuZ28tYW51bmNpb3Muc29seWQuY29tLmJyL2F1dG9tb3ZlaXMvCg=='


def GET(url):
    try: 
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except Exception as erro:
        print('Houve um erro inesperado, desculpe.')
        print(erro)


def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except Exception as erro:
        print('Erro no parsing.')
        print(erro)


def find_link(soup):
    card_pai = soup.find('div', class_='ui three doubling link cards')
    cards = card_pai.find_all('a')

    links = []
    for card in cards:
        try:
            link = card['href']
            links.append(link)
        except:
            pass
    return links


def play_find_link(url):
    resposta = GET(url)
    if resposta:
        soup = parsing(resposta)
        if soup:
            links_found = find_link(soup)
            if links_found:
                full_link = []
                for link in links_found:
                    dir = dominio + link
                    full_link.append(dir)
                return full_link


def find_cell(full_link):
    for link in full_link:
        resposta = GET(link)
        if resposta:
            soup = parsing(resposta)
            if soup:
                try:
                    descricao = soup.find_all('div', class_='sixteen wide column')[2].p.get_text().strip()
                except:
                    print('Erro ao incontrar descrição')
                    return None
                
                regex = re.findall(r"\(?0?([1-9]{2})[ \-\.\)]{0,2}(9[ \-\.]?\d{4})[ \-\.]?(\d{4})", descricao)
                if regex:
                    print(f'\n{link}:\nnumero: {regex}')
     

if __name__ == "__main__":
    links = play_find_link(url)
    if links:
        find_cell(links)
    