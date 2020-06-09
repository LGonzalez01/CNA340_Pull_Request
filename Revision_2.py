#Revision 2 


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

lone_sum(a, b, c)
print(lone_sum(a, b, c))