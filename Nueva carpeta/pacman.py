import pygame,sys,random,time,pacmansegundolevelcopia,pacmantercerlevelcopia
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pacm= pygame.image.load("imagenes\imagen1.png").convert_alpha()
        pacm1= pygame.image.load("imagenes\imagen2.png").convert_alpha()
        pacmiz = pygame.transform.flip(pacm,True,False)
        pacmiz2 =  pygame.transform.flip(pacm1,True,False)
        pacmarr =  pygame.transform.rotate(pacm,90)
        pacmarr2 = pygame.transform.rotate(pacm1,90) 
        pacmab =  pygame.transform.rotate(pacm,-90)
        pacmab2 = pygame.transform.rotate(pacm1,-90)
        self.imagenes = [  [pacm,pacm1],
                           [pacmiz,pacmiz2],
                           [pacmarr,pacmarr2],
                           [pacmab,pacmab2]]
        self.imagenA = 0
        self.imagen = self.imagenes[self.imagenA][0]
        self.rect = self.imagen.get_rect()
        self.rect.top,self.rect.left = 210,0
        self.direccion = 0
        self.pati = False
        self.f= False
        
    def mover(self,velx,vely):
        self.rect.move_ip(velx,vely)
    def actualizar(self,ventana,velx,vely,t,listarects,enemigos):
        if t == 1:
            self.imagenA +=1
        if vely > 0:
            self.direccion = 3
        elif vely <0:
            self.direccion = 2
        elif velx > 0:
            self.direccion = 0
        elif velx < 0:
            self.direccion = 1
                
        if self.imagenA+1 >= (len(self.imagenes)-1):
            self.imagenA=0
        oldx,oldy=self.rect.left,self.rect.top
        self.mover(velx,vely)
        if  self.colision(listarects):
            self.rect.top,self.rect.left=oldy,oldx
        self.imagen=self.imagenes[self.direccion][self.imagenA]
        ventana.blit(self.imagen,self.rect)
        self.colisionenemi(enemigos)

    def colision(self,listarects):
        for e in listarects:
            if self.rect.colliderect(e):
                return True
        return False

    def colisionenemi (self,enemigos):
        for i in enemigos.enemi:
             if self.rect.colliderect(i):
                 self.f = True
                 self.rect.top,self.rect.left = 210,0

class Rectangulos():
    
    def __init__(self):
        #rectangulos
        self.listarec=[
        pygame.Rect(0,0,45,210), #(x,y,x,y) Primera XY coordenada (Esquina Izquierda),Segunda XY Movimiento
        pygame.Rect(0,245,45,200),
        pygame.Rect(0,445,600,60),
        pygame.Rect(0,0,600,45),
        pygame.Rect(555,45,45,203),
        pygame.Rect(555,283,45,200),
        pygame.Rect(75,80,80,130),#Esquina superior izquierda
        pygame.Rect(185,0,50,110),#No rodea
        pygame.Rect(185,145,50,65),#No rodea
        
        #JUNTOS
        pygame.Rect(470,80,50,70),#Esquina superior derecha
        pygame.Rect(440,80,40,130),#Esquina superior derecha
        
        pygame.Rect(510,190,45,58),#Derecha al lado del pazadiso
        pygame.Rect(270,80,140,70),#Arriba de los fantasmas
        
        #MUROS DE LOS FANTASMAS
        pygame.Rect(270,245,60,125),#izq
        pygame.Rect(365,245,60,125),#der
        pygame.Rect(270,185,140,25),#abajo

        #JUNTOS
        pygame.Rect(77,245,75,70),#Esquina inferior izquierda
        pygame.Rect(77,350,75,60),#Esquina inferior izquierda
        pygame.Rect(185,245,50,124),#Esquina inferior izquierda
        
        pygame.Rect(185,405,115,45),#Abajo izquierda
        pygame.Rect(275,405,120,90),#Abajo de los fantasmas 
        pygame.Rect(455,300,70,110),#Abajo derecha
        pygame.Rect(425,245,50,20)]#En medio derecha
        
        self.r1 = pygame.Rect(600,0,200,500) #consola de info
        
    def actualizar(self,ventana,color5,color4):
        
        pygame.draw.rect(ventana, color4, self.r1)
        for re in self.listarec:
            pygame.draw.rect(ventana, color5, re)

            
