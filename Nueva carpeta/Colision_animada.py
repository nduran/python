import pygame
import random
def main():
    pygame.init() # Inicializamos todos los modulos de pygame

    # Fijo El tamano de la pantalla y creo una superficie (surface) con la misma
    
    pantalla =pygame.display.set_mode([500,500])                        # Basicamente el mismo setup de turtle pero en pygame
    pygame.display.set_caption("VENTANA x")                            # Nombrar la ventana
    fuente = pygame.font.SysFont("nose", 24, bold = True)
    
    salir = False
    #Crear un reloj que recibe como parametro fps (frames per seconds ( cuadros por segundo) )

    reloj1 = pygame.time.Clock()
    #Colores
    azul = (2,2,251)
    rojo = (200,20,50)
    verde = (2,250,2)
    blanco = (255,255,255)                                                                      # Esta tupla es el color blanco segun la paleta de colores RGB ( RED GREEN AND BLUE)
    texto = fuente.render("haga click sobre los rectangulos",0,azul)
    lis = []
    for cuad2 in range (35):
        x=random.randint(0,500)
        lis.append(pygame.Rect(x,random.randint(0,500),random.randint(20,50),random.randint(20,50)))
    cuad = pygame.Rect (250,250,50,50)                                               # submodulo .rect sirve para hacer rectangulos x,y, base, altura 

    #Cilo while para mantener abierta la ventana  ( Loop principal )
    while (salir == False):
        for event in pygame.event.get():                                                #Recorro todos los eventos producidos (se busca event en la lista de eventos de pygame.event.get())
            if (event.type == pygame.QUIT):                                             # SI el evento es igual a presionar la equis de cerrar ventana, salir es verdadero y se sale del loop
                salir = True
            if (event.type == pygame.MOUSEBUTTONDOWN):
                for cuads in lis:
                    if cuad.colliderect(cuads):                                             #si el cuadrado 1 colosiona con el 2 x y y toman el valor antes de que cambien con el mouse
                        cuads.move_ip(1000,1000)
                        
                          
              
        reloj1.tick(20)                                                                                 #Fijo a 20 los fps 
        pantalla.fill(blanco)
        (cuad.left,cuad.top) = pygame.mouse.get_pos()                                                           # Pinto la surface de blanco
        cuad.left -=   cuad.width/2
        cuad.top -= cuad.width/2
        pantalla.blit(texto,(5,5))
        pygame.draw.rect(pantalla, verde, cuad)                                # pinta rectangulo en un superficie ((superficie, color, rectangulo))
        for cuads in lis: 
            pygame.draw.rect(pantalla, rojo, cuads)
            
        pygame.display.update()                                                            # la pantalla se actualiza constantemente
    pygame.quit()                                                                                    #instruccion para cerrar la ventana cuando sale del loop
main()
