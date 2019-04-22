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
        chosen = np.random.choice([1, 2, 3])
        if game(chosen, switch) == "goat":
            goats += 1
        if game(chosen, switch) == "car":
            cars += 1
    return [goats, cars]


# running 1st set
values_switch = run(100000, True)
goats_frac_switch = str(round(values_switch[0]/np.sum(values_switch) * 100, 3)) + '%'
cars_frac_switch = str(round(values_switch[1]/np.sum(values_switch) * 100, 3)) + '%'
labels_switch = ["goats " + goats_frac_switch, "cars " + cars_frac_switch]

# running 2nd set
values_stay = run(100000, False)
goats_frac_stay = str(round(values_stay[0]/np.sum(values_stay) * 100, 3)) + '%'
cars_frac_stay = str(round(values_stay[1]/np.sum(values_stay) * 100, 3)) + '%'
labels_stay = ["goats " + goats_frac_stay, "cars " + cars_frac_stay]

# plotting 1st graph
plt.subplot(211)
plt.title("If Always Switch:")
plt.pie(values_switch, labels = labels_switch)

# plotting 2nd graph
plt.subplot(212)
plt.title("If Always Stay:")
plt.pie(values_stay, labels = labels_stay)

plt.show()
