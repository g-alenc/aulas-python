import pygame 
from pygame.locals import * 


# ADICIONANDO ALGUMAS VARIÁVEIS QUE VÃO SER ÚTEIS MAIS A FRENTE


pygame.init() 
screen_size = (600, 600) 
screen = pygame.display.set_mode(screen_size)
n_quadrados = 60 # quantidade de quadrados na tela
quadrado_tamanho = screen_size[0]//n_quadrados, screen_size[1]//n_quadrados # definindo o tamanho dos quadrados do grid

cobra = [(300, 300)] # criando uma cobra com apenas a cabeça
dir = 1, 1 # variavel que será responsavel pela direção vetical e horizontal da cobra
cor_cobra = 255, 255, 255 # definindo a cor da cobra

fps = 10 
clock = pygame.time.Clock() 
while True:
    clock.tick(fps) 
    screen.fill('BLACK') 

    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit() 

    pygame.display.update() 