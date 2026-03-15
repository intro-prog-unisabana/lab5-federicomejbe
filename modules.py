import os 
import math

directorio = os.getcwd()
print(f"Current working directory: {directorio}")

num=int(input("Enter an integer: "))
valor_log = math.log(num, 2)
print(f"log base 2 of {num} is: {valor_log}")

print(f"Floor: {math.floor(valor_log)}")
print(f"Ceiling: {math.ceil(valor_log)}")