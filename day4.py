#Coding Exercise 1
# Create a program that:
# 1. Prompts the user to input a (dollar) amount.
# 2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.
# 3. Prints out the amount in euros, as shown in the screenshot below.

doll=float(input("how many dollar you got : "))
euro=0.95*doll
print("The amount of euro is "+ str(euro) )


#The list below represents the ranking of three athletes. John won 1st place, Sen got 2nd, and Lisa the 3rd.
# ranking = ['John', 'Sen', 'Lisa']
# Create a program that:
# 1. Contains the above list.
# 2. Prompts the user to input a rank number.
# 3. Returns the person who has the given rank.

ranking = ['John', 'Sen', 'Lisa']
choice= int(input("enter the rank "))
print(ranking[choice-1])

#This time you need to create a program that:
# 1. Contains the above list.
# 2 Prompts the user to input the person's name.
# 3. Returns the rank that person has.
p_name=input("enter the person name ")
rank=ranking.index(p_name)
print(rank+1)








