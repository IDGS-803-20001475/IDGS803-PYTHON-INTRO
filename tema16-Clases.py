class padre():
    x = 1
    

class operasbas(padre):
    # definir propiedades de clase
    num1 = 0
    num2 = 0
    res = 0
    # definir constructor de la clase
    
    # definimos los metodos de la clase
    def suma(self, a, b):
        self.num1 = a
        self.num2 = b
        return a + b

    
obj = operasbas()
obj.suma(1,1)