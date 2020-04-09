

Challenge 1: Pong
=======================

This assignment is more challenging than any you've tackled so far. This is not because it is more complex than previous
ones, but rather because it brings together many different small problems.

It is important that we develop the skill of **breaking down complex tasks into smaller, manageable chunks**.

"How did the ant eat the elephant? One bite at a time"


To support you in this, I've outlined a work plan that you can find after the game description.

The game
--------

I love video games, and the history of their evolution. The earliest interactive game I could track in history is Pong.
  Here's a video of what it looked like back then: [Atari
Pong](http://www.youtube.com/watch?v=_tvTsbAXuRs&feature=player_embedded).

The game has three important behaviors:

1.  If the ball hits a vertical wall, the game is over.
2.  If the ball hits a horizontal wall, it bounces off that wall.
3.  If the ball hits the inner face of a paddle, it bounces off the
    paddle.

Each paddle is independently controllable. Six keys on the keyboard
control the game:

-   *a* moves the left paddle up.
-   *z* moves the left paddle down.
-   *k* moves the right paddle up.
-   *m* moves the right paddle down.
-   The space bar starts a new game.
-   *q* quits the program (use the function cs1_quit())

The paddles should never leave the playing surface. While a paddle is
touching the top wall, it cannot go up, and while a paddle is touching
the bottom wall, it cannot go down.

Even given these rules, you have much latitude in this assignment. You
do not have to produce something that looks identical to my version; it
is meant only to provide a demonstration of basic functionality.

Checkpoint 1 : Moving the paddles
------------------------------

You will start by putting up a graphics window with just the paddles.
Each paddle is a rectangular block, with dimensions of your choosing,
initially in the upper-left and lower-right corners of the
window.

You may choose whatever colors you like.

The paddles may move up and down as follows:

-   If the user presses the *a* key, then the left paddle moves up.
-   If the user presses the *z* key, then the left paddle moves down.
-   If the user presses the *k* key, then the right paddle moves up.
-   If the user presses the *m* key, then the right paddle moves down.

But no paddle may move outside the window. When the left paddle hits the
top window boundary, pressing *a* has no effect, and when it hits the
bottom window boundary, pressing *z* has no effect. Likewise, when the
right paddle hits the top window boundary, pressing *k* has no effect,
and when it hits the bottom window boundary, pressing *m* has no effect. This means that the impact of pressing the keys
 is **conditional**

Every time we draw the game, the position of the paddles may change from their initial set up. We will have to rely on 
some global variables to track where we should draw the paddles now. *Which of their coordinate changes as we press the
keys?*


Checkpoint 2: Ball game
-----------------------------------

As a next step, I recommend a simple animation of moving the ball. Start
with the ball in the center of the window, and have it move to the
right. Of course, in this first step, the ball
will quickly leave the window, but that's OK: it's just a first step.

Next, I recommend working on a **function** to detect whether the ball has moved beyond a vertical wall on the right hand 
side of the screen in the current time step.  (Why *moved beyond*, and not *made contact with*?  The ball might move 
more than one pixel in each time step, so perfect equality may never be achieved.  Greater-than and less-than operators 
are great!)  This function will need to take some parameters describing the location of the ball and the x-coordinate of
 the wall.  The function should return `True` or `False` depending on whether a collision has happened.  

After that, you could work on how the ball bounces when a collision happens.  I find it useful to think in terms of 
velocities and state variables.  An `x` variable might keep track of the ball location, and a `vx` variable might keep 
track of the horizontal component of the ball velocity (the amount the ball moves in the x direction each time step). 
After bouncing off of the left side of the screen, the x velocity should be positive.    

You could add three more walls, and new functions to check for collisions.  Try out different directions of motion for the ball.  Now you have a virtual pool table:  four walls and a bouncing ball.  Then you could add controllable paddles, and checks for collisions.  And you could handle the fact that the ball should have a radius greater than zero, and that this will affect where bounces occur.

Checkpoint 3: The state of the game
-----------------------------------

The game should start in a paused state, and wait until the **space** key is pressed to start the game.
In fact, whenever **space** is pressed, the game should restart, with the ball starting from the center.


How do you stop the ball's motion? One way is to keep a boolean state variable that says
whether a game is in progress. If a game is not in progress, then don't
update the ball's position. There might even be additional uses for this boolean
state variable.

How do you end the program when the user types *q*? Here's a really easy
way: call the parameterless function `cs1_quit`, from cs1lib.


Design and style
----------------

Your program should be understandable with minimum possible effort.  The logic
should be as straightforward as possible.  The beauty of a program lies in its design and in its style.

### Functions

Don't be afraid to write functions that help your program out. I
mentioned a couple earlier. But you should feel free to write
more. Your functions should all be near the top of your code, not mixed in with code at the global level. This makes it easy to quickly see what functions you will be using.

### Constants

Constant make code easier to read and modify.  You could have constants for the keys that affect the game, height and width of the paddles, initial ball velocity, etc.  Here's the rule of thumb.  If you see a raw value, like 5, or "b", anywhere in the code except in an assignment to a constant, consider using a constant.  Constants should be in all uppercase.   

Several of the constants were defined in terms of the height and width
of the window. That way, if I want to change the window size, I can
change numbers in just one place, and everything else looks right.

### Documentation

You should include comments that tell the human reader what he or she needs
to understand in order to make sense of your program.  You should also choose descriptive variable and function names.
Meaningless names are bad, and misleading names are worse.

Grading
-------

Correctness:

-   The ball bounces correctly off the paddles and the top and bottom
    walls. The game ends when the ball hits a vertical wall.
-   The new game (space bar) and quit (q) commands work correctly.

Coding proficiency:

- You correctly uses functions to organize the code's logic
- Drawing is done as per the standards of aluLib.
- Any logic in the code is handled clearly and elegantly. If statements are used appropriately.

Style:

-   Clear design and organization.
-   Good variable names, function names, and comments.
-   Functions where appropriate and not where inappropriate.

## Honor Code

Please make sure that you fully understand the Academic Honor System, and reach out if you need any clarifications. 


What to turn in
---------------

Make sure your git repository contains the following:
- A single python file for the pong game.
- Optionally: a second python file for the extra credit version of the game
- A text file describing the following:
    - An acknowledgement of upholding the honor code, or information if any breach occurred.
    - Any extra credits or additional features you attempted.
    - Any notes you want to bring to the attention of the grader. 


Extra Credit
------------

You can add all sorts of features to the basic Pong game for extra
credit. Make sure, however, before you charge off and do extra credit
that you have the basic game working correctly, that you've designed it
as cleanly as possible, and that you've documented it well. Remember, the extra credit points don't really count for anything.

Also, **before you start any extra credit, save your basic pong source
code, and submit that as your main submission. Also take a screenshot
for submission before working on extra credit. Start a new Python file
for any extra credit.**  If you do pursue extra credit, include a text
file in your submission that tells us what extra-credit features you've
included.

You can add plenty of extra-credit features. Here is a list of ideas to
get you thinking, but by all means let your imagination go.

-   When the ball bounces off a moving paddle, accelerate the ball
    slightly in the direction of the paddle's motion: 10 points.
-   Random initial direction for the ball. (But make sure that it has
    enough horizontal and enough vertical component to be interesting.
    If the ball just goes up and down, or almost just up and down, the
    game is not going to be interesting.): 5 points.
-   Ball changing color each time it bounces off a paddle: 5 points.
-   Unpredictable bouncing: 5 points.
-   Fancy .png images for ball and paddles: 5 points.

Here is how you can use .png images. Suppose you want to draw an image
of a paddle, in paddle.png, at location (100, 150). Here's what you
would do:

``` {.sourceCode .python}
from cs1lib import *
img = load_image("paddle.png")

  ## somewhere in a drawing function called by start_graphics:
  draw_image(img, 100, 150)
```

Before you run your program, make sure to drag the image file into your
PyCharm project.

Crazier, less well-specified ideas (extra credit will be assigned
relatively arbitrarily, according to how impressed we are):

-   More than two players.
-   Obstacles.
-   Obstacles that accelerate the ball.
-   [Breakout](https://en.wikipedia.org/wiki/Breakout_%28video_game%29), [Arkanoid](https://en.wikipedia.org/wiki/Arkanoid), or a pinball machine.

Acknowledgement
---------------

Many thanks to professor Devin Balkcom for allowing us to reuse this assignment, as well as the Dartmouth CS department 
for their support.