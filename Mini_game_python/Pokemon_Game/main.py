from Pokemon import *
from pessoa import *

def escolher_primeiro_pokemon(player):
    
    print(f'Bem vindo {player}, para comessar sua jornada escolha seu primeiro Pokemon.')
    pikachu = PokemonChoque('Pikachu')
    charmander = PokemonFogo('Charmander')
    squirtle = PokemonAgua('Squirtle')
    print("""Você tem 3 escolhas:
                    [1]-Pikachu
                    [2]-Charmander
                    [3]-Squirtle""")
    
    while True:
        e = input('Escolha seu Pokemon: ')

        if e == '1':
            player.capturar(pikachu)
            break
        elif e == '2':
            player.capturar(charmander)
            break
        elif e == '3':
            player.capturar(squirtle)
            break
        else:
            print('Opção invalida')

player = Player('Pedrinha')
escolher_primeiro_pokemon(player)

player.mostrar_pokemons()
