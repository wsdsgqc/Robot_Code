import matplotlib.pyplot as plt
import numpy as np
from graphics import *
import time
import math
baseX = 250
baseY = 450
shifter = 0
win = GraphWin('RobotKinematicsSimulation',500,500)
def appreance():
    p1 = Point(230,440)
    p2 = Point(270,440)
    p3 = Point(230,460)
    p4 = Point(270,460)
    polygon = Polygon(p1,p2,p4,p3)
    polygon.draw(win)
    polygon.setFill("red")
    polygon.setOutline('black')
def trajectoryGeneration():
    Generator = []
    a_s = 0.000244
    b_s = -0.031232
    c_s = 0
    a_f = -0.000488
    b_f = 0.186416   # b/(-2a) = 中线 = 192
    c_f = -15.80388    # a = 0.001 b = 192*0.001*2
    X1 = np.linspace(0, 127, 128)
    X2 = np.linspace(128, 255, 128)

    standPhase = a_s*X1**2+b_s*X1+c_s
    flyingPhase = a_f*X2**2+b_f*X2+c_f
    #plt.plot(X1, standPhase)
    #plt.plot(X2, flyingPhase)
    #plt.show()
    return standPhase,flyingPhase
    
#return value in deg 根据书上几何解内容编写
def Ik(L1,L2,x0,y0,select):
    if L1+L2 < math.sqrt(x0**2+y0**2):
        return 0,0
    seta2 = math.acos((L1**2+L2**2-(x0**2+y0**2))/(2*L1*L2))
    seta2 = math.pi-seta2
    beta = math.atan2(y0,x0)
    pesai = math.acos((x0**2+y0**2+L1**2-L2**2)/(2*L1*math.sqrt(x0**2+y0**2)))
    if select == 1:
        seta1 = beta + pesai
        return seta1,-seta2
    elif select == 2:
        seta1 = beta - pesai
        return seta1,seta2

def rad2deg(rad):
    return rad*(180/math.pi) 
def deg2rad(deg):
    return deg*(math.pi/180)

def drawLeg():
    link1length = 100 
    link2length = 100
    standPhase,flyingPhase = trajectoryGeneration()
    for i in range(0,256):
        if i < 128:
            seta1,seta2 = Ik(link1length, link2length,i-shifter,10*standPhase[i], 1)#因为要输入长度,所以减去基坐标
            if seta1 == 0 and seta2 == 0:
                print("out of range cannot reach the point")
            else:
                print("Works fine:%d"%i)
            x1 = link1length*math.cos(seta1) #使用增量  未用实际量
            y1 = math.sqrt(link1length**2-x1**2)
            x2 = link2length*math.cos(seta1+seta2)#
            y2 = math.sqrt(link2length**2-x2**2)
            link1 = Line(Point(baseX,baseY),Point(x1+baseX,baseY-y1))
            link2 = Line(Point(x1+baseX,baseY-y1),Point(baseX+x1+x2,baseY-y1-y2))

            link1.draw(win)
            link2.draw(win)
            time.sleep(0.01)
            if i < 127:
                link1.undraw()
                link2.undraw()
        if i >= 128:
            seta1,seta2 = Ik(link1length, link2length,256-i-shifter,10*flyingPhase[i-128], 2)#因为要输入长度,所以减去基坐标
            if seta1 == 0 and seta2 == 0:
                print("out of range cannot reach the point")
            else:
                print("Works fine:%d"%i)
            x1 = link1length*math.cos(seta1) #使用增量  未用实际量
            y1 = math.sqrt(link1length**2-x1**2)
            x2 = link2length*math.cos(seta1+seta2)#
            y2 = math.sqrt(link2length**2-x2**2)
            link1 = Line(Point(baseX,baseY),Point(x1+baseX,baseY-y1))
            link2 = Line(Point(x1+baseX,baseY-y1),Point(baseX+x1+x2,baseY-y1-y2))

            link1.draw(win)
            link2.draw(win)
            time.sleep(0.01)
            if i < 255:
                link1.undraw()
                link2.undraw()
    win.getMouse()
    win.close()
appreance()
drawLeg()
