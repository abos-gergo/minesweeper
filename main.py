import random
from typing import List, Tuple
import pygame
import math
import time
import sys
import os

from pygame.constants import KSCAN_KP_ENTER, K_KP_ENTER


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Tile:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.number = 0
        self.hidden = True
        self.flagged = False


class Sprites:
    Mine_png = resource_path("Assets/Mine.png")
    Mine = pygame.image.load(Mine_png)
    Flag_png = resource_path("Assets/Flag.png")
    Flag = pygame.image.load(Flag_png)
    Unknown_png = resource_path("Assets/Unknown.png")
    Unknown = pygame.image.load(Unknown_png)
    Zero_png = resource_path("Assets/Zero.png")
    Zero = pygame.image.load(Zero_png)
    One_png = resource_path("Assets/One.png")
    One = pygame.image.load(One_png)
    Two_png = resource_path("Assets/Two.png")
    Two = pygame.image.load(Two_png)
    Three_png = resource_path("Assets/Three.png")
    Three = pygame.image.load(Three_png)
    Four_png = resource_path("Assets/Four.png")
    Four = pygame.image.load(Four_png)
    Five_png = resource_path("Assets/Five.png")
    Five = pygame.image.load(Five_png)
    Six_png = resource_path("Assets/Six.png")
    Six = pygame.image.load(Six_png)
    Seven_png = resource_path("Assets/Seven.png")
    Seven = pygame.image.load(Seven_png)
    Eight_png = resource_path("Assets/Eight.png")
    Eight = pygame.image.load(Eight_png)


def createMap() -> List:
    tiles.clear()
    mines.clear()
    for y in range(27):  # Generate Tiles
        for x in range(48):
            tile = Tile(x, y)
            tiles.append(tile)
            WIN.blit(Sprites.Unknown, (tile.x * 40, tile.y * 40))

    for tile in tiles:  # Generate Mines
        if random.randint(1, 6) == 1:
            tile.number = -1
            mines.append(tile)

    for tile in tiles:  # Calculate Numbers
        if tile.number == 0:
            for checkingtile in mines:
                if (checkingtile.x + 1 == tile.x or checkingtile.x == tile.x or checkingtile.x - 1 == tile.x) and (checkingtile.y + 1 == tile.y or checkingtile.y == tile.y or checkingtile.y - 1 == tile.y):
                    tile.number += 1
    return tiles


def revealAllTiles():
    for tile in tiles:
        if(tile.number == -1):
            WIN.blit(Sprites.Mine, (tile.x * 40, tile.y * 40))  # Blit is used to show something on the screen
        elif(tile.number == 0):  # The position values are multiplied, because one tile is 40 by 40 pixels.
            WIN.blit(Sprites.Zero, (tile.x * 40, tile.y * 40))
        elif(tile.number == 1):
            WIN.blit(Sprites.One, (tile.x * 40, tile.y * 40))
        elif(tile.number == 2):
            WIN.blit(Sprites.Two, (tile.x * 40, tile.y * 40))
        elif(tile.number == 3):
            WIN.blit(Sprites.Three, (tile.x * 40, tile.y * 40))
        elif(tile.number == 4):
            WIN.blit(Sprites.Four, (tile.x * 40, tile.y * 40))
        elif(tile.number == 5):
            WIN.blit(Sprites.Five, (tile.x * 40, tile.y * 40))
        elif(tile.number == 6):
            WIN.blit(Sprites.Six, (tile.x * 40, tile.y * 40))
        elif(tile.number == 7):
            WIN.blit(Sprites.Seven, (tile.x * 40, tile.y * 40))
        elif(tile.number == 8):
            WIN.blit(Sprites.Eight, (tile.x * 40, tile.y * 40))


def convertMousePosToCoords(mousepos) -> Tuple:
    x = math.floor(mousepos[0] / 40)
    y = math.floor(mousepos[1] / 40)
    return(x, y)


def findTileUsingCoords(coords) -> Tile:
    for tile in tiles:
        if tile.x == coords[0] and tile.y == coords[1]:
            return tile


def revealTile(tile: Tile):
    tile.hidden = False
    if(tile.number == 0):  # If an adjancent tile has the number zero, it reveals all its adjancent tiles as well.
        WIN.blit(Sprites.Zero, (tile.x * 40, tile.y * 40))
        for checkingtile in tiles:
            if (checkingtile.x + 1 == tile.x or checkingtile.x == tile.x or checkingtile.x - 1 == tile.x) and (checkingtile.y + 1 == tile.y or checkingtile.y == tile.y or checkingtile.y - 1 == tile.y):
                if not (checkingtile.x == tile.x and checkingtile.y == tile.y) and checkingtile.hidden == True:
                    revealTile(checkingtile)

    elif(tile.number == 1):  # If adjancent tile's number isn't zero, it shows the correct picture depending on the tile's number
        WIN.blit(Sprites.One, (tile.x * 40, tile.y * 40))
    elif(tile.number == 2):
        WIN.blit(Sprites.Two, (tile.x * 40, tile.y * 40))
    elif(tile.number == 3):
        WIN.blit(Sprites.Three, (tile.x * 40, tile.y * 40))
    elif(tile.number == 4):
        WIN.blit(Sprites.Four, (tile.x * 40, tile.y * 40))
    elif(tile.number == 5):
        WIN.blit(Sprites.Five, (tile.x * 40, tile.y * 40))
    elif(tile.number == 6):
        WIN.blit(Sprites.Six, (tile.x * 40, tile.y * 40))
    elif(tile.number == 7):
        WIN.blit(Sprites.Seven, (tile.x * 40, tile.y * 40))
    elif(tile.number == 8):
        WIN.blit(Sprites.Eight, (tile.x * 40, tile.y * 40))


