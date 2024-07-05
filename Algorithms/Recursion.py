# Factorial
def fact(var):
    if var == 0:
        return 1
    else:
        return var * fact(var-1)
