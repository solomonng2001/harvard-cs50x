[Mario](https://cs50.harvard.edu/x/2021/psets/1/mario/more/#mario)
==================================================================

[World 1-1](https://cs50.harvard.edu/x/2021/psets/1/mario/more/#world-1-1)
--------------------------------------------------------------------------

Toward the beginning of World 1-1 in Nintendo's Super Mario Brothers, Mario must hop over adjacent pyramids of blocks, per the below.

![screenshot of Mario jumping over adjacent pyramids](https://cs50.harvard.edu/x/2021/psets/1/mario/more/pyramids.png)

Let's recreate those pyramids in C, albeit in text, using hashes (`#`) for bricks, a la the below. Each hash is a bit taller than it is wide, so the pyramids themselves are also be taller than they are wide.

```
   #  #
  ##  ##
 ###  ###
####  ####

```

The program we'll write will be called `mario`. And let's allow the user to decide just how tall the pyramids should be by first prompting them for a positive integer between, say, 1 and 8, inclusive.

Here's how the program might work if the user inputs `8` when prompted:

```
$ ./mario
Height: 8
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########

```

Here's how the program might work if the user inputs `4` when prompted:

```
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####

```

Here's how the program might work if the user inputs `2` when prompted:

```
$ ./mario
Height: 2
 #  #
##  ##

```

And here's how the program might work if the user inputs `1` when prompted:

```
$ ./mario
Height: 1
#  #

```

If the user doesn't, in fact, input a positive integer between 1 and 8, inclusive, when prompted, the program should re-prompt the user until they cooperate:

```
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####

```

Notice that width of the "gap" between adjacent pyramids is equal to the width of two hashes, irrespective of the pyramids' heights.

Create a new directory (i.e., folder) called `mario` inside of your `pset1` directory, by executing

```
~/ $ mkdir ~/pset1/mario

```

Create a new file called `mario.c` inside your `mario` directory. Modify `mario.c` in such a way that it implements this program as described!

<sub>*Assignment description taken from https://cs50.harvard.edu/x/2021/*</sub>
