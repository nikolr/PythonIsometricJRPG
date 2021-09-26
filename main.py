import pygame

from data import director
from data.scenes import title


def main():
    dir = director.Director()
    scene = title.Title(dir)
    dir.change_scene(scene)
    dir.loop()
 
if __name__ == '__main__':
    pygame.init()
    main()
