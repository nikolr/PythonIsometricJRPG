from os import stat
from typing import Tuple
from operator import sub




def isometricprojection(x_index: int, y_index: int, tilewidth: int, tileheight: int, offset_world_x: int, offset_world_y: int) -> Tuple[float, float]:
    """Takes the indices of Tile object and returns tuple of isometric coordinates in screen space"""
    x = (x_index - y_index) * (tilewidth/2) + offset_world_x
    y = (x_index + y_index) * (tileheight/2) + offset_world_y
    return (x,y)
    

def reverse_isometricprojection(x: float, y: float, tilewidth: int, tileheight: int) -> Tuple[int, int]:
    x_index = ((x) / (tilewidth) + ((y) / (tileheight)))
    y_index = ((y) / (tileheight) - ((x) / (tilewidth)))
    return (x_index, y_index)

# Create a method that gives the range of possible values for world coordinates x and y given a certain tile with indices x_index and y_index
# 
# def ranges(x_index: int, y_index: int, tilewidth: int, tileheight: int) -> Tuple[float, float]:
#     x_limit_right = Projection.isometricprojection(x_index + 1, y_index, tilewidth, tileheight)[0]
#     x_limit_left
#     y_limit = Projection.isometricprojection(x_index + 1, y_index + 1, tilewidth, tileheight)[1]
#     return (x_limit, y_limit)

#Create a method that checks if the current mouse position is within given tile. Tile coordinates given as indices

def is_over_tile(x_world, y_world, x_index, y_index, tilewidth: int, tileheight: int) -> bool:
    if reverse_isometricprojection(x_world, y_world, tilewidth, tileheight) == (x_index, y_index):
        return True
    else:
        return False
    

def get_adjecant_squares(x_index: int, y_index: int, tilemap_dimension: int = 13) -> list[Tuple[int, int]]:
    """"Returns a list of adjecant tile index tuple pairs"""
    adjecant_tiles = []
    for i in (-1, 0, 1):
        if x_index + i < 0 or x_index + i > tilemap_dimension: 
            continue

        for j in (-1, 0, 1):
            if y_index + j < 0 or y_index + j > tilemap_dimension: 
                continue
            if i == 0 and j == 0:
                continue
            adjecant_tiles.append((x_index + i, y_index + j))
    return adjecant_tiles


def get_orthogonal_adjecant_squares(x_index: int, y_index: int, tilemap_dimension = 13) -> list[Tuple[int, int]]:
    """"Returns a list of orthogonal adjecant tile index tuple pairs"""
    adjecant_tiles = []
    for i in (-1, 1):
        if x_index + i > -1 and x_index + i <= tilemap_dimension:
            adjecant_tiles.append((x_index + i, y_index))
        if y_index + i > -1 and y_index + i <= tilemap_dimension:
            adjecant_tiles.append((x_index, y_index + i))
    return adjecant_tiles


def get_isometric_tile_center(x_index: int, y_index: int, tilewidth: int, tileheight: int, offset_world_x: int, offset_world_y: int) -> Tuple[float, float]:
    x = ((x_index - 0.5)- (y_index - 0.5)) * (tilewidth/2) + offset_world_x
    y = ((x_index - 0.5) + (y_index - 0.5)) * (tileheight/2) + offset_world_y
    return (x,y)

def get_distance(point1, point2) -> int:
    """Gets two points and calculates distance between when moving from tile to tile perpendicularly"""
    substracted = sub_tuples(point1, point2)
    return abs(substracted[0]) + abs(substracted[1])

def get_closest(point, list_of_points) -> tuple((int, int)):
    """Gets closest point to given point from a list of points"""
    closest = list_of_points[0]
    for p in list_of_points[1:]:
        if get_distance(point, p) < get_distance(point, closest):
            closest = p
    return closest

def get_line(pos, facing):
    """Takes the position and facing indices and returns a list of indices continuing in a line"""
    line = [pos, facing]
    off = (facing[0] - pos[0], facing[1] - pos[1])
    while True:
        continuation = add_tuples(line[-1], off)
        if continuation[0] < 0 or continuation[0] > 12 or continuation[1] < 0 or continuation[1] > 12:
            break
        line.append(continuation)
    return line

def get_lines(pos):
    lines = []
    for t in get_orthogonal_adjecant_squares(pos[0], pos[1]):
        lines.extend(get_line(pos, t))
        print(lines)
    return lines

def add_tuples(tuple1, tuple2):
    zipped = zip(tuple1, tuple2)
    mapped = map(sum, zipped)
    return tuple(mapped)

def sub_tuples(tuple1, tuple2):
    return tuple(map(sub, tuple1, tuple2))

def restrict(val, minval, maxval):
    if val < minval: return int(minval)
    if val > maxval: return int(maxval)
    return int(val)