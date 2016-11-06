Designing Objects
=================

Now that we are starting to write our own objects, we will start designing our own objects!

By the end we will have the following file structure:

.. raw::

    project_folder/
        game.py
        hero.py
        setting.py
        walls.py

We will start with the game loop.  Create a new file called "game.py" and start putting these into there: 


The top
-------

The top of the file is pretty standard.  I have added extra imports to handle different files.

.. code-block:: python
    :linenos:
    
    import pygame
    from settings import *
    
    
The settings.py file is:

.. code-block:: python
    :linepos:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    WIDTH = 700
    HEIGHT = 500
    WINDOW_SIZE = (HEIGHT, WIDTH)
    
    SPEEDX = 5
    SPEEDY = 5
    
    FPS = 60
    
    TITLE = "My Game"
    
    
Game :code:`__init__` function
-------------------------------


Creating a :code:`class` for our game loop means we can organize all of the functionality easier!

.. code-block:: python
    :linenos:
    
    class Game:
        def __init__(self):
            
            self.walls = []
            self.hero = None
            self.done = False
            
            pygame.init()
            self.screen = pygame.display.set_mode(WINDOW_SIZE)
            self.clock = pygame.time.Clock()
            pygame.display.set_caption(TITLE)
            

Checkpoint questions:

1. What would instantiating this class look like?
2. What kinds of things could you add into the initial function? 


.. raw:: html
    
    <div id="spoiler" style="display:none"> 
    

.. code-block:: python
    :linenos:
    
    game = Game()
    game.run()
    

.. raw:: html
    
    </div> 
    <br>
        
    <button title="Click to show" type="button" 
    onclick="if(document.getElementById('spoiler').style.display=='none') {document.getElementById('spoiler') .style.display=''}">
    Show answer
    </button>


Game Loop
---------

.. code-block:: python
    :linenos:
    
    def run(self):
        while not self.done:
            #### EVENT CHECK SECTION
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                ## extra stuff will go here
            
            ### clear the screen
            self.screen.fill(WHITE)
            
            ## extra stuff will go here
                
            #### update the display and move forward 1 frame
            pygame.display.flip()
            # --- Limit to 60 frames per second
            self.clock.tick(FPS)


Checkpoint questions:

1. Given that you already answered how the class could be instantiated, how would you run this function?
2. Can you predict what it will do?  Try and run it now. 


The Hero
--------

Let's create the hero class.  You can use the one you wrote from last week. 

Put it by itself into a hero.py file and change the top of "game.py" to the following:

.. code-block:: python
    :linenos:
    
    import pygame
    from settings import *
    from hero import *

Now, you should have a hero from last week!  It should go into the hero file.
I'm going to show the bare bones here:

.. code-block:: python
    :linenos:
    
    class Hero:    
        def __init__(self, x, y, w, h):
            ''' The hero constructor function '''
            self.rect = Rect(x, y, w, h)
            ## other things could/should go here
            
        def move_right(self, step_size=SPEEDX):
            ''' Move the hero to the right '''
            pass
            
        def move_left(self, step_size=SPEEDX):
            ''' Move the hero to the left '''
            pass
        
        def move_up(self, step_size=SPEEDY):
            ''' Move the hero up '''
            pass
        
        def move_down(self, step_size=SPEEDY):
            ''' Move the hero down '''
            pass
        
        def drift(self):
            ''' drift across the screen 
            
            Note: the implementation should drift x and drift y separately
                  After the drift in x, it should check for x collisions
                  After the drift in y, it should check for y collisions
            '''
            pass
            
        def drift_x(self):
            ''' Handle the drift in x '''
            pass
        
        def drift_y(self):
            ''' Handle the drift in y '''
            pass
            
        def collides_with(self, other_rect):
            ''' return true if there is a collision '''
            pass
            
        def handle_xcollision(self, other_rect):
            ''' handle collisions going left and right '''
            pass
            
        def handle_ycollision(self, other_rect):
            ''' handle collisions going up and dowon '''
            pass
            
        
We are going to add two new functions to the :code:`Hero` class: 
:code:`update` and :code:`draw`. 
I will show the functions under the class header below.

**Assumption**: When :code:`update` is called, the hero will be passed a list of walls. 
This is so it can check for collisions. 

**Assumption**: When :code:`draw` is called, the hero will be passed the :code:`screen`.


