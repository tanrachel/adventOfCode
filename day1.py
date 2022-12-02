from aocd import get_data

def elvesLoadDataProcessing():
    data = get_data(day=1, year=2022)
    splitData = data.split("\n\n")
    elvesLoad = []
    for i in splitData:
        elvesLoad.append(i.split("\n"))
    return elvesLoad

def findMax(elves):
    maxValue = 0 
    allLoads = []
    for elf in elves:
        elfValue = 0 
        for val in elf: 
            elfValue += int(val) 
        allLoads.append(elfValue)
        if elfValue > maxValue:
            maxValue = elfValue
    allLoads.sort()
    return maxValue, allLoads

def sumOfList(start, end, array):
    sumTotal = 0
    for i in range(start, end, 1):
        sumTotal += array[i]
    return sumTotal

elvesLoad = elvesLoadDataProcessing()
maxValue, allLoads = findMax(elvesLoad)

print("Max Value: ", maxValue)
print("Top 3 value: ", sumOfList(len(allLoads)-3, len(allLoads), allLoads))

