import pygame 
from pygame.locals import * 


# CRIANDO A FUNÇÃO PARA DESENHAR A COBRA


def desenhar_cobra(cobra, cor_cobra): # função que desenha os quadrados da cobra
    for pos_quadrado in cobra: # passando por cada quadrado da cobra 
        pygame.draw.rect(screen, cor_cobra, (pos_quadrado, quadrado_tamanho)) # desenhando os quadrados da cobra

pygame.init() 
screen_size = (600, 600) 
screen = pygame.display.set_mode(screen_size)
n_quadrados = 60
quadrado_tamanho = screen_size[0]//n_quadrados, screen_size[1]//n_quadrados 

cobra = [(300, 300)] 
dir = 1, 1 
cor_cobra = 255, 255, 255 

fps = 10 
clock = pygame.time.Clock() 
while True:
    clock.tick(fps) 
    screen.fill('BLACK') 

    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit() 

    desenhar_cobra(cobra, cor_cobra) # chamando a função que desenha a cobra

    pygame.display.update() 