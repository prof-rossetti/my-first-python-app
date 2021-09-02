
# this is the "app/my_mod.py" file...

#
# We can define custom functions in a separate file (like this one),
# ... and import these functions into other Python files (like my_script.py).
#
# The spreading of functionality into logically-related modules helps us stay organized when our apps become really big.
#

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"


def calculate_rectangle_area(length, width):
    """
    Computes the area of a rectangle, given its length and width.

    Params:
        length (int or float) like 10
        width (int or float) like 3

    Examples:
        calculate_rectangle_area(10, 3)
        calculate_rectangle_area(length=10, width=3)
        calculate_rectangle_area(width=3, length=10)
    """
    return length * width


def calculate_triangle_area(base, height):
    """
    Computes the area of a triangle, given its base and height.

    Params:
        base (int or float) like 8
        height (int or float) like 6

    Examples:
        calculate_triangle_area(8, 6)
        calculate_triangle_area(base=8, height=6)
        calculate_triangle_area(height=6, base=8)
    """
    return 0.5 * base * height


if __name__ == "__main__":
    #
    # This weird "main conditional" basically says:
    # ... "only run the code below if this file is run from the command-line".
    #
    # Placing code here (instead of the global scope where the functions are defined) 
    # ... prevents that code from being executed when other Python files import from this file.
    #
    # For more information, see: https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts
    #
    
    y = int(input("Please choose a number: "))
    print(y, to_usd(y))
