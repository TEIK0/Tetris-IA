import pygame
from typing import NoReturn
from constans import(
    SCREEN_RESOLUTION,
    FPS,
    LIGTH_BLACK,
    WHITE,
    COOL_RED
)


from assets import (
    World,
    Tblock,
    Iblock,
    Oblock,
    Sblock,
    Zblock,
    Lblock,
    Jblock
)


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

def fila_vacia(fila):
    return all(valor == 0 for valor in board.grid[fila])

def primer_bloque():
    if board.block == Lblock:
        board.block_offset[0] = 0
    if board.block == Jblock:
        board.block_offset[0] = 8
    if board.block == Iblock:
        board.block_offset[0] = 0
        if fila_vacia(2):
            board.rotate()
    if board.block == Oblock:
        board.block_offset[0] = 0
    if board.block == Zblock:
        board.block_offset[0] = 0
        board.rotate()
    if board.block == Sblock:
        board.block_offset[0] = 0
        board.rotate()
    if board.block == Tblock:
        board.block_offset[0] = 0
        
def manejo_bloqueS():
    for i, row in enumerate(board.grid):
        for j in range(0,len(row)):
            if(row[j] != 0 and i>= 4):
                    if(j+2 <= 9 and i - 2 >= 1  and row[j + 2] == 0 and board.grid[i-1][j+1] == 0 and board.grid[i-1][j+2] == 0 and board.grid[i-3][j+1] == 0):
                        board.block_offset[0] = j
                        
                    elif(j-2 >= 0 and i - 2 >= 1  and row[j - 1] == 0 and board.grid[i-1][j-1] == 0 and board.grid[i-1][j-2] == 0 and board.grid[i-3][j-2] == 0):
                        board.block_offset[0] = j - 1  
                    elif(j+3 <= 9 and row[j + 1] == 0 and row[j + 2] == 0 and board.grid[i-1][j+2] == 0 and board.grid[i-1][j+3] == 0):
                        board.block_offset[0] = j
                        if fila_vacia(1):
                            board.rotate()
                            board.block = [(0, 4, 4),
                                           (4, 4, 0)]
            
                    elif(j-3 >= 0 and row[j - 2] == 0 and row[j - 3] == 0 and board.grid[i-1][j-2] == 0 and board.grid[i-1][j-1] == 0):
                        board.block_offset[0] = j
                        if fila_vacia(1):
                            board.rotate()
                            board.block = [(0, 4, 4),
                                           (4, 4, 0)]
                    
                
def manejo_bloqueZ():
    for i, row in enumerate(board.grid):
        for j in range(0,len(row)):
            if(row[j] != 0):
                if( j + 3 <= 8 and board.grid[i-1][j-1] == 0 and board.grid[i-1][j-2] == 0 and row[j - 2] == 0 and board.grid[i-1][j-3] == 0):
                    board.block_offset[0] = j
                    if fila_vacia(1):
                        board.rotate()
                        board.block = [(5, 5, 0), 
                                       (0, 5, 5)]
                elif( j + 3 <= 8 and board.grid[i-1][j] == 0 and board.grid[i-1][j+2] == 0 and row[j + 2] == 0 and row[j+3] == 0):
                    board.block_offset[0] = j
                    if fila_vacia(1):
                        board.rotate()
                        board.block = [(5, 5, 0), 
                                       (0, 5, 5)]
                    
def manejo_bloqueO ():
    for i, row in enumerate(board.grid):
        for j in range(0,len(row)):
            if(row[j] != 0):
                if( j - 2 >= 0  and row[j-1] == 0 and row[j-2] == 0 and board.grid[i-1][j-1] == 0 and board.grid[i-1][j-2] == 0 ):
                    board.block_offset[0] = j - 2
                elif( j + 2 <= 9 and row[j+1] == 0 and row[j+2] == 0 and board.grid[i-1][j+1] == 0 and board.grid[i-1][j+2] == 0):
                    board.block_offset[0] = j + 1
                    
def manejo_bloqueI ():
    for i, row in enumerate(board.grid):
        for j in range(0,len(row)):
            if(row[j] != 0):
                if( j + 1 <= 9 and i - 3 >= 1 and row[j+1] == 0 and board.grid[i-1][j+1] == 0 and board.grid[i-2][j+1] == 0 and board.grid[i-3][j+1] == 0)  :
                    board.block_offset[0] = j + 1
                elif(j - 1 >= 9 and i - 3 >= 1 and row[j-1] == 0 and board.grid[i-1][j-1] == 0 and board.grid[i-2][j-1] == 0 and board.grid[i-3][j-1] == 0):
                    board.block_offset[0] = j - 1

def manejo_bloqueT ():
    for i, row in enumerate(board.grid):
        for j in range(0,len(row)):
            if(row[j] != 0):
                if(j - 3 >= 0 and row[j-1] == 0 and row[j-2] == 0 and row[j-3] == 0 and board.grid[i-1][j-2] == 0):
                    board.block_offset[0] = j - 1
                elif(j + 3 <= 9 and row[j+1] == 0 and row[j+2] == 0 and row[j+3] == 0 and board.grid[i-1][j+2] == 0):
                    board.block_offset[0] = j + 1

def manejo_bloqueL ():
    for i, row in enumerate(board.grid):
        for j in range(0,len(row)):
            if(row[j] != 0):
                if(j - 2 >= 0 and i - 2 >= 1 and row[j-1] == 0 and row[j-2] == 0 and board.grid[i-1][j-2] == 0 and board.grid[i-2][j-2] == 0):
                    board.block_offset[0] = j - 2
                elif(j + 2 <= 9 and i - 2 >= 1 and row[j+1] == 0 and row[j+2] == 0 and board.grid[i-1][j+1] == 0 and board.grid[i-2][j+1] == 0):
                    board.block_offset[0] = j + 1
                    
def manejo_bloqueJ ():
    for i, row in enumerate(board.grid):
        for j in range(0,len(row)):
            if(row[j] != 0):
                if(j - 2 >= 0 and i - 2 >= 1 and row[j-1] == 0 and row[j-2] == 0 and board.grid[i-1][j-1] == 0 and board.grid[i-2][j-1] == 0):
                    board.block_offset[0] = j - 1
                elif(j + 2 <= 9 and i - 2 >= 1 and row[j+1] == 0 and row[j+2] == 0 and board.grid[i-1][j+2] == 0 and board.grid[i-2][j+2] == 0):
                    board.block_offset[0] = j + 1

def automatico():
    if fila_vacia(19):
        primer_bloque()
    elif board.block == Sblock:
        manejo_bloqueS()
    elif board.block == Zblock:
        manejo_bloqueZ()
    elif board.block == Oblock:
        manejo_bloqueO()
    elif board.block == Iblock:
        manejo_bloqueI()
    elif board.block == Tblock:
        manejo_bloqueT()
    elif board.block == Lblock:
        manejo_bloqueL()
    elif board.block == Jblock:
        manejo_bloqueJ()
            
    
    

#Game Loop
while not board.end:
    screen.fill(LIGTH_BLACK)
    clock.tick(30)
        
    automatico()
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                end_game()
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