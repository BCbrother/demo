'''
Tkinter
创建主窗口及Label部件（标签）创建使用
'''
import tkinter as tk

window = tk.Tk()                     # 第1步，实例化object,建立窗口window
window.title("My First Window")      # 第2步，给窗口创建标题名
window.geometry("500x300")           # 第3步，设定窗口大小

# 第4步，在图形界面上设定标签
# 说明：text为标签内的文字，bg为背景，font为字体，width是字符长，height是字符高
l = tk.Label(window,text="Hello,Tkinter!",bg='green',
                font=('Arial',12),width=30,height=2)

l.pack()                             # 第5步，放置标签   
# 说明：所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键
window.mainloop()                    # 第6步，主窗口循环显示
