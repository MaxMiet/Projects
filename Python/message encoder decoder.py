from tkinter import *
import base64
from tkinter import font

base = Tk()

base.geometry('500x300')
base.resizable(0,0)
base.title('Cryptographer')
base.configure(bg='black')


Label(base, text = 'Encoder/Decoder', bg = 'black', fg = 'ghost white', font = 'arial 20 bold').pack()

Label(base, text = 'Basiqs cryptographer', bg = 'black', fg = 'ghost white', font = 'arial 10').pack(side=BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()

def Encode(key,message):
    enc = []

    for i in range (len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode(''.join(enc).encode()).decode()

def Decode(key,message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range (len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return ''.join(dec)

def Mode():
    if(mode.get() == 'e'):
        result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        result.set(Decode(private_key.get(), Text.get()))
    else:
        result.set('Invalid Mode')

def Exit():
    base.destroy()

def Reset():
    Text.set('')
    private_key.set('')
    mode.set('')
    result.set('')

Label(base, font = 'arial 12 bold', text = 'Message:', bg = 'black', fg = 'ghost white').place(x=60, y=60)
Entry(base, font = 'arial 10', textvariable= Text, bg = 'ghost white').place(x=290, y=60)

Label(base, font = 'arial 12 bold', text = 'Cypher key', bg = 'black', fg = 'ghost white').place(x=60, y=90)
Entry(base, font = 'arial 10', textvariable = private_key, bg = 'ghost white').place(x=290, y=90)

Label(base, font = 'arial 10 bold', text ='Algorithm (e-encode, d-decode)', bg = 'black', fg = 'ghost white').place(x=60, y = 120)
Entry(base, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(base, font = 'arial 10 bold', textvariable = result, bg ='ghost white').place(x=290, y = 150)

Button(base, font = 'arial 10 bold', text = 'Run', padx =2, bg = 'light green', command = Mode).place(x=60, y = 150)
Button(base, font = 'arial 10 bold', text = 'Reset', width =6, command = Reset, bg = 'light blue', padx=2).place(x=60, y = 190)
Button(base, font = 'arial 10 bold', text= 'Exit', width = 6, command = Exit, bg = 'light blue', padx=2, pady=2).place(x=60, y = 230)

base.mainloop()