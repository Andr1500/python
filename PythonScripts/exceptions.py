#catch exceptions fron the file
import sys  #import sys libary

filename = "user_names.txt"

while True:
    try:
      print("inside TRY block")
      myfile = open(filename, mode = 'r', encoding='utf_8')

    except Exception:
        print("inside Except block")
        print("here is an error!")
        print(sys.exc_info()[1])  #system command for info about the error, 1 in is for number of the error string
        filename = input("input correct file name: ")

    else:
        print("inside Else block")
        print(myfile.read())
        sys.exit()

    #finally:  #not necessary block
        #print("inside Finally block")
print("---EOF---")
