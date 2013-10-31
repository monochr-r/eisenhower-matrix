from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class EisenMatrix:

    def __init__(self, master):
        master.wm_title("Eisenhower Matrix")
        frame = ttk.Frame(master)
        frame.grid(column=0, row=0, sticky=(N, S, E, W))

        #Create the left hand side vertical labels
        #the mess is because letters aren't properly centered with \n's
        leftLabels = 2*[[]]
        leftLetterLabels = 2 * [[]]
        for i,label in enumerate(("Important", "Not Important")):
            leftLabels[i] = ttk.Frame(frame)
            leftLabels[i].grid(column=0, row=i+1)
            leftLetterLabels[i] = len(label)*[[]]
            for j, letter in enumerate(label):
                leftLetterLabels[i][j] = ttk.Label(leftLabels[i], text=letter)
                leftLetterLabels[i][j].grid(column=0, row=j)

        #Create the top side labels
        topLabels = 2*[[]]
        for i,label in enumerate(("Urgent", "Not Urgent")):
            topLabels[i] = ttk.Label(frame, text=label)
            topLabels[i].grid(column=(i+1), row=0)

        #Create text entry boxes
        self.text = 4*[[]]
        c = 0
        bgcolors=["red", "green", "yellow", "grey"]
        for i in range(2):
            for j in range(2):
                self.text[c] = Text(frame, background=bgcolors[c], width=40, height=15)
                self.text[c].grid(column=i+1, row = j+1, sticky=(N, S, E, W))
                c+=1

        #Add buttons
        buttonFrame = ttk.Frame(frame)
        buttonFrame.grid(column=2, row=3)
        ttk.Button(buttonFrame, text="Load", command = self.open).pack(side=LEFT)
        ttk.Button(buttonFrame, text="Save", command = self.save).pack(side=LEFT)
        ttk.Button(buttonFrame, text="Quit", command=frame.quit).pack(side=LEFT)

        #Make it resizable
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.rowconfigure(2, weight=1)

    def open(self):
        if messagebox.askyesno("Load", "Delete entries and load save?"):
            for i,obj in enumerate(self.text):
                try:
                    with open("save"+str(i), 'r') as f:
                        t = f.read()
                    obj.delete(1.0, END)
                    obj.insert(1.0, t)
                except:
                    messagebox.showerror("Read Error", "Couldn't read save" + str(i) + ". Nothing read.")
 

    def save(self):
        if messagebox.askyesno("Save", "Replace old save with entries?"):
            for i,obj in enumerate(self.text):
                t = obj.get(1.0, END)
                try:
                    with open("save"+str(i), 'w') as f:
                        f.write(t.strip())
                except:
                    messagebox.showerror("Write Error", "Couldn't write save" + str(i) + ". Nothing saved.")

if __name__ == '__main__':
    root = Tk()
    app = EisenMatrix(root)
    root.mainloop()
