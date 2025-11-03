# print_01.py
# Este archivo va a tratar sobre el uso de la funcion
#  print para imprimir texto en la consola

print("Hello, World!")


# Con el argumento sep se puede separar los elementos con un caracter
print("hello", "world", sep=" ---- ")

# Con el argumento end se puede cambiar el caracter de fin de linea
print("hello", "world", end=" ---- ")

# Con el argumento file se puede cambiar el archivo de salida
print("hello", "world", file=open("output.txt", "w"))

# Con el argumento flush se puede forzar el flush del buffer
print("hello", "world", flush=True)
