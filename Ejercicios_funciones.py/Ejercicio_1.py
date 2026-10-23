"""
Cree una función para área de un triángulo por base y altura. La altura es perpendicular a la base.
Use dos llamadas y muestre las dos áreas y su suma, calculada con los retornos. Contrato: Área de un
triángulo por base y altura: recibe base y altura, reales positivos expresados en centímetros y devuelve
el área real en centímetros cuadrados

Fórmula o relación: Área = base x altura / 2. La división entre 2 obtiene la mitad del rectángulo de
igual base y altura


"""

def area(base, altura):
    resultado = base * altura / 2
    return resultado

area1 = area(23,45)
area2 = area(3,8)
suma = area1 + area2

print("Area 1", area1, "cm²")
print("Area 2", area2,"cm²")
print("suma de las areas",suma,"cm²")




