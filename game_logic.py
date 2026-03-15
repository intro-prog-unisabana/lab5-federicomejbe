from secret_number import seed_secret_numbers, generate_secret_numbers
from response import input_responses

seed = int(input("Enter a seed number: "))
seed_secret_numbers(seed)

secret = generate_secret_numbers()

numero = 0
correct = False

while not correct:
    guess = int(input("What is your guess: "))
    numero += 1
    message, correct = input_responses(secret, guess)
    print(message)

print(f"It took you {numero} tries!")