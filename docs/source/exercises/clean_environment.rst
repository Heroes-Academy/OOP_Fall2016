Clean Environment
=================

We are going to start keeping our constants and useful variables in a separate file.

1. Create a separate file, call it "settings.py"
2. Put in the following variables

.. code-block:: python
    :linenos:
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    WINDOW_SIZE = (700, 500)
    
    SPEEDX = 5
    SPEEDY = 5
    
3. Anytime you have new constant variables, they should be put into here.
4. Inside your game file, you should put the following:


.. code-block:: python
    :linenos:
    
    from settings import *
    # if the above breaks, type:
    # from .settings import *
    
    