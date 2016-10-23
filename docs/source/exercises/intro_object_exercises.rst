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


Exercises
---------

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




Exercise 4
**********

Let's make this more interactive!  
For each of the following key tests, you can change some variable inside your object. 
For instance, you could have left and right increase or decrease the speedx.
You could also have your box jump with space. Note that this last one requires thinking about gravity a bit more. 

.. code-block:: python
    :linenos:
    
    ### inside WHILE LOOP section    
    for event in pygame.event.get():
        ## standard quit 
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Do something here!")
            elif event.key == pygame.K_LEFT:
                print("do something here!")
            elif event.key == pygame.K_RIGHT:
                print("do something here!")
                
                

        
        
Extra stuff
-----------

Class __init__ method
*********************
    
Using the :code:`__init__` constructor:

.. code-block:: python
    :linenos:
    
    class Box:
        def __init__(self, x, y, w, h):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
        
        def print_info(self):
            pass
        
        @property
        def right_side(self):
            return self.x + self.w
            
    box = Box(50, 50, 100, 100)
    print(box.print_info, type(box.print_info))
    print(box.right_side, type(box.right_side))




Gravity and Jumping 1
*********************

For fun, we are going to add gravity.  Gravity is just a way of updating the y speed.
Add the following code into update_position.  Your Box class will need a new variable: mass.

.. code-block:: python
    :linenos:

    # recall that
    #          x += y
    # is the same as
    #          x = x + y
    
    ### for physics
    
    upforce = 0 # should be some number, maybe from bouncing or jumping
    
    gravity = 9.8 # is positive because 0 is the top and we want it to fall down 
    downforce = gravity * box.mass
    
    totalforce = downforce+upforce 
    acceleration = totalforce / box.mass
    
    ### update speeds and locations
    box.speedy += acceleration
    box.y += box.speedy
    


Play with different values of gravity.

Gravity+Jumping 2
*****************

Gravity is a force that acts on the y direction of an object. 
Specifically, if your object has a speed, then it is accelerating downwards by gravity. 
If you jump, you are accelerating upwards.  

Force is equal to mass times acceleration---:math:`F = m*a`. 
So, to get acceleration from two forces (gravity and jumping), we do
:math:`a=F/m`.  Jumping is our force upwards, gravity is our force downwards. 

Use the following function to compute the acceleration.  
In the event loop, you could set a boolean variable which tells you whether a space bar
press happened or not.  Then, you can pass it to this function to enable the upward force.
It would be good to have upward force be a couple times more than gravity.  
Also, the boolean for the space bar press should only be True once, because it's a burst
of energy, not a sustained force. 

.. code-block:: python
    :linenos:
    
    def compute_acceleration(box, did_jump=False):
        gravity_force = 9.8 * box.mass
        downforce = gravity_force # + any other downward forces
        
        if did_jump:
            jump_force = somenumber * box.mass
        else:
            jump_force = 0
        upforce = jump_force # + any other upward forces; maybe bouncing
        
        total_force = downforce + upforce
        acceleration = total_force / box.mass # f = m*a
        
        return acceleration
        
Property Decorator
******************

Using the property decorator for a class:

.. code-block:: python
    :linenos:
    
    class Box:
        x = 0
        y = 0
        w = 10
        h = 10
        
        def print_info(self):
            pass
        
        @property
        def right_side(self):
            return self.x + self.w
            
    box = Box()
    box.x = 50
    print(box.print_info, type(box.print_info))
    print(box.right_side, type(box.right_side))
