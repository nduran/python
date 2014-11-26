#importamos el programa pygame 
# -*- coding: utf-8 -*-
import pygame
import random
class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.fondo = pygame.image.load("Fondo.png").convert_alpha()
        self.fondoreal = pygame.transform.rotate(self.fondo,90)
        self.rect = self.fondoreal.get_rect()
    def actualizar(self,screen,vx,vy):
        self.rect.move_ip(-vx,-vy)
        screen.blit(self.fondoreal,self.rect)
class Queso (pygame.sprite.Sprite):    
    def __init__(self):
        self.imgqueso = pygame.image.load("queso.png").convert_alpha()
        self.imag = self.imgqueso
        self.rect = self.imag.get_rect()
        self.rect.left,self.rect.top = (350,250) 
    def actualizar(self,scren,vx,vy):
        self.rect.move_ip(-vx,-vy)
        scren.blit(self.imag,self.rect)
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.raton1=pygame.image.load("raton.png").convert_alpha()
        self.raton2=pygame.image.load("raton2.png").convert_alpha()
        self.ratonarr1=pygame.transform.rotate(self.raton1,180)
        self.ratonarr2=pygame.transform.rotate(self.raton2,180)
        self.ratoniz1=pygame.transform.rotate(self.raton1,-90)
        self.ratoniz2=pygame.transform.rotate(self.raton2,-90)
        self.ratonde1=pygame.transform.rotate(self.raton1,90)
        self.ratonde2=pygame.transform.rotate(self.raton2,90)
        self.anima =[[self.raton1,self.raton2],[self.ratonarr1,self.ratonarr2],
                    [self.ratonde1,self.ratonde2],[self.ratoniz1,self.ratoniz2]]
        self.imagen_actual = 0
        self.imagen = self.anima[self.imagen_actual][0]
        self.rect = self.imagen.get_rect()
        #self.rect.inflate_ip(-20,-20) mas pequeño el cuadrado o mas grande
        self.rect.top,self.rect.left=200,300
        
        self.dir = 0
        
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self,superficie,vx,vy,tiempo):
        if vy > 0:
            self.dir = 0
        else:
            if vy < 0:
                self.dir = 1
            else:
                if vx > 0:
                    self.dir = 2
                else:
                    if vx < 0:
                        self.dir = 3
        if tiempo == 1:
            self.imagen_actual +=1
        if self.imagen_actual+1 >= len(self.anima)-1:
            self.imagen_actual = 0
        vx,vy = 0,0
        self.mover(vx, vy)
        self.imagen = self.anima[self.dir][self.imagen_actual]
        superficie.blit(self.imagen,self.rect)
class Cuadrados(pygame.sprite.Sprite):
    def __init__(self):
        self.arbol= pygame.image.load("arbol.png").convert_alpha()
        self.lista=[]
        self.listarr=[]
        self.listab=[]
        self.listde=[]
        self.pared = pygame.Rect(-50,0,50,2000)
        self.pared2 = pygame.Rect(-50,-50,2240,50)
        self.pared3 = pygame.Rect(0,1894,2240,50)
        self.pared4 = pygame.Rect(2140,-50,50,2000)
        self.consola = pygame.image.load("consola.png")
        self.recta = self.consola.get_rect()
        self.recta.left,self.recta.top = 700,0
        #self.consola = pygame.Rect(700,0,400,650)
        self.rect = self.arbol.get_rect()
        self.rect.left,self.rect.top = -45,0
        for i in range(39):         
            left=self.rect.left
            top = self.rect.top
            self.rect.left += 0
            self.rect.top+= 50
            self.lista.append(pygame.Rect(left,top,self.rect.width,self.rect.height))
        self.rect.left,self.rect.top = 0,-45
        for i in range(44):
            
            leftt=self.rect.left
            topp = self.rect.top
            self.rect.left += 50
            self.rect.top+= 0
            self.listarr.append(pygame.Rect(leftt,topp,self.rect.width,self.rect.height))
        
        self.rect.left,self.rect.top = 0,1900
        for i in range(44):
            
            leftt=self.rect.left
            topp = self.rect.top
            self.rect.left += 50
            self.rect.top+= 0
            self.listab.append(pygame.Rect(leftt,topp,self.rect.width,self.rect.height))
            
        self.rect.left,self.rect.top = 2180,0
        for i in range(39):
            
            leftt=self.rect.left
            topp = self.rect.top
            self.rect.left += 0
            self.rect.top+= 50
            self.listde.append(pygame.Rect(leftt,topp,self.rect.width,self.rect.height))
    def mover(self,vy,vx):
        self.pared.move_ip(-vx,-vy)
        self.pared2.move_ip(-vx,-vy)
        self.pared3.move_ip(-vx,-vy)
        self.pared4.move_ip(-vx,-vy)
        for rectangulo in self.lista:
            rectangulo.move_ip(-vx,-vy)
        for rectangulo in self.listarr:
            rectangulo.move_ip(-vx,-vy)
        for rectangulo in self.listab:
            rectangulo.move_ip(-vx,-vy)
        for rectangulo in self.listde:
            rectangulo.move_ip(-vx,-vy)
    def draw (self,screen):
        for rectangulo in self.lista:
            screen.blit(self.arbol,rectangulo)        
        for rectangulo in self.listarr:
            screen.blit(self.arbol,rectangulo)
        for rectangulo in self.listab:
            screen.blit(self.arbol,rectangulo)
        for rectangulo in self.listde:
            screen.blit(self.arbol,rectangulo)
        screen.blit(self.consola,self.recta)
