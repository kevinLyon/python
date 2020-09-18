#####################################
# Developed for studies             #
# Developed by: Lyon kevin          #
#####################################
#####################################
# link_Api[https://www.omdbapi.com/]#
#####################################


import sys 
import requests
import json

argument = sys.argv
#MyApi_key == cfa7e3e5

def help():
    print(""" \n Man:

                    example:python .\data_film_API -f <name film>
                            
                            -f  pesquisar por filmes:\n""")

def get():
    req = requests.get('http://www.omdbapi.com/?apikey=cfa7e3e5&t='+ argument[2])
    dic = json.loads(req.text)
    #=========================#
    print(f"Title: {dic['Title']}")
    print(f"Year: {dic['Year']}")
    print(f"Released: {dic['Released']}")
    print(f"Runtime: {dic['Runtime']}")
    print(f"Director: {dic['Director']}")
    print(f"Type: {dic['Type']}")
    print(f"Poster: {dic['Poster']}")
    print(f"Note: {dic['imdbRating']}")


def man():

    if len(argument) >= 2:
        if argument[1] != '-f':
            help()
            exit()
        elif argument[1] == '-f':
            if len(argument) == 3:
                get()
                exit()
            else:
                print("\nFilme não encontrado.")
                help()
                exit()         
    else:
        help()
        exit()

#run!!
man()