#use case - Ths is a password generator which generates a password for the user of his/her desired length.

#we have imported the random function which will allow us to choose random letters, numbers and symbols further in the code
import random
import string

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = string.punctuation

letter, num, sym = True, True, True

pwd = ""

if letter:
  pwd = pwd + letters
if num:
  pwd = pwd + numbers
if sym:
  pwd = pwd + symbols


print("WELCOME TO PASSWORD GENERATOR!")
length = int(input("Enter the length of the password you want: "))
amount = 1

for i in range(amount):
  password = "".join(random.sample(pwd, length))
  print("Generated password: ",password)




