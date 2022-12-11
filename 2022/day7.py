from aocd import get_data

def getData():
    data = get_data(day=7, year=2022)
    data = data.split("\n") 
    return data[1:]
print(getData())
testData = """$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
testData = testData.split("\n")
print(testData)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size 
    def PrintFile(self):
        print("--file: ", self.name)
class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent 
        self.files = []
        self.childDirectories = {}
        self.total = 0
    def insertFile(self, file):
        self.files.append(file) 
    def insertDirectory(self, dirToInsert):
        self.childDirectories[dirToInsert.name] = dirToInsert

    def GetChildDirectories(self, findDir):
        return self.childDirectories[findDir]


def iterateAll(input,indent):
    print(" "*indent,"--dir:", input.name , " ", input.total)
    total = 0 
    indent += 3
    for file in input.files:
        print(" "*indent,"--file:", file.name, " ", file.size)
        total += int(file.size)
    input.total = total
    for key, value in input.childDirectories.items():
        iterateAll(value,indent)
        input.total += value.total
    print("catchup ",input.name , " ", input.total)

    indent -=3
    # print("final input amount: ",input.name , " ", input.total)

def processInstructions(inputData, root):
    currDirectory = root 
    for i in range(0,len(inputData),1): 
        print(i,"-",inputData[i])
        instructionProcessed = inputData[i].split(" ")
        if instructionProcessed[1] == "ls":
            continue
        if instructionProcessed[1] == "cd":
            if instructionProcessed[2] == "..":
                currDirectory = currDirectory.parent
                continue
            elif instructionProcessed[2] == "/":
                currDirectory = root
                continue
            else:
                currDirectory = currDirectory.childDirectories[instructionProcessed[2]]
                continue

        if instructionProcessed[0] != "$":
            if instructionProcessed[0] == "dir":
                currDirectory.insertDirectory(Directory(instructionProcessed[1],currDirectory))
            else: 
                currDirectory.insertFile(File(instructionProcessed[1], instructionProcessed[0]))
print("======== traversal =========")
# iterateAndPopulate(root)
# iterate(root,1)
# print(root.total)
root = Directory("/",None)

processInstructions(getData(),root)


iterateAll(root,1)
print("=========traverse and look=======")

def traverse(root):
    answer = []
    traverseThroughMap(root,answer)
    return sum(answer)
    
def traverseThroughMap(dir, answer):
    if len(dir.childDirectories)==0:
        if dir.total < 100000:
            answer.append(dir.total)
        return
    else:
        for key, value in dir.childDirectories.items():
            traverseThroughMap(value,answer)
            if value.total < 10000:
                answer.append(dir.total)

print(traverse(root))