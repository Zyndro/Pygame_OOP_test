import pygame
import time
import random

pygame.init()
szerokosc_okna=640
wysokosc_okna=480

black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)



effect = pygame.mixer.Sound('pop.ogg')
gameDisplay = pygame.display.set_mode((szerokosc_okna,wysokosc_okna))
pygame.display.set_caption("Rak Hunter")
gunImg = pygame.image.load('gun.png')
pocisk = pygame.image.load('bullet.png')
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)


rakImg=pygame.image.load('rak.png')

class gracz():

    def __init__(self):
       self.y = (wysokosc_okna - wysokosc_okna + wysokosc_okna - 45)



    def update(self,x):
        self.x = x

        if x >= 0 and x <= szerokosc_okna - 35:
            gameDisplay.blit(gunImg, (x, self.y))
        else:
            gameDisplay.blit(gunImg, ((szerokosc_okna - 35), self.y))

class szczelanie():

    def __init__(self):
        self.y = (wysokosc_okna - wysokosc_okna + wysokosc_okna - 45)

    def update(self,x ,speed):
        self.poz = speed
        self.y -= self.poz
        gameDisplay.blit(pocisk, (x, self.y))






class enemy():
    def __init__(self):
        self.x = random.randrange(35, szerokosc_okna - 35)
        self.y = random.randrange(wysokosc_okna-2000, wysokosc_okna-500)
        self.alive=True

    def update(self,speed):
        self.poz = speed
        self.y+=self.poz
        print(self.y)
        if self.y > 500:
            self.x = random.randrange(35, szerokosc_okna - 35)
            self.y = -50

        gameDisplay.blit(rakImg, (self.x, self.y))





def raki_ominiete(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("raki ominiete: "+str(count), True, black)
    pygame.draw.rect(gameDisplay, green, [0, 0, szerokosc_okna, 20])
    gameDisplay.blit(text,(0,0))




def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    duzytext=pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text,duzytext)
    TextRect.center = ((szerokosc_okna/2),(wysokosc_okna/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def smierc():
    effect.play()
    message_display('deduwa')

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
        gameDisplay.fill(green)
        gameDisplay.blit(gunImg, ((szerokosc_okna / 2 -35), wysokosc_okna-44))
        duzytext = pygame.font.Font('freesansbold.ttf', 50)
        malytext = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects('Rak Hunter', duzytext)
        TextRect.center = ((szerokosc_okna / 2), (wysokosc_okna/5))
        gameDisplay.blit(TextSurf, TextRect)
        napis, czciomka = text_objects('Wcisnij spacje aby rozpocząć!', malytext)
        czciomka.center = ((szerokosc_okna / 2), (wysokosc_okna / 2))
        gameDisplay.blit(napis, czciomka)


        pygame.display.update()
        clock.tick(15)



def game_loop():
    plejer = gracz()
    enemycounter=4
    enemiesspawned=0
    objs = list()
    bullets = list()
    bulletspoz = list()
    zyje = True

    while zyje == True:
        bulletcounter = 0
        mousepos = pygame.mouse.get_pos()
        gameDisplay.fill(white)
        raki_ominiete(0)
        if enemiesspawned < enemycounter:
            objs.append(enemy())
            enemiesspawned+=1

        for i in objs:
            i.update(3)

        for i in bullets:
            i.update(bulletspoz[bulletcounter], 6)
            bulletcounter +=1



        plejer.update(mousepos[0])



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                bullets.append(szczelanie())
                bulletspoz.append(mousepos[0])
                effect.play()

            if zyje == False:
                smierc()


        pygame.display.update()
        clock.tick(60)
game_intro()
pygame.quit()
quit()
