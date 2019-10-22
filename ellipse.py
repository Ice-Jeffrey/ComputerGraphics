import turtle
from math import sqrt

def drawpixel(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.dot(3)

def ellipse(a, b):
    x = 0
    y = b
    d1 = b * b + a * a * (0.25 - b)
    drawpixel(x,y)
    drawpixel(-x, y)
    drawpixel(-x, -y)
    drawpixel(x, -y)

    while(b * b * (x + 1) < a * a * (y-0.5)):
        if d1 < 0:
            d1 += b * b * (2 * x + 3)
            x += 1
        else:
            d1 += b * b * (2 * x + 3) + a * a * (3 - 2 * y)
            x += 1
            y -= 1
        drawpixel(x,y)
        drawpixel(-x, y)
        drawpixel(-x, -y)
        drawpixel(x, -y)
        
    d2 = sqrt(b * (x + 0.5)) + sqrt(a * (y - 1)) - sqrt(a * b)

    while y > 0:
        if d2 < 0:
            d2 += b * b * (2 * x + 2) + a * a * (-2 * y + 3)
            x += 1
            y -= 1
        else:
            d2 += a * a * (3 - 2 * y)
            y -=1
        drawpixel(x,y)
        drawpixel(-x, y)
        drawpixel(-x, -y)
        drawpixel(x, -y) 

def main():
    a = int(input('请输入椭圆的长半径a：'))
    b = int(input('请输入椭圆的短半径b：'))
    turtle.pencolor('red')
    turtle.hideturtle()
    turtle.speed(0)
    turtle.screensize(800, 600, 'white')
    ellipse(a, b)
    turtle.mainloop()

if __name__ == "__main__":
    main()