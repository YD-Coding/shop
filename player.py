import pygame
pygame.init()
class Player():

    def __init__(self, x, y, win):
        self.walkRight = [pygame.image.load(r'images\R1.png'), pygame.image.load(r'images\R2.png'), pygame.image.load(r'images\R3.png'), pygame.image.load(r'images\R4.png'), pygame.image.load(r'images\R5.png'), pygame.image.load(r'images\R6.png'), pygame.image.load(r'images\R7.png'), pygame.image.load(r'images\R8.png'), pygame.image.load(r'images\R9.png')]
        self.walkLeft = [pygame.image.load(r'images\L1.png'), pygame.image.load(r'images\L2.png'), pygame.image.load(r'images\L3.png'), pygame.image.load(r'images\L4.png'), pygame.image.load(r'images\L5.png'), pygame.image.load(r'images\L6.png'), pygame.image.load(r'images\L7.png'), pygame.image.load(r'images\L8.png'), pygame.image.load(r'images\L9.png')]
        self.char = pygame.image.load(r'images\standing.png')
        self.x = x
        self.y = y
        self.vel = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.MoneyOnHand = 20
        self.win = win
    
    def draw(self):
        if not self.standing:
            if self.left:
                if self.walkCount + 1 >= 27:
                    self.walkCount = 0
                else:
                    self.walkCount += 1
                    self.win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            elif self.right:
                if self.walkCount + 1 >= 27:
                    self.walkCount = 0
                else:
                    self.walkCount += 1
                    self.win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
        else:
            self.win.blit(self.char, (self.x, self.y))
            

    def firstDraw(self):
        return
        