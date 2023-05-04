# Python Program to Generate Password
import random
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?/()"
mypassword=int(input("Enter the length of the password you want to generate "))
finalpassword="".join(random.sample(characters,mypassword))
print(finalpassword)