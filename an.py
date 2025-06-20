import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('#262626')
t.pencolor('#540d6e')
t.speed(100)
col = ('#cc99ff', '#9933ff', '#6600cc', '#9900ff')

for n in range(5):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick()