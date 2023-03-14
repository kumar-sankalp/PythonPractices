#Please read the essay.txt file from the resources of this article. Then, create a program that reads that file and prints out its text. 
#The first letter of each word in the output should be uppercase.

file1= open("essay.txt","r")
i=file1.read()
print(i.title())
file1.close()

#Write a program that reads the essay.txt file and returns the number of characters contained in the file.
file1= open("essay.txt","r")
i=file1.read()
print(len(i))

#Please download the members.txt file from the resources of this article.
#Then, create a program that, whenever executed, asks the user to enter a new member in the command line:
#Then, the member is added to members.txt. In this case, the text file content would be:
#John Smith
#Sen Lakmi
#Sono Octonot
#Solomon Right
member = input("Add a new member: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()

#Please download the three text files a.txt, b.txt, and c.txt from the resources. 
# Then, create a program that reads each text file and prints out the content of each in the command line. 
# The expected output would be like the following:
# I am a 
# I am b
# I am c 
filename=['a.txt','b.txt','c.txt']
for item in filename:
    file1= open(f"{item}","r")
    i=file1.readlines()
    print(i)
    file1.close()

