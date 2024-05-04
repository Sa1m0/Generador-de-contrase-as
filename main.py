import random

car = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

long = int(input("Cuantos caracteres quieres en tu contraseña"))


for i in range(long):
    password += random.choice(car)

print(password)
