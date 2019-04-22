import matplotlib.pyplot as plt
import numpy as np

class door:
    """
    docstring
    """
    def __init__(self, item):
        self.item = item

def game(chosen, switch):
    """
    docstring
    """
    door_A = door("goat")
    door_B = door("goat")
    door_C = door("car")
    doors = [door_A, door_B, door_C]

    if chosen == 1:
        chosen = door_A 
    elif chosen == 2:
        chosen = door_B
    elif chosen == 3:
        chosen = door_C

    removed = False
    for i in doors:
        if i.item == "goat" and removed == False and i != chosen:
            doors.remove(i)
            removed = True

    if switch:
        for i in doors:
            if i != chosen:
                new_chosen = i

    else:
        new_chosen = chosen

    return new_chosen.item

def run(n, switch):
    """
    docstring
    """
    goats = 0
    cars = 0
    for i in range(n):
        chosen = np.random.choice([1,2,3])
        if game(chosen, switch) == "goat":
            goats += 1
        if game(chosen, switch) == "car":
            cars += 1
    return [goats, cars]

values = run(100000, True)
goats_frac = str(values[0]/np.sum(values) * 100) + '%'
cars_frac = str(values[1]/np.sum(values) * 100) + '%'
labels = ["goats " + goats_frac, "cars " + cars_frac]
plt.pie(values)
plt.legend(labels, loc = "lower left")
plt.show()









