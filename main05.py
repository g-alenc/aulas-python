import pygame 
from pygame.locals import * 
from random import randint # importando a biblioteca para gerar numeros aleatorios


# ADICIONANDO A COMIDA E A O OPÇÃO DE COME-LA


def atualizar_comida(comida): # função que atualiza a posição da comida e o tamanho da cobra
    pygame.draw.rect(screen, cor_comida, (comida, quadrado_tamanho)) # desenha a comida na tela

    if cobra[0] == comida: #confere se a posição da cobra é a mesma que a da comida
        cobra.append(cobra[0]) # adiciona mais um quadrado para a cobra
        comida = randint(1, n_quadrados-1)*quadrado_tamanho[0], randint(1, n_quadrados-1)*quadrado_tamanho[1] # atualiza a posição da comida
    
    return comida # retorna a nova posição da comida

def atualizar_cobra():
    cobra[0] = cobra[0][0] + (dir[0]*quadrado_tamanho[0]), cobra[0][1] + (dir[1]*quadrado_tamanho[1]) 

    for i in range(len(cobra)-1, 0, -1):
        cobra[i] = cobra[i-1] 

def desenhar_cobra(): 
    for pos_quadrado in cobra: 
        pygame.draw.rect(screen, cor_cobra, (pos_quadrado, quadrado_tamanho)) 

pygame.init() 
screen_size = (600, 600) 
screen = pygame.display.set_mode(screen_size)
n_quadrados = 60
quadrado_tamanho = screen_size[0]//n_quadrados, screen_size[1]//n_quadrados 

cobra = [(300, 300), (300, 300)] 
dir = 1, 0 
cor_cobra = 255, 255, 255 
comida = randint(0, n_quadrados)*quadrado_tamanho[0], randint(0, n_quadrados)*quadrado_tamanho[1] # gerando a comida em uma posição aleatoria da tela
cor_comida = 255, 0, 0 # cor da comida

fps = 10 
clock = pygame.time.Clock() 
while True:
    clock.tick(fps) 
    screen.fill('BLACK') 

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                dir = 0, -1
            if event.key == K_DOWN: 
                dir = 0, 1
            if event.key == K_LEFT: 
                dir = -1, 0
            if event.key == K_RIGHT:
                dir = 1, 0
        if event.type == QUIT: 
            pygame.quit() 

    desenhar_cobra()
    atualizar_cobra()
    comida = atualizar_comida(comida) # chama a função que criamos e atualiza a posição da cobra para uma nova posição aleatoria
    pygame.display.update() 