# Modules
from pygame.event import clear
from data.attributes.attribute_id import AttributeId
import sys

import pygame

from data.attributes.attribute import Attribute

from data.abilities import ability
from data.abilities.bash import Bash
from data.character import Character
from data.config import SCREEN_SIZE_X, SCREEN_SIZE_Y
from data.abilities.face import Face
from data.abilities.holy import Holy
from data.abilities.jump_back import JumpBack
from data.abilities.move import Move
from data.abilities.slash import Slash
from data.abilities.spear_throw import SpearThrow
from data.abilities.spin import Spin
from data.sprite import DOWN, UP, Sprite
from data.attributes.stat_collection import StatCollection
from data.tile import Tile
from data.tilemap import TileMap
from data.abilities.wait import Wait
from data.wolf import Wolf


class Director:
    """Represents the main object of the game.

    The Director object keeps the game on, and takes care of updating it,
    drawing it and propagate events.

    This object must be used with Scene objects that are defined later."""

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
        print("pygame.display initialized!")
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Tile based board demo")
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        self.time_delta = None

        # Initialize characters in demo
        # Ready sprites
        self.mage_up = pygame.image.load("resources/img/mage_up.png").convert()
        self.mage_up.set_colorkey((0, 0, 0))
        self.mage_right = pygame.image.load("resources/img/mage_right.png").convert()
        self.mage_right.set_colorkey((0, 0, 0))
        self.mage_down = pygame.image.load("resources/img/mage_down.png").convert()
        self.mage_down.set_colorkey((0, 0, 0))
        self.mage_left = pygame.image.load("resources/img/mage_left.png").convert()
        self.mage_left.set_colorkey((0, 0, 0))
        self.wolf = pygame.image.load("resources/img/wolf.png").convert()
        self.wolf.set_colorkey((0, 0, 0))
        self.wolf_sheet = pygame.image.load(
            "resources/img/wolf_down-sheet.png").convert()
        self.wolf_sheet.set_colorkey((0, 0, 0))
        self.warrior = pygame.image.load("resources/img/warrior.png").convert()
        self.warrior.set_colorkey((0, 0, 0))
        self.thief = pygame.image.load("resources/img/thief_down.png").convert()
        self.thief.set_colorkey((0, 0, 0))
        self.tr = pygame.image.load("resources/img/wrsprite.png").convert()
        self.tr.set_colorkey((0, 0, 0))
        self.selected_tile = pygame.image.load("resources/img/yrsprite.png").convert()
        self.selected_tile.set_colorkey((0, 0, 0))
        self.zone_indicator = pygame.image.load("resources/img/wbsprite.png").convert()
        self.zone_indicator.set_colorkey((0, 0, 0))

        # # Ready the map
        # f = open('resources/map_full.txt')
        # read_map = [[int(c) for c in row] for row in f.read().split('\n')]
        # f.close()

        # map = []
        # for y, row in enumerate(read_map):
        #     for x, index in enumerate(row):
        #         map.append(Tile(x, y))
        # # Create TileMap object. Used to store the list of tiles and provides functions to acess tiles given coordinates
        # self.tilemap = TileMap(13, 13, map)


        self.map = []

        for i in range(14):
            row = []
            for j in range(14):
                row.append(Tile(i, j))
            self.map.append(row)
            
        # #Test tile coordinates
        # for row in self.map:
        #     for tile in row:
        #         print(tile.get_tile_coor())
        # print(self.map[6][6])

        # Initialize sprites and characters for the demop
        self.smage = Sprite('mage', (4, 9), DOWN, self.map, [
                            self.mage_down, self.mage_right, self.mage_up, self.mage_left])
        wmhp = Attribute(AttributeId.HP, 50, 'Health', 'Hit points until down')
        wms = Attribute(AttributeId.STRENGTH, 5,
                        'Health', 'Hit points until down')
        wma = Attribute(AttributeId.AGILITY, 10,
                        'Health', 'Hit points until down')
        sc = StatCollection()
        sc.add_to_dict(AttributeId.HP, wmhp)
        sc.add_to_dict(AttributeId.STRENGTH, wms)
        sc.add_to_dict(AttributeId.AGILITY, wma)
        self.cmage = Character('WhiteMage', sc, self.smage,
                               scene=self, counter=2, innate_counter=14)

        self.swolf1 = Sprite('wolf', (2, 3), UP, self.map, [self.wolf])
        self.swolf2 = Sprite('wolf', (6, 3), UP, self.map, [self.wolf])
        self.swolf3 = Sprite('wolf', (9, 3), UP, self.map, [self.wolf])
        self.swolf4 = Sprite('wolf', (11, 3), UP, self.map, [self.wolf])
        whp1 = Attribute(AttributeId.HP, 100, 'Health',
                         'Hit points until down')
        ws1 = Attribute(AttributeId.STRENGTH, 5,
                        'Health', 'Hit points until down')
        wa1 = Attribute(AttributeId.AGILITY, 10,
                        'Health', 'Hit points until down')
        whp2 = Attribute(AttributeId.HP, 100, 'Health',
                         'Hit points until down')
        ws2 = Attribute(AttributeId.STRENGTH, 5,
                        'Health', 'Hit points until down')
        wa2 = Attribute(AttributeId.AGILITY, 10,
                        'Health', 'Hit points until down')
        whp3 = Attribute(AttributeId.HP, 100, 'Health',
                         'Hit points until down')
        ws3 = Attribute(AttributeId.STRENGTH, 5,
                        'Health', 'Hit points until down')
        wa3 = Attribute(AttributeId.AGILITY, 10,
                        'Health', 'Hit points until down')
        whp4 = Attribute(AttributeId.HP, 100, 'Health',
                         'Hit points until down')
        ws4 = Attribute(AttributeId.STRENGTH, 5,
                        'Health', 'Hit points until down')
        wa4 = Attribute(AttributeId.AGILITY, 10,
                        'Health', 'Hit points until down')
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
        self.cwolf1 = Wolf('Wolf 1', scw1, self.swolf1, playable=False,
                           scene=self, counter=7, innate_counter=10)
        self.cwolf2 = Wolf('Wolf 2', scw2, self.swolf2, playable=False,
                           scene=self, counter=7, innate_counter=10)
        self.cwolf3 = Wolf('Wolf 3', scw3, self.swolf3, playable=False,
                           scene=self, counter=7, innate_counter=10)
        self.cwolf4 = Wolf('Wolf 4', scw4, self.swolf4, playable=False,
                           scene=self, counter=7, innate_counter=10)

        self.swarrior = Sprite('warrior', (6, 8), DOWN,
                               self.map, [self.warrior])
        ahp = Attribute(AttributeId.HP, 120, 'Health', 'Hit points until down')
        ams = Attribute(AttributeId.STRENGTH, 5,
                        'Health', 'Hit points until down')
        ama = Attribute(AttributeId.AGILITY, 10,
                        'Health', 'Hit points until down')
        sca = StatCollection()
        sca.add_to_dict(AttributeId.HP, ahp)
        sca.add_to_dict(AttributeId.STRENGTH, ams)
        sca.add_to_dict(AttributeId.AGILITY, ama)
        self.cwar = Character('Warrior', sca, self.swarrior,
                              scene=self.scene, counter=5, innate_counter=8)

        self.sthief = Sprite('thief', (8, 9), DOWN, self.map, [self.thief])
        thp = Attribute(AttributeId.HP, 80, 'Health', 'Hit points until down')
        ts = Attribute(AttributeId.STRENGTH, 5,
                       'Health', 'Hit points until down')
        ta = Attribute(AttributeId.AGILITY, 20,
                       'Health', 'Hit points until down')
        sct = StatCollection()
        sct.add_to_dict(AttributeId.HP, thp)
        sct.add_to_dict(AttributeId.STRENGTH, ts)
        sct.add_to_dict(AttributeId.AGILITY, ta)
        self.cthief = Character('Thief', sct, self.sthief, scene=self.scene,
                                base_action_points=5, counter=1, innate_counter=6)

        self.attack = ability.Ability(
            "Attack", 20, 2, 1, ability.TargetingType.SINGLE)
        self.bash = Bash("Bash", 20, 2, 1,
                         ability.TargetingType.SINGLE, self.cmage)
        self.slash = Slash("Slash", 30, 2, 1,
                           ability.TargetingType.AOE, self.cwar)
        self.bite = ability.Ability(
            "Bite", 20, 1, 1, ability.TargetingType.SINGLE)
        self.knife_throw = ability.Ability(
            "Knife Throw", 20, 2, 4, ability.TargetingType.SINGLE, "Throw knife for long range damage")

        self.face = Face("Face", 0, 1, 1, ability.TargetingType.FACE)

        self.move = Move("Move", 0, 1, 0, ability.TargetingType.MOVE)
        self.jump_back = JumpBack(
            "Jump Back", 0, 1, 0, ability.TargetingType.AOE)

        self.heal = ability.Ability(
            "Heal", -40, 3, 3, ability.TargetingType.SINGLE, description="Restore some HP")
        self.spin = Spin("Spin", 30, 2, 1,
                         ability.TargetingType.AOE, self.cthief)
        self.holy = Holy("Holy", 100, 4, 1,
                         ability.TargetingType.ALL, user=self.cmage)
        self.spear_throw = SpearThrow(
            "Spear Throw", 40, 2, 1, ability.TargetingType.AOE, self.cwar)

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

        self.characters = [self.cmage, self.cwar, self.cwolf1,
                           self.cwolf2, self.cwolf3, self.cwolf4, self.cthief]

    def loop(self):
        "Main game loop."

        while not self.quit_flag:
            # self.time_delta = self.clock.tick(60)/1000.0
            self.time_delta = self.clock.tick(60)

            # Exit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()

                # Detect events
                self.scene.on_event(event)
                # self.scene.manager.process_events(event)

            # Update scene

            self.scene.on_update()
            # self.scene.manager.update(self.time_delta)

            # Draw the screen

            self.scene.on_draw(self.screen)
            # self.scene.manager.draw_ui(self.screen)
            pygame.display.flip()

    def change_scene(self, scene):
        "Changes the current scene."
        self.scene = scene

    def quit(self):
        self.quit_flag = True
