# Lección de variables en python

# Variables son un contenedor de datos
# Las variables se definen con el signo =
# Las variables se pueden redefinir
# El tipado de una variable es dinamico, no se necesita declarar el tipo de la variable

user_name = "Raphael"
document_id = 1010242843
passport_document = "AW513295"

print(user_name, document_id,passport_document,sep=", ")

# El literal de cadena de caracteres f es para formatear la cadena de caracteres
information_complete = f"User name: {user_name}, Document ID: {document_id}, Passport Document: {passport_document}"

print(information_complete)


# Variable definida pero no siignifica que no se puede redefinir
last_name: str = "Gonzalez"
print(last_name)
last_name = 10


# Asignación multiple
country, city, district = "Colombia", "Bogotá", "Cundinamarca"
print(country, city, district, sep=", ")
