Object Ecosystem Exercises
==========================

For this, you will be creating a custom, but basic pygame sprite class.
You will use this as the base for all of the sprites you draw in the game.
Then, you will extend it to make the Hero and some object type that will be used a lot.
I am going to use it to make blocks that the Hero is going to try to get.


Basic Pygame Sprite Class
-------------------------

When you have a pre-defined class, you can inherit from it and get all of its functionality.
This lets you implement common things once, and then reuse them in different ways.

We are going to start with blocks and then we will work our ways towards a fuller
implementation.

.. code-block:: python
    :linenos:

    class Block(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super(Block, self).__init__(self)

            # Create an image of the block, and fill it with a color.
            # This could also be an image loaded from the disk.
            self.image = pygame.Surface([width, height])
            self.image.fill(color)

            # Fetch the rectangle object that has the dimensions of the image
            # Update the position of this object by setting the values of rect.x and rect.y
            self.rect = self.image.get_rect()



Converting Walls to use sprites
-------------------------------

.. code-block:: python
    :linenos:

    class Walls:
        def __init__(self):
            ''' keep track of the walls
            you could maybe pass in a COLOR here'''
            self.walls = pygame.sprite.Group()

        def add_wall(self, x, y, w, h):
            ''' add a single wall'''
            new_block = Block(BLACK, w, h)
            new_block.x = x
            new_block.y = y
            self.walls.add(new_block)

If you are having trouble with the game, start here
---------------------------------------------------

We are going to debug misunderstandings.  Debugging means removing all the complex stuff and starting with simple baselines so we can know where the issue is at.

First, start with the class recap.  If there is any confusion with that, then come to me.

Then, we will move onto the basic pygame setup.  Go to either the code you wrote, or the code I wrote.

Using a series of English sentences, describe the flow of the PyGame game.
You don't have to describe every object creation, but you should describe which
functions get called and in what order.  If something is created, you should describe that.



Plan your own ecosystem of objects
----------------------------------

You can choose to start fresh now if you want, but you should make a plan with the following things:

1. What are going to be the objects in your game
    - Walls, hero, monsters, projectiles, etc
2. How the objects are going to interact?
3. What is the smallest component in your game?
    - You should plan on making this into a base class
    - Then, you can create classes that subclass it and use it as its ancestor
    - For example, you could have: :code:`Entity`, which then is subclassed by :code:`Monster`

If you should get to this point, you should start working on your game.
Please let me know when you get here.
