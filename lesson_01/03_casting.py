# Lección de casting en python

# Casting es el proceso de convertir un tipo de valor a otro
# Por ejemplo, convertir un string a un int
# o convertir un int a un string

# Ejempl de convertir un string a un int
print(int("2"))
print("The result is", int("3") + int("1"), sep=" = ")

# Ejemplo de convertir un int a un string
print(str(43))
print(str(2), str(43), str(45), end=".", sep=" + ")


# Ejemplo de convertir un string a un float
print(float(("3.2")))
print(type(float(("3.2"))))

# Ejemplo de booleanons
print(bool(1))  # True
print(bool(0))  # False
print(bool("True"))  # True
print(bool("False"))  # True
print(bool(""))  # False
print(bool(" "))  # True
print(bool("0"))  # True
print(bool("3"))
