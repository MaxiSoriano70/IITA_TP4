# 1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
# ingresado por parámetro.

# def numeros(numero):
#     for i in range(1,numero+1):
#         print(i, end=" - ")

# numeros(int(input("Ingrese un numero positivo:\n")))

# 2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
# que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
# avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
# programa de acuerdo a estos criterios:
# • Use un test condicional en el ciclo while para detener la ejecución.
# • Use un test condicional dentro del ciclo para decidir si continuar la ejecución.

# def agregar_condimentos(listaCondimentos):
#     while True:
#         condimento=input("Ingrese un condimento o si desea escriba salir. \n").lower()
#         if(condimento=="salir"):
#             return listaCondimentos
#         print(f"A su sandwich se le agrego el condimento {condimento}")
#         listaCondimentos.append(condimento)

# def condimentos():
#     condimentos_agregados=[]
#     agregar_condimentos(condimentos_agregados)
#     print(condimentos_agregados)

# condimentos()

# 3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
# tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
# describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
# usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.

# def hacer_remera(tamano,mensaje):
#     print(f"El tamaño de la es {tamano} y el mensaje que va a llevar es {mensaje}")

# hacer_remera(tamano="M",mensaje="Divididos 35 años")

# B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
# defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
# valores por defecto, y la segunda con valores diferentes.

# def hacer_remera(tamano="L",mensaje="Me gusta Python"):
#     print(f"El tamaño de la es {tamano} y el mensaje que va a llevar es {mensaje}")

# hacer_remera()

# 4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
# de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
# número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …).

# def fibonacci(n):
#     numeros_fibonacci=[0,1]
#     posicion=1
#     while len(numeros_fibonacci)<n:
#         nuevoNumero=numeros_fibonacci[posicion-1]+numeros_fibonacci[posicion]
#         numeros_fibonacci.append(nuevoNumero)
#         posicion+=1
#     print(numeros_fibonacci)

# fibonacci(10)

# 5) (Opcional) Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que
# la calculadora sea capaz de devolver el resultado solamente de una operación especificada por
# el usuario. Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la
# calculadora devuelve la suma entre los numeros x,y; si ingresa ‘2’, devuelve la resta, etc.

# def calculadora_inteligente(numero1:int,numero2:int,operacion:int):
#     if operacion==1:
#         aux=numero1+numero2
#         print(f"{numero1} + {numero2} = {aux}")
#     elif operacion==2:
#         aux=numero1-numero2
#         print(f"{numero1} - {numero2} = {aux}")
#     elif operacion==3:
#         aux=numero1*numero2
#         print(f"{numero1} x {numero2} = {aux}")
#     elif operacion==4:
#         aux=numero1/numero2
#         print(f"{numero1} / {numero2} = {aux}")
#     else:
#         print("La operación no es valida.")
#         enviar_numero()

# def enviar_numero():
#     n1=int(input("Ingrese el 1er numero:\n"))
#     n2=int(input("Ingrese el 2do numero:\n"))
#     operacion=int(input("Seleccione la operación a realizar:\n1. Suma.\n2. Resta.\n3. Multiplicación.\n4. División.\n"))
#     calculadora_inteligente(n1,n2,operacion)

# enviar_numero()

# 6) (Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir
# gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la
# conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462
# libras = 1 gramo

# def gramos_libras():
#     print("Convetir Gramos <-> Libras")
#     unidad=float(input("Ingrese cantidad a convetir:\n"))
#     medida=int(input("Selecione la conversion.\n1. Gramos -> Libras.\n2. Libras -> Gramos.\n"))
#     if(medida==1):
#         libras=unidad/453.5920865
#         print(f"{unidad} Gramos -> Libras {libras}")
#     elif(medida==2):
#         gramos=unidad/0.0022046
#         print(f"{unidad} Libras -> Gramos{gramos}")
#     else:
#         print("La opcion no es valida.")
#         gramos_libras()

# def centimetros_pulgadas():
#     print("Convetir Centimetros <-> Pulgadas")
#     unidad=float(input("Ingrese cantidad a convetir:\n"))
#     medida=int(input("Selecione la conversion.\n1. Centimetros -> Pulgadas.\n2. Pulgadas -> Centimetros.\n"))
#     if(medida==1):
#         pulgadas=unidad/2.538709
#         print(f"{unidad} Centimetros -> Pulgadas {pulgadas}")
#     elif(medida==2):
#         centimetros=unidad/0.3937008
#         print(f"{unidad} Pulgadas -> Centimetros {centimetros}")
#     else:
#         print("La opcion no es valida.")
#         centimetros_pulgadas()

# def kilometros_millas():
#     print("Convetir Kilometros <-> Millas")
#     unidad=float(input("Ingrese cantidad a convetir:\n"))
#     medida=int(input("Selecione la conversion.\n1. Kilometros -> Millas.\n2. Millas -> Kilometros.\n"))
#     if(medida==1):
#         millas=unidad/1.609344
#         print(f"{unidad} Kilometros -> Millas {millas}")
#     elif(medida==2):
#         kilometros=unidad/0.3937008
#         print(f"{unidad} Millas -> Kilometros {kilometros}")
#     else:
#         print("La opcion no es valida.")
#         kilometros_millas()

# def convertir_imperial():
#     desicion=int(input("Ingrese la medida a convertir.\n1. Gramos <-> Libras.\n2. Centimetros <-> Pulgadas.\n3. Kilometros <-> Millas.\n"))
#     if(desicion==1):
#         gramos_libras()
#     elif (desicion==2):
#         centimetros_pulgadas()
#     elif (desicion==3):
#         kilometros_millas()
#     else:
#         convertir_imperial()

# convertir_imperial()


# 7) (Opcional) Cuando un año es bisiesto, el mes más corto del año, febrero, tiene 29 días en
# vez de 28. Esto sucede casi cada 4 años. Los tres criterios que permiten saber si un año es
# bisiesto en el calendario gregoriano (el nuestro) son los siguientes:
# • Si el año es divisible enteramente por 4, es bisiesto a menos que: o El año sea divisible por
# 100, entonces NO es bisiesto, a menos que:
# ▪ El año sea también divisible por 400. Entonces sí es un año bisiesto. Esto significa que
# en el calendario gregoriano los años 2000 y 2400 son bisiestos, mientras que los años 1900,
# 2100, 2200 y 2300 no son bisiestos.
# a) Escriba una función que tome un año y diga si es bisiesto o no.
# b) Modifique su programa para que devuelva todos los años bisiestos entre el año
# actual y el año pasado a la función como parámetro (este debe ser posterior al año actual).

# def es_bisiesto(year:int):
#     if((year % 4)==0 and (year % 100)!=0) or (year % 400)==0:
#         return True
#     else:
#         return False

# def years_bisiestos(year:int):
#     for year in range(year,2024):
#         if es_bisiesto(year):
#             print(year, end=" - ")

# years_bisiestos(1996)

# 8) (Opcional) Si listamos todos los números naturales menores a 10 que son múltiplos de 3 o 5,
# obtenemos 3,5,6 y 9. La suma de estos múltiplos es 23. Encuentre la suma de todos los
# múltiplos de 3 o 5 menores a 1000.

def lista_multiplos():
    for numero in range(1,1000):
        if(numero % 3)==0 or (numero % 5)==0:
            print(numero, end=" - ")

lista_multiplos()