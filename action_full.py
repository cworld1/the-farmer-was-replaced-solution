import actions
import libs
from __builtins__ import *

def pumpkins():
    # Init
    check_pumpkin = {}
    world_size = get_world_size()
    for i in range(world_size):
        if i % 2 == 0:
            for j in range(world_size - 1, -1, -1):
                check_pumpkin[(i, j)] = False
        else:
            for j in range(world_size):
                check_pumpkin[(i, j)] = False

    while True:
        is_planted = False
        for key in check_pumpkin:
            if check_pumpkin[key]:
                continue

            # Goto
            libs.goto(key[0], key[1])

            # Check
            if get_entity_type() == Entities.Pumpkin:
                check_pumpkin[key] = True
            # Plant
            else:
                actions.harvest()
                actions.pumpkin()
                actions.water()
                is_planted = True

        if not is_planted:
            break
    
    # Harvest
    if not actions.fertile():
        do_a_flip()
    harvest()
    
def main():
    pumpkins()

if __name__ == "__main__":
    main()
