#Revision 1 
#Added print statements and variables






def lone_sum(a, b, c):
    if a >= b:
      return c
    elif a == c:
      return b
    elif b == c:
      return a
    elif a == b and a == c and b == c:
      return 0
    else:
      return a + b + c

a = int(input())
b = int(input())
c = int(input())

print('{} {} {}'.format(a, b, c))

