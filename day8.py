#A client wants to buy a coin-flip probability program from you.
#The programs should work like this:
#1. The user runs the program. The program asks the user to enter "head" or "tail".  
#The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail". The user does the same over and over again.
#In each cycle, the program should return the current percentage of heads in the program, similar to what you see in the screenshot above. 
#Also, you should write each user entry (i.e., head or tail) in a text file using a with-context manager, one entry per line.
h_count=0
t_count=0
def count_head():
    global h_count
    with open("/Users/kumarsankalp/Downloads/PythonPractice/PythonPractices/files/file.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if line in "head":
                h_count += 1
        return int(h_count)
def count_tail():
    global t_count
    with open("/Users/kumarsankalp/Downloads/PythonPractice/PythonPractices/files/file.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if line in "tail":
                t_count += 1
        return int(t_count)
    

user_input=input("Throw the coin and enter head or tail: here: ? ")
print(user_input)
user_input=user_input + "\n"

with open("/Users/kumarsankalp/Downloads/PythonPractice/PythonPractices/files/file.txt", 'r') as file:
     existing_result=file.readlines()
     print(existing_result)
     existing_result.append(user_input)
     print(existing_result)

with open('/Users/kumarsankalp/Downloads/PythonPractice/PythonPractices/files/file.txt', 'w') as file:
    existing_result=file.writelines(existing_result)
    print(existing_result)

h_count=count_head()
t_count=count_tail()
print(f"count of head is {h_count}")
print(f"count of tail is {t_count}")
print(f"percentage of head is {h_count/float(h_count+t_count)*100}")