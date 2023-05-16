import matplotlib.pyplot as pla
import matplotlib as mpl
import matplotlib.patches as mpatches
import tkinter as tk
from tkinter import filedialog as fd

mpl.use('TkAgg')

# ---------------------------------------------------------------#
"""GUI"""
window = tk.Tk()
window.title("PamStamp First derivation")
window.geometry("200x200+100+100")
window.resizable(False, False)
FONT = font=("Helvetica", 10, "bold")
label = tk.Label(window, text='PamStamp first derivation', font=FONT)
label.place(x=15, y=10)


def open_file():
    major_file = fd.askopenfilename(initialdir='/PamStamp_calculate/String', title='Open major string file')
    major_file = open(major_file, "r")
    minor_file = fd.askopenfilename(initialdir='/PamStamp_calculate/String', title='Open minor string file')
    minor_file = open(minor_file, "r")

    next(major_file)
    next(major_file)
    next(minor_file)
    next(minor_file)

    time = []
    major_strain = []
    minor_strain = []
    while True:
        line1 = major_file.readline()
        line2 = minor_file.readline()

        if not line1 or not line2:
            break

        x = line1.strip('/n').split()
        y = line2.strip('/n').split()
        time.append(float(x[0]))
        major_strain.append(float(x[1]))
        minor_strain.append(float(y[1]))

    """VYPOCET RYCHLOSTI"""

    rychlost = []
    for r in range(0, len(major_strain) - 2):
        subtraction_major_strain = major_strain[r + 2] - major_strain[r]
        subtraction_major_time = time[r + 2] - time[r]
        answer_zrychlenie = round(subtraction_major_strain / subtraction_major_time, 6)
        rychlost.append(answer_zrychlenie)
    del time[0:1]
    time.pop()
    del major_strain[0:1]
    major_strain.pop()
    del minor_strain[0:1]
    minor_strain.pop()

    """   GRAF   """

    fig, ax = pla.subplots()
    pla.title('Vypočet rychlosti')
    pla.xlabel('Čas')
    pla.ylabel('Rychlosť')
    pla.plot(time, rychlost, 'g')
    pla.plot(time, major_strain, 'r')
    pla.plot(time, minor_strain)
    red_patch = mpatches.Patch(color='red', label='Major Strain')
    green_patch = mpatches.Patch(color='green', label='Rychlosť')
    blue_patch = mpatches.Patch(color='blue', label='Minor Strain')
    ax.legend(handles=[red_patch, green_patch, blue_patch])
    pla.show()


butt_open_file = tk.Button(window, text="major string",
                            command=open_file)
img = tk.PhotoImage(file="C:/Users/juliy/PycharmProjects/PamStamp/icon/butt_icon.png")
butt_open_file.config(image=img)
butt_open_file.place(x=70, y=100)

window.mainloop()
