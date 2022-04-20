def esEntero(n):
    """ Función que regresa un valor binario 
    si se ingresa un número: si es 
    entero regresa True, caso contrario
    regresa False.
    Ejemplo: esEntero(40)=True
    esEntero(-23)= True
    esEntero(400.54) = False"""
    if isinstance(n,int):
        return True
    if isinstance(n,float):
        #return n.is_integer()
        return False
def esPositivo(n):
    """Función que regresa un valor binario
    de acuerdo a si es o no positivo un número
    Ejemplo: esPositivo(4)= True
    esPositivo(-345)= False
    esPositivo(5.6)= True"""
    if (n<0):
        return False
    else:
        return True
