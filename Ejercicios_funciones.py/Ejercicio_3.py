"""
Cree las funciones necesarias para tolerancia de una medición. Debe reutilizar una función de
valor absoluto que recibe un real y devuelve su distancia al cero. Los extremos de tolerancia se aceptan.
La función de aceptación utiliza el retorno de valor absoluto. El escenario consulta dos mediciones por
separado. Contratos en orden de parámetros: Valor absoluto: recibe real finito y devuelve real no
negativo. Aceptación: recibe medición y objetivo reales, tolerancia real no negativa y devuelve lógico


Fórmula o relación: Error = valor absoluto de (medición - objetivo); aceptable cuando error ≤ tolerancia
"""

def valor_absoluto(x):
    if x < 0:
        return -x
    return x

def acepteble(medicion,objetivo,tolerancia):
    error = valor_absoluto(medicion-objetivo)
    return error <= tolerancia

objetivo = float(input("ingrese un valor"))
tolerancia = float(input("ingrese el valor"))

a = acepteble(9.5, objetivo, tolerancia)
b = acepteble(10.6, objetivo, tolerancia)

print(f"Aceptable {a};{b}") 
