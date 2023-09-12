"""
Base de conocimiento (o de reglas): reglas que describen 
los mecanismos de razonamiento que permiten resolver problemas
"""
print("¿Lloverá?")
temperatura = int(input("Ingrese la temperatura en centígrados: "))
humedad = int(input("Ingrese el porcentaje de humedad: "))

hace_calor = temperatura > 30
posibilidad_lluvia = humedad > 80

if hace_calor and posibilidad_lluvia:
    hay_tormenta = True
    resp = "probablemente sí"
else:
    hay_tormenta = False
    resp = "no es probable"

print("Lluvia:", resp)

if hay_tormenta:
    viento = input("¿Hay fuertes vientos? ")
    bviento = viento.lower()
    if bviento == "si":
        print("Será una fuerte lluvia")
