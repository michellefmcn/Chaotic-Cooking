from cmu_graphics import *
from PIL import Image
from classes import *
import images
import time

#--TUTORIAL CODE--

def tutorial1_redrawAll(app):
    drawImage(app.startBG, 0, 0)
    drawImage(app.instruct1, -20, -10)
    drawImage(app.tutMap1, 175, 335)
    if app.tut1Pressed == True:
        drawImage(app.continueButton, 250, 530)
    drawImage(app.tutSupply, 190, 345)
    app.tut1Counter1.draw()
    drawImage(app.tutHighlight, 260, 350)
    drawImage(app.tut1CurrChar, app.tut1CharX, app.tut1CharY)
    if app.tut1IsHolding != None:
        app.tut1IsHolding.draw(app.tut1CharX + 10, app.tut1CharY + 50)

def tutorial1_onMousePress(app, mouseX, mouseY):
    if app.tut1Pressed == True and 250 <= mouseX and mouseX <= 380 and \
                                   530 <= mouseY and mouseY <= 565:
        setActiveScreen('tutorial2')

def tutorial1_onStep(app):
    #--code from sprites.py 4/11 lecture--
    app.spriteCounter = (1 + app.spriteCounter) % len(app.upSprites)
    #--lecture code end--
    if app.tut1Counter1.holding != None:
        app.tut1Pressed = True

def tutorial1_onKeyHold(app, keys): 
    #moves the character
    dx, dy = 0,0
    if 'left' in keys and 'right' not in keys:
        if app.tut1CharX >= 185:
            dx = -2
            sprite = app.tutLeftSprites[app.spriteCounter]
            app.tut1CurrChar = sprite
    elif 'right' in keys and 'left' not in keys:
        if app.tut1CharX <= 415:
            dx = 2
            sprite = app.tutRightSprites[app.spriteCounter]
            app.tut1CurrChar = sprite
    if 'up' in keys and 'down' not in keys:
        if app.tut1CharY >= 345:
            dy = -2
            sprite = app.tutUpSprites[app.spriteCounter]
            app.tut1CurrChar = sprite
    elif 'down' in keys and 'up' not in keys:
        if app.tut1CharY <= 420:
            dy = 2
            sprite = app.tutDownSprites[app.spriteCounter]
            app.tut1CurrChar = sprite
    if dx != 0 and dy != 0: #for diagonals
        dx /= 2**0.5
        dy /= 2**0.5
        if 'right' in keys:
            sprite = app.tutLeftSprites[app.spriteCounter]
            app.tut1CurrChar = sprite
        elif 'left' in keys:
            sprite = app.tutRightSprites[app.spriteCounter]
            app.tut1CurrChar = sprite
    app.tut1CharX += dx
    app.tut1CharY += dy

def tutorial1_onKeyPress(app, key):
    if key == 'space':
        if app.tut1IsHolding == None:
            if app.tut1CharX < 220 and app.tut1CharY < 360:
                app.tut1IsHolding = Bread()
            elif app.tut1Counter1.holding != None and \
                app.tut1Counter1.inBounds(app.tut1CharX, app.tut1CharY) == True:
                    app.tut1IsHolding = app.tut1Counter1.holding
                    app.tut1Counter1.removeItem()
        else:
            if app.tut1Counter1.holding == None and \
               app.tut1Counter1.inBounds(app.tut1CharX, app.tut1CharY) == True:
                app.tut1Counter1.placeItem(app.tut1IsHolding)
                app.tut1IsHolding = None

def tutorial2_reset(app):
    app.tut2Pressed = False
    app.tut2CurrChar = app.tutTempChar
    app.tut2CharX = 300
    app.tut2CharY = 350
    app.tut2IsHolding = BurgerPatty()
    app.tut2ChoppingBoard = TutorialCuttingBoard(280, 340, 350, 460)
    app.tut2Stove = TutorialStove(390, 340, 460, 460)
    app.tut2trashCan = Trash(170, 330, 250, 460)

