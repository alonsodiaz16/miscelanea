# Condicionales
import math


# Calcular si es positivo o negativo
def posiNega(num):
    if( num > 0 ):
        print(f"\n    {num} es positivo \n")
    elif( num < 0 ):
        print( f"\n    {num} es negativo \n")
    else:
        print(f"\n    {num} es neutro \n")


# Cual numero es mayor y cual es menor
def calMenMay(num1, num2):
    if( num1 > num2 ):
        print(f"\n    {num1} es mayor \n    {num2} es menor \n")
    elif( num1 < num2 ):
        print(f"\n    {num1} es menor \n    {num2} es mayor \n")
    else:
        print( f"\n    {num1} es igual a {num2} \n")


# Calcular cual de los numeros es mayor y menor
def calTresNum(num1, num2, num3):
    mayor = 0
    menor = 0

    if( num1 > num2 and num1 > num3 ):
        mayor = num1
    
    if( num2 > num1 and num2 > num3 ):
        mayor = num2
    
    if( num3 > num1 and num3 > num2 ):
        mayor = num3

    # Menores
    if( num1 < num2 and num1 < num3 ):
        menor = num1
    if( num2 < num1 and num2 < num3 ):
        menor = num2
    if( num3 < num1 and num3 < num2 ):
        menor = num3


    print(f"\n    Mayor: {mayor} \n    Menor: {menor} \n")


# A y B, si A es mayor sumarlos sino restar
def abSumRest(a, b):
    if( a > b ):
        ans = a + b
        print(f"\n    {a} es mayor que {b} por lo tanto se suma \n \n    Resultado: {ans} \n")
    else:
        ans = a - b
        print(f"\n    {b} es mayor que {a} por lo tanto se resta \n \n    Resultado: {ans} \n")


# A y B, encontrar cociente entre A y B

def abCosciente(a, b):
    if( a == 0 and b == 0 ):
        print("\n    dividir 0 entre 0 esta mal no aplica \n")
    else:
        ans = a // b
        print(f"\n    El cociente de {a} y {b} es {ans} \n")

# Dos numeros segun su valor sumar o multiplicar
def abSumMul(a, b):
    if( a < 0 and b > 0 ):
        ans = a + b
        print( f"\n    '{a}' es negativo y se suma \n     --> {a} + {b} = {ans} \n")

    elif( a > 0 and b < 0 ):
        ans = a + b
        print(f"\n    '{b}' es negativo y se suma \n     --> {a} + {b} = {ans} \n")

    elif( a < 0 and b < 0 ):
        ans = a + b
        print( f"\n    '{a}' y '{b}' son negativos y se suman \n     --> {a} + {b} = {ans} \n")

    elif( a > 0 and b > 0 ):
        ans = a * b
        print( f"\n    '{a}' y '{b}' son positivos y se multiplican \n     --> {a} + {b} = {ans} \n")

    else:
        print( "\n    Los ceros son valores qu no sirven \n")


# Comprobador de añor bisiestos
def añoBisiesto(numY):
    if( numY % 4 != 0 ):
        print( f"\n    {numY}, No es un año Bisisesto! \n")
    elif( numY % 4 == 0 and numY % 100 != 0 ):
        print( f"\n    {numY} es un año Bisiesto! \n")
    elif( numY % 4 == 0 and numY % 100 == 0 and numY % 400 != 0 ):
        print( f"\n    {numY}, No es un año Bisiesto! \n")
    elif( numY % 4 == 0 and numY % 100 == 0 and numY % 400 == 0 ):
        print( f"\n    {numY}, Es un año Bisiesto! \n")
    else:
        print( f"   Como que {numY}, que paso ?")
    






