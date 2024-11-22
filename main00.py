import pygame # importando a biblioteca PYGAME, que iremos utilizar para criar a tela do jogo
from pygame.locals import * # uma parte da biblioteca utilizada para ler as teclas do teclado


#CRIANDO UMA JANELA PRETA QUE PODE SER FECHADA


pygame.init() # iniciando a biblioteca pygame
screen_size = (600, 600) # escolhendo os valores do tamanho da tela
screen = pygame.display.set_mode(screen_size) # criando a tela 

fps = 10 # velocidade de atualização dos quadros
clock = pygame.time.Clock() # criando um objeto para regular a veloicidade dos frames

while True: # laço principal do jogo
    clock.tick(fps) # escolhendo a velocidade da atualização dos frames
    screen.fill('BLACK') # preenchendo a tela de preto

    for event in pygame.event.get(): # conferindo os eventos do usuario
        if event.type == QUIT: # conferindo se o usuário fechou a janela
            pygame.quit() # fecha a tela


    pygame.display.update() # atualiza a tela