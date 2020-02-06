#집 그리기
import turtle
t = turtle.Turtle()
t.shape=("turtle")

size=int(input("집의 크기를 얼마로 할까요? ")) #이거 다시 해봐야 함 ㅠㅠㅠㅠ
t.goto(0,0)
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(30)
t.fd(size)
t.rt(120)  
t.fd(size)

#여기서부터는 현관을 만들자
t.up()
t.rt(120)
t.fd(size/4)
t.lt(90)
t.fd(size/4)
t.down()
t.fd(3*size/5)
t.rt(90)
t.fd(size/4)
t.rt(90)
t.fd(3*size/5)
t.rt(90)
t.fd(size/4)
