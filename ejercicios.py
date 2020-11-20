#PRIMER EJERCICIO
print("Saber ganancia del capital que se invirtio")
capital = float(input("Ingrese cantidad a invertir : "))
ganancia = capital * 0.02
print(f"La ganancia de la inversion es {ganancia}")

#SEGUNDO EJERCICIO
print("Saber ganancia por comision y salario base")
salario_base = float(input("Ingrese salario base : "))
comision_venta1 = float(input("Ingrese la comision de la venta numero 1 : "))
comision_venta2 = float(input("Ingrese la comision de la venta numero 2 : "))
comision_venta3 = float(input("Ingrese la comision de la venta numero 3 : "))
total_venta = (comision_venta1 + comision_venta2) + comision_venta3
comision = total_venta * 0.10
total_pagar = salario_base + comision
print(f"El total a pagar es {total_pagar}")

#TERCER EJERCICIO
print("Saber total a pagar de una compra con descuento del 15%")
total_compra = float(input("Ingrese el total de la compra : "))
descuento = total_compra * 0.15
total_pagar_cliente = total_compra - descuento
print(f"El total a pagar es {total_pagar_cliente}")

#CUARTO EJERCICIO
print("Saber promedio de estudiante")
calificacion1 = float(input("Ingrese la primera calificacion : "))
calificacion2 = float(input("Ingrese la segunda calificacion : "))
calificacion3 = float(input("Ingrese la tercera calificacion : "))
examen_final = float(input("Ingrese la calificacion del examen final: "))
trabajo_final = float(input("Ingrese la calificacion del trabajo final: "))
promedio = (calificacion1 + calificacion2 + calificacion3) / 3
promedio_tres_Calificaciones = promedio * 0.55
promedio_examen_final = examen_final * 0.30
promedio_trabajo_final = trabajo_final * 0.15
calificacion_final = (promedio_tres_Calificaciones + promedio_examen_final) + promedio_trabajo_final
print(f"La calificacion final es {calificacion_final}")

#QUINTO EJERCICIO
print("Saber el porcentaje de hombre y mujeres en un grupo")
numerohombres = float(input("Ingrese la cantidad de hombres en el grupo de estudiantes : "))
numeromujeres = float(input("Ingrese la cantidad de mujeres en el grupo de estudiantes : "))
total_alumnos = numerohombres + numeromujeres
porcentaje_hombres = (numerohombres * 100) / total_alumnos
porcentaje_mujeres = (numeromujeres * 100) / total_alumnos
print(f"El porcentaje de hombres es del {porcentaje_hombres} ,y el porcentaje de mujeres es del {porcentaje_mujeres}")

#SEXTO EJERCICIO
print("Saber edad")
fecha_nacimiento = float(input("Ingrese el año en el cual fue su nacimiento : "))
fecha_actual = float(input("Ingrese el año actual : "))
edad = fecha_actual - fecha_nacimiento
print(f"La edad es {edad}")

#PROBLEMAS PROPUESTOS

#       EJERCICIO UNO
print("Conversion de pesos a dolares")
cantidad_pesos = float(input("Ingrese la cantidad de pesos : "))
valor_dolar = float(input("Ingrese el valor del dolar : "))
total_en_dolares = cantidad_pesos * valor_dolar
print(f"El total en dolares es {total_en_dolares}")

#       EJERCICIO DOS
print("Convertir a numero absoluto")
numero = float(input("Ingrese un numero negativo : "))
print(f"El valor absoluto es {abs(numero)}")

#       EJERCICIO TRES
print("Saber masa")
presion = float(input("Ingrese la presion : "))
volumen = float(input("Ingrese el volumen : "))
temperatura = float(input("Ingrese la temperatura : "))
masa = (presion * volumen) / (0.37 *(temperatura + 460))
print(f"La masa es : {masa}")

#       EJERCICIO CUATRO
print("Calcular numero de pulsaciones por cada 10 segundos")
edad = float(input("Ingrese la edad : "))
numero_de_pulsaciones = (220 - edad) / 10
print(f"El numero de pulsaciones debe de ser de : {numero_de_pulsaciones}")

#       EJERCICIO QUINTO
print("Saber salario actual con el incremento que se realizo del 25%")
salario_anterior = float(input("Ingrese el total del salario sin incremento : "))
incremento = salario_anterior * 0.25
salarario_actual = incremento + salario_anterior
print(f"El salario actual es de : {salarario_actual}, y el incremento fue de un total de {incremento}")

