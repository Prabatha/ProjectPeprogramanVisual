import tkinter as tk 
import tkinter.messagebox

main_window = tk.Tk()
main_window.title("TO-DO-LIST-APP")

def add_task():
    pass

#Buat GUInya
listbox_task = tk.Listbox(main_window, height=3, width=50)
listbox_task.pack()

entry_task = tk.Entry(main_window, width=50)
entry_task.pack()

button_add_task = tk.Button(main_window, text="Tambah List Kegiatan", width=48, command=add_task)
button_add_task.pack()

main_window.mainloop()