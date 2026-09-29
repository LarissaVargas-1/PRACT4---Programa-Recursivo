def fibonacci(n):
    num1, num2 = 0, 1
    
    # Bucle iterativo eficiente O(n)
    for _ in range(n):
        num1, num2 = num2, num1 + num2
        
    return num1

n = 500
resultado = fibonacci(n)

print(f"El número de Fibonacci en la posición {n} es:")
print(resultado)
