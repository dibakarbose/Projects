import tkinter as tk
import parser

flag=0

def callback():
    root.destroy()
    print("Exiting Application")

class Calculator:

  
    def __init__(self,tkObject):
        self.display=tk.Entry(tkObject,justify="right")
        self.ac=tk.Button(tkObject,text="AC",width=3,command=lambda num="AC": self.clearAll(num))
        self.delBut=tk.Button(tkObject,text="DEL",width=3,command=lambda num="DEL": self.delButton(num))
        self.div=tk.Button(tkObject,text='/',width=3,command=lambda num="/": self.buttonClick(num))
        self.add=tk.Button(tkObject,text='+',width=3,command=lambda num="+": self.buttonClick(num))
        self.sub=tk.Button(tkObject,text='-',width=3,command=lambda num="-": self.buttonClick(num))
        self.mul=tk.Button(tkObject,text='x',width=3,command=lambda num="*": self.buttonClick(num))
        self.result=tk.Button(tkObject,text='=',width=3,command=lambda num="=": self.resultClick(num))
        self.dot=tk.Button(tkObject,text='.',width=3,command=lambda num=".": self.buttonClick(num))
        self.button=[0,0,0,0,0,0,0,0,0,0]
        for i in range(0,10):
            self.button[i]=tk.Button(tkObject,text=str(i),width=3,command=lambda num=i :self.buttonClick(num))

    def init_window(self):
        self.display.insert('end',"0.")
        self.display.config(state='disabled',disabledbackground='white',disabledforeground='black')
        self.display.grid(row=0,column=0,columnspan=4,padx=3,pady=3)
        self.ac.grid(row=1,column=0)
        self.delBut.grid(row=1,column=3)
        self.button[0].grid(row=5,column=1)
        self.button[1].grid(row=4,column=0)
        self.button[2].grid(row=4,column=1)
        self.button[3].grid(row=4,column=2)
        self.button[4].grid(row=3,column=0)
        self.button[5].grid(row=3,column=1)
        self.button[6].grid(row=3,column=2)
        self.button[7].grid(row=2,column=0)
        self.button[8].grid(row=2,column=1)
        self.button[9].grid(row=2,column=2)
        self.dot.grid(row=5,column=0)
        self.result.grid(row=5,column=2)
        self.add.grid(row=5,column=3)
        self.sub.grid(row=4,column=3)
        self.mul.grid(row=3,column=3)
        self.div.grid(row=2,column=3)

    def buttonClick(self,num):
        print("Button",num,"was pressed")
        global flag
        self.display.config(state='normal')
        if self.display.get()=="0." or flag==1:
            #self.display.config(state='normal')
            self.display.delete(0,'end')
            if flag==1:
                flag=0
            
            
        self.display.insert('end',str(num))

        self.display.config(state='disabled',disabledbackground='white',disabledforeground='black')

    def resultClick(self,op):
        global flag
        whole_string = self.display.get()
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        self.display.config(state='normal')
        self.display.delete(0,'end')
        self.display.insert('end',str(result))
        self.display.config(state='disabled',disabledbackground='white',disabledforeground='black')
        flag=1

        
    def clearAll(self,but):
        self.display.config(state='normal')
        self.display.delete(0,'end')
        self.display.insert('end',"0.")
        self.display.config(state='disabled',disabledbackground='white',disabledforeground='black')

    def delButton(self,but):
        self.display.config(state='normal')
        whole_string=self.display.get()
        if len(whole_string):
            new_string=whole_string[:-1]
            self.display.delete(0,'end')
            self.display.insert('end',new_string)
        else:
            self.display.delete(0,'end')
            self.display.insert('end',"0.")
        self.display.config(state='disabled',disabledbackground='white',disabledforeground='black')

if __name__=="__main__":
    root=tk.Tk()
    newCalc=Calculator(root)
    newCalc.init_window()
    

    
    root.protocol("WM_DELETE_WINDOW", callback)

    root.mainloop()
