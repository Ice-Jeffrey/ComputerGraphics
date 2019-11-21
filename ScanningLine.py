import turtle
from math import sqrt

def drawpixel(x, y, color = 'red'):
    turtle.pencolor(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.dot(3)

class Node:
    def __init__(self, x = None, y = None, deltax = None, ymax = None):
        self.x = x
        self.y = y
        self.deltax = deltax
        self.ymax = ymax
        self.next = None
    
class SLinkedList:
    def __init__(self, node = None):
        self.head = node
        self.capacity = 0
    
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
    
    #初始化新边表
    net = {}
    for y in range(ymin, ymax + 1):
        net[y] = []

    #初始化各条边
    for i in range(len(points)):
        index1 = i
        index2 = (i+1) % len(points)
        y1 = min(points[index1][1], points[index2][1])
        y2 = max(points[index1][1], points[index2][1])
        if y1 == points[index1][1]:
            x1 = points[index1][0]
            x2 = points[index2][0]
        else:
            x1 = points[index2][0]
            x2 = points[index1][0]
        delta = (x2 - x1) / (y2 - y1)
        net[y1].append(Node(x1, y1, delta, y2))

    #开始扫描并建立活性边表
    aet = SLinkedList(Node())
    for y in range(ymin, ymax + 1):
        print(y)
        #将新边表中的各个节点按照x递增的顺序插入活性边表中
        for i in range(len(net[y])):
            data = net[y][i]
            node = aet.head
            if node.next == None:
                node.next = data
            else:
                while data.x > node.next.x:
                    node = node.next
                data.next = node.next
                node.next = data

        #寻找涂色区间
        points = []
        node = aet.head
        while node.next != None:
            ymin = node.next.y
            ymax = node.next.ymax
            if y > ymin and y < ymax:
                points.append(node.next.x)
            elif y == ymin and y < ymax:
                points.append(node.next.x)
                points.append(node.next.x)
            elif y == ymax and y > ymin:
                points.append(node.next.x)
            node = node.next
        points = sorted(points)
        
        #进行涂色
        for i in range(0, len(points), 2):
            x1 = points[i]
            x2 = points[i+1]
            for x in range(int(x1), int(x2)):
                drawpixel(x, y)

        #遍历aet表进行测试
        node = aet.head
        while node != None:
            node = node.next

        #遍历aet，把ymax = i的节点从aet删除，并把ymax > i结点的x值递增deltax
        node = aet.head
        while node.next != None:
            if node.next.ymax == y:
                node.next = node.next.next
            else:
                node.next.x = node.next.x + node.next.deltax
                node = node.next
                

if __name__ == "__main__":
    turtle.pencolor('red')
    turtle.hideturtle()
    turtle.speed(0)
    turtle.screensize(800, 600, 'white')
    main()
    turtle.mainloop()