import random
symvol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
size = int(input('введите размер пароля Цифрами'))
for i in range (size):
    password = random.randint(symvol)
print (password) 