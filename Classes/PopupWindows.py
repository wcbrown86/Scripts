from tkinter import *


class PopupWindows:

    def __init__(self, input):

        self.input = input
        print("This is just a test")

    def create_window(self):
        root = Tk()
        root.title('You have to much information to paste!!!')

        textbox = Entry(root, textvariable=self.input)
        textbox.focus_set()
        textbox.pack(pady=10, padx=10)

        root.mainloop()

