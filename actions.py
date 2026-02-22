from __builtins__ import *


# Manage
def try_harvest():
    if can_harvest():
        harvest()
        return True
    return False

def water():
    if get_water() < 0.4 and num_items(Items.Water) > 0:
        use_item(Items.Water)

def fertile():
    if num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)
        return True
    return False

# Plant
def hay():
    if get_ground_type() == Grounds.Soil:
        till()

def wood():
    if (get_pos_x() - get_pos_y()) % 2 == 0:
        plant(Entities.Tree)
    else:
        plant(Entities.Bush)

def carrot():
    if num_items(Items.Hay) < 1:
        hay()
    elif num_items(Items.Wood) < 1: 
        wood()
    if get_ground_type() == Grounds.Grassland:
        till()
    plant(Entities.Carrot)

def pumpkin():
    if get_ground_type() == Grounds.Grassland:
        till()
    plant(Entities.Pumpkin)
