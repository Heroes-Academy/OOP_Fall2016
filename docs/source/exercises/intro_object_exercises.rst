Intro Object Exercises
======================

In these exercises, you will go through making objects and using them for different things.

These examples assume that you are using the basic pygame template.
If you don't have it, find it `here <https://github.com/Heroes-Academy/OOP_Fall2016/blob/master/code/base_pygame.py>`_


Anatomy of the Pygame loop
**************************

.. code-block:: python
    :linenos:

    ##### INIT SECTION
    # import pygame
    # any functions you want to use should be defined right away
    # create pygame variables
    # create variables you want to use inside the game loop


    ##### WHILE LOOP SECTION
    while not done:
        # check for events
        # fill the screen with white
        ##### ACTION CODE
        # do any actions that we want to do
        # this could be moving the box, etc
        ##### FINISHING CODE
        # end of while loop code, mostly the clock.tick()

    #### POST WHILE LOOP SECTION
    # once the code hits here, we can assume that the while loop is over and game is done
    # do any last finishing code things here
    # the important one is to tell pygame shut down


Exercise 1
**********

Inside the INIT section:

.. code-block:: python
    :linenos:

    # set up the class and the variables

    class Box:
        x = 0
        y = 0
        w = 0
        h = 0
        speedx = 0
        speedy = 0

    box_info = Box()
    box_info.x = 50
    box_info.y = 50
    box_info.w = 100
    box_info.h = 100
    box_info.speedx = 10
    box_info.speedy = 10

Similar to the other exercises, use this to make the rectangle inside the ACTION CODE section:

.. code-block:: python
    :linenos:

    # Use the box_info object to draw!

    pygame.draw.rect(surface, BLACK, [box_info.x, box_info.y, box_info.w, box_info.h])

Compare this code to the earlier exercises.  Write the "make_box" function which uses
the class instead.  Also, rewrite the "draw_box" using this class.

Exercise 2
**********

The code for getting the width and height of the screen are the following:

.. code-block:: python
    :linenos:

    # get the screen width and height

    screen = pygame.display.get_surface()
    W, H = screen.get_size()

When testing to see if the box is beyond the sides of the screen, use the correct side:

.. code-block:: python
    :linenos:

    # calculate special variables

    right_side = box_info.x + box_info.w
    left_side = box_info.x
    top_side = box_info.y
    bottom_side = box_info.y + box_info.h

Also, remember W is the width, and so is the right side of the screen.
H is the height and is the bottom side of the screen.
So, if the left_side is below 0, it is out of bounds.
If the right side is larger than W, it is out of bounds.
If the top_side is smaller than 0, it is out of bounds.
Finally, if the bottom_side is larger than H, it is out of bounds.


Write the code for the update position function:

.. code-block:: python
    :linenos:

    # Compute the new position using the box_info object

    def update_position(box_info):
        ### test if the box is out of bounds
        ### if it is,
        ###        the speed should negative for
        ###        the corresponding side that is out of bounds
        ###
        ### then update the position by the speed
        ### so, the x changes by speed
        ### the y changes by speed

The function should be used inside the while loop to update the position before it is drawn.


Bonus Exercise
**************

For fun, we are going to add gravity.  Gravity is just a way of updating the y speed.
Add the following code into update_position.  Your Box class will need a new variable: mass.

.. code-block:: python
    :linenos:

    # recall that
    #          x += y
    # is the same as
    #          x = x + y
    gravity = 9.8
    acceleration = gravity / box_info.mass
    box_info.speedy += gravity


Play with different values of gravity.  Also, play with different values of mass.


Exercise 3
**********

Let's add a function into our class so that it can draw itself.



.. code-block:: python
    :linenos:

    # Compute the new position using the box_info object

    class Box:
        x = 0
        y = 0
        w = 0
        h = 0
        speedx = 0
        speedy = 0

        def update_position(self):
            ### everything stays the same, except you can get access to the variables using "self" now
            ### test if the box is out of bounds
            ### if it is,
            ###        the speed should negative for
            ###        the corresponding side that is out of bounds
            ###
            ### then update the position by the speed
            ### so, the x changes by speed
            ### the y changes by speed

    ## assume we do
    ## box = Box()
    ## then, later, you can use it with
    ## box.update_position()
