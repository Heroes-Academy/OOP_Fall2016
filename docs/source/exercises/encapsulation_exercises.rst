Encapsulation Exercises
=======================

These examples go through and make the encapsulation more and more complete for moving a square around the screen.

**STEP ONE**

Use the template. 
These examples assume that you are using the basic pygame template.
 `Get it here <https://github.com/Heroes-Academy/OOP_Fall2016/blob/master/code/base_pygame.py>`_

The examples have two parts: defining the information for the square and then using that information.

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

Example 1
*********

Inside the INIT section:

.. code-block:: python
    :linenos:

    origin_x = 50
    origin_y = 50
    square_width = 100
    square_height = 100

Inside the ACTION CODE section:

.. code-block:: python
    :linenos:

    # the syntax for rect is (display surface, color, rectangle_info)
    # and the rectangle_info is (x, y, width, height)
    pygame.draw.rect(surface, BLACK, [origin_x, origin_y, square_width, square_height])

**Your task:**

1. Create a second rectangle and that has different starting x and y variables.
    - In other words, create two new variables and use them to draw a new rectangle.
    - Use the same height and width as the first rectangle.


Example 2
*********

Inside the INIT section:

.. code-block:: python
    :linenos:

    box_info = {'x': 50, 'y': 50, 'width': 100, 'height': 100}


Inside the ACTION CODE section:

.. code-block:: python
    :linenos:

    # the syntax for rect is (display surface, color, rectangle_info)
    # and the rectangle_info is (x, y, width, height)
    pygame.draw.rect(surface, BLACK, [box_info['x'], box_info['y'], box_info['width'], box_info['height']])

**Your task:**

1. Create a second rectangle that is made up of a second dictionary.
    - It should be drawn in the exact same way as the first one, but using the second dictionary.


Example 3
*********

Inside the INIT section:

.. code-block:: python
    :linenos:

    def make_box(x, y, width, height):
        new_box_info = {'x': x, 'y': y, 'width': width, 'height': height}
        return new_box_info

    box_info = make_box(50, 50, 100, 100)

Inside the ACTION CODE section:

.. code-block:: python
    :linenos:

    # the syntax for rect is (display surface, color, rectangle_info)
    # and the rectangle_info is (x, y, width, height)
    pygame.draw.rect(surface, BLACK, [box_info['x'], box_info['y'], box_info['width'], box_info['height']])

**Your task:**

1. Create a second rectangle using the function.   Draw this rectangle as you did in example 2.


Example 4
*********

Inside the INIT section:

.. code-block:: python
    :linenos:

    def make_box(x, y, width, height):
        new_box_info = {'x': x, 'y': y, 'width': width, 'height': height}
        return new_box_info

    def draw_box(surf, color, info):
        pygame.draw.rect(surf, color, [info['x'], info['y'], info['width'], info['height']])

    box_info = make_box(50, 50, 100, 100)

Inside the ACTION CODE section:

.. code-block:: python
    :linenos:

    # the syntax for rect is (display surface, color, rectangle_info)
    # and the rectangle_info is (x, y, width, height)
    draw_box(surface, BLACK, box_info)

**Your task:**

1. Create a second rectangle as you have in the past couple of examples.  Draw it in the same way.

Final Task
**********
You will create two new functions:

1. :code:`make_circle`
    - use a dictionary to represent the necessary variables for a circle
    - it needs x, y, and radius.
2. :code:`draw_circle` function
    - in the same way :code:`draw_box` is written, write a :code:`draw_circle` function
    - the syntax for drawing a circle is :code:`pygame.draw.circle(surface_object, some_color, center_point, radius)`
    - the center point is just :code:`(x,y)` or :code:`[x,y]`

