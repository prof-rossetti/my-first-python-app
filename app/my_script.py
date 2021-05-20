
# this is the "app/my_script.py" file...

#
# 1) At the top of the file, we import some helpful functionality, as desired:
# ... from built-in Python modules like the "os" module (do not require separate installation),
# ... from third-party packages like the "python-dotenv" package (requires separate installation, see "requirements.txt" file),
# ... and from from other local files like the "app/my_mod.py" file
#

import os
from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv
#from app.my_mod import calculate_rectangle_area

#
# 2) After that, we generally run any setup code, like setting environment variables:
#

load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the "python-dotenv" package docs for more info

USER_NAME = os.getenv("USER_NAME", default="Player One") # uses the os module to read the specified environment variable and store it in a corresponding python variable
SECRET_PASSWORD = os.getenv("SECRET_PASSWORD") # uses the os module to read the specified environment variable and store it in a corresponding python variable

#
# 3) After that, we define any additional custom functions required by our program:
#

def enlarge(n):
    """
    This function enlarges a given number by 100.

    Params : n (integer or float) like 9 or 9.9
    """
    return n * 100

#
# Finally, at the bottom, we write code to perform the desired functionality.
#
# If we don't need to import any functions from this file to other files:
# ... we can keep the functionality on the left margin, in the global scope (as it is right now).
#
# Otherwise if we need to import functionality from this file to other files:
# ... we'd need to nest this code under the "main conditional" (see "app/my_mod.py")
#

print("-------------------")
print("WELCOME TO MY APP!")
print(f"PLAYER: '{USER_NAME}'")
print(f"PASSWORD: '{SECRET_PASSWORD}'")

print("-------------------")
print("ENLARGE FUNCTION INVOCATION EXAMPLE...")
x = 5
result = enlarge(x)
print(x, "becomes...", result)

#print("-------------------")
#print("AREA FUNCTION INVOCATION EXAMPLE...")
#l = 6
#w = 4
#area = calculate_rectangle_area(l,w)
#print("L:", l, "W:", w, "AREA:", area)
