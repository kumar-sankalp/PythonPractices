#Coding Exercise 1
#Write a program that asks users to enter a password. Then, it checks if the password length is greater than 7 and returns "Great password there!".
#if the password has 7 or fewer characters, the program returns, "Your password is weak".

choice=input("Enter the pass: ")
if len(choice)>7:
    print("Great password there!")
elif len(choice) ==7:
    print("Pass is okay But not strong")
else:
    print("Your password is weak")
