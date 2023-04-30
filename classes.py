from cmu_graphics import *
from PIL import Image
import images
import random, time

#'super().' syntax from https://www.programiz.com/python-programming/inheritance

class Drawable:
    def __init__(self, image, width, height):
        start = Image.open(image)
        self.image = CMUImage(start.resize((width, height)))

    def draw(self, x, y):
        drawImage(self.image, x, y)

class Order(Drawable):
    orderCount = 0
    imageList = [app.orderBurger, app.orderCheeseburger, app.orderTomatoBurg]
    def __init__(self, time):
        self.startTime = time
        self.expireTime = 40
        self.displayTime = 40
        self.totalTimeLeft = self.startTime + self.expireTime
        self.completed = False
        self.expired = False
        Order.orderCount += 1
        self.orderCount = Order.orderCount
        self.imageIndex = random.randint(0, 2)
        self.image = Order.imageList[self.imageIndex]
        if self.imageIndex == 0:
            self.details = [Bread, BurgerPatty]
        elif self.imageIndex == 1:
            self.details = [Bread, Cheese, BurgerPatty]
        else:
            self.details = [Bread, Tomato, Cheese, BurgerPatty]

    def orderExpired(self):
        if self.totalTimeLeft >= time.time():
            return self.expired
        self.expired = True
        return self.expired
    
    def timeLeft(self):
        if self.displayTime > 0:
            self.displayTime = self.totalTimeLeft - time.time()
        return str(rounded(self.displayTime))
    
    def draw(self, x, y):
        super().draw(x, y) #draw the order tickets
            
class FoodItem(Drawable):
    def __init__(self, image, width, height):
        self.cookable = False
        self.choppable = True
        self.chopped = False
        self.readyToAssemble = False
        super().__init__(image, width, height)

