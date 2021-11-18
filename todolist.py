from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        listbox_task.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    listbox_task.delete(ANCHOR)

main_window = Tk()
main_window.title("                                                       TO-DO-LIST-APP          ")
main_window.geometry('500x450+500+200')
main_window.config(bg='#223441')
main_window.resizable(width=False, height=False)

def add_task():
   task = entry_task.get()

frame = Frame(main_window)
frame.pack(pady=10)

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
listbox_task.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    listbox_task.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

listbox_task.config(yscrollcommand=sb.set)
sb.config(command=listbox_task.yview)

my_entry = Entry(
    main_window,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(main_window)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)

delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

main_window.mainloop()
