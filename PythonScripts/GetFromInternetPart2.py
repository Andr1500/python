from urllib import request, parse  #the lib for work with internet
import sys

myurl = "http://www.google.com/search?"

value = {'q': 'ANDESA Soft'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'
#for the way for acceptin the request by google we need to add value about user agent, it is fron some
#site, page 'Network', the column 'Headers'

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myurl = myurl + mydata
    req = request.Request(myurl, headers=myheader)
    answer = request.urlopen(req)
    answer = answer.readlines()
    for line in answer:
        print(line)

except Exception:
    print("error in web request:")
    print(sys.exc_info()[1])