import numpy as np
import turtle
from math import *

class Edge:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

def drawpixel(x, y, color = 'red'):
    turtle.pencolor(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.dot(3)

def BresenhamLine(x0, y0, x1, y1, color = 'red'):   #用中点画线法画出椭圆的各条边
    dx = x1 - x0
    dy = y1 - y0
    e = -dx
    x = x0
    y = y0
    i = 0
    while i <= dx:
        drawpixel(x, y, color)
        x += 1
        e += 2 * dy
        if e >= 0:
            y += 1
            e -= 2 * dx
        i += 1

def PointstoEdges(points): #根据各个点转化成各条边
    edges = []
    for i in range(len(points)):
        index1 = i
        index2 = (i + 1) % len(points)
        if points[index1][0] < points[index2][0]:
            x0 = points[index1][0]
            y0 = points[index1][1]
            x1 = points[index2][0]
            y1 = points[index2][1]
        else:
            x0 = points[index2][0]
            y0 = points[index2][1]
            x1 = points[index1][0]
            y1 = points[index1][1]
        edges.append(Edge(
            x0, y0, x1, y1
        ))
    return edges

def main():
    # 输入六边形的六个顶点坐标
    points = []
    ymin = 1000
    ymax = -1000
    print("请按照x递增的顺序顺时针依次输入六边形六个顶点的坐标：")
    for i in range(6):
        x, y = input().split()
        x = int(x)
        y = int(y)
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
        points.append([x, y])
    print(points)

    #将六边形的顶点转换成各条边
    edges = PointstoEdges(points)
    print(edges)
    
    #画出六边形
    for edge in edges:
        x0 = edge.x0
        y0 = edge.y0
        x1 = edge.x1
        y1 = edge.y1
        print(x0, y0, x1, y1)
        BresenhamLine(x0, y0, x1, y1)

    #将各条边转化成以指定点为起点的齐次向量，并直接进行旋转
    x_original, y_original = input("请输入指定点的坐标：").split()
    theta = int(input("请输入指定的角度："))
    rotation_array = np.array([cos(theta), sin(theta), 0, -sin(theta), cos(theta), 0, 0, 0, 1]).reshape(3, 3)
    for point in points:
        point[0] -= int(x_original)
        point[1] -= int(y_original)
        point.append(1)
        point = np.array(point).dot(rotation_array)
        point[0] += int(x_original)
        point[1] += int(y_original)
        point = list(point)
        point.pop()
        print(point)

    print(points)
    #将六边形的顶点转换成各条边
    edges = PointstoEdges(points)
    print(edges)
    
    #画出六边形
    for edge in edges:
        x0 = edge.x0
        y0 = edge.y0
        x1 = edge.x1
        y1 = edge.y1
        print(x0, y0, x1, y1)
        BresenhamLine(x0, y0, x1, y1, 'blue')

    
if __name__ == "__main__":
    turtle.pencolor('red')
    turtle.hideturtle()
    turtle.speed(0)
    turtle.screensize(800, 600, 'white')
    main()
    turtle.mainloop()