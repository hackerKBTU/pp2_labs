import pygame
import time
pygame.init()

AurmaidiZhurekPath = "C:\\Users\\Lenovo\\Desktop\\Kajjrat_Nurtas_-_Aurmajjdy_zhurek_75536447.mp3"
IamsexyandIknowitpath = "C:\\Users\\Lenovo\\Desktop\\LMFAO_-_Sexy_And_I_Know_It_47961221.mp3"
Aiptamamenipath = "C:\\Users\\Lenovo\\Desktop\\Ninetu_one_-_Ajjyptama_68980079.mp3"

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("OLENDER ")
clock = pygame.time.Clock()
KairatNurtas = pygame.mixer.music.load(AurmaidiZhurekPath)
Dance = pygame.mixer.music.load(IamsexyandIknowitpath)
Ninetyone = pygame.mixer.music.load(Aiptamamenipath)
musicList = [AurmaidiZhurekPath, IamsexyandIknowitpath, Aiptamamenipath]
pygame.mixer.music.play(-1)
monkey = pygame.image.load("C:\\Users\\Lenovo\\Desktop\\maxresdefault.jpg")

screen.blit(monkey, ((1280 - monkey.get_width()) // 2, (720 - monkey.get_height()) // 2))
flPlay = False
run = True
index = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                index += 1
                if index == len(musicList):
                    index = 0
                pygame.mixer.music.load(musicList[index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList) - 1
                pygame.mixer.music.load(musicList[index])
                pygame.mixer.music.play()

    pygame.display.flip()
    clock.tick(60)



