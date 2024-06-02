import random  

import string

char=string.ascii_letters +string.digits+string.punctuation 

password_len=int(input("Enter length of password : "))

password=""

for i in range(password_len):
    password+=random.choice(char)

print(password)