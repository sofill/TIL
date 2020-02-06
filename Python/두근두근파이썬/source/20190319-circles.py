Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Turtle()
>>> t.shape="turtle"
>>> t = turtle.Turtle()
>>> t.shape="turtle"
>>> t.shape("turtle")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t.shape("turtle")
TypeError: 'str' object is not callable
>>> t-turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t-turtle.Turtle()
TypeError: unsupported operand type(s) for -: 'Turtle' and 'Turtle'
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> t.circle(100)
>>> t.up()
>>> t.goto(50,50)
>>> t.goto(0,0)
>>> t.goto(100,0)
>>> t.down()
>>> t.circle(100)
>>> t.up()
>>> t.goto(200,0)
>>> t.down()
>>> t.circle(100)
>>> t.up()
>>> t.goto(200,-100)
>>> t.goto(100,-100)
>>> t.goto(150,-100)
>>> t.down()
>>> t.circle(100)
>>> t.up()
>>> t.goto(50,-100)
>>> t.down()
>>> t.circle(100)
>>> t.up
<bound method TPen.penup of <turtle.Turtle object at 0x0000020AA54756A0>>
(
>>> t.up()
>>> t.shape("classic")
>>> 
