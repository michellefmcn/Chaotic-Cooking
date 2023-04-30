from cmu_graphics import *
from PIL import Image
from classes import *
from tutorial import*
import images
import time

#create scenes using string headers like welcome__redrawAll(app) and 
#game_redrawAll(app) from 4/19 lecture

def onAppStart(app):
    images
    app.currTime = 0
    app.startTime = 0
    #--code from sprites.py 4/11 lecture--
    app.upSprites = []
    app.tutUpSprites = []
    for i in range(6):
        upSprite = CMUImage(app.upSprite.crop((1934//6//3*i + 15, 0, 
                                    1934//6//3 + 1934//6//3*i, 563//3)))
        tutUpSprite = CMUImage(app.tutUpSprite.crop((1934//6//5*i + 10, 0, 
                                    1934//6//5 + 1934//6//5*i, 563//5)))
        app.upSprites.append(upSprite)
        app.tutUpSprites.append(tutUpSprite)
    app.downSprites = []
    app.tutDownSprites = []
    for i in range(7):
        downSprite = CMUImage(app.downSprite.crop((1897//7//3*i, 0,
                                        1897//7//3 + 1897//7//3*i + 1, 482//3)))
        tutDownSprite = CMUImage(app.tutDownSprite.crop((1897//7//5*i, 0,
                                        1897//7//5 + 1897//7//5*i + 1, 482//5)))
        app.downSprites.append(downSprite)
        app.tutDownSprites.append(tutDownSprite)
    app.leftSprites = []
    app.tutLeftSprites = []
    for i in range(6):
        leftSprite = CMUImage(app.leftSprite.crop((1614//6//3*i, 0, 
                                            1614//6//3 + 1614//6//3*i, 480//3)))
        tutLeftSprite = CMUImage(app.tutLeftSprite.crop((1614//6//5*i, 0, 
                                            1614//6//5 + 1614//6//5*i, 480//5)))
        app.leftSprites.append(leftSprite)
        app.tutLeftSprites.append(tutLeftSprite)
    app.rightSprites = []
    app.tutRightSprites = []
    for i in range(6):
        rightSprite = CMUImage(app.rightSprite.crop((1614//6//3*i, 0, 
                                            1614//6//3 + 1614//6//3*i, 480//3)))
        tutRightSprite = CMUImage(app.tutRightSprite.crop((1614//6//5*i, 0, 
                                            1614//6//5 + 1614//6//5*i, 480//5)))
        app.rightSprites.append(rightSprite)
        app.tutRightSprites.append(tutRightSprite)

    app.spriteCounter = 0
    #--lecture code end--
    app.stepsPerSecond = 150
    app.timeLimit = 179
    #--TUTORIAL SETUP--
    app.tut1CurrChar = app.tutTempChar
    app.tut1CharX = 300
    app.tut1CharY = 400
    app.tut1IsHolding = None
    app.tut1Counter1 = TutorialCounter(240, 330, 310, 410)
    app.tut1Pressed = False
    app.tut2Pressed = False
    app.tut2CurrChar = app.tutTempChar
    app.tut2CharX = 300
    app.tut2CharY = 350
    app.tut2IsHolding = BurgerPatty()
    app.tut2ChoppingBoard = TutorialCuttingBoard(280, 340, 350, 460)
    app.tut2Stove = TutorialStove(390, 340, 460, 460)
    app.tut2trashCan = Trash(170, 330, 250, 460)
    app.tut3Pressed = False
    app.tut3Profit = 0
    app.tut3CurrChar = app.tutTempChar
    app.tut3CharX = 300
    app.tut3CharY = 350
    app.tut3IsHolding = None
    app.tut3Window = ServingWindow(210, 360, 270, 515)
    app.tut3Counter1 = TutorialCounter(185, 320, 235, 355)
    app.tut3Counter1.holding = Cheese()
    app.tut3Counter2 = TutorialCounter(240, 320, 315, 355)
    app.tut3Counter2.holding = Bread()
    app.tut3Counter2.holding.chopped = True
    app.tut3Counter2.holding.image = app.tut3Counter2.holding.choppedImage
    app.tut3Counter3 = TutorialCounter(320, 320, 375, 355)
    app.tut3Counter3.holding = BurgerPatty()
    app.tut3Counter3.holding.chopped = True
    app.tut3Counter3.holding.image = app.tut3Counter3.holding.cookedImage
    app.tut3Counter4 = TutorialCounter(380, 320, 500, 355)
    app.tut3Counter4.holding = Plate()
    app.tut3Counters = [app.tut3Counter1, app.tut3Counter2, app.tut3Counter3,
                        app.tut3Counter4]
    #--GAME SETUP--
    app.currChar = app.tempChar
    app.isHolding = None
    app.currCharX = 300
    app.currCharY = 300
    app.minutes = 3
    app.seconds = 59
    app.totalProfit = 0
    app.ordersCompleted = 0
    app.orderList = []
    app.counter1 = EmptyCounter(80, 100, 120, 175) #top left
    app.counter2 = EmptyCounter(265, 100, 325, 175) # top middle
    app.counter3 = EmptyCounter(335, 375, 400, 475) # bottom
    app.counter4 = EmptyCounter(330, 100, 400, 175) #top right
    app.counterList = [app.counter1, app.counter2, app.counter3, app.counter4]
    app.choppingBoard = CuttingBoard(120, 25, 260, 175)
    app.stove1 = Stove(430, 375, 500, 475) #left stove
    app.stove2 = Stove(515, 375, 600, 475) #right stove
    app.window = ServingWindow(0, 200, 100, 350)
    app.trashCan = Trash(0, 100, 80, 175)
    app.spaces = [app.counter1, app.counter2, app.counter3, app.counter4, 
                  app.choppingBoard, app.stove1, app.stove2, app.trashCan, 
                  app.window]

#--START SCREEN CODE--

def welcome_redrawAll(app):
    drawImage(app.startBG, 0, 0) 
    drawImage(app.startScreen, app.width//2, app.height//2, align='center')
    drawImage(app.startButton, app.width//2, 525, align = 'center')

def welcome_onMousePress(app, mouseX, mouseY):
    buttonXRange = list(range(app.width//2 - 512//3, app.width//2 + 512//3))
    buttonYRange = list(range(525 - 178//3, 525 + 178//3))
    if mouseX in buttonXRange and mouseY in buttonYRange:
        setActiveScreen('tutorial1')

#--GAME CODE--

def game_redrawAll(app):
    drawImage(app.map, 0, 0)
    drawImage(app.serveWindow, -30, 275)
    drawImage(app.topBar, 0, 0)
    drawImage(app.supplies, 30, 540)
    drawImage(app.trash, 30, 137)
    drawImage(app.sink, 435, 130)
    drawImage(app.topPlate, 545, 145)
    drawImage(app.cuttingBoard, 200, 140) #png
    drawImage(app.knife, 253, 150)
    drawImage(app.stove, 450, 545) #left stove
    drawImage(app.stove, 535, 545) #right stove
    if len(app.orderList) > 0:
        for order in range(len(app.orderList)):
            app.orderList[order].draw(order * 150, 0)
            drawLabel(app.orderList[order].timeLeft(), order * 150 + 100, 
                      70, font = 'mono', size = 30)
    drawLabel(app.totalProfit, 615, 50, font = 'mono', size = 20)
    app.counter1.draw()
    app.counter2.draw()
    app.counter3.draw()
    app.counter4.draw()
    app.choppingBoard.draw()
    if app.choppingBoard.holding != None and \
       app.choppingBoard.holding.choppable == True:
        timesChopped = app.choppingBoard.holding.timesChopped
        timesToBeChopped = app.choppingBoard.holding.chopComplete
        drawLabel(f'{timesChopped}/{timesToBeChopped}', 180, 175, 
                font = 'mono', size = 20)
    if app.stove1.holding != None:
        timeCooked = app.stove1.holding.displayTime
        timeToBeCooked = app.stove1.holding.cookingTime
        if app.stove1.holding.timeCooked <= timeToBeCooked:
            drawLabel(f'{timeCooked}/{timeToBeCooked}', 450, 545, 
                        font = 'mono', size = 20)
        elif app.stove1.holding.timeCooked <= timeToBeCooked + 3:
            drawLabel('!', 450, 545, font = 'mono', size = 20)
        else:
            drawLabel('Burnt!', 450, 545, font = 'mono', size = 20)
        drawImage(app.pan, 450, 535)
    if app.stove2.holding != None:
        timeCooked = app.stove2.holding.displayTime
        timeToBeCooked = app.stove2.holding.cookingTime
        if app.stove2.holding.timeCooked <= timeToBeCooked:
            drawLabel(f'{timeCooked}/{timeToBeCooked}', 540, 545, 
                        font = 'mono', size = 20)
        elif app.stove2.holding.timeCooked <= timeToBeCooked + 3:
            drawLabel('!', 540, 545, font = 'mono', size = 20)
        else:
            drawLabel('Burnt!', 540, 545, font = 'mono', size = 20)
        drawImage(app.pan, 535, 535)
    app.stove1.draw()
    app.stove2.draw()
    app.window.draw()
    app.trashCan.draw()

    #highlight supplies
    if app.currCharX > 400 and app.currCharY < 150: #plate
        drawImage(app.sinkHighlight, 425, 125)
    elif app.currCharX < 70 and app.currCharY > 370: #bun
        drawImage(app.highlighted, 10, 525)
    elif app.currCharX < 170 and app.currCharY > 370: #meat
        drawImage(app.highlighted, 100, 525)
    elif app.currCharX < 270 and app.currCharY > 370: #cheese
        drawImage(app.highlighted, 185, 525)
    elif app.currCharX < 340 and app.currCharY > 370: #tomato
        drawImage(app.highlighted, 265, 525)

    drawImage(app.currChar, app.currCharX, app.currCharY)
    if app.seconds >= 10:
        if app.seconds == 60:
            drawLabel(f'{app.minutes}:00', 615, 85, font = 'mono', 
                    size = 20)
        else:
            drawLabel(f'{app.minutes}:{app.seconds}', 615, 85, 
                      font = 'mono', size = 20)
    else:
        drawLabel(f'{app.minutes}:0{app.seconds}', 615, 85, font = 'mono', 
                    size = 20)
    if app.isHolding != None:
        app.isHolding.draw(app.currCharX + 20, app.currCharY + 100)

def game_onStep(app):
    #--code from sprites.py 4/11 lecture--
    app.spriteCounter = (1 + app.spriteCounter) % len(app.upSprites)
    #--lecture code end--
    if len(app.orderList) > 0 and app.orderList[0].orderExpired() == True:
        app.orderList.pop(0)
    if app.currTime + 15 < time.time():
        app.currTime = time.time()
        if len(app.orderList) <= 2:
            app.orderList.append(Order(time.time()))
    app.timeLimit = 179 + app.startTime - time.time()
    app.minutes = rounded(app.timeLimit // 60)
    app.seconds = rounded(app.timeLimit % 60) 
    if app.minutes == 0 and app.seconds == 0:
        setActiveScreen('end')
    #cooking food
    if app.stove1.holding != None:
        app.stove1.cookItem()
    if app.stove2.holding != None:
        app.stove2.cookItem()
    #highlight spaces 
    for space in app.spaces:
        if space.inBounds(app.currCharX, app.currCharY) == True:
            space.showHighlight = True
        else:
            space.showHighlight = False

def game_onKeyHold(app, keys):
    #moves the character
    dx, dy = 0,0
    if 'left' in keys and 'right' not in keys:
        if app.currCharX >= 15 and (app.currCharY < 150 or app.currCharY > 350 \
                                    or app.currCharX > 60):
            dx = -5
            sprite = app.leftSprites[app.spriteCounter]
            app.currChar = sprite
    elif 'right' in keys and 'left' not in keys:
        if app.currCharX <= 535:
            dx = 5
            sprite = app.rightSprites[app.spriteCounter]
            app.currChar = sprite
    if 'up' in keys and 'down' not in keys:
        if app.currCharY >= 120 and (app.currCharY < 155 or \
                                     app.currCharY > 350 or app.currCharX > 55):
            dy = -5
            sprite = app.upSprites[app.spriteCounter]
            app.currChar = sprite
    elif 'down' in keys and 'up' not in keys:
        if app.currCharY <= 375 and (app.currCharY < 150 or \
                                     app.currCharY > 345 or app.currCharX > 55):
            dy = 5
            sprite = app.downSprites[app.spriteCounter]
            app.currChar = sprite
    if dx != 0 and dy != 0: #for diagonals
        dx /= 2**0.5
        dy /= 2**0.5
        if 'left' in keys:
            sprite = app.leftSprites[app.spriteCounter]
            app.currChar = sprite
        elif 'right' in keys:
            sprite = app.rightSprites[app.spriteCounter]
            app.currChar = sprite
    app.currCharX += dx
    app.currCharY += dy

def game_onKeyPress(app, key):
    if key == 'space': 
        if app.isHolding == None: 
            #grab plate
            if app.currCharX > 400 and app.currCharY < 150: 
                app.isHolding = Plate()
            #grab bun
            elif app.currCharX < 70 and app.currCharY > 370:
                app.isHolding = Bread()
            #grab meat
            elif app.currCharX < 170 and app.currCharY > 370:
                app.isHolding = BurgerPatty()
            #grab cheese
            elif app.currCharX < 270 and app.currCharY > 370:
                app.isHolding = Cheese()
            #grab tomato
            elif app.currCharX < 340 and app.currCharY > 370:
                app.isHolding = Tomato()
            #pick things back up
            elif app.counter1.holding != None and \
               app.counter1.inBounds(app.currCharX, app.currCharY) == True:
                app.isHolding = app.counter1.holding
                app.counter1.removeItem()
            elif app.counter2.holding != None and \
               app.counter2.inBounds(app.currCharX, app.currCharY) == True:
                app.isHolding = app.counter2.holding
                app.counter2.removeItem()
            elif app.counter3.holding != None and \
               app.counter3.inBounds(app.currCharX, app.currCharY) == True:
                app.isHolding = app.counter3.holding
                app.counter3.removeItem()
            elif app.counter4.holding != None and \
               app.counter4.inBounds(app.currCharX, app.currCharY) == True:
                app.isHolding = app.counter4.holding
                app.counter4.removeItem()
            elif app.choppingBoard.holding != None and \
               app.choppingBoard.inBounds(app.currCharX, app.currCharY) == True:
                app.isHolding = app.choppingBoard.holding
                app.choppingBoard.removeItem()
            elif app.stove1.holding != None and \
               app.stove1.inBounds(app.currCharX, app.currCharY) == True:
                app.isHolding = app.stove1.holding
                app.stove1.removeItem()
            elif app.stove2.holding != None and \
               app.stove2.inBounds(app.currCharX, app.currCharY) == True:
                app.isHolding = app.stove2.holding
                app.stove2.removeItem()
        elif app.isHolding != None:
            #place on counter
            if app.counter1.holding == None and \
               app.counter1.inBounds(app.currCharX, app.currCharY) == True:
                app.counter1.placeItem(app.isHolding)
                app.isHolding = None
            elif app.counter2.holding == None and \
               app.counter2.inBounds(app.currCharX, app.currCharY) == True:
                app.counter2.placeItem(app.isHolding)
                app.isHolding = None
            elif app.counter3.holding == None and \
               app.counter3.inBounds(app.currCharX, app.currCharY) == True:
                app.counter3.placeItem(app.isHolding)
                app.isHolding = None
            elif app.counter4.holding == None and \
               app.counter4.inBounds(app.currCharX, app.currCharY) == True:
                app.counter4.placeItem(app.isHolding)
                app.isHolding = None
            #add item to plate
            elif isinstance(app.counter1.holding, Plate) and \
                            app.isHolding.readyToAssemble == True and \
                    app.counter1.inBounds(app.currCharX, app.currCharY) == True:
                if app.counter1.holding.addItem(app.isHolding) == True:
                    app.isHolding = None
            elif isinstance(app.counter2.holding, Plate) and \
                            app.isHolding.readyToAssemble == True and \
                    app.counter2.inBounds(app.currCharX, app.currCharY) == True:
                if app.counter2.holding.addItem(app.isHolding) == True:
                    app.isHolding = None
            elif isinstance(app.counter3.holding, Plate) and \
                            app.isHolding.readyToAssemble == True and \
                    app.counter3.inBounds(app.currCharX, app.currCharY) == True:
                if app.counter3.holding.addItem(app.isHolding) == True:
                    app.isHolding = None
            elif isinstance(app.counter4.holding, Plate) and \
                            app.isHolding.readyToAssemble == True and \
                    app.counter4.inBounds(app.currCharX, app.currCharY) == True:
                if app.counter4.holding.addItem(app.isHolding) == True:
                    app.isHolding = None
            #place on chopping board
            elif isinstance(app.isHolding, FoodItem) and \
               app.choppingBoard.holding == None and \
               app.choppingBoard.inBounds(app.currCharX, app.currCharY) == True:
                app.choppingBoard.placeItem(app.isHolding)
                app.isHolding = None
            #place on stove
            elif isinstance(app.isHolding, FoodItem) and \
                          app.isHolding.cookable == True and \
                          app.isHolding.chopped == True and \
                          app.stove1.holding == None and \
                    app.stove1.inBounds(app.currCharX, app.currCharY) == True:
                app.stove1.placeItem(app.isHolding)
                app.isHolding = None
                app.stove1.cookItem()
            elif isinstance(app.isHolding, FoodItem) and \
                          app.isHolding.cookable == True and \
                          app.isHolding.chopped == True and \
                          app.stove2.holding == None and \
                    app.stove2.inBounds(app.currCharX, app.currCharY) == True:
                app.stove2.placeItem(app.isHolding)
                app.isHolding = None
                app.stove2.cookItem()
        #serve food
        if isinstance(app.isHolding, Plate) and \
                      app.window.inBounds(app.currCharX, app.currCharY) == True:
            for order in app.orderList:
                orderAccurate = True
                if len(order.details) == len(app.isHolding.holding):
                    for item in order.details:
                        itemAccurate = False
                        for food in app.isHolding.holding:
                            if isinstance(food, item) == True:
                                itemAccurate = True
                        if itemAccurate == False:
                            orderAccurate = False
                    #calculating profit
                    if orderAccurate == True:
                        app.ordersCompleted += 1
                        if order.totalTimeLeft - order.displayTime >= 10:
                            app.totalProfit += 50
                        else:
                            app.totalProfit += 30
                        for food in range(len(app.isHolding.holding)):
                            if isinstance(app.isHolding.holding[food],
                                          order.details[food]) == False:
                                app.totalProfit -= 5
                        app.orderList.remove(order)
                        break
            app.isHolding = None
    if key == 'q':
        #chop food
        if isinstance(app.choppingBoard.holding, FoodItem) and \
               app.choppingBoard.inBounds(app.currCharX, app.currCharY) == True \
               and app.isHolding == None:
                app.choppingBoard.chopItem()
    if key == 'r':
        #throw out food
        if (isinstance(app.isHolding, Plate) or \
                        isinstance(app.isHolding, FoodItem)) and \
                    app.trashCan.inBounds(app.currCharX, app.currCharY) == True:
            app.isHolding = None
            if app.totalProfit >= 10:
                app.totalProfit -= 10

def end_redrawAll(app):
    drawImage(app.startBG, 0, 0) 
    drawImage(app.end, app.width//2, app.height//2, align = 'center')
    if app.totalProfit >= 250:
        #top star:
        drawImage(app.star, app.width//2, app.height//2 - 125, align = 'center')
        #left star:
        drawImage(app.star, app.width//2 - 65, app.height//2 - 85, 
                align = 'center')
        #right star:
        drawImage(app.star, app.width//2 + 65, app.height//2 - 85, 
                align = 'center')
        drawLabel('Cooking Ability: Too Good', app.width//2, app.height//2 + 10, 
                  font = 'mono', size = 15, align = 'center')
        drawLabel(f'Orders Completed: {app.ordersCompleted}', app.width//2, 
                app.height//2 + 90, font = 'mono', size = 15, align = 'center')
    elif app.totalProfit >= 150:
        #top star:
        drawImage(app.star, app.width//2, app.height//2 - 125, align = 'center')
        #left star:
        drawImage(app.star, app.width//2 - 65, app.height//2 - 85, 
                align = 'center')
        #right star:
        drawImage(app.missingStar, app.width//2 + 65, app.height//2 - 85, 
                align = 'center')
        drawLabel('Cooking Ability: Decent', app.width//2, app.height//2 + 10, 
                  font = 'mono', size = 15, align = 'center')
        drawLabel(f'Orders Completed: {app.ordersCompleted}', app.width//2, 
                app.height//2 + 90, font = 'mono', size = 15, align = 'center')
    elif app.totalProfit >= 75:
        #top star:
        drawImage(app.star, app.width//2, app.height//2 - 125, align = 'center')
        #left star:
        drawImage(app.missingStar, app.width//2 - 65, app.height//2 - 85, 
                align = 'center')
        #right star:
        drawImage(app.missingStar, app.width//2 + 65, app.height//2 - 85, 
                align = 'center')
        drawLabel('Cooking Ability: Poor', app.width//2, app.height//2 + 10, 
                  font = 'mono', size = 15, align = 'center')
        drawLabel(f'Orders Completed: {app.ordersCompleted}', app.width//2, 
                app.height//2 + 90, font = 'mono', size = 15, align = 'center')
    elif app.totalProfit >= 0:
        #top star:
        drawImage(app.missingStar, app.width//2, app.height//2 - 125, align = 'center')
        #left star:
        drawImage(app.missingStar, app.width//2 - 65, app.height//2 - 85, 
                align = 'center')
        #right star:
        drawImage(app.missingStar, app.width//2 + 65, app.height//2 - 85, 
                align = 'center')
        drawLabel('Cooking Ability: Nonexistent', app.width//2, 
                  app.height//2 + 10, font = 'mono', size = 15, 
                  align = 'center')
        drawLabel(f'Orders Completed: {app.ordersCompleted}', app.width//2, 
                app.height//2 + 90, font = 'mono', size = 15, align = 'center')
    drawLabel('Game Over!', app.width//2, app.height//2 - 20, font = 'mono', 
              size = 35, align = 'center')
    drawImage(app.coin, 250, 355)
    drawLabel(app.totalProfit, app.width//2, 380, font = 'mono', size = 30, 
              align = 'center')

#from 4/19 lecture:
runAppWithScreens(initialScreen='welcome', width=650, height=650)