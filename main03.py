import pygame 
from pygame.locals import * 


# CRIANDO A FUNÇÃO QUE ATUALIZA A POSIÇÃO DA COBRA


def atualizar_cobra(): # atualiza a posição dos quadrados da cobra
    cobra[0] = cobra[0][0] + (dir[0]*quadrado_tamanho[0]), cobra[0][1] + (dir[1]*quadrado_tamanho[1]) # atualiza a cabeça

    for i in range(len(cobra)-1, 0, -1): # atualiza os outros quadrados da cobra
        cobra[i] = cobra[i-1] # faz um quadrado ser igual ao quadrado que o precede

def desenhar_cobra(): 
    for pos_quadrado in cobra: 
        pygame.draw.rect(screen, cor_cobra, (pos_quadrado, quadrado_tamanho)) 

pygame.init() 
screen_size = (600, 600) 
screen = pygame.display.set_mode(screen_size)
n_quadrados = 60
quadrado_tamanho = screen_size[0]//n_quadrados, screen_size[1]//n_quadrados 

cobra = [(300, 300)] 
dir = 1, 0 
cor_cobra = 255, 255, 255 
atualizar_cobra()
fps = 10 
clock = pygame.time.Clock() 
while True:
    clock.tick(fps) 
    screen.fill('BLACK') 

    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit() 

    desenhar_cobra()
    atualizar_cobra() # chamando a função que acabamos de criar

    pygame.display.update() 