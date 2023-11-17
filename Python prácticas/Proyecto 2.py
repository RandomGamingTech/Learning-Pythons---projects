name = input("¿Cuál es tu nombre?\n")
ventas_totales = (float(input("Inserta el total de tus ventas\n")))
comision = ventas_totales*13/100
redondeo = round(comision, 2)
sueldo_total = redondeo + ventas_totales
redondeo2 = round(sueldo_total, 2)
print(f"{name} tu comisión es de ${redondeo}")
print(f"Tu sueldo más la comisión es de: ${redondeo2}")