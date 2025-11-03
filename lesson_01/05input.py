# Lección de input en python
# input es una función que permite leer un valor ingresado por el usuario
# Siempre es bueno tener en cuenta que los valores ingresados por el usuario son strings
name = input("Hello how are you? \n Whats  your name: ")

print(f"Good morning, {name} \n I'm glad to meet you")

# convirtiendo un string a número por el principio de casting
age = input("How old are you? ")
print(f"You are {int(age) + 2} years old")

# Reciviendo múltiples valores
city, country = input("Enter your city and country: ").split()
print(f"You are from {city} in {country}")
