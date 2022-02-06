import matplotlib.pyplot as plt

a = []
b = []

for x in range (-1000,1001):
    for y in range (-1000,1001):
        LHS = x**2
        RHS = y
        if LHS == RHS:
            a.append(x)
            b.append(y)

print ("x:",a)
print ("y:",b)

plt.plot(a, b)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Equation graph:')
plt.show()