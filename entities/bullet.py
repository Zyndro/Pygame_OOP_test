import pygame

class bullets():

    def __init__(self):
        self.y = (480 - 45)
        self.vel=5
        self.pocisk = pygame.image.load('assets/bullet.png')
        self.collided=False

    def update(self,x ,win):
        self.x=x
        self.y -= self.vel
        self.win = win
        if self.collided==False:
            self.win.blit(self.pocisk, (self.x+13, self.y))



    def collisionx(self):
        return (self.x)

    def collisiony(self):
        return (self.y)

