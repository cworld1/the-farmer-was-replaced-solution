from __builtins__ import *
import actions
import libs
import action_full

hats = [
    # Basic
    Hats.Gray_Hat,
    Hats.Purple_Hat,
    Hats.Green_Hat,
    Hats.Brown_Hat,
    # Advanced
    Hats.Tree_Hat,
    Hats.Carrot_Hat,
    Hats.Pumpkin_Hat,
    Hats.Traffic_Cone_Stack
]
change_hat(Hats.Traffic_Cone_Stack)
# Current max size is 22
# set_world_size(6)
# pet_the_piggy()
# do_a_flip()
libs.goto(0, 0)

# Harvest & plant
def harvest_and_plant():
    need_pumpkin = False
    # Hay
    if num_items(Items.Hay) < 19200:
        actions.hay()
    # Wood
    elif num_items(Items.Wood) < 3200:
        actions.wood()
    # Carrot
    elif num_items(Items.Carrot) < 16000:
        actions.carrot()
    # Pumpkin
    else:
        need_pumpkin = True
    return need_pumpkin

def take_action():
    # Harvest or fertile
    if not actions.try_harvest() and get_entity_type() != None:
        actions.fertile()
        actions.harvest()
    # Plant
    need_pumpkin = harvest_and_plant()
    if need_pumpkin:
        action_full.pumpkins()
    # Water
    actions.water()

def main():
    # Step to southest
    for i in range(get_pos_y()):
        move(South)
    # Harvest
    oddCol = True
    while True:
        for i in range(get_world_size()-1):
            take_action()
            if oddCol:
                move(North)
            else:
                move(South)

        take_action()
        move(East)
        oddCol = not oddCol

if __name__ == "__main__":
    main()
