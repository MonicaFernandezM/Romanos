from romanos import arabigo_a_romano, romano_a_arabigo, RomanError

class RomanNumber():
    def __init__(self, entrada):
        if isinstance(entrada, str):
            self.arabigo = romano_a_arabigo(entrada)
            self.romano = entrada 
        elif isinstance(entrada, int):
            self.romano = arabigo_a_romano(entrada)
            self.arabigo = entrada 
        else: #me meten un tupla, una lista
            raise RomanError("La entrada tiene que ser entero o cadena")

    def __repr__(self):
        return self.__str__()
    
    def __str__(self): #siempre devuelve una cadena
        return f'{self.romano}'
    
    def __lt__(self, entrada):
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        
        return self.arabigo < entrada.arabigo
    
