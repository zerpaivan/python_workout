# script en que el usuario adivina un numero, entre 1 y 100) que previamente 
# a sido generado aleatoriamente por el script mediante random
# el script debe indicar si el numero esta por debajo o por encima del numero 
# ingresado por el usuario mientras este no acierte el numero.

import random
def number_guessing_game():
    rand_num = random.randint(1, 100)
    guess = False
    while guess == False:
        user_num = int(input("Ingresa un numero entre 1 y 100: "))
        if user_num == rand_num:
            guess = True
            print(f"!Adivinastes¡ el numero es: {rand_num}")
        elif user_num < rand_num:
            print("El numero es muy BAJO, intenta de nuevo")
        else:
            print("el numero es muy ALTO, intenta de nuevo")

if __name__ == "__main__":
    number_guessing_game()
    
