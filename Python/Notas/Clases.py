"""
POO 

class ClasePrueba:
    variable = "blah"

    def function (self): # self es un parametro que debe estar dentro de una funcion dentro de una clase, pero no es requerido
        print("esto es un mensaje dentro de una clase")
    pass # pasa, es para crear una funcion, ciclo o clase vacia

#metodo incorrecto
# ClasePrueba().function()

miobjetox = ClasePrueba() # instanciacion, crear una instancia de la clase en una valiable, lo que la convierte en un objeto

miobjetox.function()
print(miobjetox.variable)

#============================================ ejemplo ============================================#

class Perro:
    color = "Blanco" # las variables dentro de una clase se les llama atributo
    def ladrar(self, volumen = "ruidoso"): # las funcines dento de una clase se les llama metodos
        print(f"Este perro ladra: {volumen}")

p = Perro()
print(p.color)
p.tamaño = 37 # para crear un atributo dentro de un objeto es como nombrar una variale normal, pero antes el nombre del objeto y un punto
# pero este cambio solo es para el objeto, no para la clase
p2 = Perro()
print(p.tamaño)
try:
    print(p2.tamaño)
except:
    print("p2 no tiene tamaño asignado")
    
p2.color = "Café" # para cambiar el valor de un atributo es como cambiar el valor de una variable
print(p2.color)

p.ladrar()
p.ladrar("silencioso")
"""
#======================================= metodo iniciador ========================================#

class Sapo:
    croa = False
    def __init__(self): # init hace que se inicie sin llamar la clase y/o funcionw
        print("Se creó un sapo")

    def croar(self):
        self.croa = True # self se pone porque sin el, la variable es local de la funcion, no de la clase

sapo1 = Sapo() # para que se inicie la clase se debe nombrar un objeto
print(sapo1.croa)
sapo1.croar()
print(sapo1.croa)