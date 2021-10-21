import tkinter as tk 

main_window = tk.Tk()
main_window.title("TO-DO-LIST-APP")
main_window.geometry('500x250+500+200')
main_window.config(bg='#223431')

def add_task():
   task = entry_task.get()

listbox_task = tk.Listbox(main_window, height=3, width=50)
listbox_task.pack()

entry_task = tk.Entry(main_window, width=50)
entry_task.pack()

button_add_task = tk.Button(main_window, text="Tambah List Kegiatan", width=48, command=add_task)
button_add_task.pack()

main_window.mainloop()
