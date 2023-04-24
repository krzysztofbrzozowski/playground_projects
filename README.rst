Current list of playground projects
====
rock_paper_scissors_game
----
Play rock-paper-scissors with computer.
Select paper, rock or scissors and computer will randomly select its own.

.. code-block:: console

    Select one choice: (p)aper, (r)ock, (s)cissors, (e)xit
    p
    self.user_choice='paper', self.computer_choice='rock'
    ---> User win

tic_tac_toe_game
----
Play tic-tac-toe with second player by providing X and Y coordinates of your 'X' or 'O'

.. code-block:: console

    Provide X and Y coordinates for your point
    0,0
    User 0 set x_coordinates=0, y_coordinates=0
    ['x', None, None]
    [None, None, None]
    [None, None, None]
    Provide X and Y coordinates for your point

    ...

    Provide X and Y coordinates for your point
    2,2
    User 0 set x_coordinates=2, y_coordinates=2
    ['x', 'o', None]
    [None, 'x', None]
    ['o', None, 'x']
    --->  Player User 0 won -> diagonal equal

algorithms
----
TODO

* binary search algo
* selection sort algo

docker_testing
----
Sample projects from tutorials as a cheatsheet for future actions
Uses:

* Docker
* GitHub workflows