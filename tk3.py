# Tkinter - 单行文本输入
'''
Entry 窗口部件
* 简单说明：　　
用来输入显示一行文本，收集键盘输入(类似 HTML 中的 text)。
* 什么时候用：
需要用户输入用户信息时，交互界面让我们登录账户信息等时候就可以用到。
'''
import tkinter as tk

window = tk.Tk()
window.title("Entry Window")
window.geometry("500x400")

e1 = tk.Entry(window,show='*',font=('Arial',13))
e2 = tk.Entry(window,show=None,font=('Arial',13))

e1.pack()
e2.pack()

tk.mainloop()