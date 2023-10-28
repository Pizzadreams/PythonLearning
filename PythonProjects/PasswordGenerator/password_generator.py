import random

class PasswordGenerator:

    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def generate_password(self, letters, symbols, numbers):
        password = ""
        for i in range(letters):
            password += random.choice(self.letters)

        for j in range(symbols):
            password += random.choice(self.symbols)

        for k in range(numbers):
            password += random.choice(self.numbers)

        # Shuffle the list
        string_chars = list(password)
        random.shuffle(string_chars)

        # Join them into a new string
        randomized_pw = ''.join(string_chars)

        return randomized_pw  # Return the generated password

if __name__ == '__main__':
    generator = PasswordGenerator()
    input_letters = int(input("How many letters would you like in your password?\n"))
    input_symbols = int(input(f"How many symbols would you like?\n"))
    input_numbers = int(input(f"How many numbers would you like?\n"))
    generated_password = generator.generate_password(input_letters, input_symbols, input_numbers)
    print(f"Generated Password: {generated_password}")
