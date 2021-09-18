from group_manager import GroupManager
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
from collections import deque
from attribute import Attribute
from character import Character
from attribute_modifier import AttributeModType, AttributeModifier
from stat_collection import StatCollection
from attribute_id import AttributeId

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
        self.warrior = pygame.image.load("img/warrior.png").convert()
        self.warrior.set_colorkey((0, 0, 0))
        self.thief = pygame.image.load("img/thief_down.png").convert()
        self.thief.set_colorkey((0, 0, 0))
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
        for y, row in enumerate(read_map):
            for x, index in enumerate(row):
                map.append(Tile(x, y))
        #Create TileMap object. Used to store the list of tiles and provides functions to acess tiles given coordinates
        self.tilemap = TileMap(13, 13, map)

        #Initialize sprites and characters
        self.smage = Sprite('mage', (4, 7), (4, 6), self.tilemap, [self.mage])
        wmhp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        wms = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wma = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sc = StatCollection()
        sc.add_to_dict(AttributeId.HP, wmhp)
        sc.add_to_dict(AttributeId.STRENGTH, wms)
        sc.add_to_dict(AttributeId.AGILITY, wma)
        cmage = Character('WhiteMage', sc, self.smage, counter = 10)
        self.swolf = Sprite('wolf', (2, 3), (3, 3), self.tilemap, [self.wolf])
        whp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ws = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wa = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        scw = StatCollection()
        scw.add_to_dict(AttributeId.HP, whp)
        scw.add_to_dict(AttributeId.STRENGTH, ws)
        scw.add_to_dict(AttributeId.AGILITY, wa)
        cwolf = Character('Wolf', scw, self.swolf, counter = 5)

        self.swarrior = Sprite('warrior', (8, 7), (8, 6), self.tilemap, [self.warrior])

        self.sthief = Sprite('thief', (11, 7), (11, 6), self.tilemap, [self.thief])

        self.sprites = [self.smage, self.swarrior, self.swolf, self.sthief]

        # Background sound
        pygame.mixer.music.load('The Hero Approaches.wav')
        mixer.music.play(loops=-1)

        #TODO TEST RIGOROUSLY
        group_manager = GroupManager([cmage, cwolf])
        group_manager.determine_turn_queue()


    def on_update(self):
        #Keeps track where the mouse is pointing and converts it into isometric indices
        x_world, y_world = pygame.mouse.get_pos()
        self.x_index, self.y_index = projection.reverse_isometricprojection(x_world - (DSX - self.camera.x), y_world - (DSY - self.camera.y), 64, 32)
        self.x_index = self.x_index - 1
        #Restric to map size
        self.x_index = projection.restrict(self.x_index, 0, 13)
        self.y_index = projection.restrict(self.y_index, 0, 13)

        #current_tile = self.tilemap.get_tile_in_coor(self.x_index, self.y_index)
        # print(self.x_index, end = ", ")
        # print(self.y_index)
    
        keys = pygame.key.get_pressed()
        #Camera movement
        if keys[pygame.K_LEFT]:
            self.camera.x -= 15

        if keys[pygame.K_RIGHT]:
            self.camera.x += 15

        if keys[pygame.K_UP]:
            self.camera.y -= 15

        if keys[pygame.K_DOWN]:
            self.camera.y += 15
    #Gets event passed as an argument by director loop. Identifies it and acts accordingly. Listens only to events allowed by current state. Still working on that
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

            


    def on_draw(self, screen):
        screen.fill((0,0,0))
        self.disp.fill((0,0,0))
        
        for tile in self.tilemap.map:
            #Highlights currently selected tile
            if tile.xcoor == self.x_index and tile.ycoor == self.y_index:
                self.disp.blit(self.selected_tile, (projection.isometricprojection(self.x_index, self.y_index, 32, 16, (DSX / 2), (DSY / 2))))
            #Blits arena tile on current tile 
            else:
                self.disp.blit(self.tr, projection.isometricprojection(tile.xcoor, tile.ycoor, 32, 16, (DSX / 2), (DSY / 2)))
            # #Loops through the current tiles adjecant tiles and blits a zone indicator tile on each of them
            # for adj in projection.get_adjecant_squares(self.x_index, self.y_index, 13):
            #     self.disp.blit(self.zone_indicator, projection.isometricprojection(adj[0], adj[1], 32, 16, (DSX / 2), (DSY / 2)))
            #If there exists a sprite on tile, it is drawn there. Important for image layering
            for sprite in self.sprites:
                if tile.get_tile_coor() == sprite.pos:
                    sprite.draw_sprite(self.disp, 0)

        screen.blit(pygame.transform.scale(self.disp, screen.get_size()), (0, 0), self.camera)




