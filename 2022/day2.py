from aocd import get_data

# A - rock - X
# B - paper - Y
# C - scissor - Z


Scores = { 
    "A X": [0,0],
    "A Y": [0,1],
    "A Z": [1,0],
    "B X": [1,0],
    "B Y": [0,0],
    "B Z": [0,1],
    "C X": [0,1],
    "C Y": [1,0],
    "C Z": [0,0]
}

scenario = {
    "X": [1,0],
    "Y": [0,0],
    "Z": [0,1]
}

scoreGrid = {
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3

}

def drawBonus(seq): 
    if seq == [0,0]:
        return 3
    else:
        return 0
def winnerBonus(win):
    if win:
        return 6
    else:
        return 0
def calculateGame(sequence):
    firstPlayer = 0
    secondPlayer = 0
    for seq in sequence:
        sequencesSplit = seq.split(" ")
        firstPlayerChoice = sequencesSplit[0]
        secondPlayerChoice = sequencesSplit[1]
        scores = Scores[seq]
        firstPlayerWin = scores[0]
        secondPlayerWin = scores[1]

        #processFirstPlayer
        firstPlayer += scoreGrid[firstPlayerChoice] +drawBonus(scores) + winnerBonus(firstPlayerWin)
        secondPlayer += scoreGrid[secondPlayerChoice] +drawBonus(scores) + winnerBonus(secondPlayerWin)
    return firstPlayer, secondPlayer

    


def rockPaperScissorData():
    data = get_data(day=2, year=2022)
    splitData = data.split("\n")
    return splitData

testData = ["A Y","B X","C Z"]
firstPlayer, secondPlayer = calculateGame(rockPaperScissorData())
print("FirstPlayer: ", firstPlayer)
print("SecondPlayer: ", secondPlayer)

############## part 2 ############### 
from aocd import get_data

# A - rock - X
# B - paper - Y
# C - scissor - Z


Scores = { 
    "A A": [0,0],
    "A B": [0,1],
    "A C": [1,0],
    "B A": [1,0],
    "B B": [0,0],
    "B C": [0,1],
    "C A": [0,1],
    "C B": [1,0],
    "C C": [0,0]
}

scenario = {
    "X": [1,0],
    "Y": [0,0],
    "Z": [0,1]
}

scoreGrid = {
    "A": 1,
    "B": 2,
    "C": 3

}

def drawBonus(seq): 
    if seq == [0,0]:
        return 3
    else:
        return 0
def winnerBonus(win):
    if win:
        return 6
    else:
        return 0
def calculateGame(seq):
    opponentChoice, neededScenario = processPair(seq) 
    searchScenario = scenario[neededScenario]
    myMatch, scoreScenario = lookForMatch(opponentChoice, searchScenario)
    doIWin = scoreScenario[1]
    myScore = drawBonus(scoreScenario) + winnerBonus(doIWin)  + scoreGrid[myMatch]
    return myScore

def calculateGames(games):
    totalScore = 0
    for game in games:
        totalScore += calculateGame(game)
    return totalScore

def lookForMatch(opponentChoice, searchScenario):
    for score in Scores:
        if Scores[score] == searchScenario:
            opponentMatch, myMatch = processPair(score)
            if opponentMatch == opponentChoice:
                return myMatch, searchScenario

def processPair(seq):
    pairs = seq.split(" ")
    firstPair = pairs[0]
    secondPair = pairs[1]
    return firstPair, secondPair
    


def rockPaperScissorData():
    data = get_data(day=2, year=2022)
    splitData = data.split("\n")
    return splitData

testData = ["A Y","B X","C Z"]
myScore = calculateGames(rockPaperScissorData())
print("FirstPlayer: ", myScore)
