
# app/my_script.py

#
# 1) At the top of the file, we import all the modules and third-party packages that contain the functionality we need:
#

import os
import random

from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv

#from app.my_mod import to_usd

#
# 2) After that, we generally run any setup code, like setting environment vars:
#

load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the package docs for more info

USER_NAME = os.getenv("USER_NAME", default="Player One") # uses the os module to read the specified environment variable and store it in a corresponding python variable

#
# 3) After that, we define any custom functions required by our program:
#

def enlarge(n):
    """
    This function enlarges a given number by 100.

    Params : n (integer or float) like 9 or 9.9
    """
    return n * 100

#
# Finally, at the bottom, we write code to perform the desired functionality:
#

print("-------------------")
print("WELCOME TO MY APP!")
print(f"PLAYER: '{USER_NAME}'")

print("-------------------")
print("EXAMPLE USAGE OF VARS AND FUNCTIONS...")
x = 5
result = enlarge(x)
print(result)
#formatted_result = to_usd(result)
#print(formatted_result)
