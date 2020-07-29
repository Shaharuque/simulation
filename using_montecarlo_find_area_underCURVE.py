# QUS:3(assignment 2)
import random as r
import matplotlib.pyplot as plt
r.seed(0)
import math
trails = [100, 1000, 5000, 10000]
hits = 0
for n in trails:

    for i in range(n):

        # X
        x = r.uniform(0, 8)
        # Y
        y = r.uniform(0, 4)
        plt.scatter(x, y, color="green")

        dist = math.sqrt(4 * x)
        dist1 = 8 - x
        # condition
        if y <= dist and y <= dist1:
            hits = hits + 1
            plt.scatter(x, y, color="red")

    area = (4 * 8) * (hits / n)
    hits = 0
    print("area under the curve is:" + str(area))
    plt.show()