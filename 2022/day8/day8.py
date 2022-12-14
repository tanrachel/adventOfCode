from itertools import count
from aocd import get_data

def getData():
    data = get_data(day=8, year=2022)
    data = transformData(data)
    return data

testData = """30373
25512
65332
33549
35390"""

class Tree:
    def __init__(self, x, y,z):
        self.x = int(x) 
        self.y = int(y) 
        self.z = int(z)
        self.scenicScore = int(1)
        self.isOnBorder = False 
    def setIsBorder(self, boolean):
        self.isOnBorder = boolean 
    def __str__(self):
        return str(self.scenicScore)
    def updateScenicScore(self, score):
        self.scenicScore = self.scenicScore * score 
    
def transformData(input):
    input = input.split("\n")
    matrix = []
    for i in range(0,len(input),1): 
        rowOfTree = []
        for j in range(0,len(input[i]),1):
            tree = Tree(j,i,input[i][j])
            isBorderTree(tree,len(input[i]),len(input))
            rowOfTree.append(tree) 
        matrix.append(rowOfTree)
    return matrix 
            
def isBorderTree(treeToCheck,maxLength, maxHeight):
    if treeToCheck.x == 0 or treeToCheck.x == maxLength-1:
        treeToCheck.setIsBorder(True)
        return 
    if treeToCheck.y == 0 or treeToCheck.y == maxHeight-1:
        treeToCheck.setIsBorder(True)
        return
    else:  
        treeToCheck.setIsBorder(False)

def treeRowChecker(treeToCheck,data):
    rowTreeIsOn = treeToCheck.y
    centerPoint = treeToCheck.x 

    rowOfTreesToCheck = data[rowTreeIsOn]
    #check left of the tree 
    maxHeightLeft = 0 
    unblockedViewLeft = False 
    unblockedTreeLeft = 0
    for i in range(centerPoint-1, -1,-1):
        if rowOfTreesToCheck[i].z > maxHeightLeft:
            maxHeightLeft = rowOfTreesToCheck[i].z
        if unblockedViewLeft == False: 
            unblockedTreeLeft += 1
            if rowOfTreesToCheck[i].z >= treeToCheck.z:
                    unblockedViewLeft = True

    #check right of the tree
    maxHeightRight = 0 
    unblockedViewRight = False 
    unblockedTreeRight = 0
    for i in range(centerPoint+1, len(rowOfTreesToCheck),1):
        if rowOfTreesToCheck[i].z > maxHeightRight:
            maxHeightRight = rowOfTreesToCheck[i].z
        if unblockedViewRight == False: 
            unblockedTreeRight += 1
            if rowOfTreesToCheck[i].z >= treeToCheck.z:
                    unblockedViewRight = True
    treeToCheck.updateScenicScore(unblockedTreeRight*unblockedTreeLeft)
    if treeToCheck.z <= maxHeightLeft and treeToCheck.z <= maxHeightRight:
        return True
    else: 
        return False 

def treeColumnChecker(treeToCheck,data): 
    colTreeIsOn = treeToCheck.x
    centerPoint= treeToCheck.y

    #check top half of the tree
    maxHeightTop = 0
    unblockedViewTop = False 
    unblockedTreeTop = 0
    for i in range(centerPoint-1, -1, -1):
        if data[i][colTreeIsOn].z > maxHeightTop: 
            maxHeightTop = data[i][colTreeIsOn].z
        if unblockedViewTop == False: 
            unblockedTreeTop += 1
            if data[i][colTreeIsOn].z >= treeToCheck.z:
                    unblockedViewTop = True
    # check bottom half of the tree
    maxHeightBottom = 0
    unblockedViewBottom = False 
    unblockedTreeBottom = 0
    for i in range(centerPoint+1, len(data),1):
        if data[i][colTreeIsOn].z > maxHeightBottom: 
            maxHeightBottom = data[i][colTreeIsOn].z
        
        if unblockedViewBottom == False: 
            unblockedTreeBottom += 1
            if data[i][colTreeIsOn].z >= treeToCheck.z:
                    unblockedViewBottom = True
    treeToCheck.updateScenicScore(unblockedTreeBottom*unblockedTreeTop)
    if treeToCheck.z <= maxHeightTop and treeToCheck.z <= maxHeightBottom:
        return True
    else: 
        return False 
def countVisibleTrees(data):
    visibleTree = 0 
    for eachTreeRow in data: 
        for eachTree in eachTreeRow:             
            if eachTree.isOnBorder == True:
                visibleTree +=1 
            else:
                columnChecker = treeColumnChecker(eachTree,data)
                rowChecker = treeRowChecker(eachTree,data)
                if columnChecker == False or rowChecker == False:
                    visibleTree += 1
    return visibleTree 
def getHighestScenicScore(data):
    maxScore = 0
    for eachTreeRow in data: 
        for eachTree in eachTreeRow:             
            if eachTree.scenicScore > maxScore:
                maxScore = eachTree.scenicScore
    return maxScore

data = getData()
print("Part 1 Answer: ", countVisibleTrees(data))

print("Part 2 Answer: ", getHighestScenicScore(data))
