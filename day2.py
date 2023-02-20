#Coding Exercise 1
#Create a program that prompts the user to input their name once. 
# Then, the program prints out the name once with the first letter capitalized.

name1=input("Enter Your Name :")
print(name1.title())

#CCreate a program that prompts the user to input their name repeatedly. 
# Then, the program repeatedly prints out the name with the first letter capitalized.

i='y'
while i in ('yes' ,'y'):
    name2=input('Enter Your Name : ')
    print(name2.title())
    i=input('Do you want to enter your name again?(yes or no)')


countries = []
 
 #testing list 
while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)

