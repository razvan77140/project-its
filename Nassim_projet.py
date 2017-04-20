from tkinter import*

root = Tk()

def get_list():
        index = listbox1.curselection()[0]
        seltext = listbox1.get(index)
        enter1.delete(0, 50)
        enter1.insert(0, seltext)        
    
        
def add_item():
        listbox1.insert(END, enter1.get())
#fonction qui permet d'ajouter des caracteres 
        
def delete_item():
        try:
                index = listbox1.curselection()[0]
                listbox1.delete(index)
#fonction qui permet de supprimer des elements de la liste 
        except IndexError:
                pass        
# permet de parametrer la taille de la fenetre d'affichage        
listbox1 =Listbox(root, width=30, height=20)
listbox1.grid(row=0, column=0)

yscroll = Scrollbar(command=listbox1.yview, orient=VERTICAL)
yscroll.grid(row=0, column=1, sticky=N+S)
listbox1.configure(yscrollcommand=yscroll.set)

#permet de parametrer la taille de la bare de saisie
enter1 = Entry(root, width=10)
enter1.insert(0, '')
enter1.grid(row=1, column=0)

button = Button(root, text='Ajouter', command=add_item)
#affichage du bouton qui permet d'ajouter des caractères

button.grid(row=2, column=0, sticky=W)
#affichage du bouton qui permet de supprimer des caractères
button1 = Button(root, text='Supprimer', command=delete_item)
button1.grid(row=2, column=0, sticky=E)


root.mainloop()
