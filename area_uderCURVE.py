# QUS:2(assignment 2)
import random as r

import matplotlib.pyplot as plt

r.seed(0)
trails = [100, 1000, 5000, 10000]
hits = 0
for n in trails:

    for i in range(n):

        # X
        x = r.uniform(0, 3)
        # Y
        y = r.uniform(0, 5)
        plt.scatter(x, y, color="green")
        dist = x + 2
        # condition
        if y <= dist:
            hits = hits + 1
            plt.scatter(x, y, color="red")
    area = 15 * (hits / n)
    hits = 0
    print("area of the shaded part is:" + str(area))
    plt.show()