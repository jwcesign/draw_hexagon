# -*- coding:utf-8 -*-
#author :muweiqian 2016.06.23
#绘制蜂窝正六边形图片
import turtle
n = 20 #m边型每条边的长度
m = 10 #第几圈
turtle.speed(100000)
for t in range(m+1):
        for p in range(6):
             for q in range(t+1):
                turtle.dot(n / 4, "blue") #中心点的大小
                turtle.up()
                turtle.seth(- 60 * p + 60)
                turtle.fd(n)
                turtle.down()
                turtle.rt(120)
                for i in range(6):
                    turtle.color("black")
                    turtle.fd(n)
                    turtle.rt(60)
                turtle.up()
                turtle.seth(-120-60*p)
                turtle.fd(2 * n)
                turtle.rt(60)
                turtle.fd(n)
                turtle.down()
             turtle.up()
             turtle.rt(120)
             turtle.fd(n)
             turtle.left(60)
             turtle.fd(n)
        turtle.up()
        turtle.seth(0)
        turtle.fd(n)
        turtle.seth(-60)
        turtle.fd(n)
        turtle.down()