class Enemigos(pygame.sprite.Sprite):
    
    def __init__(self):
        self.fan=pygame.image.load("imagenes/Uribe1.png") #azul
        self.fantasma= self.fan
        self.rect= self.fantasma.get_rect()
        self.rect.top=45
        self.rect.left=160
        
        self.fan2=pygame.image.load("imagenes/Santos1.png") #rojo
        self.fantasma2= self.fan2
        self.rect2= self.fantasma2.get_rect()
        self.rect2.top=45
        self.rect2.left=410
        
        self.fan3=pygame.image.load("imagenes/Uribe1.png") #verde
        self.fantasma3= self.fan3
        self.rect3= self.fantasma3.get_rect()
        self.rect3.top=210
        self.rect3.left=333
        
        self.fan4=pygame.image.load("imagenes/Santos1.png") #amarillo
        self.fantasma4= self.fan4
        self.rect4= self.fantasma4.get_rect()
        self.rect4.top=370
        self.rect4.left= 235

        self.enemi = [self.rect, self.rect2, self.rect3, self.rect4]
        
        self.vely1 = 5
        self.vely2 = 5
        self.vely3 = 5
        self.vely4 = 5
        
        
    def mover (self):
        self.rect.move_ip(0,self.vely1)
        self.rect2.move_ip(self.vely2,0)
        self.rect3.move_ip(0,self.vely3)
        self.rect4.move_ip(self.vely4,0)


    def colision (self,listarec):
        for m in listarec:
            if self.rect.colliderect(m):
                self.vely1 = self.vely1*(-1)
                
            if self.rect2.colliderect(m):
                self.vely2 = self.vely2*(-1)
                
            if self.rect3.colliderect(m):
                self.vely3 = self.vely3*(-1)
                
            if self.rect4.colliderect(m):
                self.vely4 = self.vely4*(-1)

    def colisionpac(self,objetos,player):
        if objetos.comer == True:
            for m in self.enemi:
                if m.colliderect(player.rect):
                    m.move_ip(500,500)
                
    def actualizar(self,ventana,listarec,player,objetos):
        self.mover()
        self.colision(listarec)
        self.colisionpac(objetos,player)
        ventana.blit(self.fantasma,self.rect)
        ventana.blit(self.fantasma2,self.rect2)
        ventana.blit(self.fantasma3,self.rect3)
        ventana.blit(self.fantasma4,self.rect4)  

