from aocd import get_data

def getData():
    data = get_data(day=6, year=2022)
    return list(data)
testData = list("mjqjpqmgbljsphdztnvjfqwrcgsmlb")

def findFirstMarkerin4(input):
    for i in range(3, len(input),1):
        setTracker = set()
        for j in range(i-3,i+1,1):
            setTracker.add(input[j])
        if len(setTracker)==4:
            return i+1
        print("i: ",i," - set: ", setTracker)
def findFirstMarkerin14(input):
    for i in range(13, len(input),1):
        setTracker = set()
        for j in range(i-13,i+1,1):
            setTracker.add(input[j])
        if len(setTracker)==14:
            return i+1
print(findFirstMarkerin4(getData()))
print(findFirstMarkerin14(getData()))
