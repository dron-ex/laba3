import math

sum = float(0)
b = 0
a = float(10)
while b < 8:
    b +=1
    sum = sum + a
    a = a + a/10
    if b == 7:
      break
print("S = ", sum)
