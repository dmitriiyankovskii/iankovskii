import numpy as np
import matplotlib.pyplot as plt
import textwrap
from matplotlib.ticker import AutoMinorLocator
long_title = "график зависимости U(t)"
wrapped_title = textwrap.fill(long_title, width=20)
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
data_array = np.loadtxt("data.txt", dtype=int)
data_array = data_array*(3.3/256)
data_time = np.arange(0, 898*0.0134, 0.0134)
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)
ax.set_xlim(0, 12)
ax.set_ylim(0, 3.3)
plt.plot(data_time[::10], data_array[::10], color='red', marker = 'o', markersize=1, label='U(t)')
plt.legend(loc='upper right',fontsize=10,title='Легенда',title_fontsize=12)
plt.title(
    wrapped_title,
    y=1.05,         
    fontsize=16,
    fontweight='bold'
)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))  
ax.yaxis.set_minor_locator(AutoMinorLocator(2))  

ax.grid(which='major', color='black', linestyle='-', linewidth=0.5, alpha=0.7)

ax.grid(which='minor', color='gray', linestyle=':', linewidth=0.3, alpha=0.3)

plt.text(
    1, 1,
    f"Время зарядки:  4.5 сек\nВремя разрядки: 5.5 сек",
    fontsize=10,
    bbox=dict(facecolor='white', edgecolor='gray', alpha=0.7, boxstyle='round')
)

plt.ylabel("U, В")
plt.xlabel("t, c")
plt.savefig("test.png")
plt.show()