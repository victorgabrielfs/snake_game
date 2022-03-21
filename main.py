import random

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.load('./soundtrack/Lavender Town - Musica Da Deep Web.mp3')
pygame.mixer.music.play(-1)
som_colisao = pygame.mixer.Sound('./soundtrack/Som de moeda do sonic.mp3')
som_colisao.set_volume(0.2)
largura, altura = 640, 480
x_snake = largura/2 - 20
y_snake = altura/2 - 25
x_apple = random.randint(0, largura)
y_apple = random.randint(0, altura)
font = pygame.font.SysFont('gabriola', 40, False, True)
pontos = 0
lista_snake = []
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
x_controle = 20
y_controle = 0


def aumenta_snake(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (255, 255, 255), (XeY[0], XeY[1], 20, 20))


# Loop infinito
while True:
    clock.tick(10)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = font.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == 20:
                    pass
                else:
                    x_controle = -20
                    y_controle = 0
            if event.key == K_s:
                if y_controle == -20:
                    pass
                else:
                    x_controle = 0
                    y_controle = 20
            if event.key == K_w:
                if y_controle == 20:
                    pass
                else:
                    x_controle = 0
                    y_controle = -20
            if event.key == K_d:
                if x_controle == -20:
                    pass
                else:
                    x_controle = 20
                    y_controle = 0

    x_snake += x_controle
    y_snake += y_controle
    snake = pygame.draw.rect(tela, (255, 255, 255), (x_snake, y_snake, 20, 20))
    apple = pygame.draw.rect(tela, (255, 0, 0), (x_apple, y_apple, 20, 20))
    lista_head = []
    if snake.colliderect(apple):
        x_apple = random.randint(0, largura - 50)
        y_apple = random.randint(0, altura - 50)
        pontos = pontos + 1
        som_colisao.play()

    if len(lista_snake) > pontos:
        del(lista_snake[0])

    lista_head.append(x_snake)
    lista_head.append(y_snake)

    lista_snake.append(lista_head)

    aumenta_snake(lista_snake)

    tela.blit(texto_formatado, (450, 40))

    pygame.display.update()

