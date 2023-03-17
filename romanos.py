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

simbolos_romanos = {
    'I': 1, 
    'V': 5, 
    'X': 10, 
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000
}


class RomanError(Exception):
    pass

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

def simbolo_a_valor(simbolo):
        try:
            return simbolos_romanos[simbolo]
        except KeyError as simbolo:
            raise RomanError(f"Error de sintaxis. Simbolo {simbolo} no permitido")

def romano_a_arabigo(cadena):
    resultado = 0
    cont_repeticiones = 0 
    cadena = cadena.upper()

    for ix in range(len(cadena)-1):
        letra = cadena[ix]
        siguiente = cadena[ix + 1]
        valor = simbolo_a_valor(letra)
        siguiente_valor = simbolo_a_valor(siguiente)

        #comprobar de repeticiones
        if valor == siguiente_valor: 
            cont_repeticiones += 1
        elif valor < siguiente_valor and cont_repeticiones > 0:
            raise RomanError(f"Error de sintaxis. {letra} repeticiones antes que resta")
        else:
            cont_repeticiones = 0

        if letra in 'VLD' and cont_repeticiones > 0: #porque letra es una sola, y revisa y si esa letra esta en esa cadena 
            raise RomanError("Error de sintaxis. Demasiadas repeticiones de {letra}")
        elif cont_repeticiones > 2: #para el test de cuatro repeticiones Error
            raise RomanError("Error de sintaxis. Demasiadas repeticiones de {letra}")


        if valor >= siguiente_valor:
            #siempre suma
            resultado += valor
        else:
            #comprobar restas
            if letra in 'VLD': #lo incluimos en el else, porque aqui vemos lo de menor 
                raise RomanError("Error de sintaxis. {letra} no puede restar")
            elif letra == 'I' and siguiente not in ('XV'):
                raise RomanError(f"Error sintaxis {letra}{siguiente} no permitido")
            elif letra == 'X' and siguiente not in ('LC'):
                raise RomanError(f"Error sintaxis {letra}{siguiente} no permitido")
            elif letra == 'C' and siguiente not in ('DM'):
                raise RomanError(f"Error sintaxis {letra}{siguiente} no permitido")

            resultado -= valor

    resultado += simbolo_a_valor(cadena[-1])
    return resultado 
        
            