class ParedLaberinto(pygame.sprite.Sprite):
    def __init__(self):
        self.arbolito = pygame.image.load("arbolesV.png").convert_alpha()
        self.imagen = self.arbolito
        self.rect = self.imagen.get_rect()
        self.rect.left,self.rect.top = 200,0
        self.rect2 = self.imagen.get_rect()
        self.rect2.left,self.rect2.top = 1000,0
        self.rect3 = self.imagen.get_rect()
        self.rect3.left,self.rect3.top = 1900,0
        self.rect4 = self.imagen.get_rect()
        self.rect4.left,self.rect4.top = 500,650
        self.rect5 = self.imagen.get_rect()
        self.rect5.left,self.rect5.top = 1350,650
        self.rect6 = self.imagen.get_rect()
        self.rect6.left,self.rect6.top = 200,1320
        self.rect7 = self.imagen.get_rect()
        self.rect7.left,self.rect7.top = 1000,1320        
        self.rect8 = self.imagen.get_rect()
        self.rect8.left,self.rect8.top = 1900,1320
        self.arbolitoh = pygame.image.load("arbolesH.png").convert_alpha()
        self.imagen2 = self.arbolitoh
        self.rect9 = self.imagen2.get_rect()
        self.rect9.left,self.rect9.top = 280,420
        self.rect10 = self.imagen2.get_rect()
        self.rect10.left,self.rect10.top = 770,210
        self.rect11 = self.imagen2.get_rect()
        self.rect11.left,self.rect11.top = 1080,420
        self.rect12 = self.imagen2.get_rect()
        self.rect12.left,self.rect12.top = 1700,210
        self.rect13 = self.imagen2.get_rect()
        self.rect13.left,self.rect13.top = 270,900
        self.rect14 = self.imagen2.get_rect()
        self.rect14.left,self.rect14.top = 575,905
        self.rect15 = self.imagen2.get_rect()
        self.rect15.left,self.rect15.top = 1115,900
        self.rect16 = self.imagen2.get_rect()
        self.rect16.left,self.rect16.top = 1420,905
        self.rect17 = self.imagen2.get_rect()
        self.rect17.left,self.rect17.top = 270,1700
        self.rect18 = self.imagen2.get_rect()
        self.rect18.left,self.rect18.top = 770,1490
        self.rect19 = self.imagen2.get_rect()
        self.rect19.left,self.rect19.top = 1080,1700
        self.rect20 = self.imagen2.get_rect()
        self.rect20.left,self.rect20.top = 1700,1490
        self.lista = [self.rect,self.rect2,self.rect3,self.rect4,self.rect5,
                      self.rect6,self.rect7,self.rect8]
        self.listaH=[self.rect9,self.rect10,self.rect11,self.rect12,self.rect13,
                     self.rect14,self.rect15,self.rect16,self.rect17,self.rect18,
                     self.rect19,self.rect20]
    def mover(self,vx,vy):
        for arbol in range(len(self.lista)):
            self.lista[arbol].move_ip(-vx,-vy)
        for arbol in range(len(self.listaH)):
            self.listaH[arbol].move_ip(-vx,-vy)
    def actualizar(self,screen):
        for arbol in range(len(self.lista)):
            screen.blit(self.imagen,self.lista[arbol])
        for arbol in range(len(self.listaH)):
            screen.blit(self.imagen2,self.listaH[arbol])
