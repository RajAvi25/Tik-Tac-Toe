import pygame
from sys import exit
from Board import *

# Initialize pygame
pygame.init()

board = Board()

# Set the dimensions of the game window
width = 500
height = 650

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

# Load the game assets
background = pygame.image.load("Background.jpg").convert()
cross = pygame.image.load("Cross.jpg").convert()
circle = pygame.image.load("Circle.jpg").convert()
AI_button = pygame.image.load("AI button.jpg").convert()

# Define the positions of each tile on the game board
position = {
    0: (0, 160),
    1: (170, 160),
    2: (175 * 2, 160),
    3: (0, 325),
    4: (170, 325),
    5: (170 * 2, 325),
    6: (0, 490),
    7: (170, 490),
    8: (170 * 2, 490)
}

# Function to check which tile position was clicked
def checkClickPosition(_mouse_pos, player):
    global isAIPlaying
    if _mouse_pos[0] in range(120, 370) and _mouse_pos[1] in range(10, 60):
        isAIPlaying = True
    if _mouse_pos[0] in range(1, 160) and _mouse_pos[1] in range(164, 313):
        board.updateboard(0,player)
    if _mouse_pos[0] in range(172, 327) and _mouse_pos[1] in range(164, 316):
        board.updateboard(1,player)
    if _mouse_pos[0] in range(338, 496) and _mouse_pos[1] in range(160, 316):
        board.updateboard(2,player)
    if _mouse_pos[0] in range(1, 161) and _mouse_pos[1] in range(329, 477):
        board.updateboard(3,player)
    if _mouse_pos[0] in range(172, 327) and _mouse_pos[1] in range(329, 479):
        board.updateboard(4,player)
    if _mouse_pos[0] in range(337, 500) and _mouse_pos[1] in range(327, 479):
        board.updateboard(5,player)
    if _mouse_pos[0] in range(1, 162) and _mouse_pos[1] in range(490, 645):
        board.updateboard(6,player)
    if _mouse_pos[0] in range(172, 328) and _mouse_pos[1] in range(490, 645):
        board.updateboard(7,player)
    if _mouse_pos[0] in range(340, 500) and _mouse_pos[1] in range(490, 640):
        board.updateboard(8,player)


# Store the clicked tile positions in a list
player = True

isAIPlaying = False

while True:
    # Set the background image on the game window
    window.blit(background, (0, 0))
    window.blit(AI_button,(120,10))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the window is closed
            pygame.quit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                checkClickPosition(mouse_pos, player)
                if isAIPlaying:
                    move = board.moveAI(player)
                    # idxChange = board.values -move
                    # board.updateboard(idxChange,player)
                player = not player

    # Draw the circle or cross image on the clicked tile positions
    for idx,value in enumerate(board.values):
        if value == "X":
            window.blit(cross, position[idx])
        if value == "O":
            window.blit(circle, position[idx])

    # Update the game display
    pygame.display.update()
