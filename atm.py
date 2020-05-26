# atm class
import pygame
from button import Button
pygame.init()

#! CREATING ATM BUTTONS

#! CREATING BLIT BUTTONS FUNC

class atm(Button):
    def __init__(self, image, x, y, win):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.moneyInAtm = 100
        self.win = win
    def drawATM(self, deposit_button, withdraw_button, cancel_button, atm_inside):
        self.win.fill((0,0,0))
        self.win.blit(atm_inside, (0,0))
        #self.win.blit(self.image, (self.x,self.y))
        for button in [deposit_button, withdraw_button, cancel_button]:
            button.draw(self.win, (0, 0, 0))
            

    def withdraw(self):
        return
    def deposit(self):
        return