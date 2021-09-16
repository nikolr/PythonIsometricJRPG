from pygame.sprite import Sprite
from config import *
import pygame, sys, time, random

from sprite import Direction, Sprite
from projection import Projection
from tilemap import TileMap
from tile import Tile
from pygame import *
import os
import sys


#TODO Implement camera movement with arrow keys. Readup on surfaces, rects, and blit


dsx = 640
dsy = 480

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Tile based board demo')

# - window -

screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
screen_rect = screen.get_rect()

# - map - 
display = pygame.Surface((dsx, dsy)).convert()
display_rect = display.get_rect()

mage = pygame.image.load("img/mage1.png").convert()
mage.set_colorkey((0, 0, 0))
wolf = pygame.image.load("img/wolf.png").convert()
wolf.set_colorkey((0, 0, 0))
tr = pygame.image.load("img/wrsprite.png").convert()
tr.set_colorkey((0, 0, 0))
selected_tile = pygame.image.load("img/yrsprite.png").convert()
selected_tile.set_colorkey((0, 0, 0))
zone_indicator = pygame.image.load("img/wbsprite.png").convert()
zone_indicator.set_colorkey((0, 0, 0))

#Ready the tilemap
tilemap = TileMap(13, 13, 'map_full.txt')
maps = tilemap.make_full_map()
full_map_list = maps[0]
isometric_map_list = maps[1]
map_data = full_map_list
isometric_map_data = isometric_map_list

camera = screen.get_rect()

for tile in map_data:
    pygame.draw.rect(display, (255, 255, 255), pygame.Rect(tile.xcoor * 15, tile.ycoor * 15, 15, 15), 1)
    # surf = tile.get_text_surface()
    # text_rect = surf.get_rect(center=t.center)
    # display.blit(surf, text_rect)


smage = Sprite('mage', (4, 7), (4, 6), [mage])

swolf = Sprite('wolf', (2, 3), (3, 3), [wolf])


#Background sound
pygame.mixer.music.load('The Hero Approaches.wav')
mixer.music.play(loops=-1)

while True:
    screen.fill((0,0,0))
    display.fill((0,0,0))
    x_world, y_world = pygame.mouse.get_pos()
    x_index, y_index = Projection.reverse_isometricprojection(x_world - (dsx - camera.x), y_world - (dsy - camera.y), 64, 32)
    x_index = x_index - 1
    x_index = Projection.restrict(x_index, 0, 13)
    y_index = Projection.restrict(y_index, 0, 13)
    print(x_index, end = ", ")
    print(y_index)
    x_iso, y_iso = Projection.isometricprojection(x_index, y_index, 32, 16, (dsx / 2), (dsy / 2))
    
    for tile in map_data:
        if tile.xcoor == x_index and tile.ycoor == y_index:
            # display.blit(selected_tile, ((dsx / 2), (dsx / 2) + x_index * 16 - y_index * 16, (dsx / 2), (dsx / 2) + x_index * 8 + y_index * 8))
            display.blit(selected_tile, (x_iso, y_iso))
            # for adj in Projection.give_adjecant_squares(x_index, y_index, 13):
            #     display.blit(zone_indicator, ((dsx / 2), (dsx / 2) + adj[0] * 16 - adj[1] * 16, (dsx / 2), (dsx / 2) + adj[0] * 8 + adj[1] * 8))
        else:
            # display.blit(tr, ((dsx / 2), (dsx / 2) + tile.xcoor * 16 - tile.ycoor * 16, (dsx / 2), (dsx / 2) + tile.xcoor * 8 + tile.ycoor * 8))
            display.blit(tr, Projection.isometricprojection(tile.xcoor, tile.ycoor, 32, 16, (dsx / 2), (dsy / 2)))
        for adj in Projection.get_adjecant_squares(x_index, y_index, 13):
            # display.blit(zone_indicator, ((dsx / 2), (dsx / 2) + adj[0] * 16 - adj[1] * 16, (dsx / 2), (dsx / 2) + adj[0] * 8 + adj[1] * 8))
            display.blit(zone_indicator, Projection.isometricprojection(adj[0], adj[1], 32, 16, (dsx / 2), (dsy / 2)))

    # display.blit(mage, Projection.get_isometric_tile_center(4, 7, 32, 16, (dsx / 2), (dsy / 2)))

    smage.draw_sprite(display,0)
    swolf.draw_sprite(display, 0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_w:
                smage.change_facing(Direction.UP)
                smage.move_a_square()
            if event.key == K_d:
                smage.change_facing(Direction.RIGHT)
                smage.move_a_square()
            if event.key == K_s:
                smage.change_facing(Direction.DOWN)
                smage.move_a_square()
            if event.key == K_a:
                smage.change_facing(Direction.LEFT)
                smage.move_a_square()
            if event.key == K_SPACE:
                smage.move_a_square()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            smage.set_facing((x_index, y_index))
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            smage.set_pos((x_index, y_index))
        
    keys = pygame.key.get_pressed()
        
    # - updates (without draws) -
    if keys[pygame.K_LEFT]:
        camera.x -= 15
        # if camera.left < fullmap_rect.left:
        #     camera.left = fullmap_rect.left
    if keys[pygame.K_RIGHT]:
        camera.x += 15
        # if camera.right > fullmap_rect.right:
        #     camera.right = fullmap_rect.right
    if keys[pygame.K_UP]:
        camera.y -= 15
        # if camera.top < fullmap_rect.top:
        #     camera.top = fullmap_rect.top
    if keys[pygame.K_DOWN]:
        camera.y += 15
        # if camera.bottom > fullmap_rect.bottom:
        #     camera.bottom = fullmap_rect.bottom

    
    #Implement later. First fix coordinate accuracy with different screen sizes
    #Idea: When zooming in, check to see where the mouse is, then move the camera rect accordingly
    #Take zoom level into consideration

    

    # - draws (without updates) -
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0), camera)
    # screen.blit(pygame.transform.scale(display, (SCREEN_SIZE_X, SCREEN_SIZE_Y)), (0, 0), camera)
    pygame.display.update(screen_rect)
    clock.tick(60)