# raton

def raton ():
    posicionx = 30 #posicion en x del raton malo
    posiciony = 30 #posicion en y del raton malo

    eje = 0 #si me muevo en el eje x(0) o eje y(1)
    
    yox = 0 #posicion inicial en x del jugador
    yoy = 0 #posicion inicial en y del jugador
    
    while posicionx != yox and posiciony != yoy:
        movx = input ("se mueve en el eje x: ") #lo que se hace con las teclas
        movy = input ("se mueve en el eje y: ")
        yox = yox + movx #para saber la posicion del usuario y el malo se mueva
        yoy = yoy + movy
        if eje == 0:
            if yox < posicionx: #moviemiento hacia la izq del malo
                posicionx = posicionx - 10
            if yox > posicionx: #movimiento hacia la der del malo
                posicionx = posicionx + 10
            if yox == posicionx: #ahora se va a mover en el eje y
                eje = 1
        if eje == 1:
            if yoy < posiciony: #movimiento hacia arriba del malo
                posiciony = posiciony - 10
            if yoy > posiciony: #movimiento hacia abajo del malo
                posiciony = posiciony + 10
            if yoy == posiciony: #cambia el eje y para moverse en el eje x
                eje = 0

        print ("mi posicion en x= " +str(yox) +" y en y= " +str(yoy))
        print ("la posicion del malo en x= " +str(posicionx) +" en y= " +str(posiciony))
