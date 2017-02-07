#!usr/bin/python3

# Ejercicio 13.6 Calculadora
# Christian Bermejo Guerrero
import sys

def suma(operando1, operando2):
    return int(operando1) + int(operando2)

def resta(operando1, operando2):
    return int(operando1) - int(operando2)

def multiplicar(operando1, operando2):
    return int(operando1) * int(operando2)

def dividir(operando1, operando2):
    return int(operando1) / int(operando2)
try:
    if (sys.argv[1] == 'suma'):
        print (suma(sys.argv[2],sys.argv[3]))
    elif (sys.argv[1] == 'resta'):
        print (resta(sys.argv[2],sys.argv[3]))
    elif (sys.argv[1] == 'multiplicar'):
        print (multiplicar(sys.argv[2],sys.argv[3]))
    elif (sys.argv[1] == 'dividir'):
        print (dividir(sys.argv[2],sys.argv[3]))
    else:
        print ('Operacion no valida')
except ZeroDivisionError:
    print('No debes dividir entre 0')
