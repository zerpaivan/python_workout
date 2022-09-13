# script para sumar numeros de un arreglo

# ingreso de la lista de numeros. Se detiene cuando no ingresa nada
def sumalist():
    n = 1
    numbers_list = []
    while True:

        try:
            num = input(f"Ingresa un numero {n}: ")
            if num != "":
                numbers_list.append(float(num))
                n = n + 1
            else:
                break
        except ValueError as val_e:
            print("Ingrese solo valores numericos", val_e)

    print(numbers_list)
    return sum(numbers_list)


print(sumalist())
