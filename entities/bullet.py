import pygame

class bullets():

    def __init__(self,x):
        self.x = x
        self.y = (480 - 45)
        self.vel=5
        self.pocisk = pygame.image.load('assets/bullet.png')


    def update(self ,win):
        self.y -= self.vel
        self.win = win
        self.win.blit(self.pocisk, (self.x+13, self.y))



    def collisionx(self):
        return (self.x)

    def collisiony(self):
        return (self.y)

