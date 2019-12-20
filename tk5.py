# Tkinter - Messagebox 消息弹框部件
'''
tkinter.messagebox 窗口部件

'''
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("Messagebox Window")
window.geometry("500x400")

# print(type(words))
def hit_me():
    tkinter.messagebox.showinfo(title="Message Box",message="Hello,I'm a message")
    # 提出警告对话窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！') 
    # 提出错误对话窗      
    # tkinter.messagebox.showerror(title='Hi', message='出错了！')  
    # 询问选择对话窗return 'yes', 'no'      
    # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  
    # return 'True', 'False'
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))  
    # return 'True', 'False   
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！')) 

b = tk.Button(window,text='Hit me',bg='green',font=('Arial',13),command=hit_me)
b.pack()

tk.mainloop()