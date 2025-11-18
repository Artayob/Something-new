import math
import turtle

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) \
           - 5 * math.cos(2 * k) \
           - 2 * math.cos(3 * k) \
           - math.cos(4 * k)

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.penup()

for i in range(5000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    t.goto(x, y)
    t.dot(5, "pink")   # safer than color()+dot()

t.goto(0, 0)

turtle.done()