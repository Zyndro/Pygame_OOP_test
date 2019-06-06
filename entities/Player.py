import pygame

class gracz():

    def __init__(self):
       self.y = 435
       self.img=pygame.image.load('assets/gun.png')



    def update(self,x,win):
        self.x = x
        self.win=win
        self.win.blit(self.img, (x, self.y))
