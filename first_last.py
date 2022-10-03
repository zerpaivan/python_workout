# tomar una iterable (lista, tupla o string) y devolver el primer y ultimo valor
# dentro del arreglo correspondiente
def first_last(iter):
    return iter[:1]+ iter[-1:]

if __name__ == "__main__":
    print(first_last('abcdef'))
