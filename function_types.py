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

datos = [2.0, 4.0, 6.0, 8.0]

prom = calc_avg(datos)         # 5.0
list_shift(datos, -prom)       # datos se convierte en [-3.0, -1.0, 1.0, 3.0]
print_normalized(datos)        # imprime [-3.0, -1.0, 1.0, 3.0]