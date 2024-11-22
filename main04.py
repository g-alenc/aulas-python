import pygame 
from pygame.locals import * 


# ADICIONANDO A POSSIBILIDADE DE MUDARMOS A DIREÇÃO  DA COBRA COM AS TECLAS


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

fps = 10 
clock = pygame.time.Clock() 
while True:
    clock.tick(fps) 
    screen.fill('BLACK') 

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # confere se alguma tecla foi pressionada
            if event.key == K_UP: # confere se a tecla UP foi clicada 
                dir = 0, -1
            if event.key == K_DOWN: # confere se a tecla DOWN foi clicada 
                dir = 0, 1
            if event.key == K_LEFT: # confere se a tecla LEFT foi clicada 
                dir = -1, 0
            if event.key == K_RIGHT: # confere se a tecla RIGHT foi clicada 
                dir = 1, 0
        if event.type == QUIT: 
            pygame.quit() 

    desenhar_cobra()
    atualizar_cobra() 

    pygame.display.update() 