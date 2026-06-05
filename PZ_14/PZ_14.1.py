import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Registration Form")
root.geometry("750x450")
root.configure(bg="#2E6B9E")

frame = tk.LabelFrame(
    root, text=" Registration Details ", fg="white", bg="#2E6B9E"
)
frame.grid(row=0, column=0, padx=20, pady=20)

def make_lbl(txt, r):
    tk.Label(
        frame, text=txt, font=("Arial", 10, "bold"), fg="white", bg="#2E6B9E"
    ).grid(row=r, column=0, sticky="e", padx=10, pady=8)


make_lbl("University :", 0)
tk.Entry(frame, width=40).grid(row=0, column=1, sticky="w")

make_lbl("Institute :", 1)
tk.Entry(frame, width=40).grid(row=1, column=1, sticky="w")

make_lbl("Branch :", 2)
cmb_branch = ttk.Combobox(frame, width=20, values=[])
cmb_branch.insert(0, "-- select --")
cmb_branch.grid(row=2, column=1, sticky="w")

make_lbl("Degree :", 3)
f_deg = tk.Frame(frame, bg="#2E6B9E")
f_deg.grid(row=3, column=1, sticky="w")
cmb_deg = ttk.Combobox(f_deg, width=12, values=[])
cmb_deg.insert(0, "-- select --")
cmb_deg.grid(row=0, column=0)

tk.Radiobutton(
    f_deg, text="Pursuing", bg="#2E6B9E", fg="white", selectcolor="#2E6B9E", state="disabled"
).grid(row=0, column=1, padx=10)
tk.Radiobutton(
    f_deg, text="Completed", bg="#2E6B9E", fg="white", selectcolor="#2E6B9E", state="disabled"
).grid(row=0, column=2)

make_lbl("Avarage CPI :", 4)
f_cpi = tk.Frame(frame, bg="#2E6B9E")
f_cpi.grid(row=4, column=1, sticky="w")
tk.Spinbox(f_cpi, from_=0, to=0, width=5).grid(row=0, column=0)
tk.Label(f_cpi, text=" Upto ", fg="white", bg="#2E6B9E").grid(row=0, column=1)
tk.Spinbox(f_cpi, from_=0, to=0, width=4).grid(row=0, column=2)
tk.Label(f_cpi, text=" Th Semester", fg="white", bg="#2E6B9E").grid(row=0, column=3)

make_lbl("Experience :", 5)
f_exp = tk.Frame(frame, bg="#2E6B9E")
f_exp.grid(row=5, column=1, sticky="w")
tk.Spinbox(f_exp, from_=0, to=0, width=5).grid(row=0, column=0)
tk.Label(f_exp, text=" Years", fg="white", bg="#2E6B9E").grid(row=0, column=1)

make_lbl("Your Website Or Blog :", 6)
ent_web = tk.Entry(frame, width=40)
ent_web.insert(0, "http://")
ent_web.grid(row=6, column=1, sticky="w")

btn = tk.Button(
    root, text="◀ Step 2 ▶", bg="#76B82A", fg="white", font=("Arial", 10, "bold")
)
btn.grid(row=1, column=0, pady=(0, 15))

root.mainloop()