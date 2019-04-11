import cfg
cfg.init()

import lang
lang.init()

import tkinter as tk



def closeWin (win):
    win.destroy()
    message = tk.Tk()
    m = tk.Message(message, text='window destroyed', padx=40, pady=40)
    m.config(bg='lightgreen', font=('times', 24))
    m.pack()
    b = tk.Button(message, text='close', command=message.destroy).pack()
    message.mainloop()



#root = tk.Tk()
#im = tk.PhotoImage(file='alice_profile.gif')
#w1 = tk.Label(root, image=im).pack(side='right')
#w2 = tk.Label(root, text='Hello', padx=40).pack(side='left')
#button = tk.Button(root, text='Close', command=lambda: closeWin(root)).pack()
#root.mainloop()

#d2 = tk.Tk()
#b2 = tk.Button(d2, text='l337', command=lambda: closeWin(d2)).pack()
#d2.mainloop()

def sayHello():
    print("Hello")

def clrWindow():
    import os
    os.system('cls')
    print("clear window")


#dia = tk.Tk()
#frame = tk.Frame(dia)
#frame.pack()
#q = tk.Button(dia, text="QUIT", fg='red', command=quit).pack(side=tk.LEFT)
#c = tk.Button(dia, text="CLR", command=clrWindow).pack(side=tk.LEFT)
#h = tk.Button(dia, text="Hello", command=sayHello).pack(side=tk.LEFT)
#dia.mainloop()




class Counter():

    def __init__ (self, args = {}):
        self.instance = args.get('instance', tk.Tk())
        self.i = args.get('i', 0)
        self.active = True
        self.label = tk.Label(self.instance, fg='red', font = ('arial', 30) )
        self.label.pack()
        b = tk.Button(self.instance, text=lang.close, command=self.instance.destroy)
        b.pack(side=tk.LEFT)
        s = tk.Button(self.instance, text=lang.stop, command=self.stopCounter)
        s.pack(side=tk.LEFT)
        p = tk.Button(self.instance, text=lang.start, command=self.startCounter)
        p.pack(side=tk.LEFT)
        r = tk.Button(self.instance, text=lang.reset, command=self.resetCounter)
        r.pack(side=tk.LEFT)
        self.job = False
        #self.myLoop()
        self.label.config(text = '0')
        self.instance.mainloop()

    def stopCounter (self):
        self.label.after_cancel(self.job)
        self.active = False

    def startCounter (self):
        self.active = True
        #self.myLoop()
        self.job = self.label.after(1000, lambda: self.myLoop())

    def resetCounter (self):
        self.i = 0
        self.label.config(text = '0')

    def myLoop (self):

        def myCount (self):
            self.i += 1
            self.label.config(text = str(self.i))
            if self.active:
                self.job = self.label.after(1000, lambda: myCount(self))
        myCount(self)


    def test (self):
        print('test ok')




o = tk.Tk()
l = tk.Label(o, text=cfg.title).pack()
b = tk.Button(o, text=lang.open, command=lambda: Counter())
b.pack(side=tk.LEFT)
b2 = tk.Button(o, text=lang.close, command=o.destroy)
b2.pack(side=tk.LEFT)
o.mainloop()






