import tkinter
from tkinter import ttk
from .window import Window

class AdsWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1, minsize=20)
        this.rowconfigure(index=0, weight=1)
        this.reset()
        
    def reset(this) -> None:
        canvas = tkinter.Canvas(this)
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.grid(row=0, column=0, sticky="NESW")
        canvas.columnconfigure(index=0, weight=1)
        canvas.rowconfigure(index=0, weight=1)

        scrollbar = ttk.Scrollbar(this, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="NES")

        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.grid(row=0, column=0, sticky="EW")
        scrollable_frame.columnconfigure(index=0, weight=1)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for i in range (10):
            scrollable_frame.rowconfigure(index=i, weight=1)
            tkinter.Label(scrollable_frame, text="Valami", font=(None, 25)).grid(row=i, column=0, sticky="NESW")

        