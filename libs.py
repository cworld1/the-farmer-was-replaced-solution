from __builtins__ import *


# Till all
# for i in range(get_world_size()):
#     for i in range(get_world_size()):
#         till()
#         move(North)
#     move(West)

def goto(x, y):
    world_size = get_world_size()
    def get_step(step):
        if step > 0:
            # To negative
            if step > world_size // 2:
                step = world_size - step
                is_positive = False
            else:
                is_positive = True
        else:
            # To positive
            if -step > world_size // 2:
                step = world_size + step 
                is_positive = True
            else:
                step = -step
                is_positive = False
            
        return is_positive, step

    # Move horizontally
    delta_x_positive, delta_x = get_step(x - get_pos_x())
    if delta_x_positive:
        x_direction = East
    else:
        x_direction = West
    # print(x_direction, delta_x)
    for i in range(delta_x):
        move(x_direction)

    # Move vertically
    delta_y_positive, delta_y = get_step(y - get_pos_y())
    if delta_y_positive:
        y_direction = North
    else:
        y_direction = South
    for i in range(delta_y):
        move(y_direction)
