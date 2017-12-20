from tkinter import *  
import tkinter as tk#引用tkinter函数
import math #引用math函数，运算需要的
import tkinter.messagebox
def x1():#用于某些需要重复调用的函数 
    cd = entryCd.get()
    if  cd.replace('.', '', 1).isdigit() or cd[1:].replace('.', '', 1).isdigit()or cd.replace(' ', '', 1).isdigit():#判断输入内容是否为数字，排除了非数字、不输入的差异       
        cd=float(cd)
        labelcTof.config(text = '%1fdbm  =%4fmW =%4fW'%(cd,10**(cd/10),10**(cd/10)/1000))
    else:
        tkinter.messagebox.showinfo('警告', '非法输入！')
def x2():
    cd = entryCd.get()
    if  cd.replace('.', '', 1).isdigit() or cd.replace(' ', '', 1).isdigit() :
        if float(cd)<=0 :
            tkinter.messagebox.showinfo('提示', '输入错误，请重新输入！')
        else:
            cd=float(cd)    
            labelcTof.config(text = '%1fmW=%.4fW  =%4fdbm'%(cd,cd/1000,10*math.log10(cd)))
    else:
        tkinter.messagebox.showinfo('提示', '输入错误，请重新输入！')
def x3():
    cd = entryCd.get()
    if  cd.replace('.', '', 1).isdigit() or cd.replace(' ', '', 1).isdigit():
        if  float(cd)<=0:
            tkinter.messagebox.showinfo('提示', '输入错误，请重新输入！')
        else:
            cd=float(cd)
            labelcTof.config(text = '%1fW=%.1fmW  =%.4fdbm'%(cd,cd*1000,10*math.log10(cd*1000)))
    else:
        tkinter.messagebox.showinfo('提示', '输入错误，请重新输入！')
class App:
    def __init__(self, master):
        #使用Frame增加一层容器
        fm = Frame(master)
        Button(fm, text='已知dbm', command =x1,padx=3).pack(side=LEFT)
        Button(fm, text='已知mW', command = x2,padx=4).pack(side=LEFT)
        Button(fm, text='已知W', command = x3,padx=10).pack(side=LEFT)        
        fm.pack(side = BOTTOM,padx=10,pady=10)       
root = tk.Tk()
root.title('单位换算')
display = App(root)
labelcTof = tk.Label(root,text = '单位之间的转换',height =4,width=40,fg='blue')
labelcTof.pack()
entryCd = tk.Entry(root,text='0')
entryCd.pack()
root.mainloop()
