#importamos el programa pygame 
# -*- coding: utf-8 -*-
import pygame
import time
import sys
class Player(object):
    
    def __init__(self):
        self.raton1=pygame.image.load("raton.png").convert_alpha()
        #self.rect = pygame.Rect(32, 32, 16, 16)
        self.raton1=pygame.image.load("raton.png").convert_alpha()
        self.raton2=pygame.image.load("raton2.png").convert_alpha()
        self.ratonarr1=pygame.transform.rotate(self.raton1,180)
        self.ratonarr2=pygame.transform.rotate(self.raton2,180)
        self.ratoniz1=pygame.transform.rotate(self.raton1,-90)
        self.ratoniz2=pygame.transform.rotate(self.raton2,-90)
        self.ratonde1=pygame.transform.rotate(self.raton1,90)
        self.ratonde2=pygame.transform.rotate(self.raton2,90)
        self.anima =[[self.raton1,self.raton2],[self.ratonarr1,self.ratonarr2], #creamos una lusta de listas donde los elementos
                    [self.ratonde1,self.ratonde2],[self.ratoniz1,self.ratoniz2]] #de la lista principal son la imagen en cierta direccion y los elementos secundarios son con la cola hacia un lado
        self.imagen_actual = 0 #Variable auxiliar que nos dira a que direccion ira el raton
        self.imagen = self.anima[self.imagen_actual][0] #
        self.rect = self.imagen.get_rect()#        #self.rect.inflate_ip(-20,-20) mas pequeño el cuadrado o mas grande
        self.rect.top,self.rect.left=200,250
    
        self.dir = 0
    def move(self, dx, dy):
        dx,dy = 0,0
        # Move each axis separately. Note that this checks for collisions both times.
        #if dx != 0:
        self.move_single_axis(dx, dy)
        #if dy != 0:
        #self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
    def update(self,superficie,vx,vy,tiempo):
        if tiempo == 1:
            self.imagen_actual +=1
        if vy > 0:
            self.dir = 0
        elif vy < 0:           
            self.dir = 1
        elif vx > 0:
            self.dir = 2
        elif vx < 0:
            self.dir = 3
         
        if self.imagen_actual+1 >= len(self.anima)-1:
            self.imagen_actual = 0
     
        self.imagen = self.anima[self.dir][self.imagen_actual]

class Fondo(pygame.sprite.Sprite): #Creamos la clase Fondo
    def __init__(self): #Creamos el metodo __init__ el cual inicializa las variables
        self.fondo = pygame.image.load("Fondo.png").convert_alpha() #Cargamos la imagen
        self.fondoreal = pygame.transform.rotate(self.fondo,90) #guardamos la imagen rotada
        self.rect = self.fondoreal.get_rect() #convertimos el fondo en un cuadrado gigante
    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        #if dx != 0:
        self.move_single_axis(dx, dy)
        #if dy != 0:
        #self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.left += dx
        self.rect.top += dy
    def actualizar(self,screen,vx,vy,lista,player1):
        self.move(-vx,-vy) #el fonfo de mueve de su lugar -vx en el eje x  y -vy en el eje y
        screen.blit(self.fondoreal,self.rect) #dibujamos en pantalla el fondo
    
    
class Queso (pygame.sprite.Sprite):    
    def __init__(self): 
        self.imgqueso = pygame.image.load("queso.png").convert_alpha()
        self.imag = self.imgqueso
        self.rect = self.imag.get_rect()
        self.rect.left,self.rect.top = (350,250) #definimos las posicion x,y del sprite del queso 
    def actualizar(self,scren,vx,vy):
        self.rect.move_ip(-vx,-vy)
        #scren.blit(self.imag,self.rect)
        

class Cuadrados(pygame.sprite.Sprite):
    def __init__(self):
        self.meta = pygame.image.load("meta.png")
        self.enemigo = pygame.image.load("ratonmalo.png")
        self.arbol= pygame.image.load("arbol.png").convert_alpha()
        self.consola = pygame.image.load("consola.png")
        self.recta = self.consola.get_rect()
        self.recta.left,self.recta.top = 700,0
        self.rect = self.arbol.get_rect()
        self.rect.left,self.rect.top = -45,0
        


