[Week 4] Our First Object
=========================

Class Summary
-------------

Last week we looked at how to encapsulate code.  There were some hiccups so we will covered this a bit more.

Part 1: Encapsulation Exercise
******************************

`Link to exercises <>`_

On this page, you will find a set of exercises.  They are to help you understand what it means to encapsulate code and why it is useful.


Part 2: Creating an Object
**************************

Objects are a way to group either variables or functionality into useful chunks.
Like functions, they let us have cleaner code, and repeat ourselves less.

Objects being with "class" definitions.  These definitions are like the blueprints or the recipe.
Using these blueprints, we can create an object.  Let's look at a simple one:
::
    class Point:
        x = 0
        y = 0

    p1 = Point()
    p1.x = 50
    p1.y = 50

The first 3 lines define our class.  This is the blue print for our object.
We create our object by using the class like a function.
This is usually referred to as "construction" or "instantiation".

For the rest of this part, you will make your own objects to represent boxes.
`Click here for the exercises <>`_
