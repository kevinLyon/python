class Pokemon:

    def __init__(self, especie, nivel=1, nome=None):
        self.especie = especie
        self.nivel = nivel
        if nome:
            self.nome = nome
        else:
            self.nome = especie


    def __str__(self):
        return f'{self.nome}, nivel {self.nivel}'


    def atacar(self, pokemon):
        print(f'{self.especie} atacou {pokemon.especie}!')


class PokemonChoque(Pokemon):
    
    tipo = 'Eletrico'
    def atacar(self, pokemon):
        print(f'{self.especie} lançou um ataque do trovão em {pokemon.especie}')


class PokemonFogo(Pokemon):

    tipo = 'Fogo'
    def atacar(self, pokemon):
        print(f'{self.especie} lançou uma bola de fogo em {pokemon.especie}')


class PokemonAgua(PokemonChoque):

    tipo = 'Água'
    def atacar(self, pokemon):
        print(f'{self.especie} lançõu uma bola de água em {pokemon.especie}')
