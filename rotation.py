import numpy as np
import cv2
from math import *

def rotate(points):
    #输入旋转点和旋转角度
    x_original, y_original = input("请输入指定点的坐标：").split()
    theta = int(input("请输入指定的角度："))

    #初始化旋转矩阵
    rotation_array = np.array([cos(theta), sin(theta), 0, -sin(theta), cos(theta), 0, 0, 0, 1]).reshape(3, 3)

    #开始旋转
    new_points = []
    for point in points:
        #将该点转换成向量
        point[0] -= int(x_original)
        point[1] -= int(y_original)

        #坐标转换为齐次坐标
        point.append(1)

        #进行旋转
        point = np.array(point).dot(rotation_array)

        #旋转后的向量转化为坐标
        point = list(point)
        point[0] = int(point[0] + int(x_original))
        point[1] = int(point[1] + int(x_original))

        #将齐次坐标变为正常坐标
        point.pop()
        new_points.append(point)
    
    return new_points

def draw(points):
    # 初始化一个空画布 1000×500 三通道 背景色为白色
    col = 1500
    row = 800
    canvas = np.ones((row, col, 3), dtype="uint8")
    canvas *= 255
    
    # 点集矩阵变形
    points = np.array(points)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(canvas, pts=[points], isClosed=True,color=(0, 0, 0), thickness=2)
    cv2.imshow("polylines", canvas)
    cv2.waitKey(0)

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
    
    # 画出旋转前的六边形
    draw(points)

    #对六边形进行旋转
    points = rotate(points)
    
    #画出旋转后的六边形
    draw(points)    
    
if __name__ == "__main__":
    main()