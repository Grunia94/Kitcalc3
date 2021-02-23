import tkinter as tk
import math
import tkvalidate as tkv
import re
from tkinter import *

master = tk.Tk()
master.title('Kitcalc')
tk.output = tk.Text

master.configure(bg='#0f4c81')

def callback(text, wid):
    if str.isdigit(text) or not text:
        text = text if text else 0
        if wid == str(entry3):
            n = entry2.get() if entry2.get() else 0
        if wid == str(entry2):
            n = entry3.get() if entry3.get() else 0
        return True
    return False


def set_label(name, index, mode):
    if var1.get() == '' or var2.get() == '':
        pass
    else:
        res = float(var1.get()) * float(var2.get())
        result.set('{number:.{digits}f}'.format(digits=2))

def validate(string):
    regex = re.compile(r"(\+|\-)?[0-9.]*$")
    result = regex.match(string)
    return (string == ""
            or (string.count(',') <= 1
                and result is not None
                and result.group(0) != ""))


def on_validate(P):
    return validate(P)


Tluszcz = DoubleVar()
Bialko = DoubleVar()
Popiol = DoubleVar()
Wlokno = DoubleVar()
Wilgontnosc = DoubleVar()
Waga = DoubleVar()

def trace_callback(*args):
    try:
        print(Tluszcz.get())
        print(Bialko.get())
        print(Popiol.get())
        print(Wlokno.get())
        print(Wilgontnosc.get())
        print(Waga.get())
    except:
        print("value not a valid double")



tk.Label(master, text="Białko surowe",bg='#0f4c81', fg='#f5f2e9',font=("Comic Sans", 13)).grid(row=0,sticky=W,pady=2)
Bialko2 = Entry(master,validate="key",textvariable=Bialko,font=("Lato", 13), justify='center')
vcmd = (Bialko2.register(on_validate), '%P')
Bialko.trace('w', trace_callback)
Bialko2.config(validatecommand=vcmd)
Bialko2.grid(row=0, column=1,sticky=W,pady=2)
tk.Label(master, text="Tłuszcz surowy",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=1,sticky=W,pady=2)
Tluszcz2 = Entry(master,validate="key",textvariable=Tluszcz,font=("Lato", 13), justify='center')
vcmd = (Tluszcz2.register(on_validate), '%P')
Tluszcz.trace('w', trace_callback)
Tluszcz2.config(validatecommand=vcmd)
Tluszcz2.grid(row=1, column=1)
tk.Label(master, text="Popiół surowy",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=2,sticky=W,pady=2)
Popiol2 = Entry(master,validate="key",textvariable=Popiol,font=("Lato", 13), justify='center')
vcmd = (Popiol2.register(on_validate), '%P')
Popiol.trace('w', trace_callback)
Popiol2.config(validatecommand=vcmd)
Popiol2.grid(row=2, column=1)
tk.Label(master, text="Włókno surowe",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=3,sticky=W,pady=2)
Wlokno2 = Entry(master,validate="key",textvariable=Wlokno,font=("Lato", 13), justify='center')
vcmd = (Wlokno2.register(on_validate), '%P')
Wlokno.trace('w', trace_callback)
Wlokno2.config(validatecommand=vcmd)
Wlokno2.grid(row=3, column=1)
tk.Label(master, text="Wilgotność",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=4,sticky=W,pady=2)
Wilgontnosc2 = Entry(master,validate="key",textvariable=Wilgontnosc,font=("Lato", 13), justify='center')
vcmd = (Wilgontnosc2.register(on_validate), '%P')
Wilgontnosc.trace('w', trace_callback)
Wilgontnosc2.config(validatecommand=vcmd)
Wilgontnosc2.grid(row=4, column=1)
tk.Label(master, text="Waga kota",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=5,sticky=W,pady=2)
Waga2 = (Entry(master,validate="key",textvariable=Waga,font=("Lato", 13), justify='center'))
vcmd = (Waga2.register(on_validate), '%P')
Waga.trace('w', trace_callback)
Waga2.config(validatecommand=vcmd)
Waga2.grid(row=5, column=1)

button1 = tk.Button(master, text='Oblicz',command= lambda: result())

button1.grid(row=7,column=0)
tk.Label(text="Procentowa wartość węglowodanów w mokrej masie [%]",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=9,sticky=W,pady=2)
a1 = StringVar()
a = Label(textvariable=a1,bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13))
a.grid(row=9, column=1)
tk.Label(text="Gęstość energetyczna karmy [kcal/100g]",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=10,sticky=W,pady=2)
c1 = StringVar()
c = Label(textvariable=c1,bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13))
c.grid(row=10, column=1)
tk.Label(text="Rozmieczenie energii w karmie",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=11,sticky=W,pady=2)
d1 = StringVar()
d = Label(textvariable=d1,bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13))
d.grid(row=11, column=1)
tk.Label(text="Dzienne zapotrzebowanie energetyczne (MER) [kcal/dzień]",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=12,sticky=W,pady=2)
e1 = StringVar()
e = Label(textvariable=e1,bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13))
e.grid(row=12, column=1)
tk.Label(text="Dzienna dawka pokarmowa [g/dzień]",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=13,sticky=W,pady=2)
f1 = StringVar()
f = Label(textvariable=f1,bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13))
f.grid(row=13, column=1)
tk.Label(text="Procent białka w suchej masie [%]",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=14,sticky=W,pady=2)
b1 = StringVar()
b = Label(textvariable=b1,bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13))
b.grid(row=14, column=1)
tk.Label(text="Procent węglowodanów w suchej masie [%]",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=15,sticky=W,pady=2)
g1 = StringVar()
g = Label(textvariable=g1,bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13))
g.grid(row=15, column=1)
tk.Label(text="Procent tłuszczu w suchej masie [%]",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=16,sticky=W,pady=2)
h1 = StringVar()
h = Label(textvariable=h1,bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13))
h.grid(row=16, column=1)
tk.Label(text="Zapotrzebowanie na wodę [ml]",bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13)).grid(row=17,sticky=W,pady=2)
i1 = StringVar()
i = Label(textvariable=i1,bg='#0f4c81', fg='#f5f2e9',font=("Lato", 13))
i.grid(row=17, column=1)



def result():

                B = Bialko.get()
                T = Tluszcz.get()
                P = Popiol.get()
                Wl = Wlokno.get()
                Wi = Wilgontnosc.get()
                Wa = Waga.get()
                Wynik1=(100 - B - T - P - Wl - Wi)

                a1.set(float(round((100 - B - T - P - Wl - Wi),2)))
                b1.set(float(round((((B) / (100 - Wi)) * 100),2)))
                c1.set(float(round((B*3.5)+(T*8.5)+(((100 - B - T - P - Wl - Wi))*3.5),2)))
                d1.set(float(round((((B * 3.5) / ((B*3.5)+(T*8.5)+(((100 - B - T - P - Wl - Wi))*3.5))) * 100),2)))
                e1.set(float(round((60 * (math.pow(Wa, 0.67))),2)))
                f1.set(float(round(((((60 * (math.pow(Wa, 0.67)))) / ((B*3.5)+(T*8.5)+(((100 - B - T - P - Wl - Wi))*3.5))) * 100),2)))
                g1.set(float(round(((100-B-T-P-Wl-Wi)/((100-Wi))*100),2)))
                h1.set(float(round((((T) / (100 - Wi)) * 100),2)))
                i1.set(float(round((50*Wa),2)))


master.mainloop()

