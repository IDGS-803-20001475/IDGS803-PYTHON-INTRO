
def suma(x,y):
    print("{} + {} = {}".format(x,y,(x+y)))

def resta(x,y):
    print("{} - {} = {}".format(x,y,(x-y)))

def multiplicacion(x,y):
    print("{} * {} = {}".format(x,y,(x*y)))

def division(x,y):
    print("{} / {} = {}".format(x,y,(x/y)))

def opciones():
    print("1. Sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")
    opcion = int(input("Selecciona una opcion"))
    main(opcion) 


def main(opcion):
    x = float(input("Introduce el primer numero"))
    y = float(input("Introduce el segundo numero"))
    if(opcion == 5):
        print("Cerrando programa")
        
    if(opcion == 1):
        suma(x,y)
        opciones()
    elif(opcion == 2):
        resta(x,y)
        opciones()
    elif(opcion == 3):
        multiplicacion(x,y)
        opciones()
    elif(opcion == 4):
        division(x,y)
        opciones()


if __name__=="__main__":
    opciones()