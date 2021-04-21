from  urllib import request

myurl = "http://www.astahov.net"

answer = request.urlopen(myurl)

mytext1 = answer.readlines()
mytext2 = answer.read()

print(answer)
print(mytext2)

for line in mytext1:
    print(line)


