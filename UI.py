import pygame
from sys import exit

pygame.init()

width = 500
height = 650
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

background = pygame.image.load("Background.jpg").convert()
cross = pygame.image.load("Cross.jpg").convert()
circle = pygame.image.load("Circle.jpg").convert()

position = {
    1:(0,160),
    2:(175,160),
    3:(175*2,160),
    4:(0,325),
    5:(170,325),
    6:(170*2,325),
    7:(0,490),
    8:(170,490),
    9:(170*2,490)
}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.blit(background,(0,0))
    window.blit(circle,position[9])
    window.blit(circle,position[7])
    pygame.display.update()
    
    
