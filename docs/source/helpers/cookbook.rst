Heroes Cookbook
===============

This is a set of recipes that you should use while solving problems!


Numbers
-------

Integers
^^^^^^^^

.. code-block:: python
    :linenos:

    # create an integer
    x = 5

    # convert an integer string
    x = str('5')

    # convert a float to an integer
    ## note: don't depend on this for rounding, it rounds in weird ways
    x = int(5.5)

    # convert a string of any number base
    # for example, binary
    x = int('1010101', base=2)

Floats
^^^^^^

.. code-block:: python
    :linenos:

    # create a float
    x = 5.5

    # convert a float string
    x = float("5.5")

    # convert an integer to a float
    x = float(5)

Basic math operations
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    x = 100

    # 1. Add
    x = x + 5
    x += 5

    # 2. Subtract
    x = x - 5
    x -= 5

    # 3. Multiply
    x = x * 5
    x *= 5

    # 4. Divide
    x = x / 5
    x /= 5

    # 5. Power
    x = x ** 2
    x **= 2


Advanced math operations
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    # 1. Integer Division
    x = x // 5
    x //= 5

    # 2. Modulo
    x = 84
    x = x % 5
    x %= 5

Use the math library
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    import math

    x = 10

    # pow is power, same as x ** 2
    x = math.pow(x, 2)

    # ceil rounds up and floor rounds down
    x = 5.5
    y = math.ceil(x) # y is 6.0
    z = math.floor(x) # z in 5.0

    # some other useful ones:
    math.sqrt(x)
    math.cos(x)
    math.sin(x)
    math.tan(x)

    # this will give you pi:
    math.pi

Strings
-------

Add two strings together
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    first_name = "euclid "
    space = " "
    last_name = "von rabbitstein"
    full_name = first_name + space + last_name

Repeat a string
^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    message = "Repeat me!"
    repeated10 = message * 10

    # I like to use it for pretty printing code results
    line = "-" * 12
    print("   Title!   ")
    print(line)

Index into a string
^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    first_name = "Euclid"
    last_name = "Von Rabbitstein"
    first_initial = first_name[0]
    last_initial = last_name[0]
    initials = first_initial + last_initial

Slice a string
^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    # the syntax is
    #   my_string[start:stop]
    # this includes the start position but goes UP TO the stop
    # you can leave either empty to go to the front or end

    target = "door"
    last_three = target[1:]
    first_three = target[:3]
    middle_two = target[1:3]

    # you can use negatives to slice off the end!
    all_but_last = target[:-1]

    pig_latin = target[1:] + target[0] + "ay"


String's inner functions
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    full_name = "euclid von Rabbitstein"

    # all caps
    full_name_uppered = full_name.upper()

    # all lower
    full_name_lowered = full_name.lower()

    # use lower to make sure something is lower before you compare it
    user_command = "Exit"
    if user_command.lower() == "exit":
        print("now I can exit!")

    # first letter capitalized
    full_name_capitalized = full_name.capitalize()

    # split into a list
    full_name_list = full_name.split(" ")

    # strip off any extra spaces
    test_string = "   extra spaces everywhere   "
    stripped_string = test_string.strip()

    # replace things in a string
    full_name_replaced = full_name.replace("von", "rabbiticus")

    # use replace to delete things from a string!
    test_string = "annoying \t tabs in \t the string"
    fixed_string = test_string.replace("\t","")


Built-in Functions
------------------

.. code-block:: python
    :linenos:

    print("This prints to the console/terminal!")

    # notice the space at the end!
    # it helps so that what you type isn't right next to the ?
    name = input("What is your name? ")

    # use input to get an integer
    age = input("How old are you?")
    # but it's still a string!
    # convert it
    age = int(age)

    # test the length of a list or string
    name_length = len(name)

    # get the absolute value of a number
    positive_number = abs(5 - 100)

    # get the max and min of two or more numbers
    num1 = 10**3
    num2 = 2**5
    num3 = 100003
    biggest_one = max(num1, num2, num3)
    smallest_one = min(num1, num2, num3)
    # can do any number of variables here
    #   max(num1, num2) works
    #   and max(num1, num2, num3,  num4)

    ## max/min with a list
    ages = [12, 15, 13, 10]
    min_age = min(age)
    max_age = max(age)

    # sum over the items in a list
    # more list stuff is below
    ages = [12, 15, 13, 10]
    sum_of_ages = sum(ages)
    number_of_ages = len(ages)
    average_age = sum_of_ages / number_of_ages


Boolean algebra
---------------

Create a literal boolean variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    literal_boolean = True
    other_one = False

Create a boolean variable from comparisons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    x = 9
    y = 3
    x_is_bigger = x > y # True
    x_is_even = x % 2 == 0 # False
    x_is_multiple_of_y = x % y == 0 # True

Combine two boolean variables with 'and' and 'or'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    # example data
    card_suit = "Hearts"
    card_number = 7

    # save the results from comparisons!
    card_is_hearts = card_suit == "Hearts"
    card_is_diamond = card_suit == "Diamond"
    card_is_big = card_number > 8

    # only 1 of them needs to be true
    card_is_red = card_is_hearts or card_is_diamond

    # both need to be true
    card_is_good = card_is_red and card_is_big

    # creates the opposite!
    card_is_bad = not card_is_good

