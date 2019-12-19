#display opening
print("Hello and welcome to my final project!")
#declaring while statement
while True:
    #start the generator
    start = input("To start generating passwords please type 'START'! ")
    #assigning variable true to the string START
    true = "START"
    #stating that if start is typed to beging the program
    if start == true:
        #if start is chosen the program will begin
        print("Lets begin!")
        break
    else:
        #if something else is entered try again
        print("Try again! Please type 'START'!")
        continue
        break
#generates a random number
import random
#choosing the number of passwords you need
numpass = int(input('Enter the number of passwords needed: '))
#choosing the length of your password
passlen = int(input('Enter password length: '))
#the characters that your password will have
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@$%&"
#takes the amount of passwords needed and then generates the length of the passwords
for p in range(numpass):
   password = ''
   for c in range(passlen):
      password += random.choice(chars)
    #prints the password
   print(password)
