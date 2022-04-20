def CuponDescuento(num_productos,monto_compra):
    """Función que calcula el porcentaje de descuento del cliente,
    los parámetros de entrada son el número de productos y el monto de la compra.
    La salida es un número decimal con el descuento correspondiente.
    Ejemplo: CuponDescuento(13,14500) = 8.5"""
    if (num_productos<10 and monto_compra >10000):
        # Si el número de productos es menor a 10 y el monto de la compra menor a 10,000
        # no hay descuento
        desc = 0
        print('Sin Descuento')
    elif (num_productos>=10 and monto_compra > 10000 and monto_compra<=30000):
        # Si  10 <= num productos y además 10,000 <= monto < 30,000, descuento de 8.75% 
        desc = 8.5
    elif (num_productos>=15 and monto_compra>30000 and monto_compra<=45000):
        # Si  15 <= num productos y además 30,000 <= monto < 45,000, descuento de 12.65% 
        desc = 12.65
    elif (num_productos>15 and num_productos<=30 and monto_compra > 45000 and monto_compra<=72000):
        # Si  15 < num productos < = 30 y además 45,000 <= monto < 72,000, descuento de 15.75% 
        desc = 15.75
    elif (num_productos>20 and num_productos<=40 and monto_compra > 72000 and monto_compra<=96000):
        # Si  20 <num productos <=40 y además 72,000 <= monto < 96,000, descuento de 20.5% 
        desc = 20.5
    elif (num_productos>20 and num_productos<=40 and monto_compra > 96000):
        # Si  20 < num productos y además monto > 96,000, descuento de 25.67% 
        desc = 25.67
        # Regresa la variable del descuento
    return desc
