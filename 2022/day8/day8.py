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
        self.isOnBorder = False 
    def setIsBorder(self, boolean):
        self.isOnBorder = boolean 
    def __str__(self):
        return str(self.z)
    
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

def treeRowChecker(treeToCheck):
    rowTreeIsOn = treeToCheck.y
    centerPoint = treeToCheck.x 

    rowOfTreesToCheck = data[rowTreeIsOn]
    #check left of the tree 
    maxHeightLeft = 0 
    for i in range(0, centerPoint,1):
        if rowOfTreesToCheck[i].z > maxHeightLeft:
            maxHeightLeft = rowOfTreesToCheck[i].z
    #check right of the tree
    maxHeightRight = 0 
    for i in range(centerPoint+1, len(rowOfTreesToCheck),1):
        if rowOfTreesToCheck[i].z > maxHeightRight:
            maxHeightRight = rowOfTreesToCheck[i].z
    if treeToCheck.z <= maxHeightLeft and treeToCheck.z <= maxHeightRight:
        return True
    else: 
        return False 

def treeColumnChecker(treeToCheck): 
    colTreeIsOn = treeToCheck.x
    centerPoint= treeToCheck.y

    #check top half of the tree
    maxHeightTop = 0
    for i in range(0, centerPoint, 1):
        if data[i][colTreeIsOn].z > maxHeightTop: 
            maxHeightTop = data[i][colTreeIsOn].z
        
    # check bottom half of the tree
    maxHeightBottom = 0
    for i in range(centerPoint+1, len(data),1):
        if data[i][colTreeIsOn].z > maxHeightBottom: 
            maxHeightBottom = data[i][colTreeIsOn].z
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
                if treeColumnChecker(eachTree) == False or treeRowChecker(eachTree) == False:
                    visibleTree += 1
    return visibleTree 


data = transformData(testData)
for i in data: 
    eachLine = ""
    for j in i: 
        eachLine += str(j.z) + " "
    print(eachLine)
print("Answer: ",countVisibleTrees(data))
