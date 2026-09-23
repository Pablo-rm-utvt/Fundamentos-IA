promedio=float(input("Ingresa tu promedio"))
asistencia=float(input("Ingresa tu porcentaje de asistencia"))
proyecto=input("Entregaste el proyecto?").lower()
afirmacion=input("Eres de DUAL?").lower()

P=asistencia>=80
Q=promedio>=8
R=proyecto=="si"
A= afirmacion=="si"

Resultado = P and Q and R

print("Bienvenido al sistema de evaluacion de alumnos")

print("Es DUAL : ", afirmacion)
print("Tu promedio es: ", promedio)
print("Tu porcentaje de asistencia es: ", asistencia)
print("Proyecto entregado: ", proyecto)


if Resultado or A:
    print("Has aprobado")
else:
    print("Has reprobado")