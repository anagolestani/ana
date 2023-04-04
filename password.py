from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from random import *

root=Tk()
root.title("password")
root.resizable(False,False)
root.geometry("400x300")
root.configure(bg="black")
txt=StringVar()
txt_1=StringVar()

def password_1():
    random_0=randint(1,100)
    list_2=(random_0,"q","w","e","r","t","y","u","i","o","p","a","s","d","f","Q","W","E","R"
            ,"T","Y","U","I","O","P","A","S","D","F","G","H"
            ,"J","K","L","Z","X","C","V","B","N","M"
            ,"g","h","j","k","l","z","x","c","v","b","n","m")
    vlu=int(txt.get())
    random_1=sample(list_2,vlu)
    txt_1.set(random_1)
    list1.insert(END,entry_1.get())
    if vlu >= 40:
        list1.delete(END)
        messagebox.showerror("shoerror","The number entered for the password is too many")
def save():
    files=[("text cocument","*.text"),("ALL","*.*")]
    file = asksaveasfile(filetypes=files,defaultextension=files)
    if file is None:
        return
    text2save=str(list1.get(END))
    file.write(text2save)
    file.close()
def delet():
    list1.delete(0,END)

mnubar=Menu(root)
filemenu=Menu(mnubar,tearoff=0,bg="black",fg="Purple")
filemenu.add_command(label="save as",command=save)
filemenu.add_command(label="delet",command=delet)
filemenu.add_separator()
mnubar.add_cascade(label="menu",menu=filemenu)
root.config(menu=mnubar)

label_entry=Label(root,text="enter your length password: ",bg="black",fg="Purple")
label_entry.grid(row=1,column=0)

entry=Entry(root,textvariable=txt,bg="Purple",fg="white")
entry.grid(row=2,column=0)

but=Button(root,text="ok",command=password_1,bg="black",fg="Purple")
but.grid(row=2,column=1)

scrollbar1=Scrollbar(root)
scrollbar1.grid(row=40,column=1)


entry_1=Entry(root,textvariable=txt_1,width=20)
list1=Listbox(root,height=10,width=60,bg="Purple",fg="black",yscrollcommand=scrollbar1.get())
list1.grid(row=40,column=0)

for line in enumerate(txt_1.get()):
    list1.insert(END,str(line))
scrollbar1.config(command=list1.yview)    
root.mainloop()