def main():
    pygame.init()
    
    #creamos la pantalla y el tamaño
    
    screen=pygame.display.set_mode((1100,650))
    
    #sirve para senalar el nombre que va a aparecer en la pantalla
    
    pygame.display.set_caption('Proyecto Raton')
    fuente = pygame.font.Font("fuentes/m04.TTF",18)
    temp=0
    
    #numqueso = fuente.render("Numero de quesos"+str(temp),0,(250,250,250)) 
    salir=False
    reloj=pygame.time.Clock()
    meta = pygame.image.load("ratonmeta.png")
    player1 = Player()
    puntos = Queso()
    fondo = Fondo()
    rects = Cuadrados()
    laberint = ParedLaberinto()
    vx=0
    vy=0
    velocidad= 12
    tiempo= 0
    while salir!=True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            while True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vx = velocidad 
                        vy = 0
                    if event.key == pygame.K_LEFT:
                        vx = -velocidad
                        vy = 0
                    if event.key == pygame.K_DOWN:
                        vy = velocidad 
                        vx = 0
                    if event.key == pygame.K_UP:
                        vy = -velocidad 
                        vx = 0
                break 
        numqueso = fuente.render("Numero de quesos "+str(temp),0,(250,250,250))    
        gameOver = fuente.render("GAME OVER!!",0,(250,250,250))
        ganaste= fuente.render("Felicitaciones, Has Ganado",0,(250,250,250))
        consigue = fuente.render("20 quesos para ganar",0,(250,250,250))
        x=pygame.time.get_ticks()/1000
        y= 60
        z = y-x
        
        time = fuente.render("Hay 60 segundos "+str(z),0,(250,250,250))
        
        reloj.tick(30)        
        tiempo = tiempo + 1
        if tiempo > 1:
            tiempo = 0   
        screen.fill((0,0,0))
        rects.mover(vy, vx)
        fondo.actualizar(screen,vx,vy)
        puntos.actualizar(screen,vx,vy)
        player1.update(screen,vx,vy,tiempo)
        
        if player1.rect.colliderect(puntos):
            puntos.rect.move_ip(random.randint(-300,300),random.randint(-300,300))
            if rects.pared.left+10 >= puntos.rect.left:
                puntos.rect.move_ip(500,0)
            if rects.pared2.top-10 >= puntos.rect.top:
                puntos.rect.move_ip(0,500)
            if  rects.pared3.top+10 <= puntos.rect.top:
                puntos.rect.move_ip(0,-500)
            if  rects.pared4.left-10 <= puntos.rect.left:
                puntos.rect.move_ip(-500,0)
            temp = temp + 1
            
        for cont in range(len(laberint.lista)):
            if laberint.lista[cont].colliderect(puntos.rect):
                puntos.rect.move_ip(20,20)
                
        for cont in range(len(laberint.listaH)):
            if laberint.listaH[cont].colliderect(puntos.rect):
                puntos.rect.move_ip(20,20)
        laberint.mover(vx,vy)    
        if (player1.rect.colliderect(rects.pared)or 
            player1.rect.colliderect(rects.pared2) or 
            player1.rect.colliderect(rects.pared3) or 
            player1.rect.colliderect(rects.pared4)):
            vx,vy = -vx,-vy        
        
        
        for col in range(len(laberint.lista)):    
            if laberint.lista[col].colliderect(player1.rect):
                vx,vy = -vx,-vy 
        for col in range(len(laberint.listaH)):    
            if laberint.listaH[col].colliderect(player1.rect):
                vx,vy = -vx,-vy 
        
        laberint.actualizar(screen)
        if temp ==20:
            vx,vy=0,0
            screen.blit(ganaste,(150,300))
            pygame.time.delay(3000)
            salir=True
        if z == 0:
            screen.blit(gameOver,(300,300))
            screen.blit(meta,(320,320))
        if z < 0:
            z=0
            vx,vy = 0,0
            screen.blit(gameOver,(300,300))
            pygame.time.delay(3000)
            salir = True
        rects.draw(screen)
        screen.blit(time,(728,50))
        screen.blit(numqueso,(728,30))
        screen.blit(consigue,(728,70))
        pygame.display.update()
        
    pygame.quit()
    
main()