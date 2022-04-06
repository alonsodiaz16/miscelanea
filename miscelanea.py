
import math
import os
import time

import operadores
import condicionales
import ciclos



print("-----" * 10, "\n")
print("               -- Welcome --", "\n")
print( "-----" * 10)
time.sleep(0.5)
print("  Escoge alguna de las areas segun el \n  numero que corresponda (0, 1, 2, etc...) \n")
print("           ¡Ingresa solo numeros!")
print( "-----" * 10 , "\n")

# Menu de area
print("   MENU: \n")
print("    1. Operaciones \n    2. Condicionales \n    3. Ciclos \n    0. Salir \n");

opcion = int(input('--> '))



# Reinicio de sistema
def reiniciar():
    print("  Reinicio")
    time.sleep(2)
    os.system("python main.py")

# Salir del sistema
def salirWe():
    print( "Adios")
    exit()


# Operadores
def operaciones():
    print("-----" * 10)
    print( "             -Operador-")
    print( "-----" * 10, "\n")
    print( "   MENU: \n")
    print("    1. Area de Triangulo \n    2. Sumar dos numeros \n    3. Elevar un numero al cuadrado \n    4. Euros a dolares \n    5. Area y perimetro de un cuadrado \n    6. Area y volumen de un cilindro \n    7. Longitud y area de una circunferencia \n    8. Promedio de tres numeros \n \n    9. Reiniciar \n    0. Salir \n");

    opcion = int(input( '--> '))

    if( opcion == 0 ):
        salirWe()
    elif( opcion == 9 ):
        reiniciar()
    elif( opcion == 1 ):
        print( "-----" * 10)
        print( "  Area de un Triangulo \n")
        base = int(input( "    Base del triangulo en cm: "))
        altura = int(input("    Altura del triangulo en cm: "))
        print( "\n    El area del triangulo es:", operadores.areadelTri(base, altura), "\n")

    elif( opcion == 2 ):
        print("-----" * 10)
        print( "  Sume dos numeros \n")
        num1 = int(input( "    Ingresa el primer valor: "))
        num2 = int(input("    Ingresa el segundo valor: "))
        print( "\n    El resultado es:", operadores.suma(num1, num2), "\n")
    
    elif( opcion == 3 ):
        print("-----" * 10)
        print( "  Eleva un numero al cuadrado \n")
        num = int(input( "    Ingresa el valor: "))
        print( f"\n    {num} elevado, es {operadores.elevado(num)} \n")

    elif( opcion == 4 ):
        print( "-----" * 10)
        print( " Conversion de euros a US \n  ( 0.90 EUR --> 1 USD ) \n")
        num = int(input("    Cuantos Euros tienes?: "))
        print( f"\n    {num} EUR son {operadores.conversiones(num)} USD \n")

    elif( opcion == 5 ):
        print("-----" * 10)
        print("  Calcula el Area y Perimetro \n  de un cuadrado \n")
        num = int(input("    Cuanto mide cada lado en(cm): "))
        print( f"\n    Lados de: {num} cm \n    Area: {operadores.area(num)} cm² \n    Perimetro: {operadores.perimetro(num)} cm \n")

    elif( opcion == 6 ):
        print( "-----" * 10)
        print( "  Calcula el Area y Volumen \n  de un cilindro \n")
        base = float(input("    Escribe el diametro de la base del cilindro?(cm): "))
        altura = float(input("    Cual es la altura del cilindro?(cm): "))
        areaCil = operadores.areaCir(base, altura)
        volCil = operadores.volCil(base, altura)

        print( f"\n    Area Total: {round(areaCil, 2)} cm² \n    Volumen Total: {round(volCil, 2)} cm² \n")

    elif( opcion == 7 ):
        print( "-----" * 10)
        print( "  Calcula la longitud y area \n  de una circunferencia \n")
        num = int(input("    Cuanto mide el radio(cm): "))
        print( f"\n    Radio: {num} cm \n    Longitud: {num * 2} cm \n    Area: {operadores.areaCir(num)} cm² \n")

    elif( opcion == 8 ):
        print("-----" * 10)
        print("  Calcula el promedio de tres numeros \n")
        num1 = float(input("    Ingrese el primer numero: "))
        num2 = float(input( "    Ingrse el segundo numero: "))
        num3 = float(input( "    Ingrese el tercer numero: "))
        ans = operadores.promedio(num1, num2, num3)

        print(f"\n    El promedio de {round(num1, 2)}, {round(num2, 2)}, {round(num3, 2)} --> {round(ans, 2)} \n")

# Condicionales
def condiciones():
    print( "-----" * 10)
    print( "             -Condicionales-")
    print("-----" * 10, "\n")
    print( "   MENU: \n")
    print("    1. Tu numero es positivo o negativo? \n    2. Calcular cual numero es mayor \n    3. Cual de los numero es mayor y menor \n    4. A es menor que B o sino restarlos \n    5. Cociente de dos numeros \n    6. Dos numeros, segun su valor sumar o multiplicar \n    7. Determinar si un año es bisiesto o no \n \n    8. Reiniciar \n    0. Salir \n");

    opcion = int(input( '--> '))

    if( opcion == 0 ):
        salirWe()
    elif( opcion == 8 ):
        reiniciar()
    elif( opcion == 1 ):
        print( "-----" * 10)
        print( "  Numero positivo o negativo \n")
        num = int(input("    Ingrese un numero: "))

        condicionales.posiNega(num)
        


# Menu de inicio
def inicio():
    if( opcion == 0 ):
        salirWe()
    elif( opcion == 1 ):
        operaciones()
    elif( opcion == 2 ):
        condiciones()
    elif( opcion == 3 ):
        print("3")
    else:
        print( " ¡Escoge un numero valido!")
        exit()


# Flujo
inicio()


# Condicionales

# Ciclos

