

def promedio():
    pro = 0
    
    salir = "s"
    while salir=="s":
        x = input("Digite la nota del primer parcial: ")
        y = input("Digite la nota del segundo parcial: ")
        z = input("Digite la nota del parcial final: ")
        pro = (x*0.30)+(y*0.30)+(z*0.40)
        print "su promedio es de :" + str(pro)
        salir = raw_input("Desea continuar calculando promedios? (s/n): ")
    
    
    return pro
    
    
promedio()

