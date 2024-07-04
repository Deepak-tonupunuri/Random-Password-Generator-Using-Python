#simple password generator
import random
import string

length=int(input("Enter the lenght of the password:"))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation
letters=lower+upper
n_letters=int(input('Enter the no of letters:'))
n_numbers=int(input('Enter the no of numbers:'))
n_symbols=int(input('Enter the no of symbols:'))
password=""
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password += char
for i in range(1,n_numbers+1):
    char=random.choice(num)
    password += char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password += char
print(password)


