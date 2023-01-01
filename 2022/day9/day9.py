
from aocd import get_data

def getData():
    data = get_data(day=9, year=2022)
    return data
testData = """R 5"""
# U 8"""
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""
def processData(inputData):
    data = inputData.split("\n")
    processData = [] 
    for row in data:
        instructions = row.split(" ")
        processData.append(instructions)
    return processData 

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0 
    def getPoint(self):
        return (self.x, self.y)
    def isFarFromSecondPoint(self, secondPoint):
        xDist = abs(self.x - secondPoint.x)
        yDist = abs(self.y - secondPoint.y)
        if xDist == 2:
            return True 
        if yDist == 2: 
            return True 
        return False
    def isDiagonalMove(self, secondPoint):
        if self.x == secondPoint.x or self.y == secondPoint.y:
            return False
        else: 
            return True 
    def moveDiagonally(self, direction, Point):
        if direction == "U" or direction == "D": 
            if Point.x > self.x:
                secondDirection = "R"
            else:
                secondDirection = "L"
        if direction == "R" or direction == "L":
            if Point.y > self.y:
                secondDirection = "U"
            else:
                secondDirection = "D"
        self.movePoint(direction, 1)
        self.movePoint(secondDirection,1)

    def movePoint(self, direction, steps):
        if direction == "U":
            self.y += steps
        if direction == "D":
            self.y -= steps
        if direction == "R":
            self.x += steps
        if direction == "L":
            self.x -= steps 
def movePoint(point, direction, steps):
    for i in range(0, steps, 1):
        point.movePoint(direction, 1)

headPoint = Point()
tailPoint = Point()

instructionData = processData(testData)
tailHistoryPosition = set()
for row in instructionData: 
    direction = row[0]
    steps = int(row[1])
    for i in range(0, steps,1):
        headPoint.movePoint(direction,1)
        if headPoint.isFarFromSecondPoint(tailPoint)==True:
            if headPoint.isDiagonalMove(tailPoint) == True:
                tailPoint.moveDiagonally(direction, headPoint)
            else:
                tailPoint.movePoint(direction, 1)
        tailHistoryPosition.add(tailPoint.getPoint())

print("Part 1: length: ", len(tailHistoryPosition))
masterHeadPoint = Point()
tailKnots = []
lastTailHistory = set()
for i in range(0, 9, 1):
    tailKnots.append(Point())
for row in instructionData: 
    direction = row[0]
    steps = int(row[1])
    headPoint = masterHeadPoint
    tailPoint = tailKnots[0]
    for i in range(0, steps,1):
        headPoint.movePoint(direction,1)
        if headPoint.isFarFromSecondPoint(tailPoint)==True:
            if headPoint.isDiagonalMove(tailPoint) == True:
                tailPoint.moveDiagonally(direction, headPoint)
            else:
                tailPoint.movePoint(direction, 1)
        for i in range(1, len(tailKnots), 1):
            headPoint = tailKnots[i-1]
            tailPoint = tailKnots[i]
            print("Checking headPoint: ", tailPoint.getPoint())
            print("Checking tailPoint: ", tailPoint.getPoint())
            if headPoint.isFarFromSecondPoint(tailPoint)==True:
                if headPoint.isDiagonalMove(tailPoint) == True:
                    tailPoint.moveDiagonally(direction, headPoint)
                else:
                    tailPoint.movePoint(direction, 1)
        print("H: ", headPoint.x, headPoint.y," T: ", tailPoint.x, tailPoint.y, "L: ", tailKnots[-1].x,tailKnots[-1].y)

        lastTailHistory.add(tailKnots[-1].getPoint())

print("knots in total:", len(tailKnots))
print("lastKnotHistory:", len(lastTailHistory))