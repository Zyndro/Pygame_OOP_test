import pygame
import random

class enemy():


    def __init__(self):
        self.y=-200
        self.x= random.randrange(35, 640 - 35)
        self.width=40
        self.heigth=69
        self.health = 1
        self.vel=5
        self.Img = pygame.image.load('assets/rak.png')

    def draw(self,win):
        self.win=win
        self.win.blit(self.Img, (self.x,self.y))
        self.move()



    def move(self):
        self.y += self.vel
        if self.y > 500:
            self.x = random.randrange(35, 640 - 35)
            self.y = -50

"""         
    def collide(self,X,Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.heigth and Y >= self.y:
                return True
        return False
"""

