# Guess_the_Number
Game

Mi direccion de Github para este repositorio es la siguiente :[Github] (https://github.com/paulaanb/Guess_the_Number)
https://github.com/paulaanb/Guess_the_Number

En este juego hemos resuelto un juego basado en adivinar un numero comprendido entre 0 y 99.

El diagrama de flujo introducido es:

![Adivina_el_Numero](https://user-images.githubusercontent.com/91721496/140508292-653fd739-13ba-40da-be41-bf68bcc0ab2e.jpg)

El código que creamos para este juego es el mostrado abajo:

```#Creamos el juego donde el jugador debe intoducir un número aleatorio entre 0 y 100, debiendo adivinar dicho número.
#Metodo para generar el número aleatorio dentro del rango.
import random
number = random.randint(0,100)

#Generamos el enunciado del juego
print("Adivina el número generado desde 0 a 100")

#Bases del juego
user_number = int(input("Introduzca el número a adivinar:"))
chances = 0
if user_number < 0 or user_number > 99:
    print("El numero elegido no esta dentro del rango solicitado")
    user_number = int(input("Introduzca el número a adivinar:"))
    
while user_number != number:
    chances += 1
    if user_number < number:
        print("\n--> Su número es menor que el generado aleatoriamente.")
        user_number = int(input("\nIntroduzca el número a adivinar:"))
    elif user_number > number:
        print("\n--> Su número es mayor que el generado aleatoriamente.")
        user_number = int(input("\nIntroduzca el número a adivinar:"))
#Salimos del bucle al adivinar el número correcto.
if user_number == number:
    chances += 1
    print("\n¡Enhorabuena! Has adivinado el número aleatorio en" ,str(chances), "oportunidades")
    print("¡Bien hecho!")  
        
#Se terminó el juego
