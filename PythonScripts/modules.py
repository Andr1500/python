#import functions from another file

import modules1

# -------main body file-------
modules1.aaa()

modules1.bbb()

#or

from modules1 import *

#-------main body file-------
aaa()
bbb()