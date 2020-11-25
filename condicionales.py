#EJERCICIOS CONDICIONALES

#1 EJERCICIO
porcentaje_intereses = float(input("Digite el valor del interes: "))
print()
capital = int(input("Digite el capital: "))
print()
intereses = capital * porcentaje_intereses
if intereses > 7000:
  capital_final = capital + intereses

print(f"El capital actual o final es de:  {capital_final}" )

#2 EJERCICIO
compra = int(input("Digite el total de la compra: "))
print()

if compra > 1000:
  descuento = compra * 0.20
else:
  descuento = 0

total_pagar = compra - descuento
print(f"El total a pagar es de {total_pagar}" )

#3 EJERCICIO
calificacion_1 = int(input("Digite la calificacion numero 1: "))
print()
calificacion_2 = int(input("Digite la calificacion numero 2: "))
print()
calificacion_3 = int(input("Digite la calificacion numero 3: "))
print()
promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

if promedio >= 70:
  print(f"El alumno esta aprobado con un promedio de: {promedio}" )
else:
  print(f"El alumno esta reprobado con un promedio de: {promedio}" )

#4 EJERCICIO
horas_trabajo = int(input("Digite la cantidad de horas laboradas: "))
print()

if horas_trabajo > 40:
  horas_extra = horas_trabajo - 40
  salario_semanal = (horas_extra * 20) + (40 * 16)
else:
  salario_semanal = horas_trabajo * 16

print(f"El total del salario semanal es de: {salario_semanal}" )

#5 EJERCICIO
numero_1 = int(input("Digite un numero: "))
print()
numero_2 = int(input("Digite otro numero: "))
print()

if numero_1 < numero_2:
  print(f"{numero_1},{numero_2}" )
else:
  print(f"{numero_2},{numero_1}" )