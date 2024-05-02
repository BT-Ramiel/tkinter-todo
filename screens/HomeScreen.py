import tkinter as tk

from components.MainMenu import MainMenu
from style import styles


class HomeScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.init_widgets()

    def init_widgets(self):
        tk.Label(self, text="Welcome", justify=tk.CENTER, **styles.STYLE).pack(
            **styles.PACK
        )

        MainMenu(self, self.manager).pack(**styles.PACK)
