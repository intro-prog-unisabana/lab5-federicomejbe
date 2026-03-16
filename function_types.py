def list_shift(lst, dato):
    for i in range(len(lst)):
        lst[i] = lst[i] + dato

def calc_avg(lst):
    suma = 0 
    for numero in lst:
        suma = suma + numero
    promedio = suma / len(lst)
    return promedio

def print_normalized(lst):
    print(lst)
