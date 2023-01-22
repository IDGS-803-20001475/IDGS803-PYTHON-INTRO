dato1="Hola"
dato2="Mundo"

datoFinal = dato1 + " " + dato2
print(datoFinal)

print("El saludo es: %s %s" % (dato1,dato2) )

saludo = "Saludo2 {0} {1}".format(dato1,dato2)
print(saludo)


saludo = "Saludo2 {1} {0}".format(dato1,dato2)
print(saludo)


saludo = "Saludo2 {a} {b}".format(a=dato1,b=dato2)
print(saludo)