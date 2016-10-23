Intro Object Exercises
======================

In these exercises, you will go through making objects and using them for different things.

These examples assume that you are using the basic pygame template.
If you don't have it, find it `here <https://github.com/Heroes-Academy/OOP_Fall2016/blob/master/code/base_pygame.py>`_


Exercse 1
*********

Before the while loop, have the following code:
::
    class Box:
        x = 0
        y = 0
        w = 0
        h = 0

    box_info = Box()
    box_info.x = 50
    box_info.y = 50
    box_info.w = 100
    box_inof.h = 100

Similar to the other exercises, use this to make the rectangle inside the while loop:
::
    pygame.draw.rect(surface, BLACK, [box_info.x, box_info.y, box_info.w, box_info.h])
