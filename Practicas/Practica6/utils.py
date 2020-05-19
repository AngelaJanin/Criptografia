def prime_relative(a, b):
    if(b == 0):
        return a == 1
    else:
        return prime_relative(b, a%b)
