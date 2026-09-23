import time

print("Bienvenido al diagnóstico inteligente de equipo")
print("-" * 40)

print("Hola, voy a ayudarte a revisar tu equipo.")
print("Te haré algunas preguntas para encontrar el posible problema.")
print("-" * 40)

errores = []

electricidad = input("¿El equipo tiene electricidad? (s/n): ").lower() == "s"

for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.3)
    
if electricidad:
    print("\nPerfecto, detecto que el equipo tiene alimentación eléctrica.")
else:
    print("\nEntendido. Parece que tenemos un problema con la alimentación.")
    errores.append("No se detectó alimentación eléctrica. \n Revisa el cable de corriente, el enchufe y la fuente de alimentación.")

enciende = input("¿El equipo enciende? (s/n): ").lower() == "s"

for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.3)

if enciende:
    print("\nMuy bien, el equipo logra encender.")
else:
    print("\nEntiendo. Revisa el cable de video (HDMI, VGA, DVI), esto también puede ser un problema de la fuente de poder.")
    errores.append("El equipo no encendió. \n Revisa la fuente de poder y sus conexiones.")

imagen = input("¿El equipo muestra imagen? (s/n): ").lower() == "s"

for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.3)

if imagen:
    print("\nPerfecto, el equipo está mostrando imagen.")
else:
    print("\nNo se está mostrando imagen. Esto puede estar relacionado con el monitor o la memoria.")
    errores.append("El equipo no mostró imagen. \n Revisa el monitor, el cable de video y la memoria RAM.")


for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.3)

print("\n" + "-" * 40)
print("RESUMEN DEL DIAGNÓSTICO")
print("-" * 40)

print("Electricidad:", electricidad)
print("Enciende:", enciende)
print("Imagen:", imagen)


print("\n" + "-" * 40)

if not errores:
    print("¡Todo parece estar en orden! No se detectaron problemas.")
else:
    print("Se han detectado los siguientes problemas:")
    for error in errores:
        print("\n- " + error)
        

print("-" * 40)

print("\nDiagnóstico finalizado. ¡Gracias por utilizar el asistente!")

