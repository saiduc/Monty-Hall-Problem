# Demonstration of Monty Hall Problem using Python

This is a simple demonstration of the Monty Hall problem in Python. The Monty
Hall Problem is a famous statistics problem with an unintuitive solution that
often surprises people. I put this together just for fun after watching a
Brooklyn Nine-Nine episode about it!

## The Problem

So what is the Monty Hall problem? You are on a game show with the charismatic
host Monty Hall. The game is simple. There are 3 doors. There are goats behind 2
of the doors, and a car behind the 3rd. You don't know what is behind any of the
doors, but the host, Monty Hall, does.

You get to pick a door to open. After you have made your choice, Monty Hall (who
knows what is behind each door) will open one of the other doors to reveal a
goat. He will then ask, "Do you want to switch your choice, or stick to the door
you chose initially?" You will then be able to make that decision. After this,
Monty Hall will open your final choice of door to reveal what your prize will be
that evening (ideally a car).

So what do you do? Obviously you can't be tactical with your initial choice (it
is just a random choice between 3 doors). But what about your 2nd decision?
Should you switch or should you stay?

## The Solution

The solution is that you should always switch. Many people believe it makes no
difference, as for the 2nd decision you have a 50/50 chance between a goat and a
car. But this is in fact incorrect.

If stick with your initial choice, then in order to win the car, you have to
have chosen the door with the car with your initial choice. There is a 1/3
chance of doing this.

However if you switch your initial choice, then in order to win the car, you
have to have chosen a door with the goat with your initial choice. This is
because the door the host opens will always have a goat behind it. So if your
initial choice is a goat door, and the host opens the other goat door, then when
you switch you will have chosen the door with the car. And there is a 2/3 chance
of picking a door with a goat in your initial choice.

So if you always switch, you have a 2/3 chance of winning a car, as opposed to
1/3 if you always stick with your initial choice.

## The Code

The code is very simple. It sets up the problem and runs n = 100000 trials of
always switching the door, and n = 100000 trials of always sticking with the
original door. It then plots pie charts showing the outcomes.

As expected, we see 2/3 car if you always switch and 1/3 car if you don't.

## Acknowledgements

* A fun numberphile video on the subject: 
https://www.youtube.com/watch?v=4Lb-6rxZxx0
* A good paper on simulating the problem: 
https://pdfs.semanticscholar.org/344f/0c38c9391a02ad26d82f20263b646ba895f1.pdf

