class HangarRangoInvalido(Exception):
    pass

espaciohLista = []
while True:
    try :
        hangar = int(input("Ingrese el numero de hangares: "))
        if not ((hangar > 0)&(hangar <= 10)):
            raise HangarRangoInvalido
        for i in range(hangar):
            espacioHangares = int(input("Ingrese el tamano del hangar {}: ".format(i+1)))
            espaciohLista.append(espacioHangares)
        break
    except HangarRangoInvalido:
        print("Rango invalido de numero de hangares")
    
print(espaciohLista)

lleno = False

def buscarMayorHangar():
    iMayor = 0

    for i in range(hangar):
        if (espaciohLista[iMayor] < espaciohLista[i]):
            iMayor = i
    return iMayor

print("el hangar con mayor tamno es ",buscarMayorHangar())

#espacionLista=[]
while True:
    try:
        nave = int(input("Ingrese la cantidad de naves: "))
        for i in range(nave):
            espacioNave = int(input("Ingrese el tamano de la nave {}: ".format(i+1)))
            #espacionLista.append(espacioNave)
            if not (lleno):
                mayorHangar = buscarMayorHangar()
                if (espacioNave <= espaciohLista[mayorHangar]):
                    espaciohLista[mayorHangar] = espaciohLista[mayorHangar] - espacioNave
                else:
                    lleno = True
        continue
    except ValueError:
        print("Introduzca un numero!")



