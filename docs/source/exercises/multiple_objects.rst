Multiple Objects Exercises
==========================

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

Exercise 0
**********

Clean your environment (:doc:`click here <clean_environment>`)!

Exercise 1
**********

This week, we will start making the Hero of a game.

.. code-block:: python
    :linenos:

    class Hero:    
        def __init__(self, x, y, w, h):
            ''' this is a constructor function 
                when you create a new Hero, it requires these 4 variables
            '''
            
            
            # Remember that classes act like factories
            # when we are inside this function, we are inside a single Hero instance
            # and we need to be able to reference the current hero 
            # so, a self variable is a way of referencing the current Hero
            self.x = x
            self.y = y
            self.w = w
            self.h = h

    hero1 = Hero() # this will break.  
    hero1 = Hero(10, 10, 50, 50)
    print(hero1.x)
    
Add the following

1. A variable into the constructor (:code:`__init__` function) for the hero's name
    - don't forget to "save" it to the hero using :code:`self.name = name` 
    

Exercise 2
**********

This week, we will start making the Hero of a game.

.. code-block:: python
    :linenos:

    class Hero:    
        def __init__(self, x, y, w, h):
            ''' this is a constructor function 
                when you create a new Hero, it requires these 4 variables
            '''
            
            # Remember that classes act like factories
            # when we are inside this function, we are inside a single Hero instance
            # and we need to be able to reference the current hero 
            # so, a self variable is a way of referencing the current Hero
            self.rect = Rect(x, y, w, h)
        
        def say_hi(self):
            print("Hello, my name is {}".format(self.name))
            
        def move_right(self, step_size=0):
            self.rect.x += step_size

    hero1 = Hero(10, 10, 50, 50)
    print(hero1.x) # this will break
    print(hero1.rect) 
    hero1.say_hi()
    
    
We are going to save the coordinate information into Pygame's :code:`Rect` class.
They offer some really neat functions if we do this. 

Also, :code:`Rect` has the following variables:
::
    x,y
    top, left, bottom, right
    topleft, bottomleft, topright, bottomright
    midtop, midleft, midbottom, midright
    center, centerx, centery
    size, width, height
    w,h

Add the following:

1. Add the :code:`name` code from the first exercise into this class.
2. The three other functions that move the hero:
    1. :code:`def move_left(self, step_size=0)`
    2. :code:`def move_down(self, step_size=0)`
    3. :code:`def move_up(self, step_size=0)`
3. Code that does the following:

.. code-block:: python
    :linenos:
    
    hero1.move_right(100)
    hero1.move_down(100)
    hero1.move_left(100)
    hero1.move_up(100)


Exercise 3
**********

Let's make the hero move on their own! 

Note: this code assumes you have done the :raw:`Clean Environment` exercise 
because it assumes the :code:`SPEEDX` and :code:`SPEEDY` variables.

NOTE: here we will pass in :code:`SPEEDX` and :code:`SPEEDY` explicitly into the move functions.
However, you could (and should) change the defaults inside those functions to :code:`SPEEDX` and :code:`SPEEDY`.

Add the following code into the :code:`Hero.__init__` function:

.. code-block:: python
    :linenos: 
    
    self.going_right = True
    self.going_down = True

And now, a new function inside the :code:`Hero` class:

.. code-block:: python
    :linenos: 
    
    def drift(self):
        if self.going_right:
            self.move_right(SPEEDX)
        else:
            self.move_left(SPEEDX)
        
        if self.going_down:
            self.move_down(SPEEDY)
        else:
            self.move_up(SPEEDY)
        

Add the following:

1. Inside :code:`def drift(self)`, after the code which moves the hero, 
check to see if :code:`self.rect` is outside of the screen. I have done the first one for you. 

