names = ["john smith", "jay santi", "eva kuki"]

#Extend the code above so the code capitalizes all the names and the surnames of the list and then prints the new list.

#The output of your code should be as below:
#['John Smith', 'Jay Santi', 'Eva Kuki']
new_names=[]
for item in names:
    item = item.capitalize()
    new_names.append(item)
print(new_names)

usernames = ["john 1990", "alberta1970", "magnola2000"]

#Extend the code above so the code prints out a list containing the number of characters for each username.
#The output of your code should be as below:
#[9, 11, 11]
new_usernames=[]
for items in usernames:
    new_usernames.append(len(items))
print(new_usernames)

user_entries = ['10', '19.1', '20']
#Extend the code above so the code prints out a list containing the same items as floats.
#The output of your code should be as below:
#[10.0, 19.1, 20.0]
new_user_entry=[]
for i in user_entries:
    new_user_entry.append(float(i))
print(new_user_entry)    
