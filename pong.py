import pygame
import random


#Definição das cores
preto = 0, 0, 0
branco = 255, 255, 255


#Criação da tela
tamanho = 600 , 600
tela = pygame.display.set_mode(tamanho)
fim = False
tela_retangulo = tela.get_rect()
print(tela_retangulo)
pygame.display.set_caption('Pong')
imagem = pygame.image.load("icone.png")
icone = pygame.display.set_icon(imagem)


#Criação da linha  divisória
class Linha:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 35

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class Linha2:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 85

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class Linha3:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 135

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class Linha4:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 185

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class Linha5:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 235

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class Linha6:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 285

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class Linha7:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 335

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class Linha8:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 385

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class Linha9:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 435

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class Linha10:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 485

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class Linha11:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 300
        self.imagem_retangulo[1] = 535

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)


#Criação da bola
class Bola:
    def __init__(self , tamanho):
        self.altura, self.largura = tamanho
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_quadrado = self.imagem.get_rect()
        self.imagem_quadrado[0] = 300
        self.imagem_quadrado[1] = 300 
        self.velocidade = 0.4
        self.set_bola()

    def aleatorio(self):
        while True:
            num = random.uniform(-1.0 , 1.0)
            if num > -.5 and num < 0.5:
                continue
            else:
                return num
            
    def set_bola(self):
        x = self.aleatorio()
        y = self.aleatorio()
        self.v = [x , y]
        self.pos = list(tela_retangulo.center)


    def colide_parede(self):
        if self.imagem_quadrado.y < 0 or self.imagem_quadrado.y > tela_retangulo.bottom - self.altura:
            self.v[1] *= -1
        if self.imagem_quadrado.x < 0 or self.imagem_quadrado.x > tela_retangulo.right - self.largura:
            self.v[0] *= -1


    def colide_raquete(self):
        if self.imagem_quadrado.colliderect(raquete.imagem_retangulo) or self.imagem_quadrado.colliderect(raquete2.imagem_retangulo):
            self.v[0] *= -1

    def movimento(self):    
        self.pos[0] += self.v[0] * self.velocidade
        self.pos[1] += self.v[1] * self.velocidade
        self.imagem_quadrado.center = self.pos
 
    def atualiza(self):
        self.colide_parede()
        self.colide_raquete()
        self.movimento()
    def realiza(self):
        tela.blit(self.imagem, self.imagem_quadrado)


#Criação da raquete do player
class Raquete:
    def __init__(self , tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 40
        self.imagem_retangulo[1] = 20

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)


#Criação da raquete do bot
class Raquete_bot:
    def __init__(self , tamanho):
        self.altura, self.largura = tamanho
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(branco)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 560
        self.imagem_retangulo[1] = 20
        self.velocidade = 0.24777777
        self.set_raquete()

    def aleatorio(self):
        while True:
            num = random.uniform(-1.0 , 1.0)
            if num > -.5 and num < 0.5:
                continue
            else:
                return num
            
    def set_raquete(self):
        self.pos = list(self.imagem_retangulo.center)
        self.v = [0, random.choice([-1 , 1])]

    def segue_bola(self):
        if self.imagem_retangulo.centery < bola.imagem_quadrado.centery:
            self.v[1] = 1
        elif self.imagem_retangulo.centery > bola.imagem_quadrado.centery:
            self.v[1] = -1
        else:
            self.v[1] = 0

    def movimento(self):    
        self.pos[1] += self.v[1] * self.velocidade
        self.imagem_retangulo.center = self.pos
        if self.imagem_retangulo.top < tela_retangulo.top:
            self.imagem_retangulo.top = tela_retangulo.top
            self.v[1] = 1
        if self.imagem_retangulo.bottom > tela_retangulo.bottom:
            self.imagem_retangulo.bottom = tela_retangulo.bottom
            self.v[1] = -1
 
    def atualiza(self):
        self.segue_bola()
        self.movimento()

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)


#Criação do placar do player
class Placar:
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 50)
        self.pontos = 0

    def contagem(self):
        self.texto = self.fonte.render(str(self.pontos) , 1 , branco)
        self.textopos = self.texto.get_rect()
        self.textopos.centerx = self.textopos[0] = 200
        self.textopos.centery = self.textopos[1] = 15
        if bola.imagem_quadrado.x > tela_retangulo.right - bola.largura:
            self.pontos += 1
        tela.blit(self.texto, self.textopos)
        tela.blit(tela , (0 , 0))


#Criação do placar do bot
class Placar_bot:
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 50)
        self.pontos = 0

    def contagem(self):
        self.texto = self.fonte.render(str(self.pontos) , 1 , branco)
        self.textopos = self.texto.get_rect()
        self.textopos.centerx = self.textopos[0] = 400
        self.textopos.centery = self.textopos[1] = 15
        if bola.imagem_quadrado.x < 0:
            self.pontos += 1
        tela.blit(self.texto, self.textopos)
        tela.blit(tela , (0 , 0))


#Definição dos objetos para o jogo
raquete = Raquete((12, 57))
raquete2 = Raquete_bot((12, 57))
bola = Bola((15, 15))
placar1 = Placar()
placar2 = Placar_bot()
linha = Linha((6 , 40))
linha2 = Linha2((6 , 40))
linha3 = Linha3((6 , 40))
linha4 = Linha4((6 , 40))
linha5 = Linha5((6 , 40))
linha6 = Linha6((6 , 40))
linha7 = Linha7((6 , 40))
linha8 = Linha8((6 , 40))
linha9 = Linha9((6 , 40))
linha10 = Linha10((6 , 40))
linha11 = Linha11((6 , 40))


#Jogo
while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True
    tela.fill(preto)
    linha.realiza()
    linha2.realiza()
    linha3.realiza()
    linha4.realiza()
    linha5.realiza()
    linha6.realiza()
    linha7.realiza()
    linha8.realiza()
    linha9.realiza()
    linha10.realiza()
    linha11.realiza()
    raquete.realiza()
    raquete2.realiza()
    raquete2.atualiza()
    bola.realiza()
    bola.atualiza()
    placar1.contagem()
    placar2.contagem()
    pygame.display.update()
    posicao_mouse = pygame.mouse.get_pos()
    raquete.imagem_retangulo.centery = posicao_mouse[1]
    raquete.imagem_retangulo.centerx = 40
    if raquete.imagem_retangulo.top < tela_retangulo.top:
        raquete.imagem_retangulo.top = tela_retangulo.top
    if raquete.imagem_retangulo.bottom > tela_retangulo.bottom:
        raquete.imagem_retangulo.bottom = tela_retangulo.bottom