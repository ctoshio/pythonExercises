# Validar numeros negativos
class numeroNegativo(Exception):
    pass

# Validar notas mayores a 20
class mayora20(Exception):
    pass

sumaNota = 0
while True:
    try:
        nombreEstudiante = input("Hola pon tu nombre : ")
        if (not nombreEstudiante.isalpha()):
            raise ValueError("Poner un nombre correcto!")
    except ValueError as ve:
        print(ve)
    else:
        break

for i in range(4):
    while True:
        try:         
            nota= float(input("Hola {} pon tu nota {} : ".format(nombreEstudiante,i+1)))
            if (nota< 0):
                raise numeroNegativo
            if (nota > 20):
                raise mayora20
            sumaNota +=nota
        except ValueError:
                print("Ingrese un numero valido")            
        except numeroNegativo:
                print("NO negativos!!!!")
        except mayora20:
                print("Ingrese un numero menor a 20")
        else:
            break

print("Tu promedio {} es {}".format(nombreEstudiante, sumaNota/4))
""""
while True:
    for i in range(4):
        try:
            notita= float(input("Hola {} pon tu nota {} : ".format(nombreEstudiante,i+1)))
            if (notita < 0):
                raise numeroNegativo
        except numeroNegativo:
            print("NO negativos!!!!")
    i=i-1

    break"""
    
print("Tu promedio {} es {}".format(nombreEstudiante, sumaNota/4))
    








    


        





