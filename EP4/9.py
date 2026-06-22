# AI/ML Series - Episode 4
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2)

ax[0].plot([1, 2, 3], [1, 4, 9])
ax[1].bar(["A", "B", "C"], [3, 5, 2])

plt.show()