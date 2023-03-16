valores_romanos = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

def valida_numero(n):
    if not isinstance(n, int):
        raise TypeError("f{n} debe ser de tipo int")
    
    if n <= 0:
        raise ValueError(f"{n} debe ser un entero positivo")
    

def arabigo_a_romano(n): 
    valida_numero(n)
    romano = '' 
    resto = None

    while resto != 0: 
        for valor in sorted(valores_romanos.keys(), reverse=True): 
            if n >= valor: 
                break

        cociente = n // valor
        resto = n % valor
        romano += cociente * valores_romanos[valor]
        n = resto 

    return romano  

def romano_a_arabigo(cadena):
    resultado = 0
    for ix in range(len(cadena)-1):
        letra = cadena[ix]
        siguiente = cadena[ix + 1]
        if d[letra] >= d[siguiente]:
            resultado += d[letra]
        else:
            resultado -= d[letra]

    resultado += d[len(cadena)-1]
        
            