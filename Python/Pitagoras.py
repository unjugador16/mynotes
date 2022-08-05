from math import sqrt

cateto_a = float(input('Ingrese el valor de un lado del triangulo: '))
cateto_b = float(input('Ingrese el valor del otro lado del triangulo: '))

cateto_a = cateto_a ** 2
cateto_b = cateto_b ** 2
hipotenusa = cateto_a + cateto_b

hipotenusa = sqrt(hipotenusa)
print(f'La hipotenusa del triangulo es {hipotenusa}')