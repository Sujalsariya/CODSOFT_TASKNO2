from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        
root = Tk()

root.geometry("1000x1000")
root.title("Calculator by CODSOFT")
root.wm_iconbitmap(r'C:\Users\win\Downloads\calculator image.ico')
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="serif 40 bold")
screen.pack(fill=X, ipadx=10, pady=9, padx=9)

f = Frame(root, bg="#36454F")

b = Button(f, text="9", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="#36454F")

b = Button(f, text="6", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="#36454F")

b = Button(f, text="3", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="#36454F")

b = Button(f, text="0", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=12, pady=8)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="#36454F")

b = Button(f, text="+", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=4, pady=9)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="#36454F")

b = Button(f, text="=", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=2, pady=2, font="serif 30 bold")
b.pack(side=LEFT, padx=5, pady=9)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()