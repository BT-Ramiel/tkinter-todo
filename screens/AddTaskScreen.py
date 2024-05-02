import tkinter as tk
import tkinter.messagebox
from sqlite3 import ProgrammingError

from components.MainMenu import MainMenu
from style import styles


class AddTaskScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.manager = manager
        self.init_widgets()

    def init_widgets(self):
        tk.Label(self, text="Task title", justify=tk.CENTER, **styles.STYLE).pack(
            **styles.PACK
        )

        self.task_entry = tk.Entry(self, justify=tk.CENTER, **styles.STYLE)
        self.task_entry.pack(**styles.PACK)
        self.task_entry.bind("<Return>", self.add_task)

        MainMenu(self, self.manager).pack(**styles.PACK)

    def add_task(self, _):
        task_title = self.task_entry.get()
        if task_title == "":
            tk.messagebox.showinfo(title="Error", message="Task title cannot be empty")
        else:
            try:
                self.manager.controller.create_empty_task(task_title)
            except ProgrammingError:
                tk.messagebox.showinfo(
                    title="Error", message="This task title is already in use"
                )
