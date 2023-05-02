import random
import sympy

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