class matriz(object):    
    def __init__(self, pos):      
        walls.append(self)
        self.rect = pygame.Rect((pos[0]-150)*2, (pos[1]-20)*1.45, 40, 40)
def mover(rectangulo,dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        #if dx != 0:
    rectangulo.rect.left += dx
    rectangulo.rect.top += dy    #if dy != 0:
        #self.move_single_axis(0, dy)
    

        
        # Move the rect
class Cursor(pygame.Rect): 
    def __init___(self):
        pygame.Rect(self,0,0,1,1)
    def actualizar(self):
        self.left,self.top = pygame.mouse.get_pos()
class Botones(pygame.sprite.Sprite):
    def __init__(self,x=400,y=250):
        self.nose =pygame.Rect(0,0,8000,800)
        self.imagen_titulo = pygame.image.load("titulo.png")
        self.recttitulo = self.imagen_titulo.get_rect()
        self.recttitulo.left, self.recttitulo.top = -35,0
        
        self.imagen_quit = pygame.image.load ("Quit.png")
        self.imagen_quit1= pygame.image.load ("Quit2.png")
        self.imagen_act = self.imagen_quit
        self.rectquit= self.imagen_act.get_rect()
        self.rectquit.left, self.rectquit.top = 400,450
        
        self.imagen_normal = pygame.image.load("Play.png")
        self.imagen_seleccion = pygame.image.load("Play2.png")
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = x,y #posicion de los botones
    
    def actualizar2 (self,ventana,cursor):
        if cursor.colliderect(self.rectquit):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
            self.imagen_act = self.imagen_quit1
        else:
            self.imagen_act = self.imagen_quit
        ventana.blit(self.imagen_act,self.rectquit)
                
    def actualizar (self,ventana,cursor):
        pygame.draw.rect(ventana,(63,63,63),self.nose)
        ventana.blit(self.imagen_titulo,self.recttitulo)
        if cursor.colliderect(self.rect):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        self.rect.move_ip(5000,5000)
                        self.recttitulo.move_ip(5000,5000)
                        self.nose.move_ip(5000,5000)
                        self.rectquit.move_ip(5000,5000)
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal
        ventana.blit(self.imagen_actual,self.rect)
        
        
        
walls = []
class Quesos(object):
    def __init__(self, pos):      
        quesos.append(self)
        self.rect = pygame.Rect((pos[0]-150)*2, (pos[1]-20)*1.45, 40, 40)
quesos = []
radarpared =[]
radarqueso = []
enemigo = []
radarenemigos =[]
class RadarPared (object):
    def __init__(self,pos):
        radarpared.append(self)
        self.rect = pygame.Rect((pos[0]*0.9)+690,(pos[1])+100,3,3)
class RadarQueso (object):
    def __init__(self,pos):
        radarqueso.append(self)
        self.rect = pygame.Rect((pos[0]*0.9)+690,(pos[1])+100,3,3)
class Poder(pygame.sprite.Sprite):
    def __init__(self):
        self.estrellas = pygame.image.load("estrellas.png")
        self.rect = self.estrellas.get_rect()
        self.rect.left,self.rect.top = 400,400
        self.lista = []
class Enemigos(object):
    def __init__(self,pos):
        
        enemigo.append(self)
        self.rect = pygame.Rect((pos[0]-150)*2,(pos[1]-20)*1.45,40,40)
class RadarEnemigos(object):
    def __init__(self,pos):
        
        radarenemigos.append(self)
        self.rect = pygame.Rect((pos[0]*0.9)+690,(pos[1]+100),3,3)    
        
class Vidas():
    def __init__(self,pos):
        self.vidas = pygame.Rect(728,620,15,15)
        self.vidas2 = pygame.Rect(728,0,15,15)
        self.vidas3 = pygame.Rect(728,0,15,15)
        self.lista = [self.vidas,self.vidas2,self.vidas3]
    def update(self,screen):
        for corazon in self.lista: 
            pygame.draw.rect(screen,(250,250,250),corazon)
        
        
def main():
    
    dsk = True
    
    
    pygame.init()
    
    #creamos la pantalla y el tamaño
    
    screen=pygame.display.set_mode((1100,650))
    
    #sirve para senalar el nombre que va a aparecer en la pantalla
    
    pygame.display.set_caption('Proyecto Raton')
    fuente = pygame.font.Font("fuentes/m04.TTF",18)
    nome = fuente.render("",0,(250,250,250))
    temp=20
    
    #numqueso = fuente.render("Numero de quesos"+str(temp),0,(250,250,250)) 
    salir=False
    reloj=pygame.time.Clock()
    player1 = Player()
    puntos = Queso()
    fondo = Fondo()
    #life = Vidas
    rects = Cuadrados()
    pru=pygame.Rect(0,0,1,1)
    botones = Botones()
    cursor = Cursor(pru)
    poder = Poder()
    
    nepe2 = False
    nepe = 1
    numero= 0

    vx=0
    vy=0
    vele = 4
    veley = 0
    velocidad= 5
    tiempo= 0
    NOMBRE = []
    h=False
    m= False
    asd=120
    izquierda = False
    derecha = False
    abajo = False
    arriba = False
    nivel = 1
    cilantro = 0
    
    
    patata = False
    ############################################################################
    level1 = [
            "*****                                *****",
            "*****#################################### ",
            "*****# **** ************#*#########*****#*",
            "*****# ********** ****####**######## ***#*",
            "*****# ****E************#*********** ***#*",
            "*****# *#*************************** ***#*",
            "*****#    ###*###*# E # # ##  #### ###  # ",
            "*****#  TTTTTTTTTTTTTTTTTTT# ### ### ***#*",
            "*****# ###########           #### ## ***#*",
            "*****#             ### ####TTTTTT    ***#*",
            "*****#   ###### # ####  #### ####### ***#*",
            "*****# #      # # ###    TT          ***#*",
            "*****# # #### # # ### ### #########  ***#*",
            "*****# # #    # # ### ### #       #  ***#*",
            "*****# # # ## # #     ### #       #  ***#*",
            "*****# # # ## # # ### ### # ##### #  ***#*",
            "*****# # #    # # ### ### # ##### #  ***#*",
            "*****### # #### #         #       #  ***#*",
            "*****#   #      # ### ##  ###  ####  ***#*",
            "*****# # # ###### ### ##  ###  ####  ***#*",
            "*****# #          ### ##  ###  ####  ***#*",
            "*****############ ###                ***#*",
            "*****#     ##                  ### # ***#*",
            "*****##### ## #######  ######  ### # ***#*",
            "*****#####        ###  ######      ###**#*",
            "*****##### ## ### ###      ##  ###   ***#*",
            "*****#     ## ###      ##  ##  ###   ***#*",
            "*****# ###### #######  ##  ##  #######**#*",
            "*****#                 ##            ***#*",
            "*****# ###### #######  ######  ####  ***#*",
            "*****# ###### #######  ######  #######**#*",
            "*****#                               ***#*",
            "*****# ### ## #### ##  ### ##  ######***#*",
            "*****# ### ## #### ##  ### ##  ####  ***#*",
            "*****# ### ## ##           ##  ##    ***#*",
            "*****# ### ## ## # ##  ### ##  ## ###***#*",
            "*****#             ##  ###     ## #  ***#*",
            "*****# ## ### #### ##      ##     ###***#*",
            "*****#                               ***#*",
            "*****#          ## ##  ### ##  #######**#*",
            "*****# #### ###                      ***#*",
            "*****# #### ###                      ***#*",
            "*****#        ### ## ### ####  ## ## ***#*",
            "*****# ## ### ### ## ### ####  ## ## ***#*",
            "*****####################################*",

        ]
    #######################################################   
    x = y = 0
    for row in level1:
        for col in row:
            if col == "#":
                matriz((x, y))
            x += 30
        y += 30
        x = 0
    ########################################################    
    wq = qw = 0
    for row in level1:
        for col in row:
            if col == "T":
                #end_rect = pygame.Rect(x, y, 20, 20)
                Quesos((wq,qw))
            wq += 30
        qw += 30
        wq = 0
    xx = yy = 0
    for row in level1:
        for col in row:
            if col == "#":
                #end_rect = pygame.Rect(x, y, 20, 20)
                RadarPared((xx,yy))
            xx += 10
        yy += 10
        xx = 0 
    xxx = yyy = 0   
    for row in level1:
        for col in row:
            if col == "T":
                #end_rect = pygame.Rect(x, y, 20, 20)
                RadarQueso((xxx,yyy))
            xxx += 10
        yyy += 10
        xxx = 0 
    ######################################################## 
    xxxx = yyyy = 0
    for row in level1:
        for col in row:
            if col == 'E':
                #end_rect = pygame.Rect(x, y, 20, 20)
                Enemigos((xxxx,yyyy))
            xxxx += 30
        yyyy += 30
        xxxx = 0 
        
    xxxxx = yyyyy = 0
    for row in level1:
        for col in row:
            if col == "E":
                #end_rect = pygame.Rect(x, y, 20, 20)
                RadarEnemigos((xxxxx,yyyyy))
            xxxxx += 10
        yyyyy += 10
        xxxxx = 0 
        
    while salir!=True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            while True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vx=velocidad
                        vy= 0
                       
                    if event.key == pygame.K_LEFT:
                        vx=-velocidad
                        vy= 0
                        
                    if event.key == pygame.K_DOWN:
                        vx= 0
                        vy= velocidad
                       
                    if event.key == pygame.K_UP:
                        vx=0
                        vy=-velocidad
                        
                    if event.key == pygame.K_SPACE:
                        nepe = asd
                        nepe2 = True
                        
                        if vx > 0:
                            poder.rect.left,poder.rect.top = player1.rect.left-40,player1.rect.top
                            izquierda = True
                            poder.lista.append([poder.rect.left,poder.rect.top])
                            
                        if vy > 0:
                            poder.rect.left,poder.rect.top = player1.rect.left,player1.rect.top-40
                            arriba = True
                        if vx < 0:
                            poder.rect.left,poder.rect.top = player1.rect.left+40,player1.rect.top
                            derecha = True
                        if vy <0 :
                            poder.rect.left,poder.rect.top = player1.rect.left,player1.rect.top+40
                            abajo = True
                        
                    if h == False:
                        NOMBRE.append (event.key)
                        acum = ""
                        for i in NOMBRE:
                            try:
                                if i == 8:
                                    NOMBRE = []
                                    print ""
                                g= chr(i)
                                acum = acum +g
                                nome = fuente.render(acum,0,(250,250,250))
                                
                            except:
                                    if dsk == True:
                                        m = True
                                        x= 120 + time.time()#tiempo limite
                                        dsk = False
                                    break
                            
                break
        if nepe2 == True:
            if nepe - asd == 7:
                poder.rect.move_ip(5000,5000)
        player1.move(vx,vy) 
        numqueso = fuente.render("Quesos Cogidos :"+str(temp),0,(250,250,250))    
        gameOver = fuente.render("GAME OVER!!",0,(250,250,250))
        ganaste= fuente.render("¡¡¡¡¡FELICITACIONES, HAS GANADO!!!!",0,(250,250,250))
        nivelU = fuente.render("Nivel: "+ str(nivel),0,(250,250,250))
        
        times = fuente.render("Hay 60 segundos "+str(asd),0,(250,250,250))
        
        reloj.tick(120)        
        tiempo = tiempo + 1
        if tiempo > 1:
            tiempo = 0   
        screen.fill((0,0,0))
        #rects.mover(vy, vx)
        fondo.actualizar(screen,vx,vy,walls,player1)
        for wall in walls:
            screen.blit(rects.arbol,wall.rect)
            anx,anyy = wall.rect.left,wall.rect.top
            #pygame.draw.rect(screen, (255, 255, 255), wall.rect)
            #wall.rect.move_ip(-vx,-vy)
            mover(wall, -vx, -vy)
            
            if wall.rect.colliderect(player1.rect):
                wall.rect.left,wall.rect.top = anx, anyy
                if vx > 0:
                    wall.rect.left,wall.rect.top = anx, anyy
                
                    vy = 0
                    vx = -velocidad
                if vy > 0:
                    wall.rect.left,wall.rect.top = anx, anyy
                
                    vy = 0
                    vx = velocidad
                if vx < 0:
                    wall.rect.left,wall.rect.top = anx, anyy
                
                    vy = velocidad
                    vx = 0
                if vy < 0:
                    wall.rect.left,wall.rect.top = anx, anyy
                
                    vy = 0
                    vx = velocidad      
        for points in quesos:
            screen.blit(puntos.imgqueso,points.rect)
            points.rect.move_ip(-vx,-vy)
            quesos[numero].rect.move_ip(-3000,-3000) 
            if player1.rect.colliderect(points.rect):
                numero = quesos.index(points.rect,0)
                points.rect.move_ip(-3000,-3000)
                temp -= 1
        
        cursor.actualizar()
        if m == True:
            
            while True:
                tiempo = x - time.time()
                break
            if asd >= 1:
                asd = int(tiempo)
                if temp == 0:
                    cilantro = asd
                    patata = True
                    screen.blit(ganaste,(70,200))
                    screen.blit(rects.meta,(300,300))
                    
                    if patata == True:
                        if asd - cilantro == 3:
                            screen.blit(ganaste,(310,310))
                            screen.blit(rects.meta,(310,310))
                    
                    nivel = 2
                    vx,vy = 0,0
        
        screen.blit(nome,(700,100))
        puntos.actualizar(screen,vx,vy)
        if patata == True:
                if asd - cilantro == 3:
                    screen.blit(ganaste,(310,310))
                    screen.blit(rects.meta,(310,310))
        if asd == 0:
            vx,vy = 0,0
            screen.blit(gameOver,(10,0))
        
        
        if izquierda == True:    
            screen.blit(poder.estrellas,poder.rect)
            mover(poder, -vx, -vy)
            derecha = False
            arriba = False
            abajo = False
        
        if derecha == True:
            screen.blit(poder.estrellas,poder.rect)
            mover(poder, -vx, -vy)
            izquierda = False
            arriba = False
            abajo = False
        if arriba == True:
            screen.blit(poder.estrellas,poder.rect)
            derecha = False
            izquierda = False
            abajo = False
            mover(poder, -vx, -vy)
        if abajo == True:
            derecha = False
            arriba = False
            izquierda = False
            screen.blit(poder.estrellas,poder.rect)
            mover(poder, -vx, -vy)
        
        for enemies in enemigo:
            screen.blit(rects.enemigo,enemies.rect)
            anx,anyy = enemies.rect.left,enemies.rect.top
            enemies.rect.move_ip(vele,veley)
            for wall in walls:
                if (enemies.rect.colliderect(wall.rect) and vele > 0): 
                    enemies.rect.left,enemies.rect.top = anx,anyy
                    vele = 0
                    veley = 4
                    
                if enemies.rect.colliderect(wall.rect) and veley > 0:
                    enemies.rect.left,enemies.rect.top = anx,anyy
                    vele = -4
                    veley = 0
                if enemies.rect.colliderect(wall.rect) and veley < 0:
                    enemies.rect.left,enemies.rect.top = anx,anyy
                    vele = 4
                    veley = 0
                if enemies.rect.colliderect(wall.rect) and vele < 0:
                    enemies.rect.left,enemies.rect.top = anx,anyy
                    vele = 0
                    veley = -4
                if enemies.rect.colliderect(poder.rect):
                    enemies.rect.left,enemies.rect.top = anx,anyy
                    
            mover(enemies, -vx, -vy)
        screen.blit(player1.imagen, player1.rect)
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(700,0,400,650))
        screen.blit(rects.consola,rects.recta)
        screen.blit(times,(728,50))
        screen.blit(nome,(728,70))
        screen.blit(nivelU,(728,90))
        
            
        
        screen.blit(numqueso,(728,30))
        player1.update(screen, vx, vy, tiempo)
        for pared in radarpared:
            pygame.draw.rect(screen,(250,250,250),pared.rect)
            
        for quesp in radarqueso:
            
            pygame.draw.rect(screen,(0,200,200),quesp.rect)
            radarqueso[numero].rect.move_ip(-2000,-2000)

        for zxc in radarenemigos:
            #radarenemigos[segundonumero].rect.move_ip(zxc.rect.left,zxc.rect.top)
            pygame.draw.rect(screen,(250,0,0),zxc.rect)
            for enemies in enemigo:
                zxc.rect.move_ip(enemies.rect.left,enemies.rect.top)
        
        #life.update(screen)
        
        botones.actualizar(screen,cursor)
        botones.actualizar2(screen,cursor)
        pygame.display.update()
    pygame.quit()
    
main()