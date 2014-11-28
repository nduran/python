import pygame
def main():
    pygame.init() # Inicializamos todos los modulos de pygame

    # Fijo El tamano de la pantalla y creo una superficie (surface) con la misma
    
    pantalla =pygame.display.set_mode([500,500])                        # Basicamente el mismo setup de turtle pero en pygame
    pygame.display.set_caption("HOLITAAAA :B")                            # Nombrar la ventana
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

    #Cilo while para mantener abierta la ventana  ( Loop principal )
    
    while (salir == False):
        for event in pygame.event.get():                                                #Recorro todos los eventos producidos (se busca event en la lista de eventos de pygame.event.get())
            if (event.type == pygame.QUIT):                                             # SI el evento es igual a presionar la equis de cerrar ventana, salir es verdadero y se sale del loop
                salir = True
                          
              
        reloj1.tick(20)                                                                                 #Fijo a 20 los fps 
        pantalla.fill(blanco)   
        (cuad.left,cuad.top) = pygame.mouse.get_pos()                                                           # Pinto la surface de blanco
        cuad.left -=   cuad.width/2
        cuad.top -= cuad.width/2
        pygame.draw.rect(pantalla, verde, cuad)                                # pinta rectangulo en un superficie ((superficie, color, rectangulo))
        pygame.draw.rect(pantalla, azul, cuad2)
        pygame.display.update()                                                            # la pantalla se actualiza constantemente
    pygame.quit()                                                                                    #instruccion para cerrar la ventana cuando sale del loop
main()
