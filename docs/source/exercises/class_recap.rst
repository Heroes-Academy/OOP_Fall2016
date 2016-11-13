Classes Recap
==============

This is a set of exercises for refreshing your knowledge of classes.


The basic class
---------------

.. code-block:: python
    :linenos:

    class Dog:
        name = ''
        age = 0

    # Dog is called like a function to **instantiate** the object
    fido = Dog()
    # have to set the variables manually
    fido.name = "Fido"
    fido.age = 7


Class with an initial function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    # now we can accept arguments when we **instantiate** the object!
    fido = Dog("Fido", 7)


Thinking about how self works
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you need to understand self better, try this out.

.. code-block:: python
    :linenos:

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            print("-2--")
            print("Inside the init function")
            print(self)

    # now we can accept arguments when we **instantiate** the object!
    print("-1--")
    print("Before creating fido")
    fido = Dog("Fido", 7)
    print("-3--")
    print("After creating fido")
    print(fido)

Look at the code above and run it in PyCharm.
Notice what is printed by :code:`print(self)` inside the init function and :code:`print(fido)`
outside the class. They are both pointing at the same object!  :code:`self` is
just a way of getting access to the object while inside the object.



