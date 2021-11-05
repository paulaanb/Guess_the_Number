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
    number = int(number)
    chances = 0
    if user_number < 0 or user_number > 99:
    print("El numero elegido no esta dentro del rango solicitado")
    user_number: int(input("Introduzca el número a adivinar:"))
    
    while user_number != number:
        
        