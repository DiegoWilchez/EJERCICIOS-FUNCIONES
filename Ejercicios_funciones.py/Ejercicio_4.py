"""
Cree una función para pago semanal con horas extra. Es un modelo ficticio: las primeras 40 horas
se pagan a la tarifa ordinaria; solo las horas que exceden 40 se pagan a 1,5 veces esa tarifa. Llame para
dos personas y sume los retornos, sin redondearlos antes de sumar. Contrato: Pago semanal con horas
extra: recibe horas semanales reales no negativas y tarifa real no negativa en pesos por hora y devuelve
el pago real semanal en pesos


Fórmula o relación: Pago = horas x tarifa si horas ≤ 40; si horas > 40, pago = 40 x tarifa + (horas -40) x tarifa x 1,5

"""
def pago_semanal(horas,tafira):
    if horas <= 40:
        return horas + tafira

pago1 = int(input("ingrese el pago numero 1"))
pago2 = int(input("ingrese el pago numero 2"))
total = pago1 + pago2

print("pagos",pago1, "y" ,pago2,"pesos",total)