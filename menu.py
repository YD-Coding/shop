import pygame
from button import Button
pygame.init()

shop_button = Button((255,255,255), 540, 140, 220, 110, "SHOP!", 60)

class menu():
    def __init__(self, width, height, caption, image, func):
        self.width = width
        self.height = height
        self.caption = caption
        self.menu_run = False
        self.image = pygame.image.load(image)
        self.func = func
        
    def draw(self):
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

    def mainloop(self):
        self.menu_run = True  
        self.draw()       

        while self.menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_run = False
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if shop_button.isOver(pos):
                        self.menu_run = False
                        self.func()
                if event.type == pygame.MOUSEMOTION:
                    if shop_button.isOver(pos):
                        shop_button.color = (211,211,211)
                    else:
                        shop_button.color = (255, 255, 255)

            
            self.win.blit(self.image, (0,0))
            shop_button.draw(self.win, True)
            pygame.display.update()
        