def tutorial2_redrawAll(app):
    drawImage(app.startBG, 0, 0)
    drawImage(app.instruct2, -20, -10)
    drawImage(app.tutMap2, 175, 335)
    drawImage(app.tut2CurrChar, app.tut2CharX, app.tut2CharY)
    if app.tut2ChoppingBoard.holding != None:
        timesChopped = app.tut2ChoppingBoard.holding.timesChopped
        timesToBeChopped = app.tut2ChoppingBoard.holding.chopComplete
        drawLabel(f'{timesChopped}/{timesToBeChopped}', 275, 460, 
                font = 'mono', size = 20)
    if app.tut2Stove.holding != None:
        timeCooked = app.tut2Stove.holding.displayTime
        timeToBeCooked = app.tut2Stove.holding.cookingTime
        if app.tut2Stove.holding.timeCooked <= timeToBeCooked:
            drawLabel(f'{timeCooked}/{timeToBeCooked}', 380, 455, 
                        font = 'mono', size = 20)
        elif app.tut2Stove.holding.timeCooked <= timeToBeCooked + 3:
            drawLabel('!', 380, 455, font = 'mono', size = 20)
        else:
            drawLabel('Burnt!', 380, 455, font = 'mono', size = 20)
        drawImage(app.pan, 380, 410)
    app.tut2ChoppingBoard.draw()
    app.tut2Stove.draw()
    drawImage(app.reset, 180, 525)
    if app.tut2Pressed == True:
        drawImage(app.continueButton, 340, 525)
    if app.tut2IsHolding != None:
        app.tut2IsHolding.draw(app.tut2CharX + 10, app.tut2CharY + 50)

def tutorial2_onMousePress(app, mouseX, mouseY):
    if 180 <= mouseX and mouseX <= 305 and 525 <= mouseY and mouseY <= 560:
        tutorial2_reset(app)
    if app.tut2Pressed == True and 340 <= mouseX and mouseX <= 470 and \
                                   525 <= mouseY and mouseY <= 560:
        setActiveScreen('tutorial3')

def tutorial2_onStep(app):
    #--code from sprites.py 4/11 lecture--
    app.spriteCounter = (1 + app.spriteCounter) % len(app.upSprites)
    #--lecture code end--
    if app.tut2Stove.holding != None:
        app.tut2Stove.cookItem()

def tutorial2_onKeyHold(app, keys): 
    #moves the character
    dx, dy = 0,0
    if 'left' in keys and 'right' not in keys:
        if app.tut2CharX >= 185:
            dx = -2
            sprite = app.tutLeftSprites[app.spriteCounter]
            app.tut2CurrChar = sprite
    elif 'right' in keys and 'left' not in keys:
        if app.tut2CharX <= 415:
            dx = 2
            sprite = app.tutRightSprites[app.spriteCounter]
            app.tut2CurrChar = sprite
    if 'up' in keys and 'down' not in keys:
        if app.tut2CharY >= 325:
            dy = -2
            sprite = app.tutUpSprites[app.spriteCounter]
            app.tut2CurrChar = sprite
    elif 'down' in keys and 'up' not in keys:
        if app.tut2CharY <= 350:
            dy = 2
            sprite = app.tutDownSprites[app.spriteCounter]
            app.tut2CurrChar = sprite
    if dx != 0 and dy != 0: #for diagonals
        dx /= 2**0.5
        dy /= 2**0.5
        if 'right' in keys:
            sprite = app.tutLeftSprites[app.spriteCounter]
            app.tut2CurrChar = sprite
        elif 'left' in keys:
            sprite = app.tutRightSprites[app.spriteCounter]
            app.tut2CurrChar = sprite
    app.tut2CharX += dx
    app.tut2CharY += dy

def tutorial2_onKeyPress(app, key):
    if key == 'space':
        if app.tut2IsHolding == None:
            if app.tut2ChoppingBoard.holding != None and \
                app.tut2ChoppingBoard.inBounds(app.tut2CharX, app.tut2CharY) == True:
                    app.tut2IsHolding = app.tut2ChoppingBoard.holding
                    app.tut2ChoppingBoard.removeItem()
            elif app.tut2Stove.holding != None and \
               app.tut2Stove.inBounds(app.tut2CharX, app.tut2CharY) == True:
                app.tut2IsHolding = app.tut2Stove.holding
                app.tut2Stove.removeItem()
        elif app.tut2IsHolding.chopped == True and \
                          app.tut2Stove.holding == None and \
                    app.tut2Stove.inBounds(app.tut2CharX, app.tut2CharY) == True:
                app.tut2Stove.placeItem(app.tut2IsHolding)
                app.tut2IsHolding = None
                app.tut2Stove.cookItem()
        else:
            if app.tut2ChoppingBoard.holding == None and \
               app.tut2ChoppingBoard.inBounds(app.tut2CharX, app.tut2CharY) == True:
                app.tut2ChoppingBoard.placeItem(app.tut2IsHolding)
                app.tut2IsHolding = None
    if key == 'q':
        #chop food
        if app.tut2ChoppingBoard != None and \
           app.tut2ChoppingBoard.inBounds(app.tut2CharX, app.tut2CharY) == True:
                app.tut2ChoppingBoard.chopItem()
    if key == 'r':
        #throw out food
        if app.tut2IsHolding != None and \
                    app.tut2trashCan.inBounds(app.tut2CharX, 
                                              app.tut2CharY) == True:
            app.tut2IsHolding = None
            app.tut2Pressed = True 

