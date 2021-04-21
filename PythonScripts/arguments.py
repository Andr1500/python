import sys  #import system libary

import os  #import os libary

print("hi")

print(sys.argv[1:])  #import array to the program, 1 element is the name of the file
                    #python3 arguments.py help  - request from the console


x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "help":
        print("help is requested")
    print("arguments:" + str(sys.argv[1:]))
else:
    print("arguments don't provided")

os.system("ls -la")