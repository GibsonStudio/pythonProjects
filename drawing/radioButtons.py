import tkinter as tk


root = tk.Tk()

v = tk.StringVar()
v.set("gib")

tk.Label(root, text="Choose a guitar:", width=100).pack()
tk.Radiobutton(root, text="Gibson", variable=v, value="gib", indicatoron=0, width=100).pack(anchor=tk.W)
tk.Radiobutton(root, text="Fender", variable=v, value="fen", indicatoron=0,width=100).pack(anchor=tk.W)
tk.Button(root, text="close", command=root.destroy).pack(anchor=tk.W)
root.mainloop()
print(v.get())
