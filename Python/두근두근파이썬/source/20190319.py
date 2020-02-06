import turtle

colors = ["red", "purple", "skyblue", "green", "yellow", "orange", "white", "brown", "khaki"]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(10)
t.width(3)
length = 1

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%9])
    t.right (89)
    length += 5
