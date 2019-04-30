def sumaTodo(limitTo):
    resultado = 0
    for i in range(0, limitTo + 1):
        resultado += 1
    return resultado
    

def sumaTodosCuadrados(limitTo):
    resultado = 0
    for i in range(limitTo+1):
        resultado +=i*1
        
    return resultado

print(sumaTodo(100))
print (sumaTodosCuadrados(3))