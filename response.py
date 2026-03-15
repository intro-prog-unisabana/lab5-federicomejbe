def input_responses(secret_value, user_input):
    if user_input < secret_value:
        return "Too low! Try a higher number.", False
    elif user_input > secret_value:
        return "Too high! Try a lower number.", False
    else:
        return "Correct! You guessed the number!", True