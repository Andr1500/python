import re  #import the libary for reg expressions

mytext = "Vasia 2910, Kolia - 1990: Oleh 2010 a@mail.com," \
         "fhgyfhjjhk.dhdhfh@gmail.com, Vova bdtrr, 1317, asfgfgdb@mail.lp, "

"""
\d  - any digit 0-9
\D  - any non digit
\w  - any alphabet symbol [a-z A-Z]
\W  - any non alphabet symbol
\s  - break space
\S  - non break space
[0-9]{4} - searching 4 digits
[A-Z][a-z]+  - 1 is capital leter, next is non capital leter plus all leters
\w+\.\w+@\w+\.\w+  - template for searchng emails

Best Regular Expression for email addresses: 
email_address  = r"[\w._-]+@[\w._-]+\.[\w.]+"

https://regex101.com/​   Cайт для тренировки и составления Регулярных Выражений
http://www.generatedata.com/​   Сайт генератор демо данных

"""
textlookfor = r"mail"  #the template for searching all words contain "mail"
allresults = re.findall(textlookfor, mytext)
print(allresults)

textlookfor = r"\d\d\d\d"  #the template for searching 4 digits one by one
allresults = re.findall(textlookfor, mytext)
print(allresults)

textlookfor = r"[0-9]{4}"  #the template for searching 4 digits one by one
allresults = re.findall(textlookfor, mytext)
print(allresults)

textlookfor = r"[A-Z][a-z]+"  #the template for searching names
allresults = re.findall(textlookfor, mytext)
print(allresults)

textlookfor = r"\w+\.\w+@\w+\.\w+"  #the template for searching emails
allresults = re.findall(textlookfor, mytext)
print(allresults)

input_filename = "dumpfile.txt"  #the template for searching email from the file
result_filename = "emails.txt"

inputfile = open(input_filename, mode='r', encoding='ASCII')
resultfile = open(result_filename, mode='w', encoding='ASCII')
mytext = inputfile.read()

lookfor = r"[\w._-]+@(?!nokia.com)[\w._-]+\.[\w.]+"  #(?!nokia.com) - is for excluding emails with this info

results = re.findall(lookfor, mytext)

for email in results:  #print all emails which we are looking for
    print(email)
    resultfile.write(email + "\n")  #write necessary emails in the file

print("Total emails: " + str(len(results)))  #print how much emails do we have
