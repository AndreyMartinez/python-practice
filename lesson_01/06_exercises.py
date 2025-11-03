###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")


print("my name is Raphael", "i'm from Colombia", "Bogotá" , sep=", ")

### Completa aquí

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(type(a), type(b), type(c), type(d), type(e), sep=", ")

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

chain = 123456
print(type(chain) ,str(chain))
chain = str(chain)
print(type(chain),float(chain))
chain = float(chain)
print(type(chain))

## En el segundo ejercicio lo que va hacer es que toma el 3 ya que no va aredonder los valores correspondientes



### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

name, age, height = "Raphael", 20, 1.75
print(f"Hello! My name is {name} and I'm {age} years old, I'm {height} meters tall")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")


pi = 3.14
round_number = round(pi) / 2
print(round_number)

result_operation = int(round_number)
print(result_operation)
