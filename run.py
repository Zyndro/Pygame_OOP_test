import pygame
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
        self.clock = pygame.time.Clock()





    def game_intro(self):
        intro = True
        font = pygame.font.Font('freesansbold.ttf', 50)
        fontsmall = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Rak Hunter", True, (255, 255, 255))
        text2 = fontsmall.render("Press Space to start!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.szerokosc_okna/2, self.wysokosc_okna/2))
        while intro == True:
            self.gameDisplay.fill((0, 0, 255))
            self.gameDisplay.blit(text, text_rect)
            self.gameDisplay.blit(text2, ((220, self.wysokosc_okna-100)))

            self.clock.tick(30)

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
        plejer = gracz() #spawning player
        points=0
        respawn=60


        while run == True:
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render("Score: " + str(points), True, (0,0,0))

            self.clock.tick(30)
            pos = pygame.mouse.get_pos()
            self.gameDisplay.fill((255,255,255))
            plejer.update(pos[0],self.gameDisplay)


            if points < 0: #restarting the game on negative points
                self.raki.clear()
                self.pociski.clear()
                gra.game_intro()
                points=0

            for i in self.raki:
                i.draw(self.gameDisplay)
                #print(i.collisiony())
                if i.collisiony() > 495:
                    points -= 1

            for i in self.pociski:
                i.update(self.gameDisplay)
                if i.collisiony() < 0: #bullets leaving the gamearea
                   self.pociski.remove(i)
                for r in self.raki: #collision between bullets and cancers
                    #print(r.collisionx(), i.collisionx())
                    if r.collisionx() <= i.collisionx()+20 and r.collisionx()+20 >= i.collisionx() and i.collisiony() < r.collisiony()+69:
                        print("deduwa occured")
                        self.raki.remove(r)
                        points+=1



            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pos)
                    self.shot.play()
                    self.pociski.append(bullets(pos[0])) #spawning bullets(shooting)


            pygame.draw.rect(self.gameDisplay, (255, 250, 0), [0, 0, self.szerokosc_okna, 20])
            self.gameDisplay.blit(text, (0, 0))
            self.draw()
            respawn-=1

            if respawn < 0:
                self.raki.append(enemy())
                respawn=60
            print(respawn)



    def draw(self):
        pygame.display.update()


gra=Game()
gra.game_intro()
gra.run()