.. code-block:: python
    
    # this will assume WINDOW_SIZE
    WIDTH = WINDOW_SIZE[0]
    HEIGHT = WINDOW_SIZE[1]
    # you can also do "unpacking"
    # WIDTH, HEIGHT = WINDOW_SIZE 
    
    if self.rect.left < 0:
        # we will now switch directions
        self.going_right = False
        # we will also set the left side to be equal to the window side
        # this means we won't go off screen and bug out
        self.rect.left = 0
    elif self.rect.right > WIDTH:
        print("you should write code here!")
    elif self.rect.top < 0:
        print("you should write code here!")
    elif self.rect.bottom > HEIGHT:
        print("you should write code here!")

Exercise 4
**********

Now, we will give our hero a wall to bump into!  
This will demonstrate why we use :code:`Rect`.
Check out this documentation: `PyGame Rect Docs for Colliding <https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect>`_

This code should go into the INIT SECTION part of the code:

.. code-block:: python
    :linenos:
    
    # this will assume WINDOW_SIZE
    WIDTH = WINDOW_SIZE[0]
    HEIGHT = WINDOW_SIZE[1]
    # you can also do "unpacking"
    # WIDTH, HEIGHT = WINDOW_SIZE 
    wall1 = Rect(WIDTH // 2, 0, WIDTH // 10, HEIGHT)

Then, after having moved, inside the :code:`while` loop ACTION CODE:

.. code-block:: python
    :linenos:
    
    ### assume hero moves here in some way
    ### could be calling hero1.move()
    
    if hero1.rect.colliderect(wall1):
        print("The hero has collided with the wall!")
        print("You should be adding code here!")
        
        if hero1.rect.right > wall1.left:
            hero1.rect.right = wall1.left
            hero1.going_right = False
        elif hero1.rect.left < wall1.right:
            print("Add code here!")
        elif hero1.rect.bottom > wall1.top:
            print("Add code here!")
        elif hero1.rect.top < wall1.bottom:
            print("Add code here!")

You should finish the code inside the :code:`if` statements.

Exercise 5
**********

Move the above code into the :code:`Hero` class. 

.. code-block:: python
    :linenos:
    
    def handle_collision(self, other_rect):
        if self.rect.colliderect(other_rect):
            print("The code is basically the same from Exercise 4!")
            
            
The major differences will be that :code:`hero1` is used to refer to the hero OUTSIDE of itself,
but when the code is INSIDE itself, you use the :code:`self` variable to reference it. 

What should the code look like now inside the :code:`while` loop?  

.. raw:: html
    
    <div id="spoiler" style="display:none"> 
    
    hero1.handle_collision(wall1)
    
    </div> 
    <button title="Click to show" type="button" 
    onclick="if(document.getElementById('spoiler') .style.display=='none') {document.getElementById('spoiler') .style.display=''}else{document.getElementById('spoiler') .style.display='none'}">
    Show/hide
    </button>

Exercise 6
**********

Now you will add multiple walls.  

.. code-block:: python
    :linenos:

    two_thirds_height = 2 * HEIGHT//3
    one_tenth_width = WIDTH // 10
    one_third_width = WIDTH // 3
    
    ### Rects want x, y, w, h
    ### x and y are for the TOP LEFT corners. 
    wall1 = Rect(one_third_width, 0, one_tenth_width, two_thirds_height)
    wall2 = Rect(2 * one_third_width, HEIGHT - two_thirds_height, one_tenth_width, two_thirds_height)
    
    walls = [wall1, wall2]
    

Inside the loop:

.. code-block:: python
    :linenos:

    for wall in walls:
        hero1.handle_collision(wall)


You should draw out a maze and plan the x, y, w, and h coordinates.  You should be using at least 5 walls. 


Bonus Exercise
**************

If you want to add human movement to the hero, you can do the following:

Up-Down triggers
****************

Let's say you want somethign constant to be happening while a button is pressed.
You could do the following:

.. code-block:: python
    :linenos:
    
    ### inside WHILE LOOP section    
    for event in pygame.event.get():
        ## standard quit 
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero1.move_left()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                spacedown = False
                
