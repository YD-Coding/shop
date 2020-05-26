class Item():
    def __init__(self, x, y, image, cost, win):
        self.x = x
        self.y = y
        self.image = image
        self.cost = cost
        self.win = win
    def draw(self):
        self.win.blit(self.image, (self.x, self.y))
        