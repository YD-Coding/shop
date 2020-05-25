import pygame
pygame.init()


class menu():
    def __init__(self, width, height, caption, image):
        self.width = width
        self.height = height
        self.caption = caption
        self.menu_run = False
        self.image = pygame.image.load(image)

        
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
            
            self.win.blit(self.image, (0,0))
            pygame.display.update()
        
