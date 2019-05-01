from funciones1 import sumaTodos

# Quant es vol reutiltzar s'utilitza 
# doble = lambda x: x*2
# triple = lambda x: x**3
# print(sumaTodos(3, doble))
# print(sumaTodos(100, triple))

#Si no es reutilitza
print(sumaTodos(3, lambda x: x*2))
print(sumaTodos(100, lambda x: x*3))