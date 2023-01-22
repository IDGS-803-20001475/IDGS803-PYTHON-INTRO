texto = "universidad tecnologica de leon"

print(type(texto))
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.find("de"))
print(texto.count("a"))

texto2 = texto.replace("e","3")
print(texto2)

texto3 = texto.split(" ")
print(texto3)