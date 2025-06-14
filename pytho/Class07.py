"""
En este archivo se va a 
trabajar la continuación de la estructura 
control condicional: If y else
"""


#Si el número que ingresa el usuario es
# negativo, se imprime las lineas 5,6
# Si es positivo  y menor a 10 se imprimen las lineas 7 y 8
# Si  el numero es positivo mayor o igual a 10 se imprimen 9 y 10 

numero = float(input('Ingrese un número: '))
print('Linea 2 ')
print('Linea 3 ')
print('Linea 4 ')

if numero < 0:
    print('Linea 5 ')
    print('Linea 6 ')

elif numero >= 0 and numero < 10:
    
    print('Linea 7 ')
    print('Linea 8 ')
    
elif numero >10 :    
    print('Linea 9 ')
    print('Linea 10 ')