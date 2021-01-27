
# app/my_mod.py

#
# We can define custom functions in a separate file (like this one), and import and use these functions in other Python files (like my_script.py).
# The spreading of functionality into logically-related modules helps us stay organized when our apps become really big.
#

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#
# If we import functions from a file like this, it will be important to ensure this file contains no code in its global scope.
# In other words, all code in this module file should be contained within other stand-alone functions.
#
# Otherwise, if you were to uncomment the block of code below, save this file, and then re-run the my_script.py file,
# ... you'll see this code breaks our ability to import from other files.
#
# y = int(input("Please choose a number"))
# print(y, enlarge(y))

#
# To overcome this limitation, if we nest the same block of code inside a special conditional called if __name__ == "__main__"
# ... then it will allow us to cleanly import the function from other files
# ... while simultaneously allowing us to run this script to perform its own functionality:
#
#if __name__ == "__main__":
#    #
#    # This conditional basically says "only run the code below if this script is invoked from the command-line"
#    # ... (but not if it is imported from another script)
#    # For more information, see: https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts
#
#    y = int(input("Please choose a number: "))
#    print(y, to_usd(y))
