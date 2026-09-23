valores = [True, False]

proposiciones = int(input("¿Cuántas proposiciones quieres evaluar? "))

for i in range(proposiciones):
    print(f"P{i+1}\t", end="")

print("AND")

print("-" * (8 * proposiciones + 8))

# Generar tabla de verdad
for i in range(2 ** proposiciones):

    fila = []

    for j in range(proposiciones):
        valor = bool((i >> (proposiciones - j - 1)) & 1)
        fila.append(valor)
        print(valor, "\t", end="")

    resultado = True

    for valor in fila:
        resultado = resultado and valor

    print(resultado)
    


for i in range(proposiciones):
    print(f"P{i+1}\t", end="")

print("OR")

print("-" * (8 * proposiciones + 8))

# Generar tabla de verdad
for i in range(2 ** proposiciones):

    fila = []

    for j in range(proposiciones):
        valor = bool((i >> (proposiciones - j - 1)) & 1)
        fila.append(valor)
        print(valor, "\t", end="")

    resultado = True

    for valor in fila:
        resultado = resultado or valor

    print(resultado)
    


for i in range(proposiciones):
    print(f"P{i+1}\t", end="")

print("->")

print("-" * (8 * proposiciones + 8))

# Generar tabla de verdad
for i in range(2 ** proposiciones):

    fila = []

    for j in range(proposiciones):
        valor = bool((i >> (proposiciones - j - 1)) & 1)
        fila.append(valor)
        print(valor, "\t", end="")

    resultado = True

    for valor in fila:
        resultado = (not resultado) and valor

    print(resultado)


for i in range(proposiciones):
    print(f"P{i+1}\t", end="")

print("<->")

print("-" * (8 * proposiciones + 8))

# Generar tabla de verdad
for i in range(2 ** proposiciones):

    fila = []

    for j in range(proposiciones):
        valor = bool((i >> (proposiciones - j - 1)) & 1)
        fila.append(valor)
        print(valor, "\t", end="")

    resultado = True

    for valor in fila:
        resultado = resultado == valor

    print(resultado)
