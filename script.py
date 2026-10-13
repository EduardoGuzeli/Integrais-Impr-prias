from sympy import *

# Integrais Impróprias

#A)
x = symbols('x')

f = 1/x**4
print(integrate(f, (x, 1, oo)))

#B)
f = 1/x**4
print(integrate(f, (x, -oo, -1)))

#C)
f = 1/x**4
print(integrate(f, (x, -oo, oo)))

#D)
f = x**2
print(integrate(f, (x, 1, oo)))

#E)
f = 1/x**2
print(integrate(f, (x, -oo, -1)))

