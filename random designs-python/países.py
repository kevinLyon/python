import json
import sys

import requests

#Local API url_all"https://restcountries.eu/"
#Local API url_name "https://restcountries.eu/rest/v2/name/"

url_all = "https://restcountries.eu/rest/v2/all"
url_name = "https://restcountries.eu/rest/v2/name/"


def requesicao(url):
    try:
        get = requests.get(url)
        if get.status_code == 200:
            return get.text
    except Exception as error:
        print('Erro ao localizar o país.')
        print(error)


def parsing(text):
    try: 
        return json.loads(text)
    except:
        print('Houve algum erro no parsing.')


def total_de_paises(json_loads):
    print(f'No total existe {len(json_loads)} países!')


def lista_paises(txt):
    for pais in txt:
        print(pais['name'])
        print('   Captital:', pais['capital'])


def mostrar_populacao(pais):
    resposta = requesicao(url_name + pais)
    if resposta:
        lis_de_pais = parsing(resposta)
        if lis_de_pais:
            for key in lis_de_pais:
                print(key['name'])
                print('   População de:', key['population'], 'pessoas.')
    else:
        print('País não encontrado.')


def ajuda():
    print('Teste de APIs:')
    print("""Modo de uso:
    [-p]- Mostrar população de um pais.
    [-l]- Mostrar lista de paises.
    [-t]- Mostrar total de países.""")

if __name__ == "__main__":
    argument = sys.argv
    if len(argument) <= 1:
        print('Argumento não passado.')
        ajuda()
    else:
        if argument[1] == '-l':
            resposta = requesicao(url_all)
            if resposta:
                jresposta = parsing(resposta)
                if jresposta:
                    lista_paises(jresposta)
        
        elif argument[1] == '-t':
            res = requesicao(url_all)
            if res:
                jres = parsing(res)
                if jres:
                    total_de_paises(jres)
        
        elif argument[1] == '-p':
            try:
                populacao = mostrar_populacao(argument[2])
            except:
                print('País inválido, ou não foi passado.')
