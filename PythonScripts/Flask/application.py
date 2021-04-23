from flask import Flask

application = Flask(__name__)

@application.route("/")

def index():
    return "<h2>in Flask main page</h2>"

@application.route("/help")
def help_page():
    return "<h2>Help Wiki contacts</h2>"

@application.route("/user")
def user_main_page():
    return "<h1>users main page</h1>"

@application.route("/user/<username>")  #the webpage for different users
def show_user_page(username):
    return "hello " + username.upper()

@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return  "subpath is: " + subpath

@application.route("/square/<int:x>") #the page for calc square of the digit
def calc_square(x):
    return "square of: " + str(x) + " = " + str(x*x)

@application.route("/htmlpage")
def show_html_page():
    my_file = open("mypage.html", mode='r')
    webpage = my_file.read()
    my_file.close()
    return webpage

#---main part---
if __name__ == "__main__":
#    application.debug = True  #comment for prod env
#    application.env = "staging"
    application.run()
#---------------