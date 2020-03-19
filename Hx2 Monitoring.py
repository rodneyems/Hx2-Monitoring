######### DEFININDO BIBLIOTECAS A SEREM UTILIADAS ###########
from pyfirmata import ArduinoMega, util
import time
from datetime import datetime
from tkinter import *
import os
import requests

def log(hibridaDeEnvio,dataEhora,tipoDeEvento):
    url = 'http://10.181.6.34:3389/add_evento_hibrida?local=DECOM-SP;hibrida='+ hibridaDeEnvio +';data_hora='+ dataEhora + ';tipo_evento=' + tipoDeEvento
    envio = requests.get(url)

    print(envio.status_code)
    pass


######### INICIO ########
print("SOFTWARE DE MONITORAÇÃO DAS HÍBRIDAS DECOM SP")

###### APELIDANDO O ARDUINOMEGA QUE ESTA NA COM3 COMO BOARD ( PADRÃO DO FIRMATA) ########
board = ArduinoMega('COM6')
util.Iterator(board).start()

###### DEFININDO OS PINOS COMO ENTRADA OU SAÍDA ########

access1 = board.get_pin('d:9:i')
access2 = board.get_pin('d:10:i')
access3 = board.get_pin('d:11:i')
access4 = board.get_pin('d:12:i')


hib9928 = board.get_pin('d:22:i')
hib9929 = board.get_pin('d:23:i')
hib9930 = board.get_pin('d:24:i')
hib9931 = board.get_pin('d:25:i')
hib9932 = board.get_pin('d:26:i')
hib9933 = board.get_pin('d:27:i')
hib9177 = board.get_pin('d:28:i')
hib9178 = board.get_pin('d:29:i')
hib9179 = board.get_pin('d:30:i')
hib5340 = board.get_pin('d:31:i')
hib9181 = board.get_pin('d:32:i')
hib9182 = board.get_pin('d:33:i')
hib5178 = board.get_pin('d:35:i')
hib5775 = board.get_pin('d:34:i')
leivoz = board.get_pin('d:50:i')
board.get_pin('d:36:o')
board.get_pin('d:37:o')
board.get_pin('d:38:o')
board.get_pin('d:39:o')
board.get_pin('d:40:o')
board.get_pin('d:41:o')
board.get_pin('d:42:o')
board.get_pin('d:43:o')
board.get_pin('d:44:o')
board.get_pin('d:45:o')
board.get_pin('d:46:o')
board.get_pin('d:47:o')
board.get_pin('d:48:o')
board.get_pin('d:49:o')
time.sleep(1)

####### VARIAVEIS PARA LOOP ###########
h9928 = "0"
h9929 = "0"
h9930 = "0"
h9931 = "0"
h9932 = "0"
h9933 = "0"
h9177 = "0"
h9178 = "0"
h9179 = "0"
h5340 = "0"
h9181 = "0"
h9182 = "0"
h5178 = "0"
h5775 = "0"

###### CONSTRUINDO JANELA DA INTERFACE GRAFICA ########
janela = Tk()
janela.title("Monitoração das Híbridas")
janela["bg"] = "white"
janela.geometry("884x625")

####### PUXANDO A IMAGEM PARA O CODIGO (SERA UTILIADA COMO BOTAO MAIS A FRENTE ########
botimageleft = PhotoImage(file="image/botoff.png")
botimageright = PhotoImage(file="image/botoff2.png")

####### DEIXANDO OS PINOS PARA DESLIGAR A HIBRIDA EM NIVEL LOGICO 1 #######
board.digital[36].write(1)
board.digital[37].write(1)
board.digital[38].write(1)
board.digital[39].write(1)
board.digital[40].write(1)
board.digital[41].write(1)
board.digital[42].write(1)
board.digital[43].write(1)
board.digital[44].write(1)
board.digital[45].write(1)
board.digital[46].write(1)
board.digital[47].write(1)
board.digital[48].write(1)
board.digital[49].write(1)

######## DEFININDO FUNCOES PARA OS BOTOES #########
def h1on():
    board.digital[36].write(0)
    time.sleep(0.3)
    board.digital[36].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9928',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass

