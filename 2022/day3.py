from aocd import get_data
import string

allAlphabets = string.ascii_lowercase + string.ascii_uppercase
totalLength = len(allAlphabets)
alphabetList = list(allAlphabets)
Scores={}
for i in range(0,totalLength,1):
    Scores[alphabetList[i]] = i+1 

def getBackPacksData():
    data = get_data(day=3, year=2022)
    backpacks = data.split("\n")
    return backpacks

testData = ["vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw"]

def findRecurrence(bag):
    items = list(bag)
    midPoint = int(len(items)/2)
    itemTracker = {}
    
    for i in range(0,midPoint,1):
        itemTracker[items[i]]=True
    for i in range(midPoint,len(items),1):
        if items[i] in itemTracker: 
            return items[i]
    return 0
def findPriority(alphabet):
    return Scores[alphabet]

def calculatePriorities(backpacks):
    totalSum = 0
    for backpack in backpacks:
        recurrence = findRecurrence(backpack)
        if recurrence != 0:
            priorityScore = findPriority(recurrence)
            totalSum += priorityScore 
    return totalSum

answer = calculatePriorities(getBackPacksData())
print(answer)

################ Part2 ####################

def findRecurrenceInTriplets(bag1,bag2,bag3):
    bag1Set=set()
    bag2Set=set()
    bag3Set=set()
    for i in bag1:
        bag1Set.add(i)
    for j in bag2:
        bag2Set.add(j)
    for k in bag3:
        bag3Set.add(k)
    bag1And2 = bag1Set.intersection(bag2Set)
    bag2And3 = bag1And2.intersection(bag3Set)
    return bag2And3.pop()


def calculatePrioritiesInTriplets(backpacks):
    totalSum = 0
    for i in range(0,len(backpacks),3):
        recurrence = findRecurrenceInTriplets(backpacks[i],backpacks[i+1],backpacks[i+2])
        priorityScore = findPriority(recurrence)
        totalSum += priorityScore 
    return totalSum

answer = calculatePrioritiesInTriplets(getBackPacksData())
print(answer)
