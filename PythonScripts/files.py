

inputfile = "list_of_passwords.txt"  #variable with the path to my file, in the same directory as another files
outputfile = "my_passwords.txt"

password_to_look_for = "sparky"

myfile1 = open(inputfile, mode='r', encoding='utf_8') #mode r is for read
myfile2 = open(outputfile, mode='a', encoding='utf_8')  #a is for append,
#myfile2 = open(outputfile, mode='w', encoding='utf_8')  #w is for write,

#print(myfile.read())  #printing all data in the file

for num, line in enumerate(myfile1, 1):  #Enumerate() method adds a counter(start from 1)
    if password_to_look_for in line:  #print only lines with necessary parameters
        print("Line N:" + str(num) + " " + line.strip()) #strip is for cutting everything in the end of file
        myfile2.write("found password: " + line)

myfile1.close()
myfile2.close()

