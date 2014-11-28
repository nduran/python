import pygame
def main():
    pygame.init() # Inicializamos todos los modulos de pygame

    # Fijo El tamano de la pantalla y creo una superficie (surface) con la misma
    
    pantalla =pygame.display.set_mode([500,500])                        # Basicamente el mismo setup de turtle pero en pygame
    pygame.display.set_caption("Ventana del juego")                            # Nombrar la ventana
    salir = False
    #Crear un reloj que recibe como parametro fps (frames per seconds ( cuadros por segundo) )

    reloj1 = pygame.time.Clock()

    #Colores
    azul = (2,2,251)
    rojo = (200,20,50)
    verde = (2,250,2)
    blanco = (255,255,255)                                                                      # Esta tupla es el color blanco segun la paleta de colores RGB ( RED GREEN AND BLUE)

    cuad = pygame.Rect (250,250,50,50)                                               # submodulo .rect sirve para hacer rectangulos x,y, base, altura
    cuad2 = pygame.Rect (250,250,25,25)  
    pulsado = False
    mover = 'n'
    x_pos = 300
    speed = 100
    tiempo = pygame.time.Clock.tick(36)
    seg = tiempo / 1000
    asd = seg * speed
    #Cilo while para mantener abierta la ventana  ( Loop principal )
    
    while (salir == False):
        for event in pygame.event.get():                                                #Recorro todos los eventos producidos (se busca event en la lista de eventos de pygame.event.get())
            if (event.type == pygame.QUIT):                                             # SI el evento es igual a presionar la equis de cerrar ventana, salir es verdadero y se sale del loop
                salir = True
                
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_DOWN):
                    pulsado = True
                    mover = 'i'
                    cuad.move_ip(0,10)
                if (event.key == pygame.K_RIGHT):
                    pulsado = True
                    mover = 'd'
                    cuad.move_ip(10,0)
                if (event.key == pygame.K_UP):
                    pulsado = True
                    mover = 'r'
                    cuad.move_ip(0,-10)
                if (event.key == pygame.K_LEFT):
                    pulsado = True
                    mover = 'p'
                    cuad.move_ip(-10,0)
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_DOWN):
                    pulsado = False
                    mover = 'n'
                    cuad.move_ip(0,10)
                if (event.key == pygame.K_RIGHT):
                    pulsado = False
                    mover = 'n'
                    cuad.move_ip(10,0)
                if (event.key == pygame.K_UP):
                    pulsado = False
                    mover = 'n'
                    cuad.move_ip(0,-10)
                if (event.key == pygame.K_LEFT):
                    pulsado = False
                    mover = 'n'
                    cuad.move_ip(-10,0)
        
            if pulsado = True:
                if mover = 'i':
                    x_pos -=asd
        
        reloj1.tick(20)                                                                                 #Fijo a 20 los fps 
        pantalla.fill(blanco)
        (oldx,oldy) = (cuad.left,cuad.top)                                                                     # Pinto la surface de blanco
        pygame.draw.rect(pantalla, verde, cuad)                                # pinta rectangulo en un superficie ((superficie, color, rectangulo))
        if cuad.colliderect(cuad2):                                             #si el cuadrado 1 colosiona con el 2 x y y toman el valor antes de que cambien con el mouse
            (cuad.left,cuad.top) = (oldx,oldy)
        pygame.draw.rect(pantalla, azul, cuad2)
        pygame.display.update()                                                            # la pantalla se actualiza constantemente
    pygame.quit()                                                                                    #instruccion para cerrar la ventana cuando sale del loop
main()
