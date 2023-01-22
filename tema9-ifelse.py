num1=int(input("Dame primer numero"))
num2=int(input("Dame segundo numero"))

if(num1 > num2):
    print("{} es mayor que {}".format(num1,num2))
else:
    print("{1} es mayor que {0}".format(num1,num2))

print("------------Dato Nuevo----------------")

edad = int(input("Dame tu edad"))

if edad > 18:
    print("eres mayor de edad")
elif edad == 18:
    print("tienes 18 años")
else:
    print("eres menor de edad")