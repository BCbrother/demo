# Tkinter - 多行文本输入
'''
Text 窗口部件

'''
import tkinter as tk

window = tk.Tk()
window.title("Text Window")
window.geometry("500x300")

e = tk.Entry(window,show=None)
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)
def insert_end():
    var = e.get()
    t.insert('end',var)
def delete_all():
    t.delete(index1=1.0,index2='end')

b1 = tk.Button(window,text='Insert Point',width=10,height=2,
                command=insert_point)
b1.pack()

b2 = tk.Button(window,text='Insert End',width=10,height=2,
                command=insert_end)
b2.pack()
      
b3 = tk.Button(window,text='整体删除',bg='purple',width=10,height=2,
                command=delete_all)
b3.pack()

t = tk.Text(window,height=3)
t.pack()

tk.mainloop()