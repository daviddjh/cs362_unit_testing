

def add(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a + b 
    else:
        raise TypeError("Only Numbers Allowed")


def subtract(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a - b 
    else:
        raise TypeError("Only Numbers Allowed")

def divide(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if b == 0:
            raise ValueError("Can't Divide By Zero")
        else:
            return a / b 
    else:
        raise TypeError("Only Numbers Allowed")

def multiply(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a * b 
    else:
        raise TypeError("Only Numbers Allowed")