Installing PyGame
=================


PyGame is a library that creates graphical interfaces for games.  
There is sometimes some difficultly in installing it, so below I have listed information to help you out. 


Where to get it
---------------

There are a couple of good directions on the internet: 

1. `The main pygame repository <https://bitbucket.org/pygame/pygame/downloads>`_
2. `The programarcadegames website <http://programarcadegames.com/index.php?chapter=foreword&lang=en>`_
3. `Pygame Simplifed <http://webprojects.eecs.qmul.ac.uk/fa303/pgs/install.html#installpygame>`_


Common Issues
-------------

1. I installed Pygame, but when I use python, it says it can't find it.
    - this is usually caused by having two versions of python installed
    - Email me and we will talk through the situation. It usually involves a couple things that need to be check to verify this is the situation. 

2. When installing Pygame, at the part where it says "Select Python Installation", it is showing no python installaion
    - this is can be an issue sometimes with the way Python was installed.  
    - I have had this happen to me with Anaconda
    - Try the following:
    ```
    In the Anaconda menu, choose Tools, then "open command prompt".
    
    If you don't have Anaconda and are using windows, open the Run window (hit Windows key and R at the same time).  Then, type in "cmd" and hit enter.
    
    If you don't have Anaconda and are using a mac, mac has an application called "terminal".  Open this, it is the same as the windows cmd window. 

    Inside the cmd/terminal window, type "pip install pygame" and hit enter. 
    ```
    
