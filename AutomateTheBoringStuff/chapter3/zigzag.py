import time
def main():
    drawZigzag()

def drawZigzag():
    indentMax = 32
    goingRight = True
    boundaries = [indentMax, 0]
    directions= [-1 , 1]
    while True: 
        for i in range(indentMax):
            drawIndent(boundaries[goingRight] + (i * directions[goingRight]))
            drawLine()
            time.sleep(0.025)
        goingRight = not goingRight

def drawIndent(indentWidth):
    print(" " * indentWidth, end="")

def drawLine():
    print("#" * 5)

if __name__ == "__main__":
    main()

    