If, elif, and else
------------------


Use an if to test for something
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    power_level = 1000
    min_power_level = 500
    max_power_level = 1000

    # one thing is larger than another
    if power_level > minimum_power_level:
        print("We have enough power!")

    if power_level == max_power_level:
        print("You have max power!")


Create conditional logic
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    selected_option = 2

    if selected_option == 1:
        print("Doing option 1")
    elif selected_option == 2:
        print("Doing option 2")
    elif selected_option == 3:
        print("doing option 3")
    else:
        print("Doing the default option!")

Nest one if inside another if
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    name = "euclid"
    animal = "bunny"

    if animal == "bunny":
        if name == "euclid":
            print("Euclid is my bunny")
        elif name == "leta":
            print("Leta is my bunny")
        else:
            print("this is not my bunny..")
    else:
        print("Not my animal!")


Lists
-----

Create an empty list
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    new_list = list()
    # or
    new_list = []

Create a list with items
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    my_pets = ['euclid', 'leta']

Add onto a list
^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    my_pets.append('socrates')

Index into a list
^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    first_pet = my_pets[0]
    second_pet = my_pets[1]
    third_pet = my_pets[2]

Slice a list into a new list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    # the syntax is
    #   my_list[start:stop]
    # this includes the start position but goes UP TO the stop
    # you can leave either empty to go to the front or end

    first_two_pets = my_pets[:2]
    last_two_pets = my_pets[1:]

Test if a value is inside a list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    ## with any collection, you can test if an item is inside the collection
    ## it is with the "in" keyword

    my_pets = ['euclid', 'leta']
    if 'euclid' in my_pets:
        print("Euclid is a pet!")

Sets
----

Create a set or convert a list to a set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    my_pet_list = ['euclid', 'leta']

    # you can convert lists to sets using the set keyword
    my_pet_set = set(my_pet_list)

    # sets are like lists but you can't index into them or slice them
    # they are used for fast membership testing

    # you can create a new set by:
    my_pet_set = set(['euclid', 'leta'])


Add an item to a set
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    my_new_set = set()

    # instead of append, like a list, you use 'add'
    my_new_set.add("Potatoes")


Using sets to enforce uniqueness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    my_grocery_list = ['potatoes', 'cucumbers', 'potatoes']

    # now if you want to make sure items only appear once, you can convert it to a set
    # it will automatically do this for you, because items are only allowed to be in sets one time

    my_grocery_set = set(my_grocery_list)


For Loops
---------

Write a for loop
^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    for i in range(10):
        print("do stuff here")

Use the for loop's loop variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    for i in range(10):
        new_number = i * 100
        print("The loop variable is i.  It equals {}".format(i))
        print("I used it to make a new number. That number is {}".format(new_number))


Use range inside a for loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    start = 3
    stop = 10
    step = 2

    for i in range(stop):
        print(i)

    for i in range(start, stop):
        print(i)

    for i in range(start, stop, step):
        print(i)

Use a list inside a for loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    my_pets = ['euclid', 'leta']

    for pet in my_pets:
        print("One of my pets: {}".format(pet))

Nest one for loop inside another for loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    for i in range(4):
        for j in range(4):
            result = i * j
            print("{} times {} is {}".format(i, j, result))

While Loops
-----------

Use a comparison
^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    response = ""

    while response != "exit":
        print("Inside the loop!")
        response = input("Please provide input: ")


Use a boolean variable
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    done = False

    while not done:
        print("Inside the loop!")
        response = input("Please provide input: ")
        if response == "exit":
            done = True


Loop forever
^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    while True:
        print("Don't do this!  It is a bad idea.")

Special Loop Commands
---------------------

Skip the rest of the current cycle in the loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    for i in range(100):
        if i < 90:
            continue
        else:
            print("At number {}".format(i))


Break out of the loop entirely
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    while True:
        response = input("Give me input: ")
        if response == "exit":
            break

Functions
---------

No arguments and returns nothing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    def say_hello():
        print("hello!")


Takes one argument
^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    def say_something(the_thing):
        print(the_thing)


Returns a value
^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    def double(x):
        return 2*x


Takes two arguments
^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:
    
    def exp_func(x, y):
        result = x ** y
        return result
    
    final_number = exp_func(10, 3)
    
Takes keyword arguments
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:
    
    def say_many_times(message, n=10):
        for i in range(n):
            print(message)
    
    say_many_times("Hi!", 2)
    say_many_times("Yay!", 10)


Time module
-----------

Using time.time() to count how long something takes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    import time

    start = time.time()

    for i in range(10000):
        continue

    new_time = time.time()
    total_time = new_time - start
    print(total_time)


Using time.sleep(n) to wait for n seconds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    import time

    start = time.time()

    time.sleep(10)

    end = time.time()

    print(start - end)


Random Module
-------------

Generate a random number between 0 and 1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    import random
    
    num = random.random()
    print("the random number is {}".format(num))

Generate a random number between two integers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    import random
    
    num = random.randint(5, 100)
    print("the random integer between 5 and 100 is {}".format(num))

Select a random item from a list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    import random
    
    my_pets = ['euclid', 'leta']
    fav_pet = random.choice(my_pets)
    print("My randomly chosen favorite pet is {}".format(fav_pet))
    