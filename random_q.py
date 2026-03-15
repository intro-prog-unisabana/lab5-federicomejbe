import random
random.seed(123)

start_value = int(input("Enter the start value:\n"))
end_value = int(input("Enter the end value:\n"))

num_random = random.randint(start_value, end_value)
print(f"Generated random number: {num_random}")