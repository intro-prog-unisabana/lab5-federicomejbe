from utils import *
mensaje = input("Please type your message\n")

mensaje_flip = flip(mensaje)
mensaje_a = count_letters(mensaje, "a")
mensaje_codificado = mensaje_flip + str(mensaje_a)

print(f"Your encoded message is: {mensaje_codificado}")