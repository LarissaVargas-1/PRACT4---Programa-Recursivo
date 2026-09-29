def sudan(n: int, x: int, y: int) -> int:
    """
    Función de Sudan para pruebas de teoría de la computabilidad.
    """
    if n == 0:
        return x + y
    
    if y == 0:
        return x
    
    # RECURSIVIDAD ANIDADA COMPLEJA:
    # La llamada externa utiliza el resultado de una llamada interna 
    # que a su vez decrementa 'y'
    return sudan(n - 1, sudan(n, x, y - 1), sudan(n, x, y - 1) + y)

if __name__ == "__main__":
    # Usamos números muy pequeños porque crece extremadamente rápido
    print(f"Resultado de Sudan(1, 1, 1): {sudan(1, 1, 1)}")
