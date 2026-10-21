import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot([1, 2, 3], [2, 4, 6], "r--")
ax.plot([1, 2, 3], [3, 2, 1], "g-")
ax.set_title("Example plot")
plt.show()

# 1. Does this code create one plotting panel (Axes object) or two?
# Explain briefly. A panel is a plotting area, not an individual x-axis or y-axis.
# Your answer:
# One. plt.subplots(1, 1) creates a 1x1 grid, i.e. a single Axes (ax), and both ax.plot() calls draw on it.
# 2. How many data lines are drawn? What are the y-values of the red dashed line?
# Your answer:
Two lines. The red dashed line ("r--") has y-values 2, 4, 6.