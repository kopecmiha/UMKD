import os
from tkinter import Tk, Button, Label, Entry, IntVar, filedialog, messagebox
from tkinter import *
from tkinter.ttk import Radiobutton
import time, requests
from doc import doc_open_save

compets = []
pod_compets = []
def clicked():
        DISC = txtDISC.get()
        special = txtspecial.get()
        spec = txtspec.get()
        uroven = txturo.get()
        kafedra = txtkafedra.get()
        year = txtyear.get()
        author =  txtauthor.get()
        nach_kaf = txtnach_kaf.get()
        competions = compets
        pod_competions = pod_compets
        doc_open_save(DISC, special, spec, kafedra, uroven, competions, pod_competions, year, author, nach_kaf)

def pod_com():
        lpodcom.delete(0, END)
        comp = list(lcomp.curselection())
        for ids in comp:
                ids = lcomp.get(ids)
                for each in competitons:
                        if each["code"] == ids:
                                compets.append(each)
                                idx = each["id"]
                                for eac in pod_competitons:
                                        if idx == eac["id_of_comp"]:
                                                lpodcom.insert(END,eac["code_of_pod_comp"])
def pod_competions():
        pcomp = list(lpodcom.curselection())
        for ids in pcomp:
                ids = lpodcom.get(ids)
                for each in pod_competitons:
                        if each["code_of_pod_comp"] == ids:
                               pod_compets.append(each)

def Next():
        lblauthor.config(text = 'New Lable')
        lblauthor.update()

        
        


        
competitons = requests.get("http://eldocument.tmweb.ru/get_list/competitons").json()

competitons = eval(competitons)

pod_competitons = requests.get("http://eldocument.tmweb.ru/get_list/pod_competioons").json()
pod_competitons = eval(pod_competitons)
window = Tk()

window.title("Помощь с Учебными методичками")
window.geometry('800x600')

lblDISC = Label(window, text="Введите Название Дисциплины")  
lblDISC.grid(column = 0, row = 1)
txtDISC = Entry(window,width=100)  
txtDISC.grid(column = 1, row = 1)

lblspecial = Label(window, text="Ведите Специализация/Профиль")
lblspecial.grid(column = 0, row = 2)
txtspecial = Entry(window,width=100)  
txtspecial.grid(column = 1, row = 2)

lblspec = Label(window, text="Введите Специальность/Направление подготовки")  
lblspec.grid(column = 0, row = 3)
txtspec = Entry(window,width=100)  
txtspec.grid(column = 1, row = 3)

lblkafedra = Label(window, text="Введите кафедру")  
lblkafedra.grid(column = 0, row = 4)
txtkafedra = Entry(window,width=100)  
txtkafedra.grid(column = 1, row = 4)
 
lbluro = Label(window, text="Введите Уровень обучения")  
lbluro.grid(column = 0, row = 5)
txturo = Entry(window,width=100)  
txturo.grid(column = 1, row = 5)

lblyear = Label(window, text="Введите Год")  
lblyear.grid(column = 0, row = 6)
txtyear = Entry(window,width=100)  
txtyear.grid(column = 1, row = 6)

lblauthor = Label(window, text="Введите ФИО Автора")  
lblauthor.grid(column = 0, row = 7)
txtauthor = Entry(window,width=100)  
txtauthor.grid(column = 1, row = 7)

lblnach_kaf = Label(window, text="Введите ФИО Начальника Кафедры")  
lblnach_kaf.grid(column = 0, row = 8)
txtnach_kaf = Entry(window,width=100)  
txtnach_kaf.grid(column = 1, row = 8)

btn = Button(window, text="Конвертировать", command=clicked)  
btn.grid(column = 0, row = 15)

lblcomp = Label(window, text=" Выберите компетенции ")  
lblcomp.grid(column = 0, row = 10)
lcomp = Listbox(selectmode=EXTENDED)
lcomp.grid(column = 1, row = 10)
for each in competitons:
        lcomp.insert(END,each["code"])

btnl = Button(window, text="Показать подкомпетенции", command=pod_com)  
btnl.grid(column = 0, row = 11)

lblpodcom = Label(window, text=" Выберите подкомпетенции ")
lblpodcom.grid(column = 0, row = 12)
lpodcom = Listbox(selectmode=EXTENDED)
lpodcom.grid(column = 1, row = 12)

btnl = Button(window, text="Подтвердить подкомпетенции", command=pod_competions)  
btnl.grid(column = 0, row = 13)

btn_next = Button(window, text="Далее", command=Next)  
btn_next.grid(column = 0, row = 18)


window.mainloop()

