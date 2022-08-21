import turtle
import math
bob = turtle.Turtle()
print(bob)

"""
for i in range(4):
    bob.fd(100)
    bob.lt(90)
    
turtle.mainloop()
"""
def square(t,length):
    for i in range(4):
        bob.fd(length)
        bob.lt(length)


def polygon(t,length,n):
    angle = 360/n
    for i in range(n):
        bob.fd(length)
        bob.lt(angle)


def circle(t,r):
    circumference = 2*math.pi*r
    n=int(circumference/3)+1
    length = circumference/n
    polygon(t,n,length)


circle(bob,100)
turtle.mainloop()
