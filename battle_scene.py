from scene import Scene
from pygame.sprite import Sprite
from config import *
import pygame, sys, time, random

from scene import Scene

from sprite import Direction, Sprite
import projection
from tilemap import TileMap
from tile import Tile
from pygame import *
import os
import sys

#TODO FIX EVENTS
#CLEAN
#MAKE MORE MODULAR

class BattleScene(Scene):
    def __init__(self, director):
        Scene.__init__(self, director)
        self.camera = director.screen.get_rect()
        self.disp = pygame.Surface((DSX, DSY)).convert()
        self.x_index = (0, 0)
        self.x_index = (0, 0)
        #Setup disp
        
        disp_rect = self.disp.get_rect()
        #Ready sprites
        self.mage = pygame.image.load("img/mage1.png").convert()
        self.mage.set_colorkey((0, 0, 0))
        self.wolf = pygame.image.load("img/wolf.png").convert()
        self.wolf.set_colorkey((0, 0, 0))
        self.tr = pygame.image.load("img/wrsprite.png").convert()
        self.tr.set_colorkey((0, 0, 0))
        self.selected_tile = pygame.image.load("img/yrsprite.png").convert()
        self.selected_tile.set_colorkey((0, 0, 0))
        self.zone_indicator = pygame.image.load("img/wbsprite.png").convert()
        self.zone_indicator.set_colorkey((0, 0, 0))

        #Ready the tilemap
        f = open('map_full.txt')
        read_map = [[int(c) for c in row] for row in f.read().split('\n')]
        f.close()
        map = []
        # isometricmap = []
        for y, row in enumerate(read_map):
            for x, index in enumerate(row):
                map.append(Tile(x, y))
                # xi, yi = projection.isometricprojection(x, y, 32, 16, 0, 0)
                # isometricmap.append(Tile(xi, yi))
        # isometric_map_list = maps[1]
        # self.isometric_map_data = isometric_map_list
        self.tilemap = TileMap(13, 13, map)

        self.smage = Sprite('mage', (4, 7), (4, 6), self.tilemap, [self.mage])

        self.swolf = Sprite('wolf', (2, 3), (3, 3), self.tilemap, [self.wolf])


        # Background sound
        pygame.mixer.music.load('The Hero Approaches.wav')
        mixer.music.play(loops=-1)

    def on_update(self):
        x_world, y_world = pygame.mouse.get_pos()
        self.x_index, self.y_index = projection.reverse_isometricprojection(x_world - (DSX - self.camera.x), y_world - (DSY - self.camera.y), 64, 32)
        self.x_index = self.x_index - 1
        self.x_index = projection.restrict(self.x_index, 0, 13)
        self.y_index = projection.restrict(self.y_index, 0, 13)
        current_tile = self.tilemap.get_tile_in_coor(self.x_index, self.y_index)
        # print(self.x_index, end = ", ")
        # print(self.y_index)
        x_iso, y_iso = projection.isometricprojection(self.x_index, self.y_index, 32, 16, (DSX / 2), (DSY / 2))

        keys = pygame.key.get_pressed()
        # - updates (without draws) -
        if keys[pygame.K_LEFT]:
            self.camera.x -= 15
            # if self.camera.left < fullmap_rect.left:
            #     self.camera.left = fullmap_rect.left
        if keys[pygame.K_RIGHT]:
            self.camera.x += 15
            # if self.camera.right > fullmap_rect.right:
            #     self.camera.right = fullmap_rect.right
        if keys[pygame.K_UP]:
            self.camera.y -= 15
            # if self.camera.top < fullmap_rect.top:
            #     self.camera.top = fullmap_rect.top
        if keys[pygame.K_DOWN]:
            self.camera.y += 15
            # if self.camera.bottom > fullmap_rect.bottom:
            #     self.camera.bottom = fullmap_rect.bottom

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.key == pygame.K_w:
                print("Pressed w")
                self.smage.change_facing(Direction.UP)
                self.smage.move_a_square()
            if event.key == K_d:
                self.smage.change_facing(Direction.RIGHT)
                self.smage.move_a_square()
            if event.key == K_s:
                self.smage.change_facing(Direction.DOWN)
                self.smage.move_a_square()
            if event.key == K_a:
                self.smage.change_facing(Direction.LEFT)
                self.smage.move_a_square()
            if event.key == K_SPACE:
                self.smage.move_a_square()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.smage.set_facing((self.x_index, self.y_index))
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            self.smage.set_pos((self.x_index, self.y_index))
    
        keys = pygame.key.get_pressed()
            
        # - updates (without draws) -
        if keys[pygame.K_LEFT]:
            self.camera.x -= 15
            # if self.camera.left < fullmap_rect.left:
            #     self.camera.left = fullmap_rect.left
        if keys[pygame.K_RIGHT]:
            self.camera.x += 15
            # if self.camera.right > fullmap_rect.right:
            #     self.camera.right = fullmap_rect.right
        if keys[pygame.K_UP]:
            self.camera.y -= 15
            # if self.camera.top < fullmap_rect.top:
            #     self.camera.top = fullmap_rect.top
        if keys[pygame.K_DOWN]:
            self.camera.y += 15
            # if self.camera.bottom > fullmap_rect.bottom:
            #     self.camera.bottom = fullmap_rect.bottom

    def on_draw(self, screen):
        screen.fill((0,0,0))
        self.disp.fill((0,0,0))
        
        for tile in self.tilemap.map:
            if tile.xcoor == self.x_index and tile.ycoor == self.y_index:
                # disp.blit(selected_tile, ((DSX / 2), (DSX / 2) + self.x_index * 16 - self.y_index * 16, (DSX / 2), (DSX / 2) + self.x_index * 8 + self.y_index * 8))
                self.disp.blit(self.selected_tile, (projection.isometricprojection(self.x_index, self.y_index, 32, 16, (DSX / 2), (DSY / 2))))
                # for adj in projection.give_adjecant_squares(self.x_index, self.y_index, 13):
                #     disp.blit(zone_indicator, ((DSX / 2), (DSX / 2) + adj[0] * 16 - adj[1] * 16, (DSX / 2), (DSX / 2) + adj[0] * 8 + adj[1] * 8))
            else:
                # disp.blit(tr, ((DSX / 2), (DSX / 2) + tile.xcoor * 16 - tile.ycoor * 16, (DSX / 2), (DSX / 2) + tile.xcoor * 8 + tile.ycoor * 8))
                self.disp.blit(self.tr, projection.isometricprojection(tile.xcoor, tile.ycoor, 32, 16, (DSX / 2), (DSY / 2)))
            for adj in projection.get_adjecant_squares(self.x_index, self.y_index, 13):
                # disp.blit(zone_indicator, ((DSX / 2), (DSX / 2) + adj[0] * 16 - adj[1] * 16, (DSX / 2), (DSX / 2) + adj[0] * 8 + adj[1] * 8))
                self.disp.blit(self.zone_indicator, projection.isometricprojection(adj[0], adj[1], 32, 16, (DSX / 2), (DSY / 2)))

        # disp.blit(mage, projection.get_isometric_tile_center(4, 7, 32, 16, (DSX / 2), (DSY / 2)))

        self.smage.draw_sprite(self.disp, 0)
        # self.map_data
        self.swolf.draw_sprite(self.disp, 0)
        
        screen.blit(pygame.transform.scale(self.disp, screen.get_size()), (0, 0), self.camera)






# for tile in map_data:
#     pygame.draw.rect(disp, (255, 255, 255), pygame.Rect(tile.xcoor * 15, tile.ycoor * 15, 15, 15), 1)
#     # surf = tile.get_text_surface()
#     # text_rect = surf.get_rect(center=t.center)
#     # disp.blit(surf, text_rect)


# self.smage = Sprite('mage', (4, 7), (4, 6), [mage])

# swolf = Sprite('wolf', (2, 3), (3, 3), [wolf])




