# Modules
from config import SCREEN_SIZE_X, SCREEN_SIZE_Y
from battle_scene import BattleScene
import pygame
import director
import scene_home
 
def main():
    dir = director.Director()
    print("Director created")
    scene = BattleScene(dir)
    dir.change_scene(scene)
    dir.loop()
 
if __name__ == '__main__':
    pygame.init()
    print("init called")
    main()