#       EJERCICIO SEXTO
print("Presupuesto anual")
cantidad_dinero_p = float(input("Ingrese el total del presupuesto anual : "))
area_ginecologia = cantidad_dinero_p * 0.40
area_traumatologia = cantidad_dinero_p * 0.30
area_pediatria = cantidada_dinero_p * 0.30
print(f"El presupuesto para el area de ginecologia es de : {area_ginecologia}, el presupuesto para el area de traumatologia es de {area_traumatologia}, y la cantidad de dinero para el area de pediatria es de {area_pediatria}")

#       EJERCICIO SEPTIMO
print("Cantidad de la ganancia por compra de articulos")
valor_articulo = float(input("Ingrese el valor del articulo : "))
ganancia = valor_articulo * 0.30
valor_venta = valor_articulo + ganancia
print(f"El valor en el cual debe ganar el articulo para obtener una ganancia del 30% es : {valor_venta}")

#       EJERCICIO OCTAVO
print("Promedio ruta")
ruta_lunes = float(input("Ingrese el tiempo obtenido de la ruta del dia lunes : "))
ruta_miercoles = float(input("Ingrese el tiempo obtenido de la ruta del dia miercoles: "))
ruta_viernes = float(input("Ingrese el tiempo obtenido de la ruta del dia viernes: "))
suma_tiempo = (ruta_lunes + ruta_miercoles) + ruta_viernes
promedio = suma_tiempo / 3
print(f"El tiempo promedio es de : {promedio}")

#       EJERCICIO NOVENO
print("Porcentaje de inversion entre tres personas")
inversion1 = float(input("Ingrese la cantidad de dinero a invertir de la primera persona : "))
inversion2 = float(input("Ingrese la cantidad de dinero a invertir de la segunda persona : "))
inversion3 = float(input("Ingrese la cantidad de dinero a invertir de la tercera persona : "))
suma_inversiones = (inversion1 + inversion2) + inversion3
porcentaje_invesion_1 = (inversion1 * 100) / suma_inversiones
porcentaje_invesion_2 = (inversion2 * 100) / suma_inversiones
porcentaje_invesion_3 = (inversion3 * 100) / suma_inversiones
print(f"El total de la inversion de la primera persona es de : {porcentaje_invesion_1}, el total de inversion de la segunda persona es : {porcentaje_invesion_2}, y el total de inversion de la tercera persona es de :  {porcentaje_invesion_3}")

#       EJERCICIO DECIMO
print("Promedio alumno - materias")
examen_matematicas = float(input("Ingrese nota del examen de matematicas : "))
tarea1_matematicas = float(input("Ingrese nota de la primera tarea de matematicas : "))
tarea2_matematicas = float(input("Ingrese nota de la segunda tarea de matematicas : "))
tarea3_matematicas = float(input("Ingrese nota de la tercera tarea de matematicas : "))

examen_fisica = float(input("Ingrese nota del examen de física : "))
tarea1_fisica = float(input("Ingrese nota de la primera tarea de física : "))
tarea2_fisica = float(input("Ingrese nota de la segunda tarea de física : "))

examen_quimica = float(input("Ingrese nota del examen de química : "))
tarea1_quimica = float(input("Ingrese nota de la primera tarea de química : "))
tarea2_quimica = float(input("Ingrese nota de la segunda tarea de química : "))
tarea3_quimica = float(input("Ingrese nota de la tercera tarea de química : "))

promedio_examen_m = examen_matematicas * 0.90
promedio_tareas_m = ((tarea1_matematicas + tarea2_matematicas + tarea3_matematicas) / 3) * 0.10
promedio_final_m = promedio_examen_m + promedio_tareas_m

promedio_examen_f = examen_fisica * 0.80
promedio_tareas_f = ((tarea1_fisica + tarea2_fisica) / 2) * 0.20
promedio_final_f = promedio_examen_f + promedio_tareas_f

promedio_examen_q = examen_quimica * 0.85
promedio_tareas_q = ((tarea1_quimica + tarea2_quimica + tarea3_quimica) / 3) * 0.15
promedio_final_q = promedio_examen_q + promedio_tareas_q
promedio_final = (promedio_final_m + promedio_final_f + promedio_final_q) / 3

print(f"El  promedio de matematicas es de : {promedio_final_m}, el promedio final de física es de : {promedio_final_f} y el promedio final de quimica es de {promedio_final_q}, el promedio de las tres materias es de {promedio_final}")