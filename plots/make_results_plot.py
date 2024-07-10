import matplotlib.pyplot as plt
import numpy as np

libs = ["HypEcs", "LeoEcsLite", "LeoECS", "DefaultEcs", "Svelto.ECS", "Arch", "RelEcs", "MGE.Entities", "Entitas"]
means = [1.133, 1.194, 1.208, 1.216, 1.384, 1.394, 1.401, 2.004, 4.732]
colors = ['lightgreen'] * 6 + ['khaki'] + ['lightcoral'] * 2

def make_plot(fig, ax, colors):
    bar_width = 0.5
    x = np.arange(len(libs))

    bars = ax.bar(x, means, bar_width, color=colors, edgecolor='black')

    ax.set_xlabel('Knihovny', fontsize=18)
    ax.set_ylabel('Průměrný čas (s)', fontsize=18)
    ax.set_xticks(x)
    ax.set_xticklabels(libs, rotation=45, ha='right', fontsize=16)
    ax.set_yticklabels(ax.get_yticks(), fontsize=16)

    ax.set_ylim(0, 6)
    ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.3f}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=14)

fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
make_plot(fig1, ax1, 'skyblue')
make_plot(fig1, ax2, colors)

fig1.suptitle('Výsledky měření', fontsize=20)

plt.tight_layout()
plt.show()