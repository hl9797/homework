from turtle import*

def drawSnake(rad,angle,len,neckrad):
    a="gray","green","pink","red","orange"
    l=0
    for i in range(len):
        pencolor(a[l])
        circle(rad,angle)
        circle(-rad,angle)
        l=l+1
    circle(rad,angle/2)
    fd(rad)
    circle(neckrad+1,180)
    fd(rad*2/3)

def main():
    setup(1300,800,0,0)
    pythonsize=30
    pensize(pythonsize)
    seth(-40)
    drawSnake(40,80,5,pythonsize/2)

main()