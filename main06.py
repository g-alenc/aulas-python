import pygame 
from pygame.locals import * 
from random import randint 


# ADICIONANDO AS COLISÕES COM A PAREDE


def conferir_colisao(): # função que confere se a cobra colidiu com a parede. Se colidir retorna True senão, retorna False
    if cobra[0][0] < 0: # confere se a cobra colidiu com a parede da esquerda
        return True 
    if cobra[0][1] < 0: # confere se a cobra colidiu com a parede de cima
        return True 
    if cobra[0][0] > screen_size[0]: # confere se a cobra colidiu com a parede da direita
        return True 
    if cobra[0][1] > screen_size[1]: # confere se a cobra colidiu com a parede de baixo
        return True 
    return False

def atualizar_comida(comida):
    pygame.draw.rect(screen, cor_comida, (comida, quadrado_tamanho))

    if cobra[0] == comida: 
        cobra.append(cobra[0]) 
        comida = randint(1, n_quadrados-1)*quadrado_tamanho[0], randint(1, n_quadrados-1)*quadrado_tamanho[1] 
    
    return comida

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
comida = randint(0, n_quadrados)*quadrado_tamanho[0], randint(0, n_quadrados)*quadrado_tamanho[1] 
cor_comida = 255, 0, 0 

fps = 10 
clock = pygame.time.Clock() 
while True:
    
    clock.tick(fps) 
    screen.fill('BLACK') 

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                dir = 0, -1
            if event.key == K_s: 
                dir = 0, 1
            if event.key == K_a: 
                dir = -1, 0
            if event.key == K_d:
                dir = 1, 0
        if event.type == QUIT: 
            pygame.quit() 


    if conferir_colisao(): # se a função de colisão for verdadeira, fecha a janela
        pygame.quit() 

    desenhar_cobra()
    atualizar_cobra()
    comida = atualizar_comida(comida)
    
    pygame.display.update() 