from Pokemon import PokemonFogo, PokemonChoque, PokemonAgua

class Pessoa:

    def __init__(self, nome=None, poks=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = 'Anonimo'
        self.poks = poks
    

    def __str__(self):
        return self.nome
    

    def mostrar_pokemons(self):
        if self.poks:
            print('\nPoque_deX!')
            for poke in self.poks:
                print(poke)
        else:
            print('\nPoque_deX vazia!')

class Player(Pessoa):
    
    tipo = 'Player'
    def capturar(self, pokemon):
        self.poks.append(pokemon)
        print(f'\n{self} Capturou {pokemon}')


class Inimigo(Pessoa):

    tipo = 'Inimigo'
    def pokemons_Inimigo(self, pokemon):
        self.poks.append(pokemon)


#Teste...

