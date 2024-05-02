import tkinter as tk

from style import styles


class MainMenu(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.init_widgets()

    def init_widgets(self):
        tk.Button(
            self,
            text="Create task",
            command=self.manager.from_HomeScreen_to_AddTaskScreen,
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(**styles.PACK)

        tk.Button(
            self,
            text="Week/Month tasks",
            command=lambda: print("..."),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(**styles.PACK)

        tk.Button(
            self,
            text="Progress",
            command=lambda: print("..."),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(**styles.PACK)
