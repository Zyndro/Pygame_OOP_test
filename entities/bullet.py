import pygame

class bullets():

    def __init__(self):
        self.y = (480 - 45)
        self.vel=5
        self.pocisk = pygame.image.load('assets/bullet.png')

    def update(self,x ,win):
        self.y -= self.vel
        self.win = win
        self.win.blit(self.pocisk, (x+13, self.y))