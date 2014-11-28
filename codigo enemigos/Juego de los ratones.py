#importamos el programa pygame y sys

import pygame, sys
import random
from pygame.locals import*

def main():
    pygame.init()
    
    #creamos la pantalla y el tamaño
    
    screen=pygame.display.set_mode((600,600))
    
    #sirve para señalar el nombre que va a aparecer en la pantalla
    
    pygame.display.set_caption('Escapa de los ratones')
    salir=False
    reloj=pygame.time.Clock()
    blanco=(255,255,255)
    raton1=pygame.image.load("raton.png").convert_alpha()
    raton2=pygame.image.load("raton2.png").convert_alpha()
    raton_pos_x=30
    raton_pos_y=30

    ratonmalo = pygame.image.load ("ratonmalo.png")
    posicionx = 500 #posicion en x del raton malo
    posiciony = 500 #posicion en y del raton malo
    eje = 0 #si me muevo en el eje x(0) o eje y(1)
    #yox = raton_pos_x #posicion inicial en x del jugador
    #yoy = raton_pos_y #posicion inicial en y del jugador
    
    
    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    raton_pos_x=raton_pos_x - 10
                    raton1,raton2=raton2,raton1
                    if (raton_pos_x<0):
                        raton_pos_x=raton_pos_x + 10
                if event.key==pygame.K_RIGHT:
                    raton_pos_x=raton_pos_x + 10
                    raton1,raton2=raton2,raton1
                    if (raton_pos_x>550):
                        raton_pos_x=raton_pos_x - 10
                if event.key==pygame.K_UP:
                    raton_pos_y=raton_pos_y - 10
                    raton1,raton2=raton2,raton1
                    if (raton_pos_y<0):
                        raton_pos_y=raton_pos_y + 10
                if event.key==pygame.K_DOWN:
                    raton_pos_y=raton_pos_y + 10
                    raton1,raton2=raton2,raton1
                    if (raton_pos_y>550):
                        raton_pos_y=raton_pos_y - 10
                        
        

        
            if posicionx != raton_pos_x and posiciony != raton_pos_y:
            #movx = 30 #lo que se hace con las teclas
            #movy = 30
            #yox = yox + movx #para saber la posicion del usuario y el malo se mueva
            #yoy = yoy + movy
                if eje == 0:
                    if raton_pos_x < posicionx: #moviemiento hacia la izq del malo
                        posicionx = posicionx - 10
                    if raton_pos_x > posicionx: #movimiento hacia la der del malo
                        posicionx = posicionx + 10
                    if raton_pos_x == posicionx: #ahora se va a mover en el eje y
                        eje = 1
                if eje == 1:
                    if raton_pos_y < posiciony: #movimiento hacia arriba del malo
                        posiciony = posiciony - 10
                    if raton_pos_y > posiciony: #movimiento hacia abajo del malo
                        posiciony = posiciony + 10
                    if raton_pos_y == posiciony: #cambia el eje y para moverse en el eje x
                        eje = 0


        
            
        reloj.tick(20)
        screen.fill(blanco)
        screen.blit(raton1,(raton_pos_x,raton_pos_y))
        screen.blit(ratonmalo,(posicionx, posiciony))
        pygame.display.update()
    pygame.quit()
    
main()
