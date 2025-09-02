#Julieta Yañez

limite_empleados = 3
contador_empleados = 0

contador_empleados_iot_ia = 0
contador_no_ia = 0
porcentaje_no_ia = 0

while contador_empleados < limite_empleados:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su género (masculino, femenino, otro): ")
    tecnologia_elegida = input("Ingrese la tecnología elegida: ")


    while edad < 18:
        edad = int(input("Debe ser mayor de edad. Ingrese su edad nuevamente: "))

    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input("Ingrese su genero nuevamente: ")

    while tecnologia_elegida != "IA" and tecnologia_elegida != "RV" and tecnologia_elegida != "IOT":
        tecnologia_elegida = input("Ingrese una tecnología válida: ")

    if genero == "masculino" and 25 <= edad <= 50:
        if tecnologia_elegida == "IA" or tecnologia_elegida == "IOT":
            contador_empleados_iot_ia += 1

    if genero != "femenino" and 33 <= edad <= 40:
        porcentaje_no_ia += 1
        if tecnologia_elegida != "IA": 
            contador_no_ia += 1

    if genero == "masculino" and edad > 18:
        contador_empleados += 1
    
    print(f"Su nombre es: {nombre} y votó la tecnología: {tecnologia_elegida}")

print("Encuesta finalizada.")
print(f"Cantidad de empleados masculinos entre 25 y 50 años que votaron IA o IOT: {contador_empleados_iot_ia}")

if porcentaje_no_ia > 0:
    porcentaje = (contador_no_ia / porcentaje_no_ia) * 100
    print(f"Porcentaje de empleados que NO votaron IA (entre 33 y 40 años, no femeninos): {porcentaje}%")
else:
    print("No hubieron empleados que cumplieran la condición para calcular el porcentaje.")
