import discord
from discord.ext import commands, tasks
from fx import *
from itertools import cycle

status = cycle(['stat1', 'stat2'])
client = commands.Bot(command_prefix='?')
player = client.user

@client.event
async def on_ready():
    changeStatus.start()
    
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
    if message.author == player:
        ipt = message.content.split(' ')
        userInput.extend(ipt)
        print(userInput)
    await client.process_commands(message)


@client.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@client.command()
async def tr(ctx):
    if ctx.message.author != client.user:
        player = ctx.message.author
        await ctx.send('Rozpoczynamy grę w Type Racer')
        await ctx.send('Gracz: ' + player.name)
        trGameLoop.start()
    


totalTime = 0

@tasks.loop(seconds=0)
async def trGameLoop():
    global totalTime
    global lastFrameTime
    channel = client.get_channel(744165713224138812)
    
    totalTime += 1

    if (totalTime >= 2):
        print('SPAWN')
        insertWordToLaneAuto(rd.choice(randomWords))
        totalTime = 0

    await channel.send( totalTime )
    await channel.send( returnRacingStreet() )

    tick(activeWords)       # moves the words in ascii
    #laneAvailability.printRoads()
    laneAvailability.tickAll() # lowers cooldowns and activates lanes
    deleteListOfWordsFromActive(userInput)


@tasks.loop(seconds=1)
async def changeStatus():
    await client.change_presence(activity=discord.Game(next(status)))

git a
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())
        self.totalTime = 0
        self.lastFrameTime = 0
        self.isTaskRunning = False

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        

    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(744165713224138812) # channel ID goes here
        while self.is_closed() == False:
            currentTime = time.time()
            dt = currentTime - self.lastFrameTime
            self.lastFrameTime = currentTime
            self.totalTime += dt

            if (self.totalTime > 5):
                print('SPAWN')
                insertWordToLaneAuto(rd.choice(randomWords))
                self.totalTime = 0

            #gameLoop()
            print('############################################')
            printRacingStreet()
            tick(activeWords)       # moves the words in ascii
            laneAvailability.printRoads()
            laneAvailability.tickAll() # lowers cooldowns and activates lanes
            deleteListOfWordsFromActive(userInput)

            counter += 1
            rycina = returnRacingStreet()
            await channel.send('refresh: ' + str(counter))
            await channel.send(rycina)
            await asyncio.sleep(2) # task runs every 60 seconds

#client = MyClient()

TOKEN = 'your-token'
client.run(TOKEN)

typeRacerInit = False
typeRacerRunning = False
gameChannel = ()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    global typeRacerInit
    global typeRacerRunning
    global player
    global gameChannel

    if message.author == client.user:
        return

    if message.content.startswith('chess'):
        await message.channel.send('jd max najzajeszachy we wszechswiecie')
        await message.channel.send("```♜♞♝♚♛♝♞♜\n♟︎♟︎♟︎♟︎♟︎♟︎♟︎♟︎\n☐⛆☐⛆☐⛆☐⛆\n⛆☐⛆☐⛆☐⛆☐\n☐☒☐☒☐☒☐☒\n☒☐☒☐☒☐☒☐\n♙♙♙♙♙♙♙♙\n♖♘♗♔♕♗♘♖```")


    if message.content == 'tr': #type racer
        await message.channel.send('Ścigasz się? (y/n)')
        typeRacerInit = True
        gameChannel = message.channel
        player = message.author

    elif message.content == 'n' and typeRacerInit == True:
        testmsg = await gameChannel.send('Szkoda mi ciebie lamusie ' + player.name)
       
        await testmsg.edit(content = "Szkoda mi ciebie ~~lamusie~~ kolego " + player.name)

    elif message.content == 'y' and typeRacerInit == True:
        await gameChannel.send('Gracz: ' + player.name)
        await gameChannel.send('No to ziuuuuum')
        typeRacerRunning = True
        client.isTaskRunning = True

    elif message.content == 'exit':
        await gameChannel.send('Koniec gierki :c')
        typeRacerRunning = False

    elif typeRacerRunning == True and message.author == player:
        ipt = message.content.split(' ')
        userInput.extend(ipt)
        print(userInput)





# GAME LOGIC



