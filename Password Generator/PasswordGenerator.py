import random

def password_generator(n, len):
    chars = 'qwertyuiopasdfghjklzxcvbnm1234567890-=[];\\,./!@#$%^&*()_+|}{":<>?`~'
    for pwd in range(n):
        passwords = ''
        for c in range(len):
            passwords += random.choice(chars)
        print(passwords)

n = int(input("Enter number of passwords: "))
len = int(input("Enter length of passwords: "))
password_generator(n, len)