def revealAllMines(mines):
    for mine in mines:
        mine.hidden = False
        WIN.blit(Sprites.Mine, (mine.x * 40, mine.y * 40))


def flagTile(tile: Tile, toggle: bool):
    if tile.flagged == False:
        tile.flagged = True
        WIN.blit(Sprites.Flag, (tile.x * 40, tile.y * 40))
    elif toggle:  # Toggle is required, because we don't want to unflag a tile when using the auto-completion (Right arrow key)
        tile.flagged = False
        WIN.blit(Sprites.Unknown, (tile.x * 40, tile.y * 40))


def autoSearchNext():
    done = False  # Done is required to limit the completion of the map to one tile only. It flags or reveals tiles only around one tile at a time
    for tile in tiles:
        if not done:
            if tile.hidden == False:
                adjancents = []
                for checkingtile in tiles:
                    if (checkingtile.x + 1 == tile.x or checkingtile.x == tile.x or checkingtile.x - 1 == tile.x) and (checkingtile.y + 1 == tile.y or checkingtile.y == tile.y or checkingtile.y - 1 == tile.y):
                        if not (checkingtile.x == tile.x and checkingtile.y == tile.y) and checkingtile.hidden == True:
                            adjancents.append(checkingtile)  # Collects every adjancent tile (always 8) in a list
                hidden_sum = 0
                flagged_sum = 0
                for adjancent in adjancents:
                    if adjancent.flagged:
                        flagged_sum += 1
                    if adjancent.hidden:
                        hidden_sum += 1
                if flagged_sum < tile.number:
                    if hidden_sum == tile.number:  # If there are the same amount of hidden (unknown) tiles around the tile as the number of the tile, every unknown tile is a mine, so all of them get flagged.
                        for adjancent in adjancents:
                            if adjancent.hidden:
                                flagTile(adjancent, False)
                                done = True

                elif flagged_sum == tile.number:
                    if hidden_sum > tile.number:  # If there are same amount of flagged tiles around the tile as the number of the tile,
                        for adjancent in adjancents:  # every unknown tile that isn't flagged may not be a mine, so they all get revealed.
                            if adjancent.hidden and not adjancent.flagged:
                                revealTile(adjancent)
                                done = True


WIN = pygame.display.init()
WIN = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE | pygame.FULLSCREEN)
tiles = []
mines = []


def main():
    createMap()
    pygame.display.update()  # Updtades the screen, shows a new frame
    firstClick = True
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosInCoords = convertMousePosToCoords(pygame.mouse.get_pos())
                tile = findTileUsingCoords(mousePosInCoords)
                if event.button == 1:  # Left Click
                    if tile.hidden and not tile.flagged:
                        if firstClick:
                            while True:
                                if tile.number == 0:
                                    revealTile(tile)
                                    pygame.display.update()
                                    firstClick = False
                                    break
                                else:
                                    createMap()  # If it is the game's first click, it keep genrating maps, until the clicked tile isn't a zero, so players won't click on a zero or
                                    tile = findTileUsingCoords(mousePosInCoords)  # a number as their first tile, they will see multiple tiles after the first click.

                        else:
                            if(tile.number == -1):  # Clicked on a mine -> GAME OVER
                                revealAllMines(mines)
                                pygame.display.update()
                                time.sleep(5)  # Showing all mines for 5 seconds, then resetting everything, generating a new map
                                createMap()  # The function clears the whole map, makes everything hidden, and generates new mines, new numbers
                                pygame.display.update()
                                firstClick = True
                            else:
                                revealTile(tile)  # Not clicked on a mine
                                pygame.display.update()
                elif event.button == 3:  # Right Click
                    if tile.hidden == True:  # If tile is hidden, flag it with right click.
                        flagTile(tile, True)  # If tile is flagged already, unflag it (Done with the toggle boolean in the flagTile function)
                        pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    revealAllTiles()  # You can show every tile with pressing ESC. Note: You will have to restart the application if you want a new game
                    pygame.display.update()
                if event.key == pygame.K_RIGHT:
                    autoSearchNext()  # You can auto-complete the map using the right arrow button. It goes step-by-step, so press it multiple times to reveal the whole map
                    pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
