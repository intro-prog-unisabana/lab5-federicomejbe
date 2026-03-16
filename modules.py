import os 
import math

directorio = os.getcwd()
print(f"Current working directory: {directorio}")

num=int(input("Enter an integer: "))
valor_log = math.log2(num)
print(f"Log base 2 of {num} is: {valor_log}")

print(f"Floor: {math.floor(valor_log)}")
print(f"Ceiling: {math.ceil(valor_log)}")