.. code-block:: python
    :linenos:
    
    class Hero:   
        ### all other things here
        
        def update(self, walls):
            ''' move and check for collisions '''
            pass
        
        def draw(self, screen)
            ''' draw the hero '''
            pass
    

Adding the hero into the game
-----------------------------

Into the :code:`Game` class, we will add a new function which will setup everything.
Then, inside the main loop, we will have it run the hero's functions!
This will also change how the game is instantiated and run. 
Updated code is below:

.. code-block:: python
    :linenos:

    class Game:
        def __init__(self):
            
            self.walls = []
            self.hero = None
            self.done = False
            
            pygame.init()
            self.screen = pygame.display.set_mode(WINDOW_SIZE)
            self.clock = pygame.time.Clock()
            pygame.display.set_caption(TITLE)
            
            
        def setup(self):
            self.hero = Hero(___) ### fill in the underline
            
        def run(self):
            while not self.done:
                #### EVENT CHECK SECTION
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.done = True
                    ## extra stuff will go here
                
                ### clear the screen
                self.screen.fill(WHITE)
                
                if self.hero is not None:
                    self.hero.update(self.walls)
                    self.hero.draw()
                    
                #### update the display and move forward 1 frame
                pygame.display.flip()
                # --- Limit to 60 frames per second
                self.clock.tick(FPS)
            

    
    ### this changes the running to:
    game = Game()
    game.setup()
    game.run()



Adding Walls
------------

We are going to create a wall class.  This will let us manage walls better.
We should put this in "walls.py".   I have written some code below to make this easier.

Important notes:

1. You have to write the :code:`draw` function
2. The class is able to parse a series of strings into wall placements (see :code:`parse_level`)

.. code-block:: python
    :linenos:
    
    
    class Walls:
        def __init__(self):
            ''' keep track of the walls
            you could maybe pass in a COLOR here'''
            self.walls = []
            
        def add_wall(self, x, y, w, h):
            ''' add a single wall'''
            self.walls.append(Rect(x,y,w,h))
        
        def parse_level(self, level):
            '''Parse a level string into a set of walls. I've made this for you'''
            level_width = len(level[0])
            wall_width = WIDTH / level_width
            
            level_height = len(level)
            wall_height = HEIGHT / level_height
            
            for row_index in range(level_height):
                for col_index in range(level_width):
                    cell = level[row_index][col_index]
                    if "cell" == "W":
                        x = wall_width * col_index
                        y = wall_height * row_index
                        self.add_wall(x, y, wall_width, wall_height)
        
        def set_example_level(self):
            level = [
                "WWWWWWWWWWWWW",
                "W      W    W",
                "W  W   W    W",
                "W  W   W    W",
                "W  W        W",
                "WWWWWWWWWWWWW"
            ]
            self.parse_level(level)
            
        def draw(self, screen):
            for wall in self.walls:
                ### fill in the pygame draw code here. 
        


In order to get this into the game, we have to do two things:

1. Add an import statement :code:`from walls import *` into the game.py
2. Add this to the :code:`setup` so that the game will make the walls
3. Add into the game loop a call which draws the walls. 



Adding Keyboard Input
---------------------

To get keyboard input, we need to add some extra stuff into the event loop.
Specifically, the event loop should handle more complex checks. 
Also, optionally, we could have the HERO check for game events. 


.. code-block:: python
    :linenos:
    
    class Game:
        ## code was here
        
        def run(self):
            while not self.done:
                #### EVENT CHECK SECTION
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.done = True
                    else:
                        self.handle_event(event)
                        
                ### the rest of the game loop here
        
        def handle_event(self, event):
            ## do various checks for events here. 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ## code here
                elif event.key == pygame.K_RIGHT:
                    ## code here
                elif event.key == pygame.K_DOWN:
                    ## code here
                elif event.key == pygame.K_UP:
                    ## code here        

Jumping
-------

If you'd like to make your hero jump and land on platforms, there are a couple different things that need to happen.

1. The hero can not respond to the up/down keys anymore 
2. The hero is always moving down
3. Inside the moving down, the hero has two speeds:
    1. :code:`gravity`, which is the default speed
        - this number show moving the hero DOWN (so, a positive number if adding to position)
    2. :code:`up_energy`, which gets set to some number when a key like SPACE is pressed
        - then, whenever the hero moves, the :code:`up_energy` decays, for example: :code:`up_energy = up_energy * 0.9`
