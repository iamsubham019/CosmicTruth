with open('app.py', encoding='utf-8') as f:
    lines = f.readlines()

lines[346] = '                    for sp in ax.spines.values(): sp.set_edgecolor((0.655, 0.545, 0.980, 0.14))\n'
lines[347] = "                    ax.grid(color=(0.655, 0.545, 0.980, 0.06), linestyle='--', linewidth=0.5)\n"

with open('app.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Fixed")