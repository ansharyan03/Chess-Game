import pygame as pg

pg.init() #initializes pygame
pg.font.init() #intiialize pygame's font module

resX = 1000
resY = 500

board_offsetX = (resX-400)/2
board_offsetY = (resY-400)/2 + 20

square_size = 50
current_turn = 'white' # white is always the starting color

game_window = pg.display.set_mode((resX, resY))
turnFont = pg.font.SysFont('Arial', 25)

pg.display.set_caption("Chess Game")
chessboard_image = pg.image.load("D:\\camp_chessgame\\chessgame\\chessboard-background.png")

#cb is chessboard
cb = [
    # R == rook, N == knight, B == bishop, Q == queen, K == king, p == pawn
    ['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR']
]


'''
move code:
cb[targetY][targetX] = cb[locY][locX]
cb[locY][locX] = '--'
'''
#startLoc is the location of our piece that we are moving
#endLoc is where we want to move it to
def movePiece(startLoc, endLoc):
    locY = int(startLoc[0]) # grabs row from startLoc tuple and casts to int to make sure that there's no decimal point
    locX = int(startLoc[1]) # grabs column from startLoc and makes sure that there's no decimal point
    targetY = int(endLoc[0])
    targetX = int(endLoc[1])
    
    currentColor = cb[locY][locX][0]
    currentType = cb[locY][locX][1]
    targetColor = cb[targetY][targetX][0]
    targetType = cb[targetY][targetX][1]

    #black pieces
    if currentColor == 'b' and current_turn == 'black':
        if currentType == 'p':
            if targetX == locX and targetY-locY <= 2 and targetY-locY > 0 and locY == 1: #checks if pawn has moved yet and moves it 1-2 spaces
                if cb[targetY][targetX] == '--':
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
            elif targetX == locX and targetY-locY == 1: # checks if it is moving 1 spot ahead, doesn't care about current position
                if cb[targetY][targetX] == '--':
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
            elif abs(targetX - locX) == 1 and targetY - locY == 1:
                if targetColor == 'w' and targetType != 'K':
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
        elif currentType == 'R':
            pathBlocked = False
            if(targetY-locY == 0): #this checks if it's moving like a rook should
                if(targetX < locX):
                    for x in range(targetX+1, locX):
                        if cb[locY][x] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
                elif(targetX > locX):
                    for x in range(locX + 1, targetX):
                        if cb[locY][x] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
            elif(targetX-locX == 0): #this checks if it's moving like a rook should
                if(targetY < locY):
                    for y in range(targetY+1, locY):
                        if cb[y][locX] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
                elif(targetY > locY):
                    for y in range(locY + 1, targetY):
                        if cb[y][locX] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
        elif currentType == 'N':
            if((abs(targetY-locY) == 1 and abs(targetX-locX) == 2) or (abs(targetY-locY) == 2 and abs(targetX-locX) == 1)):
                if (cb[targetY][targetX] == '--' or (cb[targetY][targetX][0] == 'w' and cb[targetY][targetX][1] != 'K')):
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
        elif(currentType == 'B'):
            pathBlocked = False
            if abs(targetY-locY) == abs(targetX-locX): #this line checks if it is moving in the standard bishop pattern
                x = locX
                y = locY
                if targetY-locY > 0 and targetX-locX > 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y+i][x+i] != '--':
                            pathBlocked == True
                elif targetY-locY > 0 and targetX-locX < 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y+i][x-i] != '--':
                            pathBlocked = True
                elif targetY - locY < 0 and targetX - locX > 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y-i][x+i] != '--':
                            pathBlocked = True
                elif targetY - locY < 0 and targetX - locX < 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y-i][x-i] != '--':
                            pathBlocked = True
                if not pathBlocked and ((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
        elif currentType == 'Q':
            pathBlocked = False
            if abs(targetY-locY) == abs(targetX-locX): #this line checks if it is moving in the standard bishop pattern
                x = locX
                y = locY
                if targetY-locY > 0 and targetX-locX > 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y+i][x+i] != '--':
                            pathBlocked == True
                elif targetY-locY > 0 and targetX-locX < 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y+i][x-i] != '--':
                            pathBlocked = True
                elif targetY - locY < 0 and targetX - locX > 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y-i][x+i] != '--':
                            pathBlocked = True
                elif targetY - locY < 0 and targetX - locX < 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y-i][x-i] != '--':
                            pathBlocked = True
                if not pathBlocked and ((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
            elif targetY-locY == 0: #this checks if it's moving like a rook should
                if(targetX < locX):
                    for x in range(targetX+1, locX):
                        if cb[locY][x] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
                elif(targetX > locX):
                    for x in range(locX + 1, targetX):
                        if cb[locY][x] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
            elif targetX - locX == 0:
                if(targetY < locY):
                    for y in range(targetY+1, locY):
                        if cb[y][locX] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
                elif(targetY > locY):
                    for y in range(locY + 1, targetY):
                        if cb[y][locX] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
        elif currentType == 'K':
            if abs(targetY - locY) == 1 and abs(targetX-locX) == 1:
                if((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
            elif (abs(targetY-locY) == 1 and targetX == locX) or (targetY == locY and abs(targetX-locX) == 1):
                if((targetColor == 'w' and targetType != 'K') or cb[targetY][targetX] == '--'):
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'

    # white pieces
    elif currentColor == 'w' and current_turn == 'white':
        if currentType == 'p':
            if targetX == locX and targetY-locY >= -2 and targetY-locY < 0 and locY == 6: #checks if pawn has moved yet and moves it 1-2 spaces
                if cb[targetY][targetX] == '--':
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
            elif targetX == locX and targetY-locY == -1: # checks if it is moving 1 spot ahead, doesn't care about current position
                if cb[targetY][targetX] == '--':
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
            elif abs(targetX - locX) == 1 and targetY - locY == -1:
                if targetColor == 'b' and targetType != 'K':
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
        elif(currentType == 'R'):
            pathBlocked = False
            if(targetY-locY == 0):
                if(targetX < locX):
                    for x in range(targetX+1, locX):
                        if cb[locY][x] != '--':
                            pathBlocked = True
                elif(targetX > locX):
                    for x in range(locX + 1, targetX):
                        if cb[locY][x] != '--':
                            pathBlocked = True
            elif(targetX-locX == 0):
                if(targetY < locY):
                    for y in range(targetY+1, locY):
                        if cb[y][locX] != '--':
                            pathBlocked = True
                elif(targetY > locY):
                    for y in range(locY + 1, targetY):
                        if cb[y][locX] != '--':
                            pathBlocked = True
            if not pathBlocked and ((targetColor == 'b' and targetType != 'K') or cb[targetY][targetX] == '--'):
                cb[targetY][targetX] = cb[locY][locX]
                cb[locY][locX] = '--'
        elif currentType == 'N':
            if((abs(targetY-locY) == 1 and abs(targetX-locX) == 2) or (abs(targetY-locY) == 2 and abs(targetX-locX) == 1)):
                if (cb[targetY][targetX] == '--' or (cb[targetY][targetX][0] == 'b' and cb[targetY][targetX][1] != 'K')):
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
        elif(currentType == 'B'):
            pathBlocked = False
            if abs(targetY-locY) == abs(targetX-locX):
                x = locX
                y = locY
                if targetY-locY > 0 and targetX-locX > 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y+i][x+i] != '--':
                            pathBlocked == True
                elif targetY-locY > 0 and targetX-locX < 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y+i][x-i] != '--':
                            pathBlocked = True
                elif targetY - locY < 0 and targetX - locX > 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y-i][x+i] != '--':
                            pathBlocked = True
                elif targetY - locY < 0 and targetX - locX < 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y-i][x-i] != '--':
                            pathBlocked = True
                if not pathBlocked and ((targetColor == 'b' and targetType != 'K') or cb[targetY][targetX] == '--'):
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
        elif currentType == 'Q':
            pathBlocked = False
            if abs(targetY-locY) == abs(targetX-locX): #this line checks if it is moving in the standard bishop pattern
                x = locX
                y = locY
                if targetY-locY > 0 and targetX-locX > 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y+i][x+i] != '--':
                            pathBlocked == True
                elif targetY-locY > 0 and targetX-locX < 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y+i][x-i] != '--':
                            pathBlocked = True
                elif targetY - locY < 0 and targetX - locX > 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y-i][x+i] != '--':
                            pathBlocked = True
                elif targetY - locY < 0 and targetX - locX < 0:
                    for i in range(1, abs(targetY-locY)):
                        if cb[y-i][x-i] != '--':
                            pathBlocked = True
                if not pathBlocked and ((targetColor == 'b' and targetType != 'K') or cb[targetY][targetX] == '--'):
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
            elif targetY-locY == 0: #this checks if it's moving like a rook should
                if(targetX < locX):
                    for x in range(targetX+1, locX):
                        if cb[locY][x] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'b' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
                elif(targetX > locX):
                    for x in range(locX + 1, targetX):
                        if cb[locY][x] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'b' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
            elif targetX - locX == 0:
                if(targetY < locY):
                    for y in range(targetY+1, locY):
                        if cb[y][locX] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'b' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
                elif(targetY > locY):
                    for y in range(locY + 1, targetY):
                        if cb[y][locX] != '--':
                            pathBlocked = True
                    if not pathBlocked and ((targetColor == 'b' and targetType != 'K') or cb[targetY][targetX] == '--'):
                        cb[targetY][targetX] = cb[locY][locX]
                        cb[locY][locX] = '--'
        elif currentType == 'K':
            if abs(targetY - locY) == 1 and abs(targetX-locX) == 1:
                if((targetColor == 'b' and targetType != 'K') or cb[targetY][targetX] == '--'):
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
            elif (abs(targetY-locY) == 1 and targetX == locX) or (targetY == locY and abs(targetX-locX) == 1):
                if((targetColor == 'b' and targetType != 'K') or cb[targetY][targetX] == '--'):
                    cb[targetY][targetX] = cb[locY][locX]
                    cb[locY][locX] = '--'
            