class Objetos():
    def __init__(self):
        self.empa = pygame.image.load("imagenes/empanada.png") #al cambiar de nivel cambiar el archivo por el de los otros
        self.empanada = self.empa
        self.rect1 = self.empanada.get_rect()
        self.rect1.top , self.rect1.left = 150,50
        
        self.saco1 = pygame.image.load("imagenes/saco1.png")
        self.saco = self.saco1
        self.rect2 = self.saco.get_rect()
        self.rect2.top , self.rect2.left = 45,240
        
        self.patines1 = pygame.image.load("imagenes/patines1.png")
        self.patines11 = self.patines1
        self.rect3 = self.patines11.get_rect()
        self.rect3.top , self.rect3.left = 152 , 330

        self.patines2 = pygame.image.load("imagenes/patines.png")
        self.patines22 = self.patines2
        self.rect4 = self.patines22.get_rect()
        self.rect4.top , self.rect4.left = 152 , 330

        self.reloj1 = pygame.image.load("imagenes/reloj.png")
        self.reloj11 = self.reloj1
        self.rect8 = self.reloj11.get_rect()
        self.rect8.top , self.rect8.left = 152 , 330

        self.reloj2 = pygame.image.load("imagenes/reloj1.png")
        self.reloj22 = self.reloj2
        self.rect5 = self.reloj22.get_rect()
        self.rect5.top , self.rect5.left = 152 , 330
        self.puntaje = 0
        self.comer= False
        self.i= 1
        self.pati = False
        self.poder = [[self.patines1,self.rect3],[self.patines2,self.rect4],[self.reloj1,self.rect8],[self.reloj2,self.rect5]]
        self.p = 0
        self.matrix=[]
        self.lista = []
        self.matrix2 = []
        self.lista2 =[]

        self.rect1.top, self.rect1.left = 135, 45
        self.lista2.append(self.rect1)
        
        self.rect10 = self.empanada.get_rect()
        self.rect10.top, self.rect10.left = 300, 240
        self.lista2.append(self.rect10)

        self.rect11 = self.empanada.get_rect()
        self.rect11.top, self.rect11.left = 155, 500
        self.lista2.append(self.rect11)

        self.rect12 = self.empanada.get_rect()
        self.rect12.top, self.rect12.left = 140, 410
        self.lista2.append(self.rect12)
        
        for i in range(9):
            left = self.rect2.left
            top = self.rect2.top
            self.rect2.top = 45
            self.rect2.left += 41
            self.lista.append(pygame.Rect(left,top,self.rect2.width,self.rect2.height))
        self.matrix.append (self.lista)
        
        self.rect2.left = 50
        
        for i in range(4):
            left = self.rect2.left
            top = self.rect2.top
            self.rect2.top = 45
            self.rect2.left += 35
            self.lista.append(pygame.Rect(left,top,self.rect2.width,self.rect2.height))
        self.matrix.append (self.lista)
        
        self.rect2.left = 0
        for i in range(13):
            left = self.rect2.left
            top = self.rect2.top
            self.rect2.top = 210
            self.rect2.left += 40
            self.lista.append(pygame.Rect(left,top,self.rect2.width,self.rect2.height))
        self.matrix.append (self.lista)

        
        self.rect2.left = 20
        for i in range(5):
            left = self.rect2.left
            top = self.rect2.top
            self.rect2.top = 317
            self.rect2.left += 35
            self.lista.append(pygame.Rect(left,top,self.rect2.width,self.rect2.height))
        self.matrix.append (self.lista)

        self.rect2.left = 20
        for i in range(5):
            left = self.rect2.left
            top = self.rect2.top
            self.rect2.top = 411
            self.rect2.left += 35
            self.lista.append(pygame.Rect(left,top,self.rect2.width,self.rect2.height))
        self.matrix.append (self.lista)

        self.rect2.left = 125
        for i in range(9):
            left = self.rect2.left
            top = self.rect2.top
            self.rect2.top = 370
            self.rect2.left += 35
            self.lista.append(pygame.Rect(left,top,self.rect2.width,self.rect2.height))
        self.matrix.append (self.lista)

        self.rect2.left = 370
        for i in range(5):
            left = self.rect2.left
            top = self.rect2.top
            self.rect2.top = 411
            self.rect2.left += 40
            self.lista.append(pygame.Rect(left,top,self.rect2.width,self.rect2.height))
        self.matrix.append (self.lista)

        self.rect2.left = 123
        for i in range(4):
            left = self.rect2.left
            top = self.rect2.top
            self.rect2.top = 110
            self.rect2.left += 40
            self.lista.append(pygame.Rect(left,top,self.rect2.width,self.rect2.height))
        self.matrix.append (self.lista)

        
    def sacos(self,player):
        
        for j in range(len(self.matrix)):
            for i in self.lista:
                if player.colliderect(i): 
                    self.puntaje = self.puntaje + 10
                    i.move_ip(500,500)
            
        return self.puntaje
    
    def poderes (self):
        self.p = random.randint(0,3)
        
    def actualizar(self,ventana,player,vel,y):
        self.sacos(player.rect)
        self.poderes()
        for i in self.lista2:
                ventana.blit(self.empa,i)
        for i in self.lista:
                ventana.blit(self.saco1,i)    
        ventana.blit(self.poder[self.p][0],self.poder[self.p][1])
    
