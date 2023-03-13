#Coding Exercise 1
filenames = ['document', 'report', 'presentation']

#Copy-paste the above list in a .py file and extend the code, so it prints out the output below:
#0-Document.txt
#1-Report.txt
#2-Presentation.txt

for i,item in enumerate(filenames):
    #print(i, item.capitalize())
    print(f"{i}-{item.capitalize()}.txt")


ips = ['100.122.133.105', '100.122.133.111', '100.122.8.111', '100.122.1.111', '100.122.133.181']

#Copy-paste the ips list in a .py file and extend the program so it:
#1. Prompts the user to input an index (e.g, 0 or 1).
#2. Returns the IP address that has that index.
#Here is how the program would behave when executed:
choice=int(input("Enter The IP you want at articular index"))
print(f" You Choose {ips[choice]}")

menu = ["pasta", "pizza", "salad"]
 
for i, j in enumerate(menu):
    print(f"{i}.{j}")

