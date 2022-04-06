# Ciclos y funciones

import math
import time


# Imprime los multiplos de 3 entre 1 y 100

def ciclo_1():
    print(f"nro multiplos de 3")
    for i in range(1, 101):
        time.sleep(0.5)
        if( i % 3 == 0 ):
            print(i)


# Imprime si el numero es impar o no
def numImpares():
    print(f"  numeros impares del nro 0 al nro 100")
    for i in range(0, 100):
        time.sleep(0.2)
        if( i % 2 != 0 ):
            print(f"   --> {i}")
    print(" final \n")
