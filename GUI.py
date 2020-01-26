import tkinter as tk
from tkinter import ttk
from ho_gyaaaa import main
import time
import webbrowser


win = tk.Tk()

win.title('Traffic congestion minimization')

label = ttk.Label(win, text="Total number of cars (1-300)   ")
label.grid(column=0, row=0)

n = tk.IntVar(value=30)
nameEntered = ttk.Entry(win, width=20, textvariable=n)
nameEntered.grid(column=1, row=0)
nameEntered.focus()

label = ttk.Label(win, text="Number of proposed routes per car (1-5)   ")
label.grid(column=0, row=1)

r = tk.IntVar(value=3)
nameEntered = ttk.Entry(win, width=20, textvariable=r)
nameEntered.grid(column=1, row=1)
nameEntered.focus()

label = ttk.Label(win, text="Map location   ")
label.grid(column=0, row=2)

loc = tk.StringVar()
numberComboBox = ttk.Combobox(win, width=20, textvariable=loc, state="readonly")
numberComboBox['values'] = ("Saddar, Rawalpindi", "G-13-3, Islamabad", "Kamppi, Finland", "Blue Area, Islamabad",
                            "NUST, Islamabad")

numberComboBox.grid(column=1, row=2)
numberComboBox.current(0)

same_source = tk.IntVar()
check1 = tk.Checkbutton(win, text="Same starting point for each car", variable=same_source)
check1.select()
check1.grid(row=3, column=0, sticky=tk.W)

same_dest = tk.IntVar()
check1 = tk.Checkbutton(win, text="Same destination point for each car", variable=same_dest)
check1.select()
check1.grid(row=4, column=0, sticky=tk.W)

qc = tk.IntVar()

label = ttk.Label(win, text="Method of computation: ")
label.grid(column=0, row=5, sticky="W")

# Radio Button 1
tabu = tk.Radiobutton(win, text="Tabu search (classical)", variable=qc, value=False)
tabu.grid(column=0, row=6, sticky="W")

# Radio Button 2
dwave = tk.Radiobutton(win, text="D-Wave (quantum annealing)", variable=qc, value=True)
dwave.grid(column=0, row=7, sticky="W")

label = ttk.Label(win, text="Time taken to solve QUBO instance (in seconds): ")
label.grid(column=0, row=8)

QUBO_time = tk.StringVar()
T_0 = tk.Label(win, height=2, width=30, text="")
T_0.grid(column=1, row=8)

T_0.configure(text=QUBO_time)

label = ttk.Label(win, text="Total runtime of program (in seconds): ")
label.grid(column=0, row=9)

total_time = tk.StringVar()
T_1 = tk.Label(win, height=2, width=30, text="")
T_1.grid(column=1, row=9)

T_1.configure(text=total_time)


# Creating a button

def clickMe():
    # aButton.configure(text = "CLICKED!")
    # aLabel.configure(foreground = "red")
    print("n: ", n.get())
    print("r: ", r.get())
    print("same_source: ", same_source.get())
    print("same_dest: ", same_dest.get())
    print("qc: ", qc.get())
    print("loc: ", loc.get())

    # QUBO_time_ = main(int(n.get()),int(r.get()), loc.get(), int(same_source.get()), int(same_dest.get()), int(qc.get()))

    start = time.clock()
    QUBO_time_ = main(n.get(), r.get(), loc.get(), int(same_source.get()), int(same_dest.get()), int(qc.get()))
    end = time.clock()
    elapsed = end - start

    QUBO_time.set(QUBO_time_)
    T_0.config(text=QUBO_time.get())
    T_1.config(text=elapsed)

    webbrowser.open("heatmap_short.html")
    webbrowser.open("heatmap_opt.html")


aButton = ttk.Button(win, text="Compute", command=clickMe)
aButton.grid(column=0, row=10, sticky="E")

win.mainloop()
