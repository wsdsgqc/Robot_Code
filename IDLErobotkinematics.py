Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from graphics import * 
win = graphics.GraphWin('RobotKinematicsSimulation',500,500)
x1 = 10
y1 = 10
x2 = 10
y2 = 10
link1 = Line(Point(250,450),Point(x1,y1))
SyntaxError: multiple statements found while compiling a single statement
>>> imo graphics
win = graphics.GraphWin('RobotKinematicsSimulation',500,500)
x1 = 10
y1 = 10
x2 = 10
y2 = 10
link1 = Line(Point(250,450),Point(x1,y1))
