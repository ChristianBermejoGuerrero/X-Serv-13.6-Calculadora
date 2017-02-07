#!usr/bin/python3

# Ejercicio 13.6 Calculadora
# Christian Bermejo Guerrero
import sys

if len(sys.argv) != 4:
    sys.exit("Usage: calculadora.py operacion operando1 operando2")

def suma(operando1, operando2):
    return float(operando1) + float(operando2)

def resta(operando1, operando2):
    return float(operando1) - float(operando2)

def multiplicar(operando1, operando2):
    return float(operando1) * float(operando2)

def dividir(operando1, operando2):
    return float(operando1) / float(operando2)

if (sys.argv[1] == 'suma'):
    print (suma(sys.argv[2],sys.argv[3]))
elif (sys.argv[1] == 'resta'):
    print (resta(sys.argv[2],sys.argv[3]))
elif (sys.argv[1] == 'multiplicar'):
    print (multiplicar(sys.argv[2],sys.argv[3]))
elif (sys.argv[1] == 'dividir'):
    try:
        print(dividir(sys.argv[2],sys.argv[3]))
    except ZeroDivisionError:
        print ("No debes dividir entre 0")
else:
    print ('Operacion no valida')
