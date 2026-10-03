###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí

print("Lluís Portals Bonich", end="\n")
print("Barcelona")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print("El tipus de la variable a és:", type(a))
print("El tipus de la variable b és:", type(b))
print("El tipus de la variable c és:", type(c))
print("El tipus de la variable d és:", type(d))
print("El tipus de la variable e és:", type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí

print("\"12345\" a enter és:", int("12345"))
print("\"12345\" a float és:", float(int("12345")))
print("3.99 a enter és:", int(3.99)) # Trunca els decimals, passant de 3.99 a 3 :)


print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

name = "Lluís"
age = 19
height = 1.71

### Completa aquí

print(f"Hola, em dic {name}, tinc {age} anys i mesuro {height} metres. ")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

### Completa aquí

pi = 3.14159
pi_arrodonit = round(pi)
divisio = pi_arrodonit // 2
print("Pi // 2 és igual a:", divisio)

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

temp = float(input("Introdueix la temperatura (Cº): "))
farenheit = temp * 9/5 + 32
print(f"{temp}ºC equivalen a {farenheit:.2f}ºF")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí

compte = float(input("Introdueix el total del compte: "))
propina = float(input("Introdueix el percentatge de propina:"))
propina_total = compte * (propina / 100)
compte_total = compte + propina_total
print(f"La propina és: {propina_total:.2f}€")
print(f"El total a pagar és: {compte_total:.2f}€")

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí

contrasenya = input("Introdueix una contrasenya: ")
if len(contrasenya) >= 8:
    print("Contrasenya vàlida!")

else:
    print("Contrasenya no vàlida!")


