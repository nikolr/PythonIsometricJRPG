from wait import Wait
from jump_back import JumpBack
from spear_throw import SpearThrow
from holy import Holy
from spin import Spin
from slash import Slash
from bash import Bash
from wolf import Wolf
from defeat import Defeat
from win import Win
from move import Move
from typing import Tuple
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

from sprite import DOWN, LEFT, UP, Direction, Sprite
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
        self.wolf_sheet = pygame.image.load("img/wolf_down-sheet.png").convert()
        self.wolf_sheet.set_colorkey((0, 0, 0))
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

        # #Test tile coordinates
        # for tile in self.tilemap.map:
        #     print(tile.get_tile_coor())

        #Initialize sprites and characters for the demop
        self.smage = Sprite('mage', (4, 9), DOWN, self.tilemap, [self.mage_down, self.mage_right, self.mage_up , self.mage_left])
        wmhp = Attribute(AttributeId.HP, 50, 'Health', 'Hit points until down')
        wms = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wma = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sc = StatCollection()
        sc.add_to_dict(AttributeId.HP, wmhp)
        sc.add_to_dict(AttributeId.STRENGTH, wms)
        sc.add_to_dict(AttributeId.AGILITY, wma)
        self.cmage = Character('WhiteMage', sc, self.smage, scene= self, counter = 2, innate_counter= 14)

        self.swolf1 = Sprite('wolf', (2, 3), UP, self.tilemap, [self.wolf])
        self.swolf2 = Sprite('wolf', (6, 3), UP, self.tilemap, [self.wolf])
        self.swolf3 = Sprite('wolf', (9, 3), UP, self.tilemap, [self.wolf])
        self.swolf4 = Sprite('wolf', (11, 3), UP, self.tilemap, [self.wolf])
        whp1 = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ws1= Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wa1= Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        whp2 = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ws2= Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wa2= Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        whp3 = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ws3= Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wa3= Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        whp4 = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ws4= Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wa4= Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        scw1 = StatCollection()
        scw1.add_to_dict(AttributeId.HP, whp1)
        scw1.add_to_dict(AttributeId.STRENGTH, ws1)
        scw1.add_to_dict(AttributeId.AGILITY, wa1)
        scw2 = StatCollection()
        scw2.add_to_dict(AttributeId.HP, whp2)
        scw2.add_to_dict(AttributeId.STRENGTH, ws2)
        scw2.add_to_dict(AttributeId.AGILITY, wa2)
        scw3 = StatCollection()
        scw3.add_to_dict(AttributeId.HP, whp3)
        scw3.add_to_dict(AttributeId.STRENGTH, ws3)
        scw3.add_to_dict(AttributeId.AGILITY, wa3)
        scw4 = StatCollection()
        scw4.add_to_dict(AttributeId.HP, whp4)
        scw4.add_to_dict(AttributeId.STRENGTH, ws4)
        scw4.add_to_dict(AttributeId.AGILITY, wa4)
        self.cwolf1 = Wolf('Wolf 1', scw1, self.swolf1, playable= False, scene= self, counter = 7, innate_counter= 10)
        self.cwolf2 = Wolf('Wolf 2', scw2, self.swolf2, playable= False, scene= self, counter = 7, innate_counter= 10)
        self.cwolf3 = Wolf('Wolf 3', scw3, self.swolf3, playable= False, scene= self, counter = 7, innate_counter= 10)
        self.cwolf4 = Wolf('Wolf 4', scw4, self.swolf4, playable= False, scene= self, counter = 7, innate_counter= 10)

        self.swarrior = Sprite('warrior', (6, 8), DOWN, self.tilemap, [self.warrior])
        ahp = Attribute(AttributeId.HP, 120, 'Health', 'Hit points until down')
        ams = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        ama = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sca = StatCollection()
        sca.add_to_dict(AttributeId.HP, ahp)
        sca.add_to_dict(AttributeId.STRENGTH, ams)
        sca.add_to_dict(AttributeId.AGILITY, ama)
        self.cwar = Character('Warrior', sca, self.swarrior, scene= self, counter = 5, innate_counter= 8)

        self.sthief = Sprite('thief', (8, 9), DOWN, self.tilemap, [self.thief])
        thp = Attribute(AttributeId.HP, 80, 'Health', 'Hit points until down')
        ts = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        ta = Attribute(AttributeId.AGILITY, 20, 'Health', 'Hit points until down')
        sct = StatCollection()
        sct.add_to_dict(AttributeId.HP, thp)
        sct.add_to_dict(AttributeId.STRENGTH, ts)
        sct.add_to_dict(AttributeId.AGILITY, ta)
        self.cthief = Character('Thief', sct, self.sthief, scene= self, base_action_points= 5 , counter = 1, innate_counter= 6)

        self.attack = ability.Ability("Attack", 20, 2, 1, ability.TargetingType.SINGLE)
        self.bash = Bash("Bash", 20, 2, 1, ability.TargetingType.SINGLE, self.cmage)
        self.slash = Slash("Slash", 30, 2, 1, ability.TargetingType.AOE, self.cwar)
        self.bite = ability.Ability("Bite", 20, 1, 1, ability.TargetingType.SINGLE)
        self.knife_throw = ability.Ability("Knife Throw", 20, 2, 4, ability.TargetingType.SINGLE, "Throw knife for long range damage")

        self.face = Face("Face", 0, 1, 1, ability.TargetingType.FACE)

        self.move = Move("Move", 0, 1, 0, ability.TargetingType.MOVE)
        self.jump_back = JumpBack("Jump Back", 0, 1, 0, ability.TargetingType.AOE)

        self.heal = ability.Ability("Heal", -40, 3, 3, ability.TargetingType.SINGLE,description="Restore some HP")
        self.spin = Spin("Spin", 30, 2, 1, ability.TargetingType.AOE, self.cthief)
        self.holy = Holy("Holy", 100, 4, 1, ability.TargetingType.ALL ,user=self.cmage)
        self.spear_throw = SpearThrow("Spear Throw", 40, 2, 1, ability.TargetingType.AOE, self.cwar) 

        self.wait = Wait("Wait", 0, 0, 0, 0, self)

        self.cwar.gain_ability(self.move)     
        self.cwar.gain_ability(self.face)
        self.cwar.gain_ability(self.slash)
        self.cwar.gain_ability(self.spear_throw)

        self.cmage.gain_ability(self.move)
        self.cmage.gain_ability(self.face)
        self.cmage.gain_ability(self.bash)
        self.cmage.gain_ability(self.heal)
        self.cmage.gain_ability(self.holy)

        self.cthief.gain_ability(self.move)
        self.cthief.gain_ability(self.jump_back)
        self.cthief.gain_ability(self.face)
        self.cthief.gain_ability(self.knife_throw)
        self.cthief.gain_ability(self.spin)

        self.cwolf1.gain_ability(self.move)
        self.cwolf1.gain_ability(self.face)
        self.cwolf1.gain_ability(self.bite)
        

        self.cwolf2.gain_ability(self.move)
        self.cwolf2.gain_ability(self.face)
        self.cwolf2.gain_ability(self.bite)
        

        self.cwolf3.gain_ability(self.move)
        self.cwolf3.gain_ability(self.face)
        self.cwolf3.gain_ability(self.bite)
        

        self.cwolf4.gain_ability(self.move)
        self.cwolf4.gain_ability(self.face)
        self.cwolf4.gain_ability(self.bite)
        

        

        self.characters = [self.cmage, self.cwar, self.cwolf1, self.cwolf2, self.cwolf3, self.cwolf4, self.cthief]
        # self.sprites = [self.smage]

        # Background sound
        pygame.mixer.music.load('The Hero Approaches.wav')
        mixer.music.play(loops=-1)




        #TODO TEST RIGOROUSLY
        self.group_manager = GroupManager([self.cmage, self.cwolf1, self.cwolf2, self.cwolf3, self.cwolf4, self.cwar, self.cthief])
        self.group_manager.determine_turn_queue()
        self.current_character = self.group_manager.get_next_character()
        self.target = None
        self.turn_state = TurnState(self.director, self)
        self.target_state = TargetState(self.director, self)
        self.state_machine = StateMachine(self.turn_state)

        self.selected_ability = None
        self.current_tile = None


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

    
    def upkeep(self):
        if self.group_manager.dead_character_indicator == True:
            print("Removing dead characters at the end of turn")
            self.group_manager.remove_dead_characters()
            if self.group_manager.player_party_is_empty() == True:
                self.director.change_scene(Defeat(self.director))
            elif self.group_manager.enemy_party_is_empty() == True:
                self.director.change_scene(Win(self.director))
        self.end_turn()
    
    def end_turn(self):
        print("Ending turn")
        self.current_character.action_points = self.current_character.base_action_points
        self.group_manager.determine_turn_queue()
        self.current_character = self.group_manager.get_next_character()
        self.state_machine.change_state(self.turn_state)


    def on_update(self):
        #Keeps track where the mouse is pointing and converts it into isometric indices
        self.x_world, self.y_world = pygame.mouse.get_pos()
        self.x_index, self.y_index = projection.reverse_isometricprojection(self.x_world - (DSX - self.camera.x), self.y_world - (DSY - self.camera.y), 64, 32)
        self.x_index = self.x_index - 1
        #Restric to map size
        self.x_index = projection.restrict(self.x_index, 0, 13)
        self.y_index = projection.restrict(self.y_index, 0, 13)

        self.current_tile = self.tilemap.get_tile_in_coor(self.x_index, self.y_index)
        # print(self.x_index, end = ", ")
        # print(self.y_index)
        # if self.current_tile.occupier_character is None:
        #     print("No one on tile")
        # else:
        #     print(self.current_tile.occupier_character.name)
    
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

        if isinstance(self.state_machine.current_state, TurnState) and self.current_character.playable == False:
            if self.current_character.action_points > 0:
                self.current_character.act()
                if self.group_manager.dead_character_indicator == True:
                                print("Removing dead characters at the end of turn")
                                self.group_manager.remove_dead_characters()
                                if self.group_manager.player_party_is_empty() == True:
                                    self.director.change_scene(Win(self.director))
                                elif self.group_manager.enemy_party_is_empty() == True:
                                    self.director.change_scene(Defeat(self.director))
            else:
                self.current_character.action_points = self.current_character.base_action_points
                self.upkeep()


    #Gets event passed as an argument by director loop. Identifies it and acts accordingly. Listens only to events allowed by current state. Still working on that
    def on_event(self, event):
        #This part of the event functions events are tracked on every frame
        ###########################################################################################################################################################

        
        #If the current state is Target state, this parts events are checked and executed if applicapble
        ###########################################################################################################################################################
        if isinstance(self.state_machine.current_state, TargetState):

            if self.selected_ability.targeting_type == ability.TargetingType.MOVE:
                if self.current_tile == self.current_character.sprite.facing_tile and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.current_character.sprite.move_a_square() == True:
                        self.current_character.action_points = self.current_character.action_points - self.selected_ability.ap_cost
                    if self.current_character.action_points > 0:
                        self.state_machine.change_state(self.turn_state)
                    else:
                        self.end_turn()

            if self.selected_ability.targeting_type == ability.TargetingType.FACE:
                            if self.current_tile in self.tilemap.get_tiles_in_coords(self.selected_ability.get_tiles_in_range(self.current_character.sprite.tile)) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                                if self.current_character.sprite.set_facing((self.x_index, self.y_index)) == True:
                                    self.current_character.action_points = self.current_character.action_points - self.selected_ability.ap_cost
                                if self.current_character.action_points > 0:
                                    self.state_machine.change_state(self.turn_state)
                                else:
                                    self.end_turn()
   
            if self.selected_ability.targeting_type == ability.TargetingType.SINGLE:
                if self.current_tile in self.selected_ability.get_possible_targets(self.tilemap.get_tiles_in_coords(self.selected_ability.get_tiles_in_range(self.current_character.sprite.tile))) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.selected_ability.activate()

            if self.selected_ability.targeting_type == ability.TargetingType.AOE and event.type == MOUSEBUTTONDOWN and event.button == 1:
                print(f"Activated ability {self.selected_ability.name}")
                self.selected_ability.activate()
            if self.selected_ability.targeting_type == ability.TargetingType.ALL and event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.selected_ability.activate()

            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                self.state_machine.change_state(self.turn_state)
                self.selected_ability = None

        #If the current state is Turn state, this parts events are checked and executed if applicapble
        ###########################################################################################################################################################
        if isinstance(self.state_machine.current_state, TurnState) and self.current_character.playable == True:
            for btn in self.state_machine.current_state.ability_buttons.values():
                if btn.clicked((self.x_world, self.y_world), event) and self.current_character.can_take_action(btn.ability):
                    self.selected_ability = btn.ability
                    print(f"Clicked button: {self.selected_ability.description}")
                    self.state_machine.change_state(self.target_state)
        if isinstance(self.state_machine.current_state, TurnState) and self.current_character.playable == True:
            for btn in self.state_machine.current_state.utility_buttons.values(): 
                if btn.clicked((self.x_world, self.y_world), event) and self.current_character.can_take_action(btn.ability):
                    btn.ability.activate()
            
    def on_draw(self, screen):
        screen.fill((0,0,0))
        self.disp.fill((0,0,0))
        
        for tile in self.tilemap.map:
            #Highlights currently selected tile
            if tile.xcoor == self.x_index and tile.ycoor == self.y_index:
                self.disp.blit(self.selected_tile, (projection.isometricprojection(self.x_index, self.y_index, 32, 16, (DSX / 2), (DSY / 2))))
            #Blits arena tile on current tile 
            else:
                if tile.xcoor != 0 and tile.ycoor != 0 and tile.xcoor != 13 and tile.ycoor != 13:
                    self.disp.blit(self.tr, projection.isometricprojection(tile.xcoor, tile.ycoor, 32, 16, (DSX / 2), (DSY / 2)))
            # #Loops through the current tiles adjecant tiles and blits a zone indicator tile on each of them
            # for adj in projection.get_adjecant_squares(self.x_index, self.y_index, 13):
            #     self.disp.blit(self.zone_indicator, projection.isometricprojection(adj[0], adj[1], 32, 16, (DSX / 2), (DSY / 2)))
        
        if isinstance(self.state_machine.current_state, TargetState):
            self.state_machine.current_state.render()


        self.disp.blit(self.zone_indicator, projection.isometricprojection(self.current_character.sprite.facing[0], self.current_character.sprite.facing[1], 32, 16, (self.disp.get_size()[0] / 2), (self.disp.get_size()[1] / 2)))
        for tile in self.tilemap.map:
            #If there exists a sprite on tile, it is drawn there. Important for image layering
            for character in self.characters:
                if tile.get_tile_coor() == character.sprite.pos:
                    character.sprite.draw_sprite(self.disp)
                    tile.occupier_character = character
                    



        # self.label_list.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (100, 25)), container= self.turn_order_panel, text=f"{self.current_character}",manager=self.manager))
        # for i in range(len(self.group_manager.character_queue)):
        #     self.label_list.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, (i+1)*20), (100, 25)), container= self.turn_order_panel, text=f"{self.group_manager.character_queue[i]}",manager=self.manager))
        #Panel 
        # turn_queue = pygame.Rect([0 + self.camera.x/2, 0 + self.camera.y/2 ,50, 200])
        
        screen.blit(pygame.transform.scale(self.disp, screen.get_size()), (0, 0), self.camera)
        
        #Disgusting. Back to the drawing board
        if isinstance(self.state_machine.current_state, TargetState):
            self.state_machine.current_state.render()
        #Disgusting. Back to the drawing board
        if isinstance(self.state_machine.current_state, TurnState):
            self.state_machine.current_state.render()

        #Create containers for ui elements. Move out of the loop
        turn_queue = pygame.Rect([screen.get_rect().topleft[0] , screen.get_rect().topleft[1] ,120, 310])
        # ability_panel = pygame.Rect([screen.get_rect().midleft[0], screen.get_rect().midleft[1] + 280, 450, 200])
        # name_panel = pygame.Rect([screen.get_rect().midleft[0], screen.get_rect().midleft[1] + 280, 225, 50])

        pygame.draw.rect(screen,(100, 100, 100), turn_queue)

        

        # pygame.draw.rect(screen,(100, 100, 100), ability_panel)
        # pygame.draw.rect(screen,(0, 0, 0), name_panel, 3)
        screen.blit(self.font.render("Turn Order:", True, (255, 255, 255)), (0, 10))
        screen.blit(self.font.render(self.current_character.name, True, (255, 255, 255)), (0, 30))
        for i in range(len(self.group_manager.character_queue)):
            screen.blit(self.font.render(self.group_manager.character_queue[i].name, True, (255, 255, 255)), (0, 50+(i*20)))








