# Tkinter - 按钮Button
'''
Tkinter
Button窗口部件
'''
import tkinter as tk

window = tk.Tk()                     # 第1步，实例化object,建立窗口window
window.title("Button Window")      # 第2步，给窗口创建标题名
window.geometry("500x300")           # 第3步，设定窗口大小

var = tk.StringVar()
l = tk.Label(window,textvariable=var,bg='green',font=('Arial',12),
                width=30,height=2)
l.pack()    

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("Hello,Tkinter!")
    else:
        on_hit = False
        var.set('')

b = tk.Button(window,text="Hit Me",font=('Arial',12),width=10,
                height=1,command=hit_me)
b.pack()

window.mainloop()                   