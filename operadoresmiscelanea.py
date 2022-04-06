# Operaciones
import math

# Calcular el area de un triangulo
def areadelTri(base, altura):
    return base * altura / 2

# Suma de dos numeros
def suma(num1, num2):
    return num1 + num2

# ELevar numero al cuadrado
def elevado(num):
    return num ** 2

# Convertidor de divisas
def conversiones(num):
    return num * 0.90 # Valor del euro respecto al dolar

# Calcular Area y Perimetro
def area(num):
    return num ** 2

def perimetro(num):
    return num * 4
    
# Area de circunferecnia
def areaCir(num):
    return ((13.1415 * num) ** 2)

# Area y volumen de un cilindro
def areaCil(base, altura):
    r = base / 2
    h = altura

    #Area Base
    aB = math.pi * (r ** 2)

    #Area Lateral
    aL = (2 * math.pi) * r * h
    
    # Area total
    aT = aB + (2 * aL)
    return aT

def volCil(base, altura):
    r = base / 2
    h = altura

    #Area Base
    aB = math.pi * (r ** 2)

    #Volumen Cilindro
    v = aB * h
    return v


# Promedio de tres numeros
def promedio(num1, num2, num3):
    ans = num1 + num2 + num3 

    return ans / 3



