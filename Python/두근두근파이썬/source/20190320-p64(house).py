#집 그리기
import turtle
t = turtle.Turtle()
t.shape=("turtle")

size=int(input("집의 크기를 얼마로 할까요? ")) #이거 다시 해봐야 함 ㅠㅠㅠㅠ
t.goto(0,0)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(30)
t.fd(100)
t.rt(120)  #후, 이 각도 찾는 게 힘들었다... 
t.fd(100)

#이거 틀렸다.  size 변수를 사용하지 않고 그냥 그렸잖아... 으이구... 다른 파일에서 다시 해 보자. 
