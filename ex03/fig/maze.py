import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    cx,cy=300,400
    tori = image=tk.PhotoImage(file="ex03/fig/8.png")
    canvas.create_image(cx,cy,image=tori,tag="kokaton")
    key=""
    root.mainloop()