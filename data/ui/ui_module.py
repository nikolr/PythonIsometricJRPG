"""Module that holds useful functions for drawing panels and blitting text. Hover info boxes?"""


from data.attributes.attribute_id import AttributeId


def draw_character_info(screen, font, character_list, color, rect_pos_x, rect_pos_y, x_off, y_off, y_internal):
    for i in range(len(character_list)):
        screen.blit(font.render(character_list[i].name, True, color), (
            rect_pos_x + x_off, rect_pos_y + (y_off*i) + y_internal*0))
        screen.blit(font.render(str(character_list[i].get_attribute_value(AttributeId.HP)), True, color), (
            rect_pos_x + x_off, rect_pos_y + (y_off*i) + y_internal*1))
        screen.blit(font.render(str(character_list[i].counter), True, color), (
            rect_pos_x + x_off, rect_pos_y + (y_off*i) + y_internal*2))

