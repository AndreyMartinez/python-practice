# Lección de operadores lógicos en python
# Operadores lógicos son: and, or, not

# AND: se ejecuta de la siguiente manera:
have_passport = input("Do you have a passport? (yes/no) ")
need_visa = input("Do you need Visa? (yes/no)")

if have_passport == "yes" and need_visa == "yes":
    print("You can travel to the country \n WELCOME")
elif have_passport == "yes" and need_visa == "no":
    print("You need to apply for a visa")
else:
    print("You dont cant travel to the country")

print(f"END THE APLICATION  your answer was have_passport: {have_passport} and need_visa: {need_visa}")



# OR: se ejecuta de la siguiente manera: Ejercicio con vacunación

have_yellow_fever_vaccine= input("Do you have a vaccine? (yes/no) ")
have_covid_vaccine = input("Do you have a covid vaccine? (yes/no) ")
if have_yellow_fever_vaccine == "yes" or have_covid_vaccine:
    print("You can travel to the country \n WELCOME")
else: 
    print("You cant travel to the country")



# Condiciones ternarias se ejecuta de la siguiente manera:
subject_school = input("Enter your subject school: ")
name_professor = "MR Carlos" if subject_school == "math" else "MR Hernesto"
print(f"the professor name is {name_professor}")


have_passport = input("Do you have a passport? (yes/no) ")
can_continue = True if have_passport == "yes" else False
print(f"You can continue: {can_continue}")
