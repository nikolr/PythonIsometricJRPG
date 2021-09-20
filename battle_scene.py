from target_state import TargetState
from turn_state import TurnState
from state_machine import StateMachine
from face import Face
from group_manager import GroupManager
from scene import Scene
from pygame.sprite import Sprite
from config import *
import pygame, sys, time, random
# import pygame_gui

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
import ability

#TODO FIX EVENTS
#CLEAN
#MAKE MORE MODULAR

class BattleScene(Scene):
    
    def __init__(self, director):
        Scene.__init__(self, director)
        self.camera = director.screen.get_rect()
        self.disp = pygame.Surface((DSX, DSY)).convert()
        self.x_world = (0, 0)
        self.y_world = (0, 0)
        self.x_index = (0, 0)
        self.x_index = (0, 0)

        #Setup disp
        disp_rect = self.disp.get_rect()

        #Ready sprites
        self.mage_up = pygame.image.load("img/mage_up.png").convert()
        self.mage_up.set_colorkey((0, 0, 0))
        self.mage_right = pygame.image.load("img/mage_right.png").convert()
        self.mage_right.set_colorkey((0, 0, 0))
        self.mage_down = pygame.image.load("img/mage_down.png").convert()
        self.mage_down.set_colorkey((0, 0, 0))
        self.mage_left = pygame.image.load("img/mage_left.png").convert()
        self.mage_left.set_colorkey((0, 0, 0))
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
        self.smage = Sprite('mage', (4, 7), (4, 6), self.tilemap, [self.mage_down, self.mage_right, self.mage_up , self.mage_left])
        wmhp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        wms = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wma = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sc = StatCollection()
        sc.add_to_dict(AttributeId.HP, wmhp)
        sc.add_to_dict(AttributeId.STRENGTH, wms)
        sc.add_to_dict(AttributeId.AGILITY, wma)
        self.cmage = Character('WhiteMage', sc, self.smage, counter = 10, innate_counter= 14)
        self.swolf = Sprite('wolf', (2, 3), (3, 3), self.tilemap, [self.wolf])
        whp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ws = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wa = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        scw = StatCollection()
        scw.add_to_dict(AttributeId.HP, whp)
        scw.add_to_dict(AttributeId.STRENGTH, ws)
        scw.add_to_dict(AttributeId.AGILITY, wa)
        self.cwolf = Character('Wolf', scw, self.swolf, counter = 13, innate_counter= 20)

        self.swarrior = Sprite('warrior', (8, 7), (8, 6), self.tilemap, [self.warrior])
        ahp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ams = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        ama = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sca = StatCollection()
        sca.add_to_dict(AttributeId.HP, ahp)
        sca.add_to_dict(AttributeId.STRENGTH, ams)
        sca.add_to_dict(AttributeId.AGILITY, ama)
        self.cwar = Character('Warrior', sca, self.swarrior, counter = 14, innate_counter= 8)

        self.sthief = Sprite('thief', (11, 7), (11, 6), self.tilemap, [self.thief])
        thp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ts = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        ta = Attribute(AttributeId.AGILITY, 20, 'Health', 'Hit points until down')
        sct = StatCollection()
        sct.add_to_dict(AttributeId.HP, thp)
        sct.add_to_dict(AttributeId.STRENGTH, ts)
        sct.add_to_dict(AttributeId.AGILITY, ta)
        self.cthief = Character('Thief', sct, self.sthief, counter = 5, innate_counter= 6)

        self.attack = ability.Ability("Slash", 5, 1, ability.TargetingType.SINGLE, 1, self.cwar)
        self.shoot = ability.Ability("Shoot", 3, 1, ability.TargetingType.SINGLE, 3, self.cwar)
        self.face = Face("Move", 0, 1, ability.TargetingType.SINGLE, 1, self.cwar)

        self.cwar.gain_ability(self.face)
        self.cwar.gain_ability(self.attack)
        self.cwar.gain_ability(self.shoot)

        self.cmage.gain_ability(self.face)
        self.cmage.gain_ability(self.attack)
        self.cmage.gain_ability(self.shoot)

        self.cthief.gain_ability(self.face)
        self.cthief.gain_ability(self.attack)
        self.cthief.gain_ability(self.shoot)

        self.cwolf.gain_ability(self.face)
        self.cwolf.gain_ability(self.attack)
        self.cwolf.gain_ability(self.shoot)

        

        self.sprites = [self.smage, self.swarrior, self.swolf, self.sthief]
        # self.sprites = [self.smage]

        # Background sound
        pygame.mixer.music.load('The Hero Approaches.wav')
        mixer.music.play(loops=-1)




        #TODO TEST RIGOROUSLY
        self.group_manager = GroupManager([self.cmage, self.cwolf, self.cwar, self.cthief])
        self.group_manager.determine_turn_queue()
        self.current_character = self.group_manager.get_next_character()
        self.target = None
        self.turn_state = TurnState(self.director, self)
        self.target_state = TargetState(self.director, self)
        self.state_machine = StateMachine(self.turn_state)

        self.selected_ability = None


        #UImanager
        # self.manager = pygame_gui.UIManager((SCREEN_SIZE_X, SCREEN_SIZE_Y))
        # self.turn_order_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 0), (100, 500)), starting_layer_height=1, manager = self.manager)
        # self.label_list = []
        # first_in_queue = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (100, 50)), container= self.turn_order_panel, text=f"{self.group_manager.character_queue[0]}",manager=self.manager)
        # second_in_queue = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 50), (100, 50)), container= self.turn_order_panel, text=f"{self.group_manager.character_queue[1]}",manager=self.manager)
        # for i in range(len(self.group_manager.character_queue)):
        #     label_list.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, i*20), (100, 25)), container= self.turn_order_panel, text=f"{self.group_manager.character_queue[i]}",manager=self.manager))

        #character_in_queue = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (100, 50)), container= turn_order_panel, text=f"{self.current_character}",manager=self.manager)

        #Panel font. Probably will make this a class
        self.font = pygame.font.Font("font/PressStart2P-vaV7.ttf", 10)


    def on_update(self):
        #Keeps track where the mouse is pointing and converts it into isometric indices
        self.x_world, self.y_world = pygame.mouse.get_pos()
        self.x_index, self.y_index = projection.reverse_isometricprojection(self.x_world - (DSX - self.camera.x), self.y_world - (DSY - self.camera.y), 64, 32)
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

        self.state_machine.current_state.update()


    #Gets event passed as an argument by director loop. Identifies it and acts accordingly. Listens only to events allowed by current state. Still working on that
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.key == pygame.K_w:
                self.current_character.sprite.change_facing(Direction.UP)
                self.current_character.sprite.move_a_square()
                self.group_manager.determine_turn_queue()
                self.current_character = self.group_manager.get_next_character()
            if event.key == K_d:
                self.current_character.sprite.change_facing(Direction.RIGHT)
                self.current_character.sprite.move_a_square()
                self.group_manager.determine_turn_queue()
                self.current_character = self.group_manager.get_next_character()
            if event.key == K_s:
                self.current_character.sprite.change_facing(Direction.DOWN)
                self.current_character.sprite.move_a_square()
                self.group_manager.determine_turn_queue()
                self.current_character = self.group_manager.get_next_character()
            if event.key == K_a:
                self.current_character.sprite.change_facing(Direction.LEFT)
                self.current_character.sprite.move_a_square()
                self.group_manager.determine_turn_queue()
                self.current_character = self.group_manager.get_next_character()
            if event.key == K_SPACE:
                #This functionality on button click. Stores ability and during targetstate get target. Then perform damage calc on targets and check end turn and end battle
                self.selected_ability = self.current_character.abilities[1]
                self.state_machine.change_state(self.target_state)
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            
            # self.smage.set_facing((self.x_index, self.y_index))
            pass
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            self.smage.set_pos((self.x_index, self.y_index))
        
        if isinstance(self.state_machine.current_state, TurnState):
            for btn in self.state_machine.current_state.ability_buttons.values():
                if btn.clicked((self.x_world, self.y_world), event):
                    self.selected_ability = btn.ability
                    self.state_machine.change_state(self.target_state)
            


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
        
        if isinstance(self.state_machine.current_state, TargetState):
            self.state_machine.current_state.render()

        # Draw range indicator demo
        # self.cwar.abilities[0].draw_range_indicator(self.disp, self.cwar.sprite.tile)
        
        for tile in self.tilemap.map:
            #If there exists a sprite on tile, it is drawn there. Important for image layering
            for sprite in self.sprites:
                if tile.get_tile_coor() == sprite.pos:
                    sprite.draw_sprite(self.disp)



        # self.label_list.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (100, 25)), container= self.turn_order_panel, text=f"{self.current_character}",manager=self.manager))
        # for i in range(len(self.group_manager.character_queue)):
        #     self.label_list.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, (i+1)*20), (100, 25)), container= self.turn_order_panel, text=f"{self.group_manager.character_queue[i]}",manager=self.manager))
        #Panel 
        # turn_queue = pygame.Rect([0 + self.camera.x/2, 0 + self.camera.y/2 ,50, 200])
        
        screen.blit(pygame.transform.scale(self.disp, screen.get_size()), (0, 0), self.camera)

        #Disgusting. Back to the drawing board
        if isinstance(self.state_machine.current_state, TurnState):
            self.state_machine.current_state.render()

        #Create containers for ui elements. Move out of the loop
        turn_queue = pygame.Rect([screen.get_rect().topleft[0] , screen.get_rect().topleft[1] ,120, 235])
        # ability_panel = pygame.Rect([screen.get_rect().midleft[0], screen.get_rect().midleft[1] + 280, 450, 200])
        # name_panel = pygame.Rect([screen.get_rect().midleft[0], screen.get_rect().midleft[1] + 280, 225, 50])

        pygame.draw.rect(screen,(100, 100, 100), turn_queue)

        

        # pygame.draw.rect(screen,(100, 100, 100), ability_panel)
        # pygame.draw.rect(screen,(0, 0, 0), name_panel, 3)
        screen.blit(self.font.render("Turn Order:", True, (255, 255, 255)), (0, 10))
        screen.blit(self.font.render(self.current_character.name, True, (255, 255, 255)), (0, 30))
        for i in range(len(self.group_manager.character_queue)):
            screen.blit(self.font.render(self.group_manager.character_queue[i].name, True, (255, 255, 255)), (0, 50+(i*20)))








