#Program to generate a password without using string module

import random

def create_password(length=8):
    
    # defining the characters to be used in generating password
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symbols = "!@#$%^&*'./?~"

    # creating a group of characters to be included in the password
    group = letters + num + symbols

    # generating a password
    password = '' #empty string 
    while password == '':
        password = ''.join(random.sample(group, length))

    return password

# example usage
password = create_password()
print(password)

