from tkinter import *
from tkinter import messagebox

main_window = Tk()
main_window.title("TO-DO-LIST-APP")
main_window.geometry('500x250+500+200')
main_window.config(bg='#223431')

def add_task():
   task = entry_task.get()

listbox_task = Listbox(
    frame,
    width=30,
    height=10,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
listbox_task.pack()

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

listbox_task.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

entry_task = Entry(main_window, width=50)
entry_task.pack()

button_add_task = Button(main_window, text="Tambah List Kegiatan", width=48, command=add_task)
button_add_task.pack()

main_window.mainloop()

print("coba git")
