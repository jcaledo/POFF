def get_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = get_gcd(b, a%b)
    x = y1
    y = x1 - (a//b) * y1
    print(f"x1 = {x1}, y1 =  {y1}")
    return gcd, x, y

print (f"The result is: {get_gcd(7,5)}")
