[Week 7] Object Practice and Projects
=====================================

Today's Task
************

1. Answer the project rubric
2. Talk your project idea with the information below to the class
3. Work on your project


Project Rubric
**************

1. Game Title
2. Overall game goal
    - What is the player trying to accomplish
3. Objects that exist in the game
    - List all objects that you want to use
    - List all objects currently implemented
    - For each object, identify the common parts and specialized parts
        - Specify which properties are inherited and which are new
    - For each object, describe when it is drawn (it can be always drawn or conditionally drawn)
4. Interaction
    - What interaction will the user have?
    - Specifically, what keys will be used and what effect will they have
5. What is the minimal set of things you need to have to have your game working?
6. List 3 1-step additions you could make
    - It has to add only 1 additional piece of complexity

Cookbooks
*********

You should be referencing at least some of these!

- :doc:`Simple PyGame cookbook <helpers/simple_pygame_cookbook>`
    - covers pygame examples without using classes
- :doc:`PyGame with Classes cookbook <helpers/pygame_classes_cookbook>` 
    - covers pygame using classes 
    - has a lot of functionality explained!
- :doc:`Python Cookbook <helpers/cookbook.rst`
    - This has examples of most of Python's syntax!
- :doc:`Classes cookbook <helpers/classes_cookbook>`
    - This has examples of the basics of classes!



Last week we talked about designing objects.
This week, we will be talking about how you can make an ecosystem of objects to work together.

Topics:

1. Inheritance and how to use it
2. Re-capping classes
    - :doc:`Click here for the class recap page <exercises/class_recap>`
3. Designing an ecosystem of objects in the game
    - :doc:`Click here for the exercise page <exercises/object_ecosystem>`

In designing the game, you should identify:

1. an entity that will be used in many places
    - examples include bricks in brickbreak games
    - monsters in other games
    - projectiles
    - etc
2. identify the basic functionality
3. plan out the flow of the game
    - what will the hero do
    - what will trigger what
    - what will be the goal
    - what will be the inputs
