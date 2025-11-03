# Lección de condicionales en python
# Condicionales de if se ejecuta de la siguiente manera:
import os
os.system("clear")
age = 18
name = "" 
if age >= 18:
    print("You are an adult")
    name = "MR Raphael"

else: 
    print("You are not an adult")
    name = "child Rapha"
## IMPORTANTE: el tabulado es importante para saber lo que se encuentra dentro de los condicionales
print(f"END THE PROGRAM {name}")


##Condiciones elif se ejecuta de la siguiente manera:
politic_position = input("Enter your politic position: ")

if politic_position == "left":
    print(f"your are leflist person {politic_position}")
elif politic_position == "right":
   print(f"you are rightist person {politic_position}")
else:
   print(f"you are not a politic person {politic_position}")


