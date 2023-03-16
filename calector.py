from tkinter import *
root=Tk()
root.title("calector")
root.geometry("255x340")
color="black"
root.configure(bg=color)
root.resizable(False,False)  
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>edit>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def add(lab,txt):
    g=lab['text']
    lab.config(text=g + txt)
    lab.update()  
def math(label):    
    g=label["text"]
    g=g.replace("⨯","*")
    g=g.replace("÷","/")
    g=g.replace("x*","**")
    anser=eval(g)
    label.config(text=str(anser))
    label.update()
def clean(labl):
    labl.config(text=str())
    labl.update()
def remove(labl):
    g= labl["text"]
    resualt=""
    if (len (g) > 0):
        for i , j in enumerate(g):
            if  i == len(g) -1 :
                pass
            else:
                resualt = resualt + j 
    labl.config(text=resualt)  
    labl.update()
# >>>>>>>>>>>>>>>>>>>>>>>>>button number>>>>>>>>>>>>>>>>>>>>>>>>.
but_0=Button(root,text="0",fg="white",width=5,height=2,command=lambda:add(anser,"0"),padx=10,pady=10,bg="black")
but_0.grid(row=15,column=1)
but_1=Button(root,text="1",fg="white",width=5,height=2,command=lambda:add(anser,"1"),padx=10,pady=10,bg="black")
but_1.grid(row=14,column=0)
but_2=Button(root,text="2",fg="white",width=5,height=2,command=lambda:add(anser,"2"),padx=10,pady=10,bg="black")
but_2.grid(row=14,column=1)
but_3=Button(root,text="3",fg="white",width=5,height=2,command=lambda:add(anser,"3"),padx=10,pady=10,bg="black")
but_3.grid(row=14,column=2)
but_4=Button(root,text="4",fg="white",width=5,height=2,command=lambda:add(anser,"4"),padx=10,pady=10,bg="black")
but_4.grid(row=13,column=0)
but_5=Button(root,text="5",fg="white",width=5,height=2,command=lambda:add(anser,"5"),padx=10,pady=10,bg="black")
but_5.grid(row=13,column=1)
but_6=Button(root,text="6",fg="white",width=5,height=2,command=lambda:add(anser,"6"),padx=10,pady=10,bg="black")
but_6.grid(row=13,column=2)
but_7=Button(root,text="7",fg="white",width=5,height=2,command=lambda:add(anser,"7"),padx=10,pady=10,bg="black")
but_7.grid(row=12,column=0)
but_8=Button(root,text="8",fg="white",width=5,height=2,command=lambda:add(anser,"8"),padx=10,pady=10,bg="black")
but_8.grid(row=12,column=1)
but_9=Button(root,text="9",fg="white",width=5,height=2,command=lambda:add(anser,"9"),padx=10,pady=10,bg="black")
but_9.grid(row=12,column=2)
# >>>>>>>>>>>>>>>>>>>>>>>>>button>>>>>>>>>>>>>>>>>>>>>>>>.
but_is=Button(root,text="=",width=5,height=2,command=lambda:math(anser),padx=10,pady=10,bg="gray")
but_is.grid(row=15,column=3)
but_min=Button(root,text="-",width=5,height=2,command=lambda:add(anser,"-"),padx=10,pady=10,bg="gray")
but_min.grid(row=13,column=3)
but_mul=Button(root,text="⨯",width=5,height=2,command=lambda:add(anser,"⨯"),padx=10,pady=10,bg="gray")
but_mul.grid(row=14,column=3)
but_add=Button(root,text="+",width=5,height=2,command=lambda:add(anser,"+"),padx=10,pady=10,bg="gray")
but_add.grid(row=12,column=3)
but_div=Button(root,text="÷",width=5,height=2,command=lambda:add(anser,"÷"),padx=10,pady=10,bg="gray")
but_div.grid(row=15,column=2)
but_clear=Button(root,text="c",width=5,height=2,command=lambda:clean(anser),padx=10,pady=10,bg="gray")
but_clear.grid(row=11,column=3)
but_remove=Button(root,text="R",width=5,height=2,command=lambda:remove(anser),padx=10,pady=10,bg="gray")
but_remove.grid(row=11,column=2)
but_x=Button(root,text="x*",width=5,height=2,command=lambda:add(anser,"x*"),padx=10,pady=10,bg="gray")
but_x.grid(row=15,column=0)
# >>>>>>>>>>>>>>>>>>>>>>>>>entry>>>>>>>>>>>>>>>>>>>>>>>>.
anser=Label(root,text=" ",fg="white",bg="black",padx=10,pady=10)
anser.grid(row=10,column=0,columnspan=5)

root.mainloop()