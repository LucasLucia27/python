precio = float(input("ingrese el precio del producto: "))
if precio >= 100:
    precio_final = precio * 0.90
else:
    precio_final = precio
    print("el precio final es: ", precio_final)