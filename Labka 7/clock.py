import pygame
import datetime

pygame.init()
clock = pygame.image.load("mickeyclock.jpeg")
size = clock.get_rect().size
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mickey clock")
fps = pygame.time.Clock()

sechand = pygame.image.load("sechand.png").convert_alpha()
minhand = pygame.image.load("minhand.png").convert_alpha()
minhand_rect = minhand.get_rect()
minhand_rect.topleft = (size[0] // 2 - 210, size[1] // 2 - 90)
sechand_rect = sechand.get_rect()
sechand_rect.topleft = (size[0] // 2 - 275, size[1] // 2 - 70)

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    screen.blit(clock, (0, 0))
    now = datetime.datetime.now()

    angle_minhand = -((now.minute + now.second / 60) * 6) + 90
    angle_sechand = -(now.second * 6) + 90

    rotated_minhand = pygame.transform.rotate(minhand, angle_minhand)
    rotated_sechand = pygame.transform.rotate(sechand, angle_sechand)

    minhand_rect_rotated = rotated_minhand.get_rect(center=minhand_rect.center)
    sechand_rect_rotated = rotated_sechand.get_rect(center=sechand_rect.center)

    screen.blit(rotated_minhand, minhand_rect_rotated.topleft)
    screen.blit(rotated_sechand, sechand_rect_rotated.topleft)

    fps.tick(60)
    pygame.display.update()

pygame.quit()
