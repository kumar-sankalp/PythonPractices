#Build a percentage calculator that gets from the user the "total value" and the 
#"value" and returns the percentage as shown below:
#The program should also print a message if the user doesn't enter a number for the "total value or for the "value":

try:
    value=float(input("Enter Value :"))
    total_value=float(input("Enter Total value :"))
    print(f"That is :{(value/total_value)*100}")
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:    
    print("Your Total value cannot be zero")