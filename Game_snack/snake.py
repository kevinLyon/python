import random

import pygame


class Cobrinha:
    cor = (255, 255, 255)
    tamanho = (10, 10)
    velocidade = 5

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(200, 200), (190, 200), (180, 200)]

        self.direcao = 'direita'

        self.pontos = 0

    def blit(self, screen):
        for posicao in self.corpo:
            screen.blit(self.textura, posicao)
    
    def andar(self):
        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        if self.direcao == 'direita':
            self.corpo.insert(0, (x + self.velocidade, y))
        elif self.direcao == 'esquerda':
            self.corpo.insert(0, (x - self.velocidade, y))
        elif self.direcao == 'cima':
            self.corpo.insert(0, (x, y - self.velocidade))
        elif self.direcao == 'baixo':
            self.corpo.insert(0, (x, y + self.velocidade))

        self.corpo.pop(-1)

    def cima(self):
        if self.direcao != 'baixo':
            self.direcao = 'cima'
    
    def baixo(self):
        if self.direcao != 'cima':
            self.direcao = 'baixo'
    
    def esquerda(self):
        if self.direcao != 'direita':
            self.direcao = 'esquerda'
    
    def direita(self):
        if self.direcao != 'esquerda':
            self.direcao = 'direita'
    
    def colisao_fruta(self, frutinha):
        return self.corpo[0] == frutinha.posicao

    def comer(self, frutinha):
        self.corpo.append((0, 0))
        self.pontos += 1
        pygame.display.set_caption(' ' * 30 + f'Snack | Pontos: {self.pontos}')
    
    def colisao_parede(self):
        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        return x < 0 or x > 390 or y < 0 or y > 390
    
    def auto_colisao(self):
        return self.corpo[0] in self.corpo[1:]


class Frutinha:
    cor = (0, 255, 0)
    tamanho = (10, 10)
    
    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        self.posicao = (x, y)

    def blit(self, screen):
        screen.blit(self.textura, self.posicao)



if __name__ == "__main__":
    
    pygame.init()
    resolucao = (400, 400)
    screen = pygame.display.set_mode(resolucao)
    pygame.display.set_caption(' ' * 40 + 'Snack')
    #fps
    clock = pygame.time.Clock()

    preto = (0, 0, 0)

    frutinha = Frutinha()
    cobrinha = Cobrinha()

    while True:
        clock.tick(30)
        #print(clock)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cobrinha.cima()
                    break
                elif event.key == pygame.K_DOWN:
                    cobrinha.baixo()
                    break
                elif event.key == pygame.K_LEFT:
                    cobrinha.esquerda()
                    break
                elif event.key == pygame.K_RIGHT:
                    cobrinha.direita()
                    break

        if cobrinha.colisao_fruta(frutinha):
            cobrinha.comer(frutinha)
            frutinha = Frutinha()
        
        if cobrinha.colisao_parede():
            cobrinha = Cobrinha()
            frutinha = Frutinha()

        if cobrinha.auto_colisao():
            cobrinha = Cobrinha()
            frutinha = Frutinha()

        cobrinha.andar()

        screen.fill(preto)
        frutinha.blit(screen)
        cobrinha.blit(screen)

        pygame.display.update()
