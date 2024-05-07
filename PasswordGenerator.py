import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)
password = [letters, numbers, symbols]

finalPassword = ''
password_num = int(input("Enter the length of password: "))

for num in range(password_num):
    mix_pass = random.choice(password)
    finalPassword += random.choice(mix_pass)

print(finalPassword)
