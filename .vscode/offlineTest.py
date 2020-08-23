# GAME LOGIC


from fx import *
#testSetup()

#deleteWordFromActive('flet')
#deleteListOfWordsFromActive(randomWords)

totalTime = 0
lastFrameTime = 0

currentTime = time.time()
dt = currentTime - lastFrameTime
lastFrameTime = currentTime

totalTime += dt

print(totalTime)
if (totalTime > 5):
    print('SPAWN')
    asyncio.run(spawnWordAfter(0))
    totalTime = 0

asyncio.run(gameLoop())