def h2on():
    board.digital[37].write(0)
    time.sleep(0.3)
    board.digital[37].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9929',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass



def h3on():
    board.digital[38].write(0)
    time.sleep(0.3)
    board.digital[38].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9930',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h4on():
    board.digital[39].write(0)
    time.sleep(0.3)
    board.digital[39].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9931',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h5on():
    board.digital[40].write(0)
    time.sleep(0.3)
    board.digital[40].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9932',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h6on():
    board.digital[41].write(0)
    time.sleep(0.3)
    board.digital[41].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9933',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h7on():
    board.digital[42].write(0)
    time.sleep(0.3)
    board.digital[42].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9177',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h8on():
    board.digital[43].write(0)
    time.sleep(0.3)
    board.digital[43].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9178',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h9on():
    board.digital[44].write(0)
    time.sleep(0.3)
    board.digital[44].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9179',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h10on():
    board.digital[45].write(0)
    time.sleep(0.3)
    board.digital[45].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('5340',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h11on():
    board.digital[46].write(0)
    time.sleep(0.3)
    board.digital[46].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9181',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h12on():
    board.digital[47].write(0)
    time.sleep(0.3)
    board.digital[47].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('9182',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h13on():
    board.digital[48].write(0)
    time.sleep(0.3)
    board.digital[48].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('5178',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass


def h14on():
    board.digital[49].write(0)
    time.sleep(0.3)
    board.digital[49].write(1)
    horalog=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        log('5775',horalog,'3')
        print("Log registrado")
    except requests.exceptions.ConnectionError:
        print("Log não registrado")
        pass

h1 = PhotoImage(file="image/9928on.png")
h1off = PhotoImage(file="image/9928off.png")
h2 = PhotoImage(file="image/9929on.png")
h2off = PhotoImage(file="image/9929off.png")
h3 = PhotoImage(file="image/9930on.png")
h3off = PhotoImage(file="image/9930off.png")
h4 = PhotoImage(file="image/9931on.png")
h4off = PhotoImage(file="image/9931off.png")
h5 = PhotoImage(file="image/9932on.png")
h5off = PhotoImage(file="image/9932off.png")
h6 = PhotoImage(file="image/9933on.png")
h6off = PhotoImage(file="image/9933off.png")
h7 = PhotoImage(file="image/9177on.png")
h7off = PhotoImage(file="image/9177off.png")
h8 = PhotoImage(file="image/9178on.png")
h8off = PhotoImage(file="image/9178off.png")
h9 = PhotoImage(file="image/9179on.png")
h9off = PhotoImage(file="image/9179off.png")
h10 = PhotoImage(file="image/5340on.png")
h10off = PhotoImage(file="image/5340off.png")
h111 = PhotoImage(file="image/9181on.png")
h111off = PhotoImage(file="image/9181off.png")
h112 = PhotoImage(file="image/9182on.png")
h112off = PhotoImage(file="image/9182off.png")
h113 = PhotoImage(file="image/5178on.png")
h113off = PhotoImage(file="image/5178off.png")
h114 = PhotoImage(file="image/5775on.png")
h114off = PhotoImage(file="image/5775off.png")


f = "%d/%m/%Y %H:%M:%S"

####### PRIMEIRA VARREDURA RÁPIDA #########

status9928 = hib9928.read()
time.sleep(0.1)
if status9928 != h9928:
    if status9928 == False:
        h9928 = status9928
        h11 = Label(janela, image=h1, borderwidth=0)
        h11.grid(row=1, column=1)
        h1desliga = Button(janela, image=botimageleft, command=h1on, height=20, width=20, borderwidth=0).place(
            x=319, y=52)
        janela.update()

    if status9928 == True:
        h9928 = status9928

        h11off = Label(janela, image=h1off, borderwidth=0)
        h11off.grid(row=1, column=1)
        janela.update()

status9929 = hib9929.read()
time.sleep(0.1)
if status9929 != h9929:
    if status9929 == False:
        h9929 = status9929
        h22 = Label(janela, image=h2, borderwidth=0)
        h22.grid(row=1, column=2)
        h2desliga = Button(janela, image=botimageright, command=h2on, height=20, width=20, borderwidth=0).place(
            x=574, y=52)
        janela.update()

    if status9929 == True:
        h9929 = status9929
        h22off = Label(janela, image=h2off, borderwidth=0)
        h22off.grid(row=1, column=2)
        janela.update()

status9930 = hib9930.read()
time.sleep(0.1)
if status9930 != h9930:
    if status9930 == False:
        h9930 = status9930
        h33 = Label(janela, image=h3, borderwidth=0)
        h33.grid(row=2, column=1)
        h3desliga = Button(janela, image=botimageleft, command=h3on, height=20, width=20, borderwidth=0).place(
            x=319, y=141)
        janela.update()

    if status9930 == True:
        h9930 = status9930
        h33off = Label(janela, image=h3off, borderwidth=0)
        h33off.grid(row=2, column=1)
        janela.update()

status9931 = hib9931.read()
time.sleep(0.1)
if status9931 != h9931:
    if status9931 == False:
        h9931 = status9931
        h44 = Label(janela, image=h4, borderwidth=0)
        h44.grid(row=2, column=2)
        h4desliga = Button(janela, image=botimageright, command=h4on, height=20, width=20, borderwidth=0).place(
            x=574,
            y=141)
        janela.update()

    if status9931 == True:
        h9931 = status9931
        h44off = Label(janela, image=h4off, borderwidth=0)
        h44off.grid(row=2, column=2)
        janela.update()

status9932 = hib9932.read()
time.sleep(0.1)
if status9932 != h9932:
    if status9932 == False:
        h9932 = status9932
        h55 = Label(janela, image=h5, borderwidth=0)
        h55.grid(row=3, column=1)
        h5desliga = Button(janela, image=botimageleft, command=h5on, height=20, width=20, borderwidth=0).place(
            x=319, y=230)
        janela.update()

    if status9932 == True:
        h9932 = status9932
        h55off = Label(janela, image=h5off, borderwidth=0)
        h55off.grid(row=3, column=1)
        janela.update()

status9933 = hib9933.read()
time.sleep(0.1)
if status9933 != h9933:
    if status9933 == False:
        h9933 = status9933
        h66 = Label(janela, image=h6, borderwidth=0)
        h66.grid(row=3, column=2)
        h6desliga = Button(janela, image=botimageright, command=h6on, height=20, width=20, borderwidth=0).place(
            x=574,
            y=230)
        janela.update()

    if status9933 == True:
        h9933 = status9933
        h66off = Label(janela, image=h6off, borderwidth=0)
        h66off.grid(row=3, column=2)
        janela.update()

status9177 = hib9177.read()
time.sleep(0.1)
if status9177 != h9177:
    if status9177 == False:
        h9177 = status9177
        h77 = Label(janela, image=h7, borderwidth=0)
        h77.grid(row=4, column=1)
        h7desliga = Button(janela, image=botimageleft, command=h7on, height=20, width=20, borderwidth=0).place(
            x=319, y=319)
        janela.update()

    if status9177 == True:
        h9177 = status9177
        h77off = Label(janela, image=h7off, borderwidth=0)
        h77off.grid(row=4, column=1)
        janela.update()

status9178 = hib9178.read()
time.sleep(0.1)
if status9178 != h9178:
    if status9178 == False:
        h9178 = status9178
        h88 = Label(janela, image=h8, borderwidth=0)
        h88.grid(row=4, column=2)
        h8desliga = Button(janela, image=botimageright, command=h8on, height=20, width=20, borderwidth=0).place(
            x=574,
            y=319)
        janela.update()

    if status9178 == True:
        h9178 = status9178
        h88off = Label(janela, image=h8off, borderwidth=0)
        h88off.grid(row=4, column=2)
        janela.update()

status9179 = hib9179.read()
time.sleep(0.1)
if status9179 != h9179:
    if status9179 == False:
        h9179 = status9179
        h99 = Label(janela, image=h9, borderwidth=0)
        h99.grid(row=5, column=1)
        janela.update()

    if status9179 == True:
        h9179 = status9179
        h99off = Label(janela, image=h9off, borderwidth=0)
        h99off.grid(row=5, column=1)
        h9desliga = Button(janela, image=botimageleft, command=h9on, height=20, width=20, borderwidth=0).place(
            x=319, y=408)
        janela.update()

status5340 = hib5340.read()
time.sleep(0.1)
if status5340 != h5340:
    if status5340 == False:
        h5340 = status5340
        h100 = Label(janela, image=h10, borderwidth=0)
        h100.grid(row=5, column=2)
        h10desliga = Button(janela, image=botimageright, command=h10on, height=20, width=20, borderwidth=0).place(
            x=574,
            y=408)
        janela.update()

    if status5340 == True:
        h5340 = status5340
        h100off = Label(janela, image=h10off, borderwidth=0)
        h100off.grid(row=5, column=2)
        janela.update()

status9181 = hib9181.read()
time.sleep(0.1)
if status9181 != h9181:
    if status9181 == False:
        h9181 = status9181
        h1111 = Label(janela, image=h111, borderwidth=0)
        h1111.grid(row=6, column=1)
        h11desliga = Button(janela, image=botimageleft, command=h11on, height=20, width=20, borderwidth=0).place(
            x=319,
            y=497)
        janela.update()

    if status9181 == True:
        h9181 = status9181
        h1111off = Label(janela, image=h111off, borderwidth=0)
        h1111off.grid(row=6, column=1)
        janela.update()

status9182 = hib9182.read()
time.sleep(0.1)
if status9182 != h9182:
    if status9182 == False:
        h9182 = status9182
        h1112 = Label(janela, image=h112, borderwidth=0)
        h1112.grid(row=6, column=2)
        h12desliga = Button(janela, image=botimageright, command=h12on, height=20, width=20, borderwidth=0).place(
            x=574,
            y=497)
        janela.update()

    if status9182 == True:
        h9182 = status9182
        h1112off = Label(janela, image=h112off, borderwidth=0)
        h1112off.grid(row=6, column=2)
        janela.update()

status5178 = hib5178.read()
time.sleep(0.1)
if status5178 != h5178:
    if status5178 == False:
        h5178 = status5178
        h1113 = Label(janela, image=h113, borderwidth=0)
        h1113.grid(row=7, column=1)
        h13desliga = Button(janela, image=botimageleft, command=h13on, height=20, width=20, borderwidth=0).place(
            x=319,
            y=586)
        janela.update()

    if status5178 == True:
        h5178 = status5178
        h1113off = Label(janela, image=h113off, borderwidth=0)
        h1113off.grid(row=7, column=1)
        janela.update()

status5775 = hib5775.read()
time.sleep(0.1)
if status5775 != h5775:
    if status5775 == False:
        h5775 = status5775
        h1114 = Label(janela, image=h114, borderwidth=0)
        h1114.grid(row=7, column=2)
        h14desliga = Button(janela, image=botimageright, command=h14on, height=20, width=20, borderwidth=0).place(
            x=574,
            y=586)
        janela.update()

    if status5775 == True:
        h5775 = status5775
        h1114off = Label(janela, image=h114off, borderwidth=0)
        h1114off.grid(row=7, column=2)
        janela.update()

t1="0"
t2="0"
t3="0"
t4="0"
t5="0"
t6="0"
t7="0"
t8="0"
t9="0"
t010="0"
t011="0"
t012="0"
t013="0"
t014="0"
a1 = "0"
a2 = "0"
a3 = "0"
a4 = "0"

access1comp = access1.read()
access2comp = access2.read()
access3comp = access3.read()
access4comp = access4.read()

###### INICIO DO LOOP #####
while 1 == 1:

    status9928 = hib9928.read()
    time.sleep(0.1)
    if status9928 != h9928:
        if status9928 == False:
            t1 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 01 9928 conectada em\t" + str(t1) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9928 conectada', t1)
            os.system('start audio/9928cone.mp3')
            h9928 = status9928
            h1 = PhotoImage(file="image/9928on.png")
            h11 = Label(janela, image=h1, borderwidth=0)
            h11.grid(row=1, column=1)
            h1desliga = Button(janela, image=botimageleft, command=h1on, height=20, width=20, borderwidth=0).place(
                x=319, y=52)
            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9928', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9928 == True:
            t11 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 01 9928 desconectada em\t" + str(t11) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9928 desconectada', t11)
            os.system('start audio/9928desc.mp3')
            h9928 = status9928
            h1off = PhotoImage(file="image/9928off.png")
            h11off = Label(janela, image=h1off, borderwidth=0)
            h11off.grid(row=1, column=1)
            janela.update()
            if t1 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9928', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass


    status9929 = hib9929.read()
    time.sleep(0.1)
    if status9929 != h9929:
        if status9929 == False:
            t2 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 02 9929 conectada em\t" + str(t2) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9929 conectada', t2)
            os.system('start audio/9929cone.mp3')
            h9929 = status9929
            h2 = PhotoImage(file="image/9929on.png")
            h22 = Label(janela, image=h2, borderwidth=0)
            h22.grid(row=1, column=2)
            h2desliga = Button(janela, image=botimageright, command=h2on, height=20, width=20, borderwidth=0).place(
                x=574, y=52)
            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9929', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9929 == True:
            t22 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 02 9929 desconectada em\t" + str(t22) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9929 desconectada', t22)
            os.system('start audio/9929desc.mp3')
            h9929 = status9929
            h2off = PhotoImage(file="image/9929off.png")
            h22off = Label(janela, image=h2off, borderwidth=0)
            h22off.grid(row=1, column=2)
            janela.update()
            if t2 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9929', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status9930 = hib9930.read()
    time.sleep(0.1)
    if status9930 != h9930:
        if status9930 == False:
            t3 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 03 9930 conectada em\t" + str(t3) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9930 conectada', t3)
            os.system('start audio/9930cone.mp3')
            h9930 = status9930
            h3 = PhotoImage(file="image/9930on.png")
            h33 = Label(janela, image=h3, borderwidth=0)
            h33.grid(row=2, column=1)
            h3desliga = Button(janela, image=botimageleft, command=h3on, height=20, width=20, borderwidth=0).place(
                x=319, y=141)

            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9930', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9930 == True:
            t33 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 03 9930 desconectada em\t" + str(t33) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9930 desconectada', t33)
            os.system('start audio/9930desc.mp3')
            h9930 = status9930
            h3off = PhotoImage(file="image/9930off.png")
            h33off = Label(janela, image=h3off, borderwidth=0)
            h33off.grid(row=2, column=1)
            janela.update()
            if t3 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9930', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status9931 = hib9931.read()
    time.sleep(0.1)
    if status9931 != h9931:
        if status9931 == False:
            t4 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 04 9931 conectada em\t" + str(t4) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9931 conectada', t4)
            os.system('start audio/9931cone.mp3')
            h9931 = status9931
            h4 = PhotoImage(file="image/9931on.png")
            h44 = Label(janela, image=h4, borderwidth=0)
            h44.grid(row=2, column=2)
            h4desliga = Button(janela, image=botimageright, command=h4on, height=20, width=20, borderwidth=0).place(
                x=574,
                y=141)

            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9931', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9931 == True:
            t44 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 04 9931 desconectada em\t" + str(t44) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9931 desconectada', t44)
            os.system('start audio/9931desc.mp3')
            h9931 = status9931
            h4off = PhotoImage(file="image/9931off.png")
            h44off = Label(janela, image=h4off, borderwidth=0)
            h44off.grid(row=2, column=2)
            janela.update()
            if t4 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9931', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status9932 = hib9932.read()
    time.sleep(0.1)
    if status9932 != h9932:
        if status9932 == False:
            t5 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 05 9932 conectada em\t" + str(t5) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9932 conectada', t5)
            os.system('start audio/9932cone.mp3')
            h9932 = status9932
            h5 = PhotoImage(file="image/9932on.png")
            h55 = Label(janela, image=h5, borderwidth=0)
            h55.grid(row=3, column=1)
            h5desliga = Button(janela, image=botimageleft, command=h5on, height=20, width=20, borderwidth=0).place(
                x=319, y=230)
            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9932', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9932 == True:
            t55 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 05 9932 desconectada em\t" + str(t55) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9932 desconectada', t55)
            os.system('start audio/9932desc.mp3')
            h9932 = status9932
            h5off = PhotoImage(file="image/9932off.png")
            h55off = Label(janela, image=h5off, borderwidth=0)
            h55off.grid(row=3, column=1)
            janela.update()
            if t5 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9932', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status9933 = hib9933.read()
    time.sleep(0.1)
    if status9933 != h9933:
        if status9933 == False:
            t6 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 06 9933 conectada em\t" + str(t6) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9933 conectada', t6)
            os.system('start audio/9933cone.mp3')
            h9933 = status9933
            h6 = PhotoImage(file="image/9933on.png")
            h66 = Label(janela, image=h6, borderwidth=0)
            h66.grid(row=3, column=2)
            h6desliga = Button(janela, image=botimageright, command=h6on, height=20, width=20, borderwidth=0).place(
                x=574,
                y=230)

            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9933', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9933 == True:
            t66 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 06 9933 desconectada em\t" + str(t66) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9933 desconectada', t66)
            os.system('start audio/9933desc.mp3')
            h9933 = status9933
            h6off = PhotoImage(file="image/9933off.png")
            h66off = Label(janela, image=h6off, borderwidth=0)
            h66off.grid(row=3, column=2)
            janela.update()
            if t6 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9933', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status9177 = hib9177.read()
    time.sleep(0.1)
    if status9177 != h9177:
        if status9177 == False:
            t7 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 07 9177 conectada em\t" + str(t7) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9177 conectada', t7)
            os.system('start audio/9177cone.mp3')
            h9177 = status9177
            h7 = PhotoImage(file="image/9177on.png")
            h77 = Label(janela, image=h7, borderwidth=0)
            h77.grid(row=4, column=1)
            h7desliga = Button(janela, image=botimageleft, command=h7on, height=20, width=20, borderwidth=0).place(
                x=319, y=319)

            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9177', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9177 == True:
            t77 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 07 9177 desconectada em\t" + str(t77) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9177 desconectada', t77)
            os.system('start audio/9177desc.mp3')
            h9177 = status9177
            h7off = PhotoImage(file="image/9177off.png")
            h77off = Label(janela, image=h7off, borderwidth=0)
            h77off.grid(row=4, column=1)
            janela.update()
            if t7 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9177', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass
    #
    status9178 = hib9178.read()
    time.sleep(0.1)
    if status9178 != h9178:
        if status9178 == False:
            t8 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 08 9178 conectada em\t" + str(t8) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9178 conectada', t8)
            os.system('start audio/9178cone.mp3')
            h9178 = status9178
            h8 = PhotoImage(file="image/9178on.png")
            h88 = Label(janela, image=h8, borderwidth=0)
            h88.grid(row=4, column=2)
            h8desliga = Button(janela, image=botimageright, command=h8on, height=20, width=20, borderwidth=0).place(
                x=574,
                y=319)

            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9928', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9178 == True:
            t88 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 08 9178 desconectada em\t" + str(t88) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9178 desconectada', t88)
            os.system('start audio/9178desc.mp3')
            h9178 = status9178
            h8off = PhotoImage(file="image/9178off.png")
            h88off = Label(janela, image=h8off, borderwidth=0)
            h88off.grid(row=4, column=2)
            janela.update()
            if t8 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9178', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status9179 = hib9179.read()
    time.sleep(0.1)
    if status9179 != h9179:
        if status9179 == False:
            t9 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 09 9179 conectada em\t" + str(t9) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9179 conectada', t9)
            os.system('start audio/9179cone.mp3')
            h9179 = status9179
            h9 = PhotoImage(file="image/9179on.png")
            h99 = Label(janela, image=h9, borderwidth=0)
            h99.grid(row=5, column=1)
            h9desliga = Button(janela, image=botimageleft, command=h9on, height=20, width=20, borderwidth=0).place(
                x=319, y=408)
            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9179', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9179 == True:
            t99 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 09 9179 desconectada em\t" + str(t99) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9179 desconectada', t99)
            os.system('start audio/9179desc.mp3')
            h9179 = status9179
            h9off = PhotoImage(file="image/9179off.png")
            h99off = Label(janela, image=h9off, borderwidth=0)
            h99off.grid(row=5, column=1)
            janela.update()
            if t9 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9179', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status5340 = hib5340.read()
    time.sleep(0.1)
    if status5340 != h5340:
        if status5340 == False:
            t010 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 10 5340 conectada em\t" + str(t010) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 5340 conectada', t010)
            os.system('start audio/5340cone.mp3')
            h5340 = status5340
            h10 = PhotoImage(file="image/5340on.png")
            h100 = Label(janela, image=h10, borderwidth=0)
            h100.grid(row=5, column=2)
            h10desliga = Button(janela, image=botimageright, command=h10on, height=20, width=20, borderwidth=0).place(
                x=574,
                y=408)
            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('5340', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status5340 == True:
            t0100 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 10 5340 desconectada em\t" + str(t0100) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 5340 desconectada', t0100)
            os.system('start audio/5340desc.mp3')
            h5340 = status5340
            h10off = PhotoImage(file="image/5340off.png")
            h100off = Label(janela, image=h10off, borderwidth=0)
            h100off.grid(row=5, column=2)
            janela.update()
            if t010 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('5340', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status9181 = hib9181.read()
    time.sleep(0.1)
    if status9181 != h9181:
        if status9181 == False:
            t011 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 11 9181 conectada em\t" + str(t011) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9181 conectada', t011)
            os.system('start audio/9181cone.mp3')
            h9181 = status9181
            h111 = PhotoImage(file="image/9181on.png")
            h1111 = Label(janela, image=h111, borderwidth=0)
            h1111.grid(row=6, column=1)
            h11desliga = Button(janela, image=botimageleft, command=h11on, height=20, width=20, borderwidth=0).place(
                x=319,
                y=497)

            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9181', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9181 == True:
            t0110 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 11 9181 desconectada em\t" + str(t0110) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9181 desconectada', t0110)
            os.system('start audio/9181desc.mp3')
            h9181 = status9181
            h111off = PhotoImage(file="image/9181off.png")
            h1111off = Label(janela, image=h111off, borderwidth=0)
            h1111off.grid(row=6, column=1)
            janela.update()
            if t011 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9181', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status9182 = hib9182.read()
    time.sleep(0.1)
    if status9182 != h9182:
        if status9182 == False:
            t012 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 12 9182 conectada em\t" + str(t012) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9182 conectada', t012)
            os.system('start audio/9182cone.mp3')
            h9182 = status9182
            h112 = PhotoImage(file="image/9182on.png")
            h1112 = Label(janela, image=h112, borderwidth=0)
            h1112.grid(row=6, column=2)
            h12desliga = Button(janela, image=botimageright, command=h12on, height=20, width=20, borderwidth=0).place(
                x=574,
                y=497)

            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('9182', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status9182 == True:
            t0120 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 12 9182 desconectada em\t" + str(t0120) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 9182 desconectada', t0120)
            os.system('start audio/9182desc.mp3')
            h9182 = status9182
            h112off = PhotoImage(file="image/9182off.png")
            h1112off = Label(janela, image=h112off, borderwidth=0)
            h1112off.grid(row=6, column=2)
            janela.update()
            if t012 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('9182', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status5178 = hib5178.read()
    time.sleep(0.1)
    if status5178 != h5178:
        if status5178 == False:
            t013 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 13 5178 conectada em\t" + str(t013) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 5178 conectada', t013)
            os.system('start audio/5178cone.mp3')
            h5178 = status5178
            h113 = PhotoImage(file="image/5178on.png")
            h1113 = Label(janela, image=h113, borderwidth=0)
            h1113.grid(row=7, column=1)
            h13desliga = Button(janela, image=botimageleft, command=h13on, height=20, width=20, borderwidth=0).place(
                x=319,
                y=586)

            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('5178', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status5178 == True:
            t0130 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 13 5178 desconectada em\t" + str(t0130) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 5178 desconectada', t0130)
            os.system('start audio/5178desc.mp3')
            h5178 = status5178
            h113off = PhotoImage(file="image/5178off.png")
            h1113off = Label(janela, image=h113off, borderwidth=0)
            h1113off.grid(row=7, column=1)
            janela.update()
            if t013 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('5178', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    status5775 = hib5775.read()
    time.sleep(0.1)
    if status5775 != h5775:
        if status5775 == False:
            t014 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 14 5775 conectada em\t" + str(t014) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 5775 conectada', t014)
            os.system('start audio/5775cone.mp3')
            h5775 = status5775
            h114 = PhotoImage(file="image/5775on.png")
            h1114 = Label(janela, image=h114, borderwidth=0)
            h1114.grid(row=7, column=2)
            h14desliga = Button(janela, image=botimageright, command=h14on, height=20, width=20, borderwidth=0).place(
                x=574,
                y=586)
            janela.update()
            horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            try:
                log('5775', horalog, '1')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass

        if status5775 == True:
            t0140 = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            imprimir = str("Híbrida 14 5775 desconectada em\t" + str(t0140) + "\n")
            with open("historico.txt", "a") as arquivo:
                arquivo.write(imprimir)
            print('Híbrida 5775 desconectada', t0140)
            os.system('start audio/5775desc.mp3')
            h5775 = status5775
            h114off = PhotoImage(file="image/5775off.png")
            h1114off = Label(janela, image=h114off, borderwidth=0)
            h1114off.grid(row=7, column=2)
            janela.update()
            if t014 != "0":
                horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                try:
                    log('5775', horalog, '2')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    statusaccess1 = access1.read()
    if statusaccess1 != access1comp:
        horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        if statusaccess1 == False:
            print("Access 1 Conectado")
            access1comp = statusaccess1
            a1 = "1"
            try:
                log('ACCESS 1 SP', horalog, '5')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass
        else:
            print("Access 1 Desconectado")
            access1comp = statusaccess1
            if a1 != "0":
                try:
                    log('ACCESS 1 SP', horalog, '6')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    statusaccess2 = access2.read()
    if statusaccess2 != access2comp:
        horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        if statusaccess2 == False:
            print("Access 2 Conectado")
            access2comp = statusaccess2
            a2 = "1"
            try:
                log('ACCESS 2 SP', horalog, '5')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass
        else:
            print("Access 2 Desconectado")
            access2comp = statusaccess2
            if a2 != "0":
                try:
                    log('ACCESS 2 SP', horalog, '6')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    statusaccess3 = access3.read()
    if statusaccess3 != access3comp:
        horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        if statusaccess3 == False:
            print("Access 3 Conectado")
            access3comp = statusaccess3
            a3 = "1"
            try:
                log('ACCESS 3 SP', horalog, '5')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass
        else:
            print("Access 3 Desconectado")
            access3comp = statusaccess3
            if a3 != "0":
                try:
                    log('ACCESS 3 SP', horalog, '6')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    statusaccess4 = access4.read()
    if statusaccess4 != access4comp:
        horalog = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        if statusaccess4 == False:
            print("Access 4 Conectado")
            access4comp = statusaccess4
            a4 = "1"
            try:
                log('ACCESS 4 SP', horalog, '5')
                print("Log registrado")
            except requests.exceptions.ConnectionError:
                print("Log não registrado")
                pass
        else:
            print("Access 4 Desconectado")
            access4comp = statusaccess4
            if a3 != "0":
                try:
                    log('ACCESS 4 SP', horalog, '6')
                    print("Log registrado")
                except requests.exceptions.ConnectionError:
                    print("Log não registrado")
                    pass

    janela.update()



