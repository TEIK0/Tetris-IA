import pygame
from typing import NoReturn
from constans import(
    SCREEN_RESOLUTION,
    FPS,
    LIGTH_BLACK,
    WHITE,
    COOL_RED
)

from assets import World


def end_game() -> None:
    pygame.quit()
    quit()

# Init
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()
pygame.display.set_caption("Tetris")

board = World()

time_delay = 100
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)


#Game Loop
while not board.end:
    screen.fill(LIGTH_BLACK)
    clock.tick(30)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                end_game()
            if event.key == pygame.K_RIGHT:
                board.move(1,0)
            if event.key == pygame.K_LEFT:
                board.move(-1,0)
            if event.key == pygame.K_UP:
                board.rotate()
        elif event.type == timer_event:
            board.move(0,1)        

    #Draw
    board.draw(screen)
    pygame.display.update()

    

#Game Loop
restart = False
while not restart:
    clock.tick(FPS)
        
    #Events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                end_game()
        
    key = pygame.key.get_pressed()
        
    #Draw
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Game over', True, COOL_RED,LIGTH_BLACK)
    textRect = text.get_rect()
    textRect.center = (SCREEN_RESOLUTION[0] // 2, SCREEN_RESOLUTION[1] // 2)
    result = font.render('Score ' + str(board.score), True, COOL_RED,LIGTH_BLACK)
    textResult = text.get_rect()
    textResult.center = (SCREEN_RESOLUTION[0] // 2, SCREEN_RESOLUTION[1] // 1.8)
    screen.blit(text, textRect)
    screen.blit(result, textResult)
        
    pygame.display.update()
        
        