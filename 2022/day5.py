from aocd import get_data

def getInstructions():
    data = get_data(day=5, year=2022)
    data = data.split("\n") 
    return data[10:]


dataMap = {
    1:["B","Z","T"],
    2:["V","H","T","D","N"],
    3:["B","F","M","D"],
    4:["T","J","G","W","V","Q","L"],
    5:["W","D","G","P","V","F","Q","M"],
    6:["V","Z","Q","G","H","F","S"],
    7:["Z","S","N","R","L","T","C","W"],
    8:["Z","H","W","D","J","N","R","M"],
    9:["M","Q","L","F","D","S"]
}

testData = {
    1: ["Z","N"],
    2: ["M","C","D"],
    3: ["P"]
}

testInstructions = ["move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2 "]

def processInstruction(singleLine):
    instructionsArray = singleLine.split(" ")
    numToShift = instructionsArray[1]
    fromLocation = instructionsArray[3]
    toLocation = instructionsArray[5]
    
    return int(numToShift), int(fromLocation), int(toLocation)

def shiftBlocks9000(numToShift, fromLocation, toLocation, blockMap):
    for i in range(0,numToShift,1):
        fetchBlock = blockMap[fromLocation].pop()
        toAddToBlock = blockMap[toLocation]
        toAddToBlock.insert(len(toAddToBlock),fetchBlock)
        blockMap[toLocation] = toAddToBlock

def shiftBlocks9001(numToShift, fromLocation, toLocation, blockMap):
        fetchBlockColumn = blockMap[fromLocation]
        fetchBlocks = fetchBlockColumn[-numToShift:]
        
        toAddToBlock = blockMap[toLocation]
        for block in fetchBlocks:
            toAddToBlock.append(block)
        
        blockMap[toLocation] = toAddToBlock
        blockMap[fromLocation] = fetchBlockColumn[:len(fetchBlockColumn)-numToShift]

def processAllInstructions(instructions, blockMap,typeCrane):
    for instruction in instructions:
        print(instruction)
        numToShift, fromLocation, toLocation = processInstruction(instruction)
        typeCrane(numToShift, fromLocation, toLocation,blockMap)    
        printBlock(blockMap)

def printBlock(block):
    for i in block:
        print(i, " - ", block[i])

def processFinalMessage(blockMap):
    message = ""
    for block in blockMap:
        message += blockMap[block][-1]
    return message

# printBlock(testData)
# print(getInstructions())
# processAllInstructions(getInstructions(),dataMap,shiftBlocks9000)
processAllInstructions(getInstructions(),dataMap,shiftBlocks9001)
print("answer: ", processFinalMessage(dataMap))