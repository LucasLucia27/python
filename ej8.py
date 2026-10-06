nombre = input("cual es tu nombre? ")
edad = int(input("cual es tu edad? "))
print("hola", nombre, "de", edad, "años")
nota1= float(input("ingrese su primera nota: "))
nota2= float(input("ingrese su segunda nota: "))
nota3= float(input("ingrese su tercera nota: "))
promedio= (nota1 +nota2 + nota3)/3
if promedio>=71:
    print("aprobaste la clase con un promedio de ", promedio) 
else:
    print("reprobaste la clase con un promedio de: ", promedio)
