import matplotlib.pyplot as plt
import numpy as np


class door:
    """
    The door object has one attribute that defines what is behind it
    """

    def __init__(self, item):
        self.item = item


def game(chosen, switch):
    """
    This runs the game. 
    Takes parameters: 
        int chosen (for initially chosen door)
        bool switch (for whether you will switch doors)

    Returns:
        item behind final chosen door
    """
    # creates door objects
    door_A = door("goat")
    door_B = door("goat")
    door_C = door("car")
    doors = [door_A, door_B, door_C]

    # matches function argument to a door
    if chosen == 1:
        chosen = door_A
    elif chosen == 2:
        chosen = door_B
    elif chosen == 3:
        chosen = door_C

    # removes 1 goat-door from the list
    removed = False
    for i in doors:
        if i.item == "goat" and removed == False and i != chosen:
            doors.remove(i)
            removed = True

    # switches door if function argument is True
    if switch:
        for i in doors:
            if i != chosen:
                new_chosen = i

    else:
        new_chosen = chosen

    # returns final result
    return new_chosen.item


def run(n, switch):
    """
    Runs game multiple times.
    Takes parameters:
        int n (the number of times you want to run the game)
        bool switch (whether you want to switch doors)

    Returns:
        List of the number of goats and cars won
    """
    goats = 0
    cars = 0
    for i in range(n):
        chosen = np.random.choice([1, 2, 3])
        if game(chosen, switch) == "goat":
            goats += 1
        if game(chosen, switch) == "car":
            cars += 1
    return [goats, cars]


# running 1st set
val_switch = run(100000, True)
goats_switch = str(round(val_switch[0]/np.sum(val_switch) * 100, 3)) + '%'
cars_switch = str(round(val_switch[1]/np.sum(val_switch) * 100, 3)) + '%'
labels_switch = ["goats " + goats_switch, "cars " + cars_switch]

# running 2nd set
val_switch = run(100000, False)
goats_stay = str(round(val_switch[0]/np.sum(val_switch) * 100, 3)) + '%'
cars_stay = str(round(val_switch[1]/np.sum(val_switch) * 100, 3)) + '%'
labels_stay = ["goats " + goats_stay, "cars " + cars_stay]

# plotting 1st graph
plt.subplot(211)
plt.title("If Always Switch:")
plt.pie(val_switch, labels=labels_switch)

# plotting 2nd graph
plt.subplot(212)
plt.title("If Always Stay:")
plt.pie(val_switch, labels=labels_stay)

plt.show()