class Bread(FoodItem):
    def __init__(self):
        super().__init__('pngs/bread.PNG', 115//3, 90//3)
        self.timesChopped = 0
        self.chopComplete = 3
        self.choppedImage = app.bun
        
class BurgerPatty(FoodItem):
    def __init__(self):
        super().__init__('pngs/raw_steak.PNG', 150//3, 85//3)
        self.cookable = True
        self.timeCooked = 0
        self.cookingTime = 3
        self.displayTime = 0
        self.timesChopped = 0
        self.chopComplete = 5
        self.choppedImage = app.rawPatty
        self.cookedImage = app.patty
        self.burntImage = app.burntPatty

class Cheese(FoodItem):
    def __init__(self):
        super().__init__('pngs/cheese.PNG', 120//3, 50//3)
        self.choppable = False
        self.chopped = True
        self.readyToAssemble = True

class Tomato(FoodItem):
    def __init__(self):
        super().__init__('pngs/tomato.PNG', 120//3, 100//3)
        self.timesChopped = 0
        self.chopComplete = 4
        self.choppedImage = app.slicedTomato

class Appliance:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.showHighlight = False
        self.holding = None
    
    def placeItem(self, item):
        self.holding = item
    
    def removeItem(self):
        self.holding = None
    
    def inBounds(self, x, y):
        if x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2:
            return True
        return False
    
    def draw(self):
        if self.holding != None and self.y1 < 350:
            self.holding.draw((self.x1 + self.x2)//2 + 40, self.y2 - 20)
        elif self.holding != None and self.y1 >= 350:
            self.holding.draw((self.x1 + self.x2)//2 + 20, self.y2 + 110)
        if self.showHighlight == True:
            if self.y1 >= 350:
                drawImage(app.highlighted, self.x1 + 10, self.y1 + 150)
            else:
                drawImage(app.highlighted, self.x1 + 80, self.y1 + 100)

class CuttingBoard(Appliance):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def chopItem(self):
        if self.holding != None:
            if self.holding.choppable == True:
                if self.holding.timesChopped < self.holding.chopComplete:
                    self.holding.timesChopped += 1
                if self.holding.timesChopped == self.holding.chopComplete:
                    self.holding.image = self.holding.choppedImage
                    self.holding.chopped = True
                    if isinstance(self.holding, Bread) or \
                            isinstance(self.holding, Tomato):
                        self.holding.readyToAssemble = True

class TutorialCuttingBoard(CuttingBoard):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
    
    def draw(self):
        if self.holding != None:
            self.holding.draw(self.x1 + 20, self.y1 + 120)

class Stove(Appliance):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)  

    def placeItem(self, item):
        self.holding = item
    
    def removeItem(self):
        self.holding = None

    def cookItem(self):
        if self.holding.cookable == True:
            self.holding.timeCooked += 1/app.stepsPerSecond
            self.holding.displayTime = rounded(self.holding.timeCooked)
            if self.holding.timeCooked >= self.holding.cookingTime:
                self.holding.image = self.holding.cookedImage
                self.holding.readyToAssemble = True
            if self.holding.timeCooked >= self.holding.cookingTime + 3:
                self.holding.image = self.holding.burntImage
                self.holding.readyToAssemble = False

class TutorialStove(Stove):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
    
    def draw(self):
        if self.holding != None:
            self.holding.draw(self.x1 + 20, self.y1 + 125)


class EmptyCounter:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.showHighlight = False
        self.holding = None
    
    def placeItem(self, item):
        self.holding = item
    
    def removeItem(self):
        self.holding = None
    
    def inBounds(self, x, y):
        if x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2:
            return True
        return False
    
    def draw(self):
        if self.holding != None and self.y1 < 350:
            self.holding.draw((self.x1 + self.x2)//2 + 30, self.y2 - 10)
        elif self.holding != None and self.y1 >= 350:
            self.holding.draw((self.x1 + self.x2)//2 + 30, self.y2 + 110)
        if self.showHighlight == True:
            if self.y1 >= 350:
                drawImage(app.highlighted, self.x1 + 15, self.y1 + 150)
            else:
                drawImage(app.highlighted, self.x1 + 25, self.y1 + 25)

class TutorialCounter(EmptyCounter):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2) 

    def draw(self):
        if self.holding != None:
            if self.y1 < 325:
                self.holding.draw(self.x1 + 40, self.y2 + 10)
            elif self.y1 < 335:
                self.holding.draw(self.x1 + 40, self.y2 - 30)
            else:
                self.holding.draw(self.x1 - 10, self.y2 - 30)

class ServingWindow:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.showHighlight = False
    
    def inBounds(self, x, y):
        if x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2:
            return True
        return False
    
    def draw(self):
        if self.showHighlight == True:
            drawImage(app.windowHighlight, self.x1 - 10, self.y1 + 70)

    
class Trash:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.showHighlight = False
        self.highlightX = x1
        self.highlightY = y1
    
    def inBounds(self, x, y):
        if x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2:
            return True
        return False
    
    def draw(self):
        if self.showHighlight == True:
            drawImage(app.highlighted, self.x1 + 20, self.y1 + 30)
    
class Plate(Drawable):
    possiblePlates = {(Bread, BurgerPatty, Cheese, Tomato): 
                                                        app.tomatoBurg,
                      (Bread, BurgerPatty, Tomato, Cheese): 
                                                        app.pattyTomatoCheese,
                      (Bread, Tomato, Cheese, BurgerPatty): 
                                                        app.tomatoCheesePatty,
                      (Bread, Tomato, BurgerPatty, Cheese):
                                                        app.tomatoPattyCheese,
                      (Bread, Cheese, BurgerPatty, Tomato):
                                                        app.cheesePattyTomato,
                      (Bread, Cheese, Tomato, BurgerPatty):
                                                        app.cheeseTomatoPatty,
                      (Bread, BurgerPatty, Cheese):     
                                                        app.cheeseBurger,
                      (Bread, Cheese, BurgerPatty):
                                                        app.cheesePatty,
                      (Bread, BurgerPatty, Tomato): 
                                                        app.pattyTomato,
                      (Bread, Tomato, Cheese): 
                                                        app.cheeseTomato,
                      (Bread, Cheese, Tomato):
                                                        app.tomatoCheese,
                      (Bread, Tomato, BurgerPatty): 
                                                        app.tomatoPatty,
                      (Bread, BurgerPatty): 
                                                        app.hamburger,
                      (Bread, Tomato): 
                                                        app.tomatoBun,
                      (Bread, Cheese): 
                                                        app.cheeseBun,
                      tuple([Bread]):                   
                                                        app.bun}

    def __init__(self):
        self.holding = []
        self.readyToAssemble = False
        self.image = app.sidePlate

    def addItem(self, food):
        if isinstance(food, Bread) or (len(self.holding) > 0 and \
                                       isinstance(self.holding[0], Bread)):
            for item in self.holding:
                if type(food) == type(item):
                    return False
            self.holding.append(food)
            return True
    
    def draw(self, x, y):
        super().draw(x, y)
        foodTypes = []
        if len(self.holding) > 0:
            for food in self.holding:
                foodTypes.append(type(food))
            drawImage(Plate.possiblePlates[tuple(foodTypes)], x + 10, y - 15)