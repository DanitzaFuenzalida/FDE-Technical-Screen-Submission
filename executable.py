import numbers

# Declare function for sorting.
def sort(width, height, length, mass):

    # Error messages here before any calculations can occur.
    if (width == None or height == None or length == None or mass == None):
        print("ERROR: ONE OR MORE VALUES DOES NOT EXIST")
        return("ERROR: ONE OR MORE VALUES DOES NOT EXIST")

    if (isinstance(width, numbers.Number) == False or isinstance(height, numbers.Number) == False or isinstance(length, numbers.Number) == False or isinstance(mass, numbers.Number) == False):
        print("ERROR: ONE OR MORE VALUES IS NON NUMERICAL")
        return("ERROR: ONE OR MORE VALUES IS NON NUMERICAL")

    if (width <= 0 or height <= 0 or length <= 0 or mass <= 0):
        print("ERROR: ZERO OR NEGATIVE VALUE")
        return("ERROR: ZERO OR NEGATIVE VALUE")
    
    # Two possible boolean statuses
    bulky = False
    heavy = False

    # Check if packages are bulky or heavy.
    if((width * height * length) >= 1000000):
        bulky = True

    if(mass >= 20):
        heavy = True

    # Return different checks based on package weight and size.
    if(bulky and heavy):
        print("PACKAGE TYPE: REJECTED")
        return("REJECTED")

    if (bulky or heavy):
        print("PACKAGE TYPE: SPECIAL")
        return("SPECIAL")
    
    else:
        print("PACKAGE TYPE: STANDARD")
        return("STANDARD")