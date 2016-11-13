Classes Cookbook
================

Design patterns and examples for classes!  Use these to help you solve problems.


Defining a class
----------------

.. code-block:: python
    :linenos:

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age


Instantiating an object
-----------------------

.. code-block:: python
    :linenos:

    # create the object!
    fido = Dog("Fido", 7)


Writing a method
----------------

A method is the name of a function when it is part of a class.

You always have to include :code:`self` as a part of the method arguments.

.. code-block:: python
    :linenos:

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print("Bow wow!")


    fido = Dog("Fido", 7)
    fido.bark()

Using the self variable
-----------------------

You can access object variables through the :code:`self` variable.
Think of it like a storage system!

.. code-block:: python
    :linenos:

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print("{}: Bow Wow!".format(self.name))


    fido = Dog("Fido", 7)
    fido.bark()

    odie = Dog("Odie", 20)
    odie.bark()

Using the property decorator
----------------------------

You can have complex properties that compute like methods but act like properties.
Properties cannot accept arguments.

.. code-block:: python
    :linenos:

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print("{}: Bow Wow!".format(self.name))

        @property
        def human_age(self):
            return self.age * 7

    fido = Dog("Fido", 7)
    fido.bark()
    print("Fido is {} in human years".format(fido.human_age))

Inheriting properties and methods
---------------------------------

You can inherit properties and methods from the ancestors!
For example, the initial function below is inherited.

.. code-block:: python
    :linenos:

    class Animal:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Dog(Animal):
        def bark(self):
            print("{}: Bow Wow!".format(self.name))

        @property
        def human_age(self):
            return self.age * 7

    class Cat(Animal):
        def meow(self):
            print("{}: Meow!".format(self.name))

    fido = Dog("Fido", 7)
    fido.bark()
    print("Fido is {} in human years".format(fido.human_age))

You can also override certain things and call the methods of the ancestor!


.. code-block:: python
    :linenos:

    class Animal:
        def __init__(self, name, age, number_legs, animal_type):
            self.name = name
            self.age = age
            self.number_legs = number_legs
            self.animal_type = animal_type

        def make_noise(self):
            print("Rumble rumble")

    class Dog(Animal):
        def __init__(self, name, age):
            super(Dog, self).__init__(name, age, 4, "dog")

        def make_noise(self):
            self.bark()

        def bark(self):
            print("{}: Bow Wow!".format(self.name))

        @property
        def human_age(self):
            return self.age * 7

    class Cat(Animal):
        def __init__(self, name, age):
            super(Dog, self).__init__(name, age, 4, "cat")

        def make_noise(self):
            self.meow()

        def meow(self):
            print("{}: Meow!".format(self.name))


    fido = Dog("Fido", 7)
    fido.make_noise()
    print("Fido is {} in human years".format(fido.human_age))

    garfield = Cat("Garfield", 5, 4, "cat")
    garfield.make_noise()

