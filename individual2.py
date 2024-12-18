import math


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if math.fabs(a) >= 4 and math.fabs(b) >= 4 and math.fabs(c) >= 4:
    print(a, ",", b, ",", c)
elif math.fabs(a) >=4 and math.fabs(b) >=4:
    print(a, ",", b)
elif math.fabs(a) >=4 and math.fabs(c) >=4:
    print(a, ",", c)
elif math.fabs(b) >=4 and math.fabs(c) >=4:
    print(b, ",", c)
elif math.fabs(a) >=4:
    print(a)
elif math.fabs(b) >=4:
    print(b)
elif math.fabs(c) >=4:
    print(c)

else:
    print("all <4")
