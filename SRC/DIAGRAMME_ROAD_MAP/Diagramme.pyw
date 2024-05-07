import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define the start date of the project
start_date = datetime(2024, 1, 1)

fig, ax = plt.subplots(figsize=(12, 8))

# Define tasks, durations (in days), and dependencies again in case of state reset
tasks = [
    {"name": "Choix de l'environnement", "duration": 2, "start": start_date} ,
    {"name": "Configuration Multi-hébergement Apache", "duration": 3, "start": start_date + timedelta(days=2)},
    {"name": "Sécurisation serveurs et bases", "duration": 4, "start": start_date + timedelta(days=5)},
    {"name": "Mise en place Infrastructure", "duration": 5, "start": start_date + timedelta(days=9)},
    {"name": "Configuration Routage et Pare-feu", "duration": 3, "start": start_date + timedelta(days=14)},
    {"name": "Configuration DNS", "duration": 2, "start": start_date + timedelta(days=17)},
    {"name": "Développement script automatisation", "duration": 3, "start": start_date + timedelta(days=19)},
    {"name": "Tests de Fonctionnalité", "duration": 2, "start": start_date + timedelta(days=22)},
    {"name": "Tests de Sécurité", "duration": 3, "start": start_date + timedelta(days=24)},
    {"name": "Tests de Performance", "duration": 2, "start": start_date + timedelta(days=27)}
]

# Prepare plotting with names
y_pos = range(len(tasks))

# Create bars for tasks
for i, task in enumerate(tasks):
    start = mdates.date2num(task["start"])
    end = mdates.date2num(task["start"] + timedelta(days=task["duration"]))
    color = "skyblue"  # Default color
    if task["name"] == "Choix de l'environnement":
        color = "orange"
    elif task["name"] in ["Développement script automatisation", "Tests de Sécurité", "Sécurisation serveurs et bases"]:
        color = "green"
    elif task["name"] in ["Configuration DNS", "Configuration Routage et Pare-feu", "Configuration Multi-hébergement Apache"]:
        color = "purple"
    ax.barh(i, end - start, left=start, color=color, edgecolor="black")

# Add names on the left side with specified colors
names = ["Eloham", "Adrien", "Matteo", "Anissa", "Groupe"]
colors = ["Green", "violet", "violet", "skyblue", "orange"]
for i, (name, color) in enumerate(zip(names, colors)):
    ax.text(start_date - timedelta(days=12), len(tasks) - i - 1, name, color=color, fontsize=10, ha="right")

# Set labels, title, and format the date display
ax.set_xlabel('Date')
ax.set_ylabel('Tâche')
ax.set_yticks(y_pos)
ax.set_yticklabels([task["name"] for task in tasks])
ax.set_title('ROAD MAP')

formatter = mdates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=45, labelsize=10)

# Adjust figure to make room for names
plt.subplots_adjust(left=0.3)

# Show grid
ax.grid(True)

# Set the icon for the Matplotlib window
plt.get_current_fig_manager().window.iconbitmap('dia.ico')

# Show the plot
plt.show()
bash
c&c

$ python3 -c 'import pty; pty.spawn("/bin/bash")'
$ CTRL + Z
$ stty raw -echo; fg
# PRESS enter
$ export TERM=xterm-256color

