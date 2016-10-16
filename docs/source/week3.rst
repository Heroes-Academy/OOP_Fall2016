[Week 3] Intro to Encapsulation
===============================

Summary
-------

Now that we've started to practice mastering the state of objects
(keeping track of their properties), we will work on making our code more efficient.

In-class code
*************
1. `Basic Pygame Template <https://github.com/Heroes-Academy/OOP_Fall2016/blob/master/code/base_pygame.py>`_
2. `Basic stick figure <https://github.com/Heroes-Academy/OOP_Fall2016/blob/master/code/week3/basic_stick.py>`_

Important Concepts
******************

1. Functions
    - A code block which packages the code and provides a shortcut to executing the code
    - The code below shows how to pass information in, how to get information out
    - **important**: remember that scope means what variables can be "seen" inside and outside the function
Example:
::
    def hello_x(x):
        y = "hello {}".format(x)
        return y
    y = hello_x("world")
    print(y)

2. Dictionaries
    - A python variable type that allows you to map keys to values
Example
::
    bob = dict()
    bob['name'] = 'bob'
    bob['species'] = 'turtle'

3. Encapsulation.
    - The packaging of code to be reused later
    - Example: if we have multiple objects, and we want to make them bounce off walls,
               then we could either write the wall bouncing code for each object, or write the code
               once and use a function to apply it to each object.



Homework
--------

To be further defined after class.


Slides
------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1DXPtoipi3ASEIk2-CC5JyRa_ow2of-8JOQEA8mDPneA/embed?start=false&loop=false&delayms=60000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>


