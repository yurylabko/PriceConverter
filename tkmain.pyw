import tkinter as tk
from tkinter import filedialog
from register_srv import load_from_file, save_to_file
from tkinter import ttk


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path == "":
        return
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)
    process_button.configure(state=tk.NORMAL)
    if output_button["state"] != tk.DISABLED:
        output_button.configure(state=tk.DISABLED)
    l_process.config(text="Load done!")


def save_file():
    file_path = filedialog.asksaveasfilename(
        filetypes=[("Excel files", "*.xlsx")], defaultextension="xlsx"
    )
    if file_path == "":
        return
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)
    process_button.configure(state=tk.DISABLED)
    try:
        save_to_file(_register, file_path)
    except Exception as e:
        l_process.config(text=f"Save error!!!: {e}")
        return
    l_process.config(text="Save done!")


def process():
    output_button.configure(state=tk.NORMAL)
    l_process.config(text="In process!")
    root.update()
    global _register
    try:
        _register = load_from_file(input_entry.get())
    except Exception as e:
        l_process.config(text=f"Process error!!!: {e}")
        output_button.configure(state=tk.DISABLED)
        return
    l_process.config(text="Done!")


_def_grid_conf = {"pady": (10, 0), "padx": (5, 5), "sticky": "ew"}


root = tk.Tk()
root.title("Price Converter")
root.geometry("440x140")
for c in range(2):
    root.columnconfigure(index=c, weight=c)
for r in range(3):
    root.rowconfigure(index=r, weight=1)
ttk.Style().theme_use("clam")


input_button = ttk.Button(root, text="Open", command=open_file, width=15)
input_button.grid(row=0, column=0, cnf=_def_grid_conf)
input_entry = ttk.Entry(root, width=50)
input_entry.grid(row=0, column=1, cnf=_def_grid_conf)


process_button = ttk.Button(
    root, text="Process", state=tk.DISABLED, width=15, command=process
)
process_button.grid(row=1, column=0, cnf=_def_grid_conf)

l_process = ttk.Label()
l_process.grid(row=1, column=1, cnf=_def_grid_conf)


output_button = ttk.Button(
    root, text="Save", state=tk.DISABLED, command=save_file, width=15
)
output_button.grid(row=2, column=0, cnf=_def_grid_conf)
output_entry = ttk.Entry(root, width=50)
output_entry.grid(row=2, column=1, cnf=_def_grid_conf)

root.mainloop()
