lista = [1,2,3,4,"hola",2,2]
conjunto = set(lista)
lista= list(conjunto)
print(conjunto)

#EJERCICIO CLASE
arreglo1 = [1,2,3,4,5,6,7,78,45,24]
conjunto1 = set (arreglo1)
print("primero arreglo", conjunto1)

arreglo2 = [0,2,3,4,5,1,7,8,10,23]
conjunto2 = set (arreglo2)
print("segundo arreglo", conjunto2)

print("arreglos combinados", arreglo1, arreglo2)

class Persona(object):
  nombre = "Jhon Felipe"
  apellido = "Medina Zapata"
  genero = ""

def mostrar_nombres(self):
  print(self.nombre)

class vehiculo:
  largochasis=250
  anchochasis=120
  ruedas=4
  encamino=False
  def funcion(self):
    pass
auto=vehiculo()
print("El largo de vehiculo es:",auto.largochasis)
print("El vehiculo tiene de ruedas:",auto.ruedas)


class vehiculo:
  largochasis=250
  anchochasis=120
  ruedas=4
  encamino=False
  def funcion(self):
    pass
  auto=vehiculo()
print("El largo de vehiculo es:",auto.largochasis)
print("El vehiculo tiene de ruedas:",auto.ruedas)


class vehiculo:
    largochasis=250
    anchochasis=120
    ruedas=4
    encamino=False
    def funcion(self):
      self.encamino=True
    def estado(self):
      if (self.encamino):
        return"El carro esta en marcha"
      else:
        return "El carro esta estático"
auto=vehiculo()
print("El largo de vehiculo es:",auto.largochasis)
print("El vehiculo tiene de ruedas:",auto.ruedas)
auto.funcion()
print(auto.estado())


class vehiculo:
  largochasis=250
  anchochasis=120
  ruedas=4
  encamino=False
  def funcion(self):
    self.encamino=True
  def estado(self):
    if (self.encamino):
      return"El carro esta en marcha"
    else:
      return "El carro esta estático"
auto=vehiculo()
print("El largo de vehiculo es:",auto.largochasis)
print("El vehiculo tiene de ruedas:",auto.ruedas)
auto.funcion()
print(auto.estado())
print("----------------------------------------------------------------------------------")
auto2=auto
print("El largo de vehiculo es:",auto2.largochasis)
print("El vehiculo tiene de ruedas:",auto2.ruedas,"ruedas")
print(auto2.estado())

# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
# Vídeo explicativo: http://youtu.be/JK5ht5_m6Mk
# Calcular las millas por galon
print("Este programa calcula mpg.")
# Obtener del usuario las millas recorridas
millas_recorridas = input("Introduce las millas recorridas: ")
# Convertimos el texto introducido a
# número en coma flotante (número real)
millas_recorridas = float(millas_recorridas)
# Obtener del usuario los galones consumidos
galones_usados = input("Introduce los galones usados: ")
# Convertimos el texto introducido a
# número en coma flotante (número real)
galones_usados = float(galones_usados)
# Calculamos e imprimimos la respuesta
mpg = millas_recorridas / galones_usados
print("Millas por galon:", mpg)

#EJERCICIO EN CLASE CONSTRUCTOR
class mascota:
  raza="pitbull"
  genero="hembra"
  edad=7
  personalidad="sociable"
  nombre="Milu"
  def funcion(self):
    pass
pet=mascota()
print("El nombre de la mascota es: ",pet.raza)
print("El nombre de la mascota es: ",pet.nombre)


#CLASES Y OBJETOS
class latinos():
  nombre= ""
  Genero = ""
  edad= " "
  pass
persona=latinos()
persona.nombre=str(input("Digite su nombre: "))
persona.Genero=str(input("Digite su genero: "))
persona.edad=int(input("Digite su edad: "))
print(f"Su nombre es: {persona.nombre},Su genero es:{persona.Genero},Su edad es:{persona.edad}")

#VENTANA

from tkinter import*
ventana=Tk()
ventana.geometry("600x500")
ventana.title("Aplicación")

Boton1 = Button(ventana, text="Inicio")
Boton1.grid(row=0,column=0)
Boton2 = Button(ventana, text="Archivos")
Boton2.grid(row=0,column=1)
ventana.mainloop()