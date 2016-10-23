Encapsulation Exercises
=======================

These examples go through and make the encapsulation more and more complete for moving a square around the screen.

These examples assume that you are using the basic pygame template.
If you don't have it, find it `here <https://github.com/Heroes-Academy/OOP_Fall2016/blob/master/code/base_pygame.py>`_

The examples have two parts: defining the information for the square and then using that information.


Example 1
*********

Before the while loop, have the following code:
::
    origin_x = 50
    origin_y = 50
    square_width = 100
    square_height = 100

Inside the while loop, after you have filled the screen:
::
    # the syntax for rect is (display surface, color, rectangle_info)
    # and the rectangle_info is (x, y, width, height)
    pygame.draw.rect(surface, BLACK, [origin_x, origin_y, square_width, square_height])


Create a second rectangle and that has different starting x and y variables.
In other words, create two new variables and use them to draw a new rectangle.
Use the same height and width as the first rectangle.


Example 2
*********

Before the while loop, have the following code:
::
    box_info = {'x': 50, 'y': 50, 'width': 100, 'height': 100}


Inside the while loop, after you have filled teh screen:
::
    # the syntax for rect is (display surface, color, rectangle_info)
    # and the rectangle_info is (x, y, width, height)
    pygame.draw.rect(surface, BLACK, [box_info['x'], box_info['y'], box_info['width'], box_info['height']])

Create a second rectangle that is made up of a second dictionary.
It should be drawn in the exact same way as the first one, but using the second dictionary.


Example 3
*********

Before the while loop, have the following code:
::
    def make_box(x, y, width, height):
        new_box_info = {'x': x, 'y': y, 'width': width, 'height': height}
        return new_box_info

    box_info = make_box(50, 50, 100, 100)

Inside the while loop, after you have filled teh screen:
::
    # the syntax for rect is (display surface, color, rectangle_info)
    # and the rectangle_info is (x, y, width, height)
    pygame.draw.rect(surface, BLACK, [box_info['x'], box_info['y'], box_info['width'], box_info['height']])

Create a second rectangle using the function.   Draw this rectangle as you did in example 2.


Example 4
*********

Before the while loop, have the following code:
::
    def make_box(x, y, width, height):
        new_box_info = {'x': x, 'y': y, 'width': width, 'height': height}
        return new_box_info

    def draw_box(surf, color, info):
        pygame.draw.rect(surf, color, [info['x'], info['y'], info['width'], info['height']])

    box_info = make_box(50, 50, 100, 100)

Inside the while loop, after you have filled teh screen:
::
    # the syntax for rect is (display surface, color, rectangle_info)
    # and the rectangle_info is (x, y, width, height)
    draw_box(surface, BLACK, box_info)

Create a second rectangle as you have in the past couple of examples.  Draw it in the same way.

Make a new function called "draw_two_boxes" that does exactly what "draw_box" does, but is modified so you can give it two boxes and have it draw two.
