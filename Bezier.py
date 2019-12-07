import numpy as np
from PIL import ImageDraw, Image

def Bezier(points, t):
    n = len(points) - 1
    p = []
    for k in range(n+1):
        p.append([])
    for k in range(n + 1):
        if k == 0:
            for i in range(n + 1):
                p[i].append(points[i])
            continue
        for i in range(n - k + 1):
            p[i].append([
                (1 - t) * p[i][k-1][0] + t * p[i+1][k-1][0],
                (1 - t) * p[i][k-1][1] + t * p[i+1][k-1][1],
            ])
    
    return p[0][n]

def main():
    points = []
    print("请按照x递增的顺序顺时针依次输入六边形六个顶点的坐标：")
    for i in range(6):
        x, y = input().split()
        x = int(x)
        y = int(y)
        points.append([x, y])
    points.append(points[0])
    

    array = np.ndarray((480, 640, 3), np.uint8)
    array[:, :, :] = 255
    image = Image.fromarray(array)
    draw = ImageDraw.Draw(image)
    for i in range(len(points) - 1):
        draw.line((points[i][0], points[i][1], points[i+1][0], points[i+1][1]), 'black')

    ts = np.linspace(0, 1, 10000)
    for t in ts:
        point = Bezier(points, t)
        draw.point(point, fill = 'red')
    image.show()    


if __name__ == "__main__":
    main()    