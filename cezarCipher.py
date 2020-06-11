#Elmaz Feratovic 30/17 --- Vladan Babic 24/17
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import askopenfile 
from tkinter.ttk import Progressbar
from tkinter import messagebox
from array import *
import random
from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style

class CezarovAlgoritam(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self): 

        self.master.title("Cezarov algoritam")
        self.pack(fill=BOTH, expand=1)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        titleLable = Label(frame1, text="DOBRODOŠLI!", font = "Verdana 15 bold")
        titleLable.pack(side=TOP, padx=5, pady=5)

        kriptoLable = Label(frame1, text="CEZAROV ALGORITAM",   font = "Verdana 15 bold")
        kriptoLable.pack(side=BOTTOM, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(side=TOP)

        selected = IntVar()

        rad1 = Radiobutton(frame2,text='Enkripcija', value=1, variable=selected, font = "Verdana 11 bold")
        rad2 = Radiobutton(frame2,text='Dekripcija', value=2, variable=selected, font = "Verdana 11 bold")

        rad1.pack(side=LEFT, anchor=N, padx=5, pady=5)
        rad2.pack(side=RIGHT, anchor=N, padx=5, pady=5)

        frame3 = Frame(self)
        frame3.pack(side=TOP, expand=True)

        plainText = scrolledtext.ScrolledText(frame3,width=45,height=7)
        plainText.insert(INSERT,'Poruka...')
        plainText.pack(side=TOP, anchor=N, padx=5, pady=5)

        pomakLabel = Label(frame3, text="Pomak : ", font = "Verdana 10 bold")
        pomakLabel.pack(side=TOP, padx=5, pady=5)

        btnPlus = Button(frame3, text ='+', width= 4,borderwidth = '1',fg = 'white',bg = 'green',font = "Verdana 10 bold", command = lambda:plus()) 
        btnPlus.pack(side=TOP, anchor=CENTER, padx=5, pady=5)
       
        
        key = Entry(frame3,width=5,font = "Verdana 10 bold")
        key.insert(INSERT,'0')
        key.pack(side=TOP, anchor=CENTER, padx=5, pady=5)

        btnMin = Button(frame3, text ='-', width= 4,borderwidth = '1',fg = 'black',bg = 'orange',font = "Verdana 10 bold", command = lambda:minus()) 
        btnMin.pack(side=TOP, anchor=CENTER, padx=5, pady=5)

        cipherText = scrolledtext.ScrolledText(frame3,width=45,height=7)
        cipherText.insert(INSERT,'Šifrovana poruka...')
        cipherText.pack(side=TOP, anchor=N, padx=5, pady=5) 

        btnSubmit = Button(frame3, text ='Počni', width= 15,borderwidth = '1',fg = 'black',bg = 'skyblue',font = "Verdana 10 bold",command = lambda:submit()) 
        btnSubmit.pack(side=TOP, anchor=CENTER, padx=5, pady=5)
       
        
        def plus():
            varKey = int(key.get())  + 1
            key.delete(first=0,last=30)
            key.insert(INSERT,str(varKey))

        def minus():
            varKey = int(key.get()) - 1
            key.delete(first=0,last=30)
            key.insert(INSERT,str(varKey))

        def submit():
            azbuka = 'ABCČĆDĐEFGHIJKLMNOPRSŠŚTUVZŹŽ'
            dozvoljeniKarakteri = ' .,][\\{\}/()0123456789`!@#$%^&*_+-<>?'
            text = list(plainText.get("1.0",END).upper())
            keyVar = key.get()
            print(len(azbuka))
            res = ""
            if validacija(azbuka, text) == 0:
           
               if selected.get() == 1:
                  print("Enrkip")
                  brojac = 0
                  for char in text:
                     
                      if dozvoljeniKarakteri.find(char) != -1:
                      
                          res = res + char  
                      else:
                          i = (azbuka.find(char) + int(keyVar)) % len(azbuka)
                          res = res + azbuka[i] 


               elif selected.get() == 2:
                  print("Dekript")
                  brojac = 0
                  for char in text:
                      if dozvoljeniKarakteri.find(char) != -1:
                      
                          res = res + char
                      else:
                          i = (azbuka.find(char) - int(keyVar)) % len(azbuka)
                          res = res + azbuka[i]

               else:
                  outPutError = messagebox.askretrycancel('Greška','Molimo Vas odaberite enkripciju ili dekripciju')
               
               res = res[0:len(res)-1]
               cipherText.delete('1.0', END)
               cipherText.insert(INSERT,res)
               print(res)



        def validacija(azbuka,text):

           nedozvoljeniKarakteri = 'XQWY'         
   
           for char in text:
               if char in nedozvoljeniKarakteri:
                    outPutError = messagebox.askretrycancel('Greška','Unijeli ste slova koja ne pripadaju crnogorskom jeziku')
                    print("Neregularno slovo : " +  char)
                    return 1
           return 0


            


        

def main():

    root = Tk()
    root.geometry("600x600")
    app = CezarovAlgoritam()
    root.mainloop()


if __name__ == '__main__':
    main()