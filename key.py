import tkinter as tk


class Kiosk(tk.Tk):
    def __init__(self):
        super().__init__()
        
        VKeyboard(self)

        tk.Entry(root).grid()
        tk.Button(root, text='withdraw').grid()
                 

if __name__ == "__main__":
    Kiosk().mainloop()
