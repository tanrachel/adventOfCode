from aocd import get_data

def getData():
    data = get_data(day=7, year=2022)
    return data.split("\n")
testData = """$ cd /
$ ls
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
folders = {}
folderPath = []

def processData(inputData): 
    for line in inputData: 
        words = line.split(" ")
        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == "/":
                    folderPath.append("/")
                    continue
                if words[2] == "..":
                    if len(folderPath)==2:
                        folderPath.pop()
                    else:
                        folderPath.pop()
                        folderPath.pop()
                    continue
                if len(folderPath) > 1:
                    # print(folderPath)
                    folderPath.append("/")
                    folderPath.append(words[2])
                else: 
                    folderPath.append(words[2])
                continue
            if words[1] == "ls":
                continue
        folder = ''.join(folderPath)
        if words[0] != "dir":
            if folder in folders:
                folders[folder] += int(words[0])
            else:
                folders[folder] = int(words[0])
        else:
            if folder not in folders:
                folders[folder] = 0

def constructFileName(array):
    fileName = ""
    for i in array:
        fileName += "/"
        fileName += i
    return fileName
def sumFolderSize(): 
    for key, value in folders.items():
        keyCopy = key.split("/")
        keyCopy.pop(0)
        if len(keyCopy) == 1:
            if keyCopy[0] != "":
                folders["/"] += value
            continue
        while keyCopy != []:
            keyCopy.pop()
            if keyCopy == []:
                continue
            keyToAddTo = constructFileName(keyCopy)
            folders[keyToAddTo] += value
            print("new value: ", keyToAddTo, "-",folders[keyToAddTo])
        folders["/"] += value


processData(getData())
sumFolderSize()
print("Folder Total: ",folders["/"])

def findPart1():
    totalSizes = 0
    for key, value in folders.items():
        if value <= 100000:
            totalSizes+=value
    return totalSizes 
print(findPart1())

print("The amount we need to delete for part 2: ", 30000000 - (70000000 - folders["/"])) #26,063,888 
targetNumber = 30000000 - (70000000 - folders["/"])

def findPart2():
    minimumValue = 70000000
    for key, value in folders.items():
        print("greaterThanTarget: ",value >= targetNumber," value: ", value, "minimumValue: ", minimumValue)

        if value >= targetNumber:
            if value < minimumValue:
                minimumValue = value
    return minimumValue
print(findPart2())
