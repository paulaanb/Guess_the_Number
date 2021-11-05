#Creamos el juego donde el jugador debe intoducir un número aleatorio entre 0 y 100, debiendo adivinar dicho número.
#Metodo para generar el número aleatorio dentro del rango.
import random
number = random.randint(0,100)

#Generamos el ennunciado del juego
print("Adivina el número generado desde 0 a 100")

#Nos disponeos a generar un bucle finito al pedir el número
while True:
    user_number = int(input("Introduzca el número a adivinar:"))

    #Bases del juego
    user_number = int(user_number)
    chances = 0
    if user_number < 0 or user_number > 99:
        print("El numero elegido no esta dentro del rango solicitado")
    user_number: int(input("Introduzca el número a adivinar:"))
    
    while user_number != number:
        chances =+ 1
        if user_number < number:
            print("\n--> Su número es menor que el generado aleatoriamente.")
            user_number = int(input("\nIntroduzca el número a adivinar:"))
        elif user_number > number:
            print("\n--> Su número es mayor que el generado aleatoriamente.")
            user_number = int(input("\nIntroduzca el número a adivinar:"))
    #Salimos del bucle al adivinar el número correcto.
    if user_number == number:
        print("\n¡Enhorabuena! Has adivinado el número aleatorio en ", str(chances), "oportunidades") 
        print("\n¡Bien hecho!")      
#Se terminó el juego