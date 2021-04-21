from urllib import request, parse  #the lib for work with internet
import sys

myurl = "http://adv400.tripod.com/kartinka.jpg"

myfile = "/home/a1500/Downloads/picture1.jpg"

try:  #check for acception
        print("start downloading :")
        request.urlretrieve(myurl, myfile)

except Exception:
    print("not ok")
    print(sys.exc_info())
    exit

print("file downloaded at: " + myfile)