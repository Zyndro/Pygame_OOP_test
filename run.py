import pygame
import time
import random
from entities.Player import gracz
from entities.Enemy import enemy
from entities.bullet import bullets

class Game():

    def __init__(self):
        pygame.init()
        self.szerokosc_okna=640
        self.wysokosc_okna=480
        self.gameDisplay = pygame.display.set_mode((self.szerokosc_okna,self.wysokosc_okna))
        self.shot = pygame.mixer.Sound('assets/pop.ogg')
        pygame.display.set_caption("Rak Hunter")
        pygame.mouse.set_visible(0)
        self.raki = list()
        self.pociski = list()
        self.pociskixpoz = list()



    def game_intro(self):
        intro = True
        clock = pygame.time.Clock()
        font = pygame.font.Font('freesansbold.ttf', 50)
        fontsmall = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Rak Hunter", True, (255, 255, 255))
        text2 = fontsmall.render("Press Space to start!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.szerokosc_okna/2, self.wysokosc_okna/2))
        while intro == True:
            self.gameDisplay.fill((0, 0, 255))
            self.gameDisplay.blit(text, text_rect)
            self.gameDisplay.blit(text2, ((220, self.wysokosc_okna-100)))

            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        intro=False
            self.draw()



    def run(self):
        run=True
        clock=pygame.time.Clock()
        plejer = gracz()
        self.raki.append(enemy())


        while run == True:
            bulletcounter=0
            clock.tick(30)
            pos = pygame.mouse.get_pos()
            self.gameDisplay.fill((255,255,255))
            plejer.update(pos[0],self.gameDisplay)

            for i in self.raki:
                i.draw(self.gameDisplay)

            for i in self.pociski:
                i.update(self.pociskixpoz[bulletcounter],self.gameDisplay)
                bulletcounter+=1
                if i.y < 0:
                    self.pociski.remove(i)
                    del self.pociskixpoz[0]

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pos)
                    self.shot.play()
                    self.pociski.append(bullets())
                    self.pociskixpoz.append(pos[0])

                    print(self.pociskixpoz)


            self.draw()



    def draw(self):
        pygame.display.update()


gra=Game()
gra.game_intro()
gra.run()


