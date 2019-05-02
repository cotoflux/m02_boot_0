def sumatorio(n):
    
    if n > 0:
        return  n + sumatorio(n-1)
    
    else:

        return 0
            
print(sumatorio(4))

def factorial(i):
    
    if i > 1:
        return i * factorial(i-1)
    
    elif i == 1:
        return 1
    else:
        return 0
    
print(factorial(4))