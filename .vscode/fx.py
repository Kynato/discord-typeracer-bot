import asyncio

from classes import *

# DEFINES
boardRows = 6
boardCols = 40
WPM = 60


randomWords = ['rzepa', 'flet', 'klawesyn', 'kartofel', 'ryba', 'mleko', 'pyton', 'anakonda', 'najprawdopodobniej', 'konstantynopol']
#randomWords = ['rzepa', 'flet', 'klawesyn'] # library of words that can be chosen
userInput = [] # 

activeWords = []
laneAvailability = roads(boardRows)


#Returns an empty board
def emptyBoard():
    arr = [['-' for i in range(boardCols)] for j in range(boardRows)]
    return arr
racingStreet = emptyBoard()

def testSetup():
    insertWordToLaneAuto(rd.choice(randomWords))
    insertWordToLaneAuto(rd.choice(randomWords))
    insertWordToLaneAuto(rd.choice(randomWords))

    printRacingStreet() # 3 words inserted
    


#Prints game board
def printRacingStreet():
    board = []
    output = ''

    for row in racingStreet:
        for char in row:
            board.append(char)
        #board.append('\n')

    for row in activeWords:
        counter = 0
        for letter in row.text:
            board[(row.lane + 1) * boardCols + counter - len(row.text) - row.drag] = letter
            counter += 1

    ctr = 0
    for char in board:
        output += char
        ctr += 1
        if (ctr % boardCols == 0):
            output += '\n'

    print(output)
    return

# Returns game board as string to print
def returnRacingStreet():
    board = []
    output = ''

    for row in racingStreet:
        for char in row:
            board.append(char)
        #board.append('\n')

    for row in activeWords:
        counter = 0
        for letter in row.text:
            board[(row.lane + 1) * boardCols + counter - len(row.text) - row.drag] = letter
            counter += 1

    ctr = 0
    for char in board:
        output += char
        ctr += 1
        if (ctr % boardCols == 0):
            output += '\n'

    return output

#Returns a lane number that is free to populate
def chooseLane():
    decision = False
    chosenLane = 0
    lanes = np.arange(0, boardRows, 1).tolist()
    while(decision == False):
        chosenLane = rd.choice(lanes)
        
        decision = laneAvailability.roadBoard[chosenLane].isAvailable

    closeLane(chosenLane)
    return chosenLane

def closeLane(laneNumber):
    laneAvailability.roadBoard[laneNumber].isAvailable = False

#Inserts a word to the end of a lane
def insertWordToLane(word, laneNumber):
    wordToInsert = activeWord(word, laneNumber) # default drag = 0

    activeWords.append(wordToInsert)
    
    
    return

#Inserts a word to lane and automaticly choses the lane
def insertWordToLaneAuto(word):
    #laneNumber = chooseLane()
    laneNumber = laneAvailability.pickEmptyRoad(word)
    if (laneNumber == -1):
        return
    else:
        wordToInsert = activeWord(word, laneNumber) # default drag = 0
        laneAvailability.roadBoard[laneNumber].setCooldown(word)

        activeWords.append(wordToInsert)
        
        return

def tick(activeWords):
    for x in activeWords:
        if (x.drag == boardCols - len(x.text)):
            activeWords.remove(x)
        else:
            x.drag += 1

    return

def deleteWordFromActive(word):
    counter = 0
    for line in activeWords:
        if (line.text != word):
            counter += 1
        else:
            del activeWords[counter]
            counter += 1

    

    return

def deleteListOfWordsFromActive(list):
    for line in list:
        deleteWordFromActive(line)

    return

#def removeWordFromActive(wordPosition, activeWords):
def calculateInterval():
    return 60/WPM


async def gameLoop():
    print('############################################')
    printRacingStreet()
    tick(activeWords)       # moves the words
    laneAvailability.printRoads()
    laneAvailability.tickAll() # lower cooldowns and activates lanes
    #insertWordToLaneAuto(rd.choice(randomWords))
    deleteListOfWordsFromActive(userInput)
    #await asyncio.sleep( calculateInterval() )

async def spawnWordAfter(delay):
    await asyncio.sleep(delay)
    insertWordToLaneAuto(rd.choice(randomWords))


    
