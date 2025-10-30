RPM_B = 0
RPM_A = 0
Resumen = {
    "registros_elevados": [],
    "registros_bajos": [],
    "Umbral_seguro": [],
    "TIEMPO": []
}

estadisticas = {"RPM_B": 0, "RPM_A": 0}

for TIEMPO in range(1, 61, 5):
    POR_POT = int(input("Introduzca un porcentaje de potencia (sin el signo %): "))
    RPM = 10 + (POR_POT / 100) * (3000 - 10)

    Resumen["TIEMPO"].append(TIEMPO)  # se guarda siempre

    if RPM <= 1000:
        RPM_B += 1
        estadisticas["RPM_B"] += 1
        Resumen["registros_bajos"].append(RPM)
        print(f" Nivel bajo de RPM ({RPM:.2f}) en el minuto {TIEMPO}")
    elif RPM <= 2500:
        Resumen["Umbral_seguro"].append(RPM)
        print(f" Umbral seguro ({RPM:.2f}) en el minuto {TIEMPO}")
    else:
        RPM_A += 1
        estadisticas["RPM_A"] += 1
        Resumen["registros_elevados"].append(RPM)
        print(f" Sobretorque ({RPM:.2f}) en el minuto {TIEMPO}")

    print(f"Contadores: RPM_Bajo={RPM_B}, RPM_Alto={RPM_A}, Tiempo={TIEMPO}\n")

print("\n Resumen de eventos:")
for clave, valor in Resumen.items():
    print(f" - {clave}: {valor}")

print("\n Estadísticas generales:")
for clave, valor in estadisticas.items():
    print(f" - {clave}: {valor}")
