# Llama a todas las funciones de la librería cupones
from cupones import *
# Llama a todas las funciones de la librería esNatural
from esNatural import *

# Captura el nombre y apellido del empleado
nombre = input('Ingrese nombre y apellido del empleado\n ')
# Captura la cantidad de productos de la última compra
num_productos = int(input('Ingrese la cantidad de productos de la última compra\n '))
# Verifica si el número de productos es natural, debe ser entero y positivo, importa
# las funciones de la librería esNatural
esNatural_numProductos = esEntero(num_productos) and esPositivo(num_productos)
# Si el numero de productos no es un natural imprime un mensaje de error y no hace el cálculo
if (not esNatural_numProductos):
    print('Error: Los valores entregados se encuentran fuera del rango esperado')
# Redondea al entero más cercano el número de productos
monto_productos  = round(float(input('Ingrese el monto de la última compra \n')))
esNatural_montoProductos = esEntero(monto_productos) and esPositivo (monto_productos)
#if (not esNatural_montoProductos):
#    print('Error: Los valores entregados se encuentran fuera del rango esperado')
# Si es natural el número de productos y es natural el monto pagado, realiza el cálculo del
# descuento
if esNatural_numProductos and esNatural_montoProductos:
    # Guarda el nombre del cliente, el monto de la última compra (convertido a string) y el 
    #número de productos adquiridos (convertido a string) en un diccionario
    dict_clientes = {
                    "Nombre del cliente:": nombre, 
                    "Monto de la última compra:": str(monto_productos),
                    "Número de productos adquiridos:": str(num_productos)
                    }
    # Calcula la longitud máxima de los encabezados (llaves) del diccionario para alinear en el print
    a = len(max(dict_clientes.keys(), key=len))
    # Calcula la longitud máxima de los valores guardados en el diccionario para alinear en el print
    b= len(max(dict_clientes.items(), key=len))
    # Calcula la cantidad de porcentaje de descuento(sobre 100) de acuerdo con las condiciones de la tabla
    porcentajeDescuento = CuponDescuento(num_productos,monto_productos)
    # Imprime la salida del programa después de calcular el descuento
    print('****************************************************************************\n')    
    for key, value in dict_clientes.items():
        # Imprime los valores del diccionario de manera justificada
        print(key.ljust(a)+'\t'+value.rjust(a))
        #print(f'{key:<{a}}\t \t{value:>{b}}')
    #print(  f"{'Nombre del cliente:':>{35}} {dict_clientes["Nombre"]:>{a}} \n",
    #        f"{'Monto de la última compra:':>{35}} {dict_clientes["Monto_compra"]:>{a}} \n",
    #        f"{'Número de productos adquiridos:':>{35}} {dict_clientes["Cantidad_productos"]:>{a}}")
    print('****************************************************************************\n')
    print('Usted acaba de ganar un cupón de descuento para su próxima compra por \n')
    # Imprime la cantidad y el porcentaje del descuento aplicado
    print(f'un monto de {(monto_productos*porcentajeDescuento)/100} pesos, equivalente al {porcentajeDescuento}% de su última compra \n')
    print('********************************************************************************')
else:
    # Envía mensaje de error en caso de que los valores del monto y cantidad de productos
    # no sean números naturales
    print('Error: Los valores entregados se encuentran fuera del rango esperado')
