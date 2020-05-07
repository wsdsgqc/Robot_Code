#from graphics import *
#import math
import matplotlib.pyplot as plt
import numpy as np

# baseX = 250
# baseY = 450
# win = GraphWin('RobotKinematicsSimulation',500,500)

# def Ik(L1,L2,x0,y0,select):
#     if L1+L2 < math.sqrt(x0**2+y0**2):
#         return 0,0
#     seta2 = math.acos((L1**2+L2**2-(x0**2+y0**2))/(2*L1*L2))
#     seta2 = math.pi-seta2
#     beta = math.atan2(y0,x0)
#     pesai = math.acos((x0**2+y0**2+L1**2-L2**2)/(2*L1*math.sqrt(x0**2+y0**2)))
#     if select == 1:
#         seta1 = beta + pesai
#         return seta1,-seta2
#     elif select == 2:
#         seta1 = beta - pesai
#         return seta1,seta2

# def rad2deg(rad):
#     return rad*(180/math.pi) 
# def deg2rad(deg):
#     return deg*(math.pi/180)
# def trajectoryGeneration():
#     a = 13
#     b = 13
#     c = 13
#     generater = []
#     for iter in range(0,256):
#         generater.append(-a*iter**2+b*iter+c)
#     return generater
Generator = []
a_s = 0.000244
b_s = -0.031232
c_s = 0
a_f = -0.000488
b_f = 0.186416   # b/(-2a) = 中线 = 192
c_f = -15.80388    # a = 0.001 b = 192*0.001*2

X1 = np.linspace(0,127,128)
X2 = np.linspace(128,255,128)

standPhase  = a_s*X1**2+b_s*X1+c_s
plt.plot(X1,standPhase) 
flyingPhase = a_f*X2**2+b_f*X2+c_f
plt.plot(X2,flyingPhase)

plt.show()
# print(trajectoryGeneration())