def tutorial3_reset(app):
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

def tutorial3_redrawAll(app):
    drawImage(app.startBG, 0, 0)
    drawImage(app.instruct3, -20, -10)
    drawImage(app.tutMap3, 150, 335)
    drawImage(app.tutOrderBurger, 155, 335)
    for counter in app.tut3Counters:
        counter.draw()
    drawImage(app.profit, 430, 490)
    drawLabel(app.tut3Profit, 470, 502, font = 'mono', size = 15)
    drawImage(app.tut3CurrChar, app.tut3CharX, app.tut3CharY)
    if app.tut3IsHolding != None:
        app.tut3IsHolding.draw(app.tut3CharX + 10, app.tut3CharY + 50)
    drawLabel('Note: Plate must be on a counter! Bread must be placed first!', 
              320, 525, align = 'center', font = 'mono', fill = 'white')
    drawImage(app.reset, 180, 530)
    if app.tut3Pressed == True:
        drawImage(app.continueButton, 340, 530)

def tutorial3_onMousePress(app, mouseX, mouseY):
    if 180 <= mouseX and mouseX <= 305 and 525 <= mouseY and mouseY <= 560:
        tutorial3_reset(app)
    if app.tut3Pressed == True and 340 <= mouseX and mouseX <= 470 and \
                                   530 <= mouseY and mouseY <= 565:
        setActiveScreen('game')
        app.startTime = time.time()
        app.currTime = time.time()
        app.orderList.append(Order(time.time()))

def tutorial3_onStep(app):
    #--code from sprites.py 4/11 lecture--
    app.spriteCounter = (1 + app.spriteCounter) % len(app.upSprites)

def tutorial3_onKeyHold(app, keys): 
    #moves the character
    dx, dy = 0,0
    if 'left' in keys and 'right' not in keys:
        if app.tut3CharX >= 225:
            dx = -2
            sprite = app.tutLeftSprites[app.spriteCounter]
            app.tut3CurrChar = sprite
    elif 'right' in keys and 'left' not in keys:
        if app.tut3CharX <= 450:
            dx = 2
            sprite = app.tutRightSprites[app.spriteCounter]
            app.tut3CurrChar = sprite
    if 'up' in keys and 'down' not in keys:
        if app.tut3CharY >= 340:
            dy = -2
            sprite = app.tutUpSprites[app.spriteCounter]
            app.tut3CurrChar = sprite
    elif 'down' in keys and 'up' not in keys:
        if app.tut3CharY <= 415:
            dy = 2
            sprite = app.tutDownSprites[app.spriteCounter]
            app.tut3CurrChar = sprite
    if dx != 0 and dy != 0: #for diagonals
        dx /= 2**0.5
        dy /= 2**0.5
        if 'right' in keys:
            sprite = app.tutLeftSprites[app.spriteCounter]
            app.tut3CurrChar = sprite
        elif 'left' in keys:
            sprite = app.tutRightSprites[app.spriteCounter]
            app.tut3CurrChar = sprite
    app.tut3CharX += dx
    app.tut3CharY += dy

def tutorial3_onKeyPress(app, key):
    if key == 'space':
        if app.tut3IsHolding == None:
            for counter in app.tut3Counters:
                if counter.holding != None and \
                    counter.inBounds(app.tut3CharX, app.tut3CharY) == True:
                        app.tut3IsHolding = counter.holding
                        counter.removeItem()
        else:
            for counter in app.tut3Counters:
                if counter.holding == None and \
                counter.inBounds(app.tut3CharX, app.tut3CharY) == True:
                    counter.placeItem(app.tut3IsHolding)
                    app.tut3IsHolding = None
                elif isinstance(counter.holding, Plate) and \
                    counter.inBounds(app.tut3CharX, app.tut3CharY) == True:
                    if counter.holding.addItem(app.tut3IsHolding) == True:
                        app.tut3IsHolding = None
           
            if isinstance(app.tut3IsHolding, Plate) and \
                      app.tut3Window.inBounds(app.tut3CharX, 
                                              app.tut3CharY) == True:
                tutOrder = [Bread, BurgerPatty, Cheese]
                if len(tutOrder) == len(app.tut3IsHolding.holding):
                    #calculating profit
                    app.tut3Profit += 50
                    for food in range(len(app.tut3IsHolding.holding)):
                        if isinstance(app.tut3IsHolding.holding[food], 
                                      tutOrder[food]) == False:
                            app.tut3Profit -= 5
                app.tut3IsHolding = None
                app.tut3Pressed = True