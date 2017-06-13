#Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function.
# Complete the test to produce the perfect function that accounts for all expectations.
#For strings, return its length.
#For None return string 'no value'
#For booleans return the boolean
#For integers return a string showing how it compares to hundred e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
#For lists return the 3rd item, or None if it doesn't exist



def data_type(param):
    if type(param) == str:
        return len(param)
    elif param is None:
        return 'no value'
    elif type(param) == bool:
        return param
    elif type(param) == int:
        if param < 100:
            return 'less than 100'
        elif param > 100:
            return 'more than 100'
        else:
            return 'equal to 100'
    else:
        if type(param) == list:
            if len(param) < 3:
                return None
            else:
                return param[2]