class Cursor(pygame.Rect): 
    def __init___(self):
        pygame.Rect(self,0,0,1,1)
    def actualizar(self):
        self.left,self.top = pygame.mouse.get_pos()

class Botones(pygame.sprite.Sprite):
    def __init__(self,x=350,y=200):
        self.nose =pygame.Rect(0,0,800,800)
        self.imagen_titulo = pygame.image.load("imagenes/titulo.png")
        self.recttitulo = self.imagen_titulo.get_rect()
        self.recttitulo.left, self.recttitulo.top = 50,0
        
        self.imagen_quit = pygame.image.load ("imagenes/boton2.png")
        self.imagen_quit1= pygame.image.load ("imagenes/boton3.png")
        self.imagen_act = self.imagen_quit
        self.rectquit= self.imagen_act.get_rect()
        self.rectquit.left, self.rectquit.top = 350,300
        
        self.imagen_normal = pygame.image.load("imagenes/boton.png")
        self.imagen_seleccion = pygame.image.load("imagenes/boton1.png")
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
        pygame.draw.rect(ventana,(0,140,60),self.nose)
        ventana.blit(self.imagen_titulo,self.recttitulo)
        if cursor.colliderect(self.rect):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        self.rect.move_ip(500,500)
                        self.recttitulo.move_ip(500,500)
                        self.nose.move_ip(500,500)
                        self.rectquit.move_ip(500,500)
                        popo = True
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal
        ventana.blit(self.imagen_actual,self.rect)
        
