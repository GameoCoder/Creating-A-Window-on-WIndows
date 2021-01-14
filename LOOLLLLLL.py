from tkinter import Tk, Button, Label, messagebox
root = Tk()
exitButton = Button(root, text = "Exit Program", command = root.destroy)
exitButton.pack()
def my_callback():
    print("Thank You, Have a Nice Day....LOL!")
msg_button = Button(root, text = "MESSAGE", command = my_callback)
msg_button.pack()
root.title("CMS")
root.geometry("1000x500")
root.mainloop()
