Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print(2*3/10)
0.6
>>> print("hello","world","!!!")
hello world !!!
>>> import turtle
>>> t=turtle.Turtle()
>>> t.shape(turtle)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t.shape(turtle)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named <module 'turtle' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\turtle.py'>
>>> t.shape(Turtle)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t.shape(Turtle)
NameError: name 'Turtle' is not defined
>>> t.shape("turtle")
>>> t.fd(100)
>>> t.lt(90)
>>> t.fd(100)
>>> t.rt(90)
>>> t.fd(100)
>>> t.rt(90)
>>> t.fd(100)
>>> t.lt(90)
>>> t.fd(100)
>>> t.width(5)
>>> t.lt(90)
>>> t.fd(100)
>>> t.width(10)
>>> t.lt(90)
>>> t.fd(100)
>>> t.rt(90)
>>> t.fd(100)
>>> t.fd(100)
>>> t.color("blue")
>>> t.lt(90)
>>> t.fd(100)
>>> t.shape("square")
>>> t.shape("round")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    t.shape("round")
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named round
>>> t.shape("circle")
>>> t.shape("arrow")
>>> t.shape("triangle")
>>> t.shape("classic")
>>> t.shape("arrow")
>>> 
