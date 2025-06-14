"""En este archo vamos a
realizar operaciones
de comparación y lógicas"""

print ('Operaciones de comparación') 
num1 = 10
num2 = 20

print(f'num1 < num2: {num1 < num2}')
print(f'num1 <= num2: {num1 <= num2}')
print(f'num1 == num2: {num1 == num2}')
print(f'num1 > num2: {num1 > num2}')
print(f'num1 >= num2: {num1 >= num2}')
print(f'num1 != num2: {num1 != num2}')

#Operaciones lógicas and, or ,  not

2+3 == 9 and 4*5 > 2

print(f'False and False:{False and False}') 
print(f'False and True:{False and True}') 
print(f'True and False:{True and False}') 
print(f'True and True:{True and True}') 

print('\n Operaciones logicas OR')
#Operacion OR
2+3 == 9 or 4*5 > 2

print(f'False or False:{False or False}') 
print(f'False or True:{False or True}') 
print(f'True or False:{True or False}') 
print(f'True or True:{True or True}') 



print('\n Operaciones logicas not')
#Operacion OR
2+3 == 9

print(f' not False:{not False}') 
print(f' not True:{not True}') 

print('\n Ejemplo:')

num1 = 10
num2 =20

print('not (num1 >= num2 and num1 < 50)')
print(not (num1 >= num2 and num1 < 50))  