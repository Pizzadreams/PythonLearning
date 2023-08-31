import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Iterate through letters, numbers, and symbols to add them into a new password var
# Convert string to list of chars, shuffle the new list, and join list to a new string and print

password = ""
for i in range(0, nr_letters):
  password += random.choice(letters)

for j in range(0, nr_symbols):
  password += random.choice(symbols)

for k in range (0, nr_numbers):
  password += random.choice(numbers)

# Convert string to list of chars
string_chars = list(password)
print(f"String converted to list: {string_chars}")

# Shuffle the list
random.shuffle(string_chars)
print(f"Shuffled list: {string_chars}")

#Join them into a new string
randomized_pw= ''.join(string_chars)

print(randomized_pw)