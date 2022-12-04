from concurrent.futures import process
from aocd import get_data

def getElvesJobs():
    data = get_data(day=4, year=2022)
    elfPairJobs = data.split("\n")
    preparedData = []
    for elfPair in elfPairJobs:
        preparedData.append(elfPair.split(","))
    return preparedData

def fullOverlapChecker(set1, set2):
    lowerBound1 = int(set1[0])
    upperBound1 = int(set1[1])

    lowerBound2 = int(set2[0])
    upperBound2 = int(set2[1])
    if (lowerBound1 <=  lowerBound2) and (upperBound1 >= upperBound2):
        return True 
    else:
        return False 
def anyOverlapChecker(set1, set2):
    lowerBound1 = int(set1[0])
    upperBound1 = int(set1[1])

    lowerBound2 = int(set2[0])
    upperBound2 = int(set2[1])
    if (lowerBound1 <=  lowerBound2) and (upperBound1 >= upperBound2):
        return True 
    elif lowerBound2 <= upperBound1 <= upperBound2:
        return True
    else:
        return False 
testData = [["2-4","6-8"],
    ["2-3","4-5"],
    ["5-7","7-9"],
    ["2-8","3-7"],
    ["6-6","4-6"],
    ["2-6","4-8"],
    ['7-7', '8-42']]

def elfAssignmentStringToArray(inputString):
    return inputString.split("-")

def compareElfPairJobs(pairElfJobs, checkerType):
    firstElfToSecondElf = checkerType(elfAssignmentStringToArray(pairElfJobs[0]),elfAssignmentStringToArray(pairElfJobs[1]))
    if firstElfToSecondElf != True:
        secondElfToFirstElf = checkerType(elfAssignmentStringToArray(pairElfJobs[1]),elfAssignmentStringToArray(pairElfJobs[0]))
        return secondElfToFirstElf
    return firstElfToSecondElf 

def processAllElvesJobs(elvesJobs, checkerType):
    overLappedJobCount = 0
    for elfPair in elvesJobs:
        overlap = compareElfPairJobs(elfPair,checkerType)
        if overlap == True:
            overLappedJobCount += 1 
    return overLappedJobCount

print(processAllElvesJobs(getElvesJobs(),fullOverlapChecker))
# print(getElvesJobs())
# print(processAllElvesJobs(testData))
print(processAllElvesJobs(getElvesJobs(),anyOverlapChecker))
