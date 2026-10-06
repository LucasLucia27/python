a = float(input("ingrese el primer número: "))
b = float(input("ingrese el segundo número: "))

print("suma:", a + b)
print("resta:", a - b)
print("multiplicación:", a * b)
print("división:", a / b)

operacion = input("Ingrese la operación que desea realizar (suma, resta, multiplicación, división): ")
if operacion == "suma":
    print("El resultado de la suma es:", a + b)
elif operacion == "resta":
    print("El resultado de la resta es:", a - b)
elif operacion == "multiplicación":
    print("El resultado de la multiplicación es:", a * b)
elif operacion == "división":
    print("El resultado de la división es:", a / b)

