###simulation lab assignment car chasing problem
import math
import matplotlib.pyplot as plt

# A,B,C,D 4 cars.
x_B = [0]
y_B = [10]
x_C = [10]
y_C = [10]
x_A = [10]
y_A = [0]
x_D = [0]
y_D = [0]

v_A = 3
v_B = 5
v_C = 7
v_D = 2

distDB = []  # Distance between B and D, D is chased by B ,B->D
distBC = []
distCA = []
distAD = []
countA = 0
countB = 0
countC = 0
countD = 0

for t in range(0, 20):
    distDB.append(math.sqrt((x_B[t] - x_D[t]) ** 2 + (y_B[t] - y_D[t]) ** 2))  # distance calculation at time =t
    distBC.append(math.sqrt((x_B[t] - x_C[t]) ** 2 + (y_B[t] - y_C[t]) ** 2))  # distance calculation at time =t
    distCA.append(math.sqrt((x_C[t] - x_A[t]) ** 2 + (y_C[t] - y_A[t]) ** 2))
    distAD.append(math.sqrt((x_A[t] - x_D[t]) ** 2 + (y_A[t] - y_D[t]) ** 2))
    print("At time= ", t)
    print("x_B =", x_B[t], "y_B= ", y_B[t])
    print("x_C = ", x_C[t], "y_C=", y_C[t])
    print("x_A = ", x_A[t], "y_A=", y_A[t])
    print("x_D = ", x_D[t], "y_D=", y_D[t])

    print("distance between DB: " + str(distDB[t]))
    print("distance between BC: " + str(distBC[t]))
    print("distance between CA: " + str(distCA[t]))
    print("distance between AD: " + str(distAD[t]))
    ##condition

    if distDB[t] < 5:
        print("B WILL SHOOTS AT D ,at time:", t)
        countD += 1
        # plt.plot(x_B,y_B, color="red")
    if distBC[t] < 5:
        print("C WILL SHOOTS AT B ,at time:", t)
        countB += 1
        # plt.plot(x_C,y_C, color="green")
    if distCA[t] < 5:
        print("A WILL SHOOTs AT C ,at time:", t)
        countC += 1
        # plt.plot(x_A,y_A, color="blue")
    if distAD[t] < 5:
        print("D WILL SHOOTS AT A ,at time:", t)
        countA += 1
        # plt.plot(x_D,y_D, color="black")

    sin = (y_D[t] - y_B[t]) / distDB[t]  # D IS CHASED BY B
    cos = (x_D[t] - x_B[t]) / distDB[t]
    x_Bnew = x_B[t] + v_B * cos
    y_Bnew = y_B[t] + v_B * sin
    x_B.append(x_Bnew)  # new x_B
    y_B.append(y_Bnew)  # new y_B

    sin = (y_C[t] - y_A[t]) / distCA[t]  # C IS CHASED BY A
    cos = (x_C[t] - x_A[t]) / distCA[t]
    x_A.append(x_A[t] + v_A * cos)  # new x_A
    y_A.append(y_A[t] + v_A * sin)  # new y_A

    sin = (y_B[t] - y_C[t]) / distBC[t]  # B IS CHASED BY C
    cos = (x_B[t] - x_C[t]) / distBC[t]
    x_C.append(x_C[t] + v_C * cos)  # new x_C
    y_C.append(y_C[t] + v_C * sin)  # new y_C

    sin = (y_A[t] - y_D[t]) / distCA[t]  # A IS CHASED BY D
    cos = (x_A[t] - x_D[t]) / distCA[t]
    x_D.append(x_D[t] + v_D * cos)  # new x_D
    y_D.append(y_D[t] + v_D * sin)  # new y_D

print("NUMBER OF TIMES EACH CAR GOT SHOT DURING SIMULATION:")
print("car A got " + str(countA) + " shots")
print("car B got " + str(countB) + " shots")
print("car C got " + str(countC) + " shots")
print("car D got " + str(countD) + " shots")

plt.plot(x_A, y_A, color="blue", label="pathA")  # cuz x_A,y_A included in the list
plt.plot(x_B, y_B, color="orange", label="pathB")
plt.plot(x_C, y_C, color="green", label="pathC")
plt.plot(x_D, y_D, color="red", label="pathD")
plt.legend()
plt.show()