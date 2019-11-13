import json
from difflib import get_close_matches as g
import createjson as cj
cj.create_json_file()

data=json.load(open("slang.json"))

keys=data.keys()

def translate():

    sw=slangworld.get()
    output.delete(0.0, END)

    if sw in data:
        for i,j in enumerate(data[sw],start = 1):
            output.insert(END,str(i)+'. '+j+'\n')
    elif sw.upper() in data:
        for i,j in enumerate(data[sw.upper()],start = 1):
            output.insert(END,str(i)+'. '+j+'\n')
    elif sw.title() in data:
        for i,j in enumerate(data[sw.title()],start = 1):
            output.insert(END, str(i) + '. ' + j + '\n')
    else:
        list=g(sw,keys,n=1,cutoff=0.8)
        if len(list)==0:
            output.insert(END,"Sorry, no word found!")
        else:
            real=list[0]
            answer=tkinter.messagebox.askquestion("Word Suggestion", "Is your word "+real+"?")

            if answer == 'yes':
                for i,j in enumerate(data[real],start = 1):
                    output.insert(END, str(i) + '. ' + j + '\n')
            else:
                output.insert(END,"Apologies, no word found. Please check your input word again.")


def Clear():
    slangworld.set("")
    output.delete(0.0,END)

from tkinter import *
import tkinter.messagebox

root=Tk()
root.geometry()
root.resizable(False,False)
root.title("Slang Dictionary")
root.configure(background="light goldenrod yellow")

slangworld=StringVar()

lblword=Label(root,width=30, text='Enter A Slang Word :', font=('arial 20 bold'),bg='light goldenrod yellow')
lblword.grid(row=0, column=1, sticky=W)

ent = Entry(root, width=30,font=('arial 18 bold'), bg='white',textvariable=slangworld)
ent.grid(row=1, column=1)

but = Button(root, padx=2, pady=2, text='Translate', command=translate, bg='light goldenrod yellow', font=('none 18 bold'))
but.grid(row=2, column=1)

but2 = Button(root, padx=2, pady=2, text="Clear", command=Clear, bg='light goldenrod yellow', font=('none 18 bold'))
but2.grid(row=3, column=1)


output = Text(root,  width=30, height=8, font=('Time 20 bold'), fg="black")
output.grid(row=4, column=1)

scrollbar=Scrollbar(root,orient=VERTICAL,command=output.yview)
scrollbar.grid(row=4,column=3,sticky='ns')
output.config(yscrollcommand=scrollbar.set)

root.mainloop()