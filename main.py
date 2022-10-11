import matplotlib.pyplot as plt
x = []
y = []
h = 10
v1 = 330
v2 = 1450
t = 0.2
r_bound = v2 * h / (v2 ** 2 - v1 ** 2) ** (0.5)
#r_bound = v1*t
r = h
n = 1000
delta = (r_bound - r) / n
while r < r_bound:
    x.append((r * r - h * h) ** (0.5) * (v1 * v1 * r + v1 * v2 * v2 * t - v2 * v2 * r) / v1 / r)
    y.append(-h - v2 * (r ** 2 * (v1 ** 2 - v2 ** 2) + (v2 * h) ** 2) ** (0.5) / (v1 * r) * (t - r / v1))
    r = r + delta
plt.plot(x, y)
plt.show()
