import tkinter as tk
import tkinter.messagebox as tkm
import math

# 練習３
def enter_bg(event):
    event.widget['bg']= '#CCFFFF' #色変え


def leave_bg(event):#マウスが離れたときに元の色に戻る
    event.widget['bg']= 'SystemButtonFace'


def button_click(event):
    btn = event.widget
    num = btn["text"]

    if num == "=":
        siki=entry.get()
        res=eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    elif num == "c": #全消し
        entry.delete(0,tk.END)
    elif num == "+/-":
        num *= -1

    else: # 「=」以外のボタン字
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        # 練習６
        entry.insert(tk.END, num)

    
# 練習１
root = tk.Tk()
root.geometry("400x500")

# 練習４
entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=4)

# 練習２
r, c = 1, 0
for num in range(9, 0, -1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<Enter>", enter_bg)
    button.bind("<Leave>", leave_bg)


    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0


# 練習５

operators1 = ["+/-",0,"."]
for ope1 in operators1:
    button1 = tk.Button(root, text=f"{ope1}", width=4, height=2, font=("", 30))
    button1.grid(row=r, column=c)
 
    button1.bind("<1>", button_click)
    button1.bind("<Enter>", enter_bg)
    button1.bind("<Leave>", leave_bg)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

operators2 = ["c","+","-","="]
c=4
r=1
for ope2 in operators2:
    button2 = tk.Button(root, text=f"{ope2}", width=4, height=2, font=("", 30))
    button2.grid(row=r, column=c)
    
    button2.bind("<1>", button_click)
    button2.bind("<Enter>", enter_bg)
    button2.bind("<Leave>", leave_bg)
 
 

    if c%4 == 0:
        r += 1
        c = 4
  


root.mainloop()