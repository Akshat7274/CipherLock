import random

def primitiveRoot(num):
    rts = []
    for i in range(2,num):
        dgs =[]
        x = 0
        while (len(dgs)!=num):
            calc = (i ** x) % num
            if (calc not in dgs):
                dgs.append(calc)
            else:
                break
            x += 1
        if (len(dgs)==num-1):
            rts.append(i)
    return rts

def gcd(x,y):
    if (y==0):
        return x
    else:
        return gcd(y,x%y)

def inverse(num,mod):
    m = mod
    y = 0
    x = 1

    while (num>1):
        q = num//mod
        t = mod
        mod  = num%mod
        num = t
        t = y

        y = x - q * y
        x = t
    if (x<0):
        x += m

    return x