import tkinter
from .window import Window

class PlayMenuWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

        this.rowconfigure(index=0, weight=1)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=1)
        this.columnconfigure(index=0, weight=1)

        this.reset()

    def reset(this) -> None:
        #MENU TITLE
        tkinter.Label(this, text="Játék menü", font=(None, 25)).grid(row=0, column=0, sticky="NESW")

        #MENU BUTTONS
        tkinter.Button(this, command=this.go_to_iq, text="IQ teszt").grid(row=1, column=0, sticky="NESW")
        tkinter.Button(this, command=this.go_to_comp, text="Verseny").grid(row=2, column=0, sticky="NESW")
        tkinter.Button(this, command=this.go_to_duel, text="Párbaj").grid(row=3, column=0, sticky="NESW")
        tkinter.Button(this, command=this.go_to_test, text="Tematikus teszt").grid(row=4, column=0, sticky="NESW")

    def go_to_iq():
        pass

    def go_to_comp():
        pass

    def go_to_duel():
        pass

    def go_to_test():
        pass