#game loop
running = True
selected = () #add this line and next line
playerClicks = []
while running:
    #this for loop handles all events, including event types that we add in the future
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN: #starting location
            location = pg.mouse.get_pos()
            col = (location[0] - board_offsetX)//square_size
            row = (location[1] - board_offsetY)//square_size
            if col >= 0 and col < 8 and row >= 0 and row < 8:
                if cb[int(row)][int(col)][0] == current_turn[0]:
                    selected = (row, col) # this is our selected square
                    if(len(playerClicks) == 0):
                        playerClicks.append(selected)
                    else:
                        playerClicks = []
        elif event.type == pg.MOUSEBUTTONUP: # ending location
            if len(playerClicks) == 1:
                location = pg.mouse.get_pos()
                col = (location[0] - board_offsetX)//square_size # NOTE: column and row are floats, so whenever we use them, we need to cast to int
                row = (location[1] - board_offsetY)//square_size
                selected = (row, col)
                playerClicks.append(selected)
                if col >= 0 and col < 8 and row >= 0 and row < 8 and playerClicks[0] != playerClicks[1]:
                    movePiece(playerClicks[0], playerClicks[1])
                if cb[int(playerClicks[0][0])][int(playerClicks[0][1])] == '--' and cb[int(playerClicks[1][0])][int(playerClicks[1][1])] != '--':
                    if current_turn == 'white':
                        current_turn = 'black'
                    else:
                        current_turn = 'white'
                playerClicks = []
    #game code goes here
    game_window.fill((0, 150, 150)) #RGB color
    game_window.blit(chessboard_image, (board_offsetX, board_offsetY))
    #searches for image associated with piece
    for row in range(8):
        for column in range(8):
            if cb[row][column] != '--':
                piece = pg.image.load("D:\\chessgame\\Pieces\\" + cb[row][column] + ".png")
                game_window.blit(pg.transform.scale(piece, (50, 50)), (board_offsetX + column * square_size, board_offsetY + row * square_size))
    
    text_surface = turnFont.render(current_turn.upper() + " TO MOVE", True, pg.Color(current_turn))
    game_window.blit(text_surface, (425, board_offsetY/2)) # if a text surface changes, you HAVE to blit it again
    pg.display.update()