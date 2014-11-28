import pygame
pygame.init()
pantalla = pygame.display.set_mode((500,500))
salir = False


while (salir == False):
        for event in pygame.event.get():                                                #Recorro todos los eventos producidos (se busca event en la lista de eventos de pygame.event.get())
            if (event.type == pygame.QUIT):                                             # SI el evento es igual a presionar la equis de cerrar ventana, salir es verdadero y se sale del loop
                salir = True
                
        pantalla.fill((200,200,200))
        pygame.display.flip()
pygame.quit()