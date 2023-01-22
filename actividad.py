num = int(input("Dame un numero a multiplicar"))
x= 0 

def multiplicacion(x):
    while x < 10:
        x = x + 1
        print("{} x {} = {}".format(num, x, (num * x)))

multiplicacion(x)