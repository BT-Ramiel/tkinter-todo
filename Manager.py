import tkinter as tk

from Controller import Controller
from screens.AddTaskScreen import AddTaskScreen
from screens.HomeScreen import HomeScreen
from style import styles


class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Personal task manager")
        self.controller = Controller()
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.configure(background=styles.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        self.frames = {}

        for screen in (HomeScreen, AddTaskScreen):
            frame = screen(container, self)
            self.frames[screen] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.show_frame(HomeScreen)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def to_AddTaskScreen(self):
        self.show_frame(AddTaskScreen)
