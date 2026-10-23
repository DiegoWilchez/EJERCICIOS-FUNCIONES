"""
Cree una función para precio unitario comparable. Dos paquetes pueden tener tamaños distintos;
no compare solo sus precios totales. Llame para dos paquetes y use los retornos para indicar el más
económico por gramo; si coinciden indique igualdad. Contrato: Precio unitario comparable: recibe
precio total real no negativo en pesos y cantidad real positiva en gramos y devuelve el precio real de un
gramo en pesos

Fórmula o relación: Precio por gramo = precio total / cantidad de gramos


"""
def  precio_por_gramo(precio,gramos):
    return precio / gramos

paquete1 = precio_por_gramo(6000,500)
paquete2 = precio_por_gramo(4200, 300)

print(f"precio por gramo {paquete1:g} y {paquete2:g} pesos")
if paquete1 < paquete2:
    print("mejor paquete 1")
elif paquete2 < paquete1:
    print("mejor paquete 2")
else:
    print("son iguales")