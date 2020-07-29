# QUS:1(assignment 2)
import random as r
import matplotlib.pyplot as plt
r.seed(0)
import math
trails = [100,1000,5000,10000]  ##different trails ar jnno different pi value
hits = 0
list1 = []
list2 = []
list3 = []
for n in trails:

    for i in range(n):

        # X
        x = r.uniform(0, 4)
        # Y
        y = r.uniform(0, 4)
        plt.scatter(x, y, color="green")
        dist = math.sqrt((x - 2) ** 2 + (y - 2) ** 2)
        # condition
        if dist <= 1.5:
            hits = hits + 1
            plt.scatter(x, y, color="red")
    pi = (16 / 2.25) * (hits / n)
    area = 16 * (hits / n)
    error_value = abs(pi - 3.1416)
    hits = 0  ##hit 0 na korley previous calculateed hit thekey jay so next pi value thik moto ashbey na so hits=0

    print("for n=" + str(n) + " pi-vaalue:" + str(pi))
    print("area of circle is:" + str(area))
    print("ESTIMATED ERROR VALUE:" + str(error_value))
    plt.show()
    list1.append(pi)
    list2.append(error_value)
    list3.append(area)

x = ['100', '500', '600', '800']
plt.bar(x, list1)
print("FIRST BAR PLOT:")
plt.show()

plt.bar(x, list2)
print("SECOND BAR PLOT:")
plt.show()

plt.bar(x, list3)
print("THIRD BAR PLOT:")
plt.show()

print("PI values LIST:")
print(list1)
print("ERROR values LIST:")
print(list2)
print("AREA OF CIRCLE values LIST:")
print(list3)