def main():
    dsk = True
    #rojo y verde y azul
    color= pygame.Color(0,140,60)
    color2=pygame.Color(0,100,255)
    color3=pygame.Color(0,0,0)
    color4=pygame.Color(190,190,190)
    color5=pygame.Color(0,0,0) 
    
    
    pygame.init()
    ventana= pygame.display.set_mode((800,500))
    pygame.display.set_caption("!!!JuanC-Man!!!") 
    reloj=pygame.time.Clock() #fps
    
    fondo = pygame.image.load("imagenes/Bandera_Colombia.jpg")
    vel=5
    
    
    pru=pygame.Rect(0,0,1,1)
    player = Player()
    
    rectangulos = Rectangulos()
    enemigos = Enemigos()
    vidas= 3
    objetos = Objetos()
    
    botones = Botones()
    cursor = Cursor(pru)
    
    velx=0
    vely=0
    
    nivel = 1
   
    
    letra=pygame.font.Font("fuente/Fipps-Regular.otf",15) 
    letra1=pygame.font.Font("fuente/Fipps-Regular.otf",50)
    
    texto2=letra1.render("!!!GAME OVER!!!",0,(255,255,255))
    texto5=letra.render("Jugador: ",0,(0,0,0))

    nome = letra.render("",0,(0,0,0))
    NOMBRE = []
    h=False
    
    popo = False
    t = 0 
    y=120
    salir = False
    m= False
    mo = 5
    
    while salir == False:
        puntaje = objetos.sacos(player.rect)
        ventana.blit(fondo,(0,0)) #el fondo de la ventana
        texto3=letra.render("Puntaje: "+ str(puntaje),0,(0,0,0))
     
        timer=letra.render("Tiempo: " + str(y),0,(0,0,0))
        texto1=letra.render("Vidas: " + str(vidas),0,(0,0,0))
        texto4=letra.render("Nivel: "+str(nivel),0,(0,0,0))
        for event in pygame.event.get():
            if event.type== QUIT :
                pygame.quit()
                sys.exit()
            
            while True:
                    
                if event.type == pygame.KEYDOWN:  #para mover la imagen con teclas
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_LEFT :
                        velx=-vel
                        vely= 0
                    if event.key==K_RIGHT :
                        velx=vel                                  
                        vely= 0
                    if event.key==K_UP : 
                        vely=-vel

                        velx= 0
                    if event.key==K_DOWN :
                        vely=vel
                        velx= 0
                        
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
                                nome = letra.render(acum,0,(0,0,0))
                                
                            except:
                                    if dsk == True:
                                        m = True
                                        x= 120 + time.time()#tiempo limite
                                        dsk = False
                                    break
                            
                break
        
        reloj.tick(20) 
        t+=1
        
        if player.rect.colliderect(objetos.rect4):
            vel = 2
            objetos.i= y
            objetos.pati = True
            
            objetos.rect4.move_ip(500,500)
            objetos.rect3.move_ip(500,500)
            objetos.rect8.move_ip(500,500)
            objetos.rect5.move_ip(500,500)
        if objetos.pati == True:
            if objetos.i - y == 10:
                vel = 5

        if player.rect.colliderect(objetos.rect3):
            vel = 10
            objetos.i= y
            objetos.pati = True
            
            objetos.rect4.move_ip(500,500)
            objetos.rect3.move_ip(500,500)
            objetos.rect8.move_ip(500,500)
            objetos.rect5.move_ip(500,500)
        if objetos.pati == True:
            if objetos.i - y == 10:
                vel = 5


        if player.rect.colliderect(objetos.rect8):
            y = y + 20

        if player.rect.colliderect(objetos.rect5):
            y = y - 10
            
        for i in objetos.lista2:
            if player.rect.colliderect(i): #las empanadas van a estar en una lista
                objetos.comer = True
                objetos.i = y
                objetos.pati = True
                objetos.puntaje = objetos.puntaje + 10
                i.move_ip(500,500)
            if objetos.pati == True:
                if objetos.i - y == 15:
                    objetos.comer= False
                    print"fn"
        


        if player.rect.colliderect(objetos.rect4) or player.rect.colliderect(objetos.rect3) or player.rect.colliderect(objetos.rect5) or player.rect.colliderect(objetos.rect8):
            objetos.i = y
            objetos.pati = True
        if objetos.pati == True:
            if objetos.i - y == 5:
                objetos.rect4.top , objetos.rect4.left = 152 , 330
                objetos.rect3.top , objetos.rect3.left = 152 , 330
                objetos.rect8.top , objetos.rect8.left = 152 , 330
                objetos.rect5.top , objetos.rect5.left = 152 , 330
            
        for i in enemigos.enemi:
            if player.rect.colliderect(i):
                vidas -= 1
        if t>1:
            t=0
            
        if player.rect.left<0:
            player.rect.move_ip(620,38)

        if player.rect.left>600:
            player.rect.move_ip(-620,-38)
        objetos.actualizar(ventana,player,vel,y)    
        player.actualizar(ventana,velx,vely,t,rectangulos.listarec,enemigos)
        rectangulos.actualizar(ventana, color5, color4)
        enemigos.actualizar(ventana,rectangulos.listarec,player,objetos)
        cursor.actualizar()
        
        
        
        
        if m == True:
            
            while True:
                tiempo = x - time.time()
                break
            if y >= 1:
                y = int(tiempo)
                if y <= 0:
                    velx,vely = 0,0
                if y==0 or vidas == 0 :
                    ventana.blit(texto2,(10,0))
                    velx,vely = 0,0
                if objetos.puntaje == 550:
                    nivel = 2
                    
        if nivel == 2:
            pacmansegundolevelcopia.main2()

                    
        ventana.blit(timer,(620,60))
        ventana.blit(texto1,(620,250))
        ventana.blit(texto3,(620,107))
        ventana.blit(texto4,(620,5))
        ventana.blit(texto5,(620,170))
        
        ventana.blit(nome,(620,200))
        
        botones.actualizar(ventana,cursor)
        botones.actualizar2(ventana,cursor)
        
        
        
        pygame.display.update()  
main()
