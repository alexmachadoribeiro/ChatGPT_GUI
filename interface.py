from numpy import imag
import pyautogui as pg
import os
from tkinter import *
from Functions import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import openai


# Variables
color01 = '#343541' #Fundo preto
color02 = '#10a37f' #Verde
color03 = '#8e8ea0' #Cinza

# ////////////////////////////////////////////////END
# Conf thw window
root = Tk()
root.geometry(center(root, 700, 600))
root.title('Roober ChatGPT - Python')
root.config(bg=color01)
# root.resizable(False, False)
root.iconbitmap('img\RoobLog_Bitmap.ico')
# ////////////////////////////////////////////////END
# Variables

img_btn_run = PhotoImage(file=r'img\btn_run.png')

img_fr_logo = PhotoImage(
    file=r'img\Logo roober.png')
# ////////////////////////////////////////////////END
# Functions

def run():
    prompt = en_input.get()
    
    if prompt == '':
        pg.alert('Escreva algo')
    else:
        tx_output.delete("1.0", END)
        openai.api_key = 'SUA_KEY_AQUI'

        model_engine = "text-davinci-003"
        o_robo = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = o_robo.choices[0].text
        # print(response)
        tx_output.insert(END,response)
        
# ////////////////////////////////////////////////END
# Containers
fr_container01 = Frame(
    root,
    width=700,
    height=233,
    bg=color01
)
fr_container02 = Frame(
    root,
    width=700,
    height=322,
    bg=color01
)

fr_container01.grid(row=0, column=0)
fr_container02.grid(row=2, column=0)
fr_container01.grid_propagate(0)
# ////////////////////////////////////////////////END
# Itens Container 01
lb_logo_roober = Label(
    fr_container01,
    image=img_fr_logo,
    bg=color01
)

lb_title = Label(
    fr_container01,
    text='Entre com sua pergunta',
    bg=color01,
    fg=color03,
    font='Verdana 10'
)

en_input = Entry(
    fr_container01,
    bg=color01,
    fg='white',
    font='Verdana 13',
    border=0,
    width=30
)
fr_row_input = Frame(
    fr_container01,
    bg=color02,
    height=2,
    width=340
)

btn_run = Button(
    fr_container01,
    bg=color01,
    height=25,
    border=0,
    image=img_btn_run,
    activebackground=color01,
    command=run
)

fr_row_division02 = Frame(
    fr_container01,
    width=700,
    height=1,
    bg=color02
)
lb_logo_roober.grid(row=0, column=1, pady=10)
en_input.grid(row=1, column=1)
btn_run.grid(row=1, column=1, sticky=E)
fr_row_input.grid(row=2, column=1)
lb_title.grid(row=3, column=1)
fr_row_division02.grid(row=4, columnspan=3, pady=74)
# ////////////////////////////////////////////////END
# Itens Container 02
lb_title02 = Label(
    fr_container02,
    text='Saída:',
    bg=color01,
    fg=color03,
    font='Verdana 10'
)
tx_output = Text(
    fr_container02,
    bg='#40414f',
    width=60,
    height=20,
    fg='white',
    bd=0,
    font='Verdana 10'
)
lb_title02.grid(row=0,column=0,sticky=W)
tx_output.grid(row=1,column=0)

# ////////////////////////////////////////////////END
# Win in loop
root.mainloop()
