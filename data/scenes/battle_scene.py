import os
import random
import sys
import time
from collections import deque
from typing import Tuple

import pygame
from pygame import *

import data.abilities.ability
import data.projection as projection
from data.config import *

from data.group_manager import GroupManager
from data.scenes.scene import Scene
from data.states.state_machine import StateMachine
from data.states.target_state import TargetState
from data.states.turn_state import TurnState
import data.scenes.defeat
import data.scenes.win

class BattleScene(Scene):

    def __init__(self, director):
        Scene.__init__(self, director)
        self.camera = director.screen.get_rect()
        self.disp = pygame.Surface((DSX, DSY)).convert()
        self.x_world = (0, 0)
        self.y_world = (0, 0)
        self.x_index = (0, 0)
        self.x_index = (0, 0)

        # Create TileMap object. Used to store the list of tiles and provides functions to acess tiles given coordinates
        self.map = director.map
        # Sprites for drawing the board
        self.tr = director.tr
        self.zone_indicator = director.zone_indicator
        self.selected_tile = director.selected_tile
        # Get characters in encounter from directors party_data
        self.characters = director.characters
        # Update character scene
        for character in self.characters:
            character.scene = self

        # Background sound
        pygame.mixer.music.load('resources/sound/The Hero Approaches.wav')
        mixer.music.play(loops=-1)

        # TODO TEST RIGOROUSLY
        self.group_manager = GroupManager(self.characters)
        self.group_manager.determine_turn_queue()
        # Initialize state relevant data
        self.current_character = self.group_manager.get_next_character()
        self.target = None
        self.selected_ability = None
        self.current_tile = None
        # Initialize states
        self.turn_state = TurnState(director, self)
        self.target_state = TargetState(director, self)
        self.state_machine = StateMachine(self.turn_state)

        # Panel font. Probably will make this a class
        self.font = pygame.font.Font("resources/font/PressStart2P-vaV7.ttf", 10)
        # Create containers for ui elements. Move out of the loop
        self.turn_queue = pygame.Rect([director.screen.get_rect(
        ).topleft[0], director.screen.get_rect().topleft[1], 120, 310])

    def upkeep(self):
        if self.group_manager.dead_character_indicator == True:
            print("Removing dead characters at the end of turn")
            self.group_manager.remove_dead_characters()
            if self.group_manager.player_party_is_empty() == True:
                self.director.change_scene(data.scenes.defeat.Defeat(self.director))
            elif self.group_manager.enemy_party_is_empty() == True:
                self.director.change_scene(data.scenes.win.Win(self.director))
        self.end_turn()

    def end_turn(self):
        print("Ending turn")
        self.current_character.action_points = self.current_character.base_action_points
        self.group_manager.determine_turn_queue()
        self.current_character = self.group_manager.get_next_character()
        self.state_machine.change_state(self.turn_state)

    def get_tiles_from_coordinate_list(self, list):
        list_of_tiles = []
        for tuple in list:
            list_of_tiles.append(self.map[tuple[0]][tuple[1]])
        return list_of_tiles

    def on_update(self):
        # Keeps track where the mouse is pointing and converts it into isometric indices
        self.x_world, self.y_world = pygame.mouse.get_pos()
        self.x_index, self.y_index = projection.reverse_isometricprojection(
            self.x_world - (DSX - self.camera.x), self.y_world - (DSY - self.camera.y), 64, 32)
        self.x_index = self.x_index - 1
        # Restric to map size
        self.x_index = projection.restrict(self.x_index, 0, 13)
        self.y_index = projection.restrict(self.y_index, 0, 13)

        self.current_tile = self.map[self.x_index][self.y_index]
        # print(self.x_index, end = ", ")
        # print(self.y_index)
        # if self.current_tile.occupier_character is None:
        #     print("No one on tile")
        # else:
        #     print(self.current_tile.occupier_character.name)

        keys = pygame.key.get_pressed()
        # Camera movement
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
                        self.director.change_scene(data.scenes.win.Win(self.director))
                    elif self.group_manager.enemy_party_is_empty() == True:
                        self.director.change_scene(data.scenes.defeat.Defeat(self.director))
            else:
                self.current_character.action_points = self.current_character.base_action_points
                self.upkeep()

    # Gets event passed as an argument by director loop. Identifies it and acts accordingly. Listens only to events allowed by current state. Still working on that
    def on_event(self, event):
        # This part of the event functions events are tracked on every frame
        ###########################################################################################################################################################
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            print(f"Current sprite tile: {self.current_character.tile}")

        # If the current state is Target state, this parts events are checked and executed if applicapble
        ###########################################################################################################################################################
        if isinstance(self.state_machine.current_state, TargetState):

            if self.selected_ability.targeting_type == data.abilities.ability.TargetingType.MOVE:
                if self.current_tile == self.current_character.sprite.facing_tile and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.current_character.sprite.move_a_square() == True:
                        self.current_character.action_points = self.current_character.action_points - \
                            self.selected_ability.ap_cost
                    if self.current_character.action_points > 0:
                        self.state_machine.change_state(self.turn_state)
                    else:
                        self.end_turn()

            if self.selected_ability.targeting_type == data.abilities.ability.TargetingType.FACE:
                if self.current_tile in self.get_tiles_from_coordinate_list(self.selected_ability.get_tiles_in_range(self.current_character.sprite.tile)) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.current_character.sprite.set_facing((self.x_index, self.y_index)) == True:
                        self.current_character.action_points = self.current_character.action_points - \
                            self.selected_ability.ap_cost
                    if self.current_character.action_points > 0:
                        self.state_machine.change_state(self.turn_state)
                    else:
                        self.end_turn()

            if self.selected_ability.targeting_type == data.abilities.ability.TargetingType.SINGLE:
                if self.current_tile in self.selected_ability.get_possible_targets(self.get_tiles_from_coordinate_list(self.selected_ability.get_tiles_in_range(self.current_character.sprite.tile))) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.selected_ability.activate()

            if self.selected_ability.targeting_type == data.abilities.ability.TargetingType.AOE and event.type == MOUSEBUTTONDOWN and event.button == 1:
                print(f"Activated ability {self.selected_ability.name}")
                self.selected_ability.activate()
            if self.selected_ability.targeting_type == data.abilities.ability.TargetingType.ALL and event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.selected_ability.activate()

            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                self.state_machine.change_state(self.turn_state)
                self.selected_ability = None

        # If the current state is Turn state, this parts events are checked and executed if applicapble
        ###########################################################################################################################################################
        if isinstance(self.state_machine.current_state, TurnState) and self.current_character.playable == True:
            for btn in self.state_machine.current_state.ability_buttons.values():
                if btn.clicked((self.x_world, self.y_world), event) and self.current_character.can_take_action(btn.ability):
                    self.selected_ability = btn.ability
                    print(
                        f"Clicked button: {self.selected_ability.description}")
                    self.state_machine.change_state(self.target_state)
        if isinstance(self.state_machine.current_state, TurnState) and self.current_character.playable == True:
            for btn in self.state_machine.current_state.utility_buttons.values():
                if btn.clicked((self.x_world, self.y_world), event) and self.current_character.can_take_action(btn.ability):
                    # btn.ability.activate()
                    self.current_character.action_points = self.current_character.base_action_points
                    self.group_manager.determine_turn_queue()
                    self.current_character = self.group_manager.get_next_character()
                    self.state_machine.change_state(self.turn_state)

    def on_draw(self, screen):
        screen.fill((0, 0, 0))
        self.disp.fill((0, 0, 0))

        for row in self.map:
            for tile in row:
                # Highlights currently selected tile
                if tile.xcoor == self.x_index and tile.ycoor == self.y_index:
                    self.disp.blit(self.selected_tile, (projection.isometricprojection(
                        self.x_index, self.y_index, 32, 16, (DSX / 2), (DSY / 2))))
                # Blits arena tile on current tile
                else:
                    if tile.xcoor != 0 and tile.ycoor != 0 and tile.xcoor != 13 and tile.ycoor != 13:
                        self.disp.blit(self.tr, projection.isometricprojection(
                            tile.xcoor, tile.ycoor, 32, 16, (DSX / 2), (DSY / 2)))
                # #Loops through the current tiles adjecant tiles and blits a zone indicator tile on each of them
                # for adj in projection.get_adjecant_squares(self.x_index, self.y_index, 13):
                #     self.disp.blit(self.zone_indicator, projection.isometricprojection(adj[0], adj[1], 32, 16, (DSX / 2), (DSY / 2)))

        # Disgusting. Back to the drawing board
        if isinstance(self.state_machine.current_state, TargetState):
            self.state_machine.current_state.render()

        self.disp.blit(self.zone_indicator, projection.isometricprojection(
            self.current_character.sprite.facing[0], self.current_character.sprite.facing[1], 32, 16, (self.disp.get_size()[0] / 2), (self.disp.get_size()[1] / 2)))
        for row in self.map:
            for tile in row:
                # If there exists a sprite on tile, it is drawn there. Important for image layering
                for character in self.characters:
                    if tile.get_tile_coor() == character.sprite.pos:
                        character.sprite.draw_sprite(self.disp)
                        tile.occupier_character = character

        screen.blit(pygame.transform.scale(
            self.disp, screen.get_size()), (0, 0), self.camera)

        # Disgusting. Back to the drawing board
        if isinstance(self.state_machine.current_state, TargetState):
            self.state_machine.current_state.render()
        # Disgusting. Back to the drawing board
        if isinstance(self.state_machine.current_state, TurnState):
            self.state_machine.current_state.render()

        pygame.draw.rect(screen, (100, 100, 100), self.turn_queue)

        screen.blit(self.font.render("Turn Order:",
                    True, (255, 255, 255)), (0, 10))
        screen.blit(self.font.render(self.current_character.name,
                    True, (255, 255, 255)), (0, 30))
        for i in range(len(self.group_manager.character_queue)):
            screen.blit(self.font.render(
                self.group_manager.character_queue[i].name, True, (255, 255, 255)), (0, 50+(i*20)))
