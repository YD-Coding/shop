import pygame
pygame.init()

class Text():
    def __init__(self, win, x, y, text, textFont, size, string=''):
        self.win = win
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.string = string
        self.font = pygame.font.Font(textFont, size)
        self.color = (0, 0, 0)
    

    def show_text(self):
        if type(self.text) == int:
            self.text = str(self.text)
        if self.string == '':
            show_text_R = self.font.render(self.text, True, (self.color))
            self.win.blit(show_text_R, (self.x, self.y))
        else:
            show_text_R = self.font.render(self.string + self.text, True, (self.color))
            self.win.blit(show_text_R, (self.x, self.y))


    


    
    


"""Score = 0
ScoreText = pygame.font.Font('freesansbold.ttf', 40)
ScoreTextX = 975
ScoreTextY = 350


def showScore():
    ScoreTextR = ScoreText.render("Score : " + str(Score), True, (0, 0, 0))
    main_win.blit(ScoreTextR, (ScoreTextX, ScoreTextY))"""
