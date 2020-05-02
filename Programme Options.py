import random
from tkinter import*
from math import*
from tkinter.messagebox import *
fact = factorial

n = 0

#-------------------------------------------------------------------------------------------------------#
#FONCTIONS

def valider():
    S.set(S0.get())
    Sround.set(round(S0.get()))
    N.set(N0.get())
    S11.set(round(S.get()*(1+b.get()),4))
    S12.set(round(S.get()*(1+a.get()),4))
    if C.get() == 1:
        ActualisationC(a.get(),b.get(),r.get(),p.get(),K.get(),S.get(),N.get())
        ActualisationWalletC(a.get(),b.get(),r.get(),K.get(),N.get(),0,S.get(),p.get())
    else:
        ActualisationP(a.get(),b.get(),r.get(),p.get(),K.get(),S0.get(),N.get())
        ActualisationWalletP(a.get(),b.get(),r.get(),K.get(),N.get(),0,S.get(),p.get())


#ACTUALISATION CALL
def ActualisationC(a,b,r,p,K,S0,N):
    print("Actu :", N,S0)
    #Gestion Call0
    #Suppression des valeurs du Call0
    for w in frameCall0.winfo_children():
        w.destroy()
    ym = 50    
    n=0
    for j in range(0,n+1):
        S = S0*((1+a)**(j))*((1+b)**(n-j))
        Label(frameCall0, text ="""{}""".format((round(calli(a,b,r,K,N,n,S),4),round(S,4))), font=("Courier",13)).place(x = 0, y = ym)
        ym = ym + 40
    #Gestion Call1
    #Suppression des valeurs du Call1
    for w in frameCall1.winfo_children():
        w.destroy()
    if N >= 1:
        ym = 30
        n=1
        for j in range(0,n+1):
            S = S0*((1+a)**(j))*((1+b)**(n-j))
            Label(frameCall1, text ="""{}""".format((round(calli(a,b,r,K,N,n,S),4),round(S,4))), font=("Courier",13)).place(x = 0, y = ym)
            ym = ym + 40
    #Gestion Call2
    #Suppression des valeurs du Call2
    for w in frameCall2.winfo_children():
            w.destroy()
    if N >= 2:
        ym= 20
        n=2
        for j in range(0,n+1):
            S = S0*((1+a)**(j))*((1+b)**(n-j))
            Label(frameCall2, text ="""{}""".format((round(calli(a,b,r,K,N,n,S),4),round(S,4))), font=("Courier",13)).place(x = 0, y = ym)
            ym = ym + 40

    
#ACTUALISATION PUT
def ActualisationP(a,b,r,p,K,S0,N):
    #Gestion Put0
    #Suppression des valeurs du Put0
    for w in frameCall0.winfo_children():
        w.destroy()
    ym = 50    
    n=0
    for j in range(0,n+1):
        S = S0*((1+a)**(j))*((1+b)**(n-j))
        temp = calli(a,b,r,K,N,n,S) - S + K*((1+r)**(n-N))
        Label(frameCall0, text ="""{}""".format((round(temp,4),round(S,4))), font=("Courier",13)).place(x = 0, y = ym)
        ym = ym + 40
    #Gestion Put1
    #Suppression des valeurs du Put1
    for w in frameCall1.winfo_children():
        w.destroy()
    ym = 30
    n=1
    for j in range(0,n+1):
        S = S0*((1+a)**(j))*((1+b)**(n-j))
        temp = calli(a,b,r,K,N,n,S) - S + K*((1+r)**(n-N))
        Label(frameCall1, text ="""{}""".format((round(temp,4),round(S,4))), font=("Courier",13)).place(x = 0, y = ym)
        ym = ym + 40
    #Gestion Put2
    #Suppression des valeurs du Put2
    for w in frameCall2.winfo_children():
        w.destroy()
    ym= 20
    n=2
    for j in range(0,n+1):
        S = S0*((1+a)**(j))*((1+b)**(n-j))
        temp = calli(a,b,r,K,N,n,S) - S + K*((1+r)**(n-N))
        Label(frameCall2, text ="""{}""".format((round(temp,4),round(S,4))), font=("Courier",13)).place(x = 0, y = ym)
        ym = ym + 40

def Suivant():
    global n
    print("S0, N0,", S0.get(), N0.get())
    Ntest = N0.get()
    if n+1 > Ntest:
        showinfo("Temps dépasse", "Impossible, la date d'echeance vient d'etre depassee")
    else:
        n=n+1
        fluctu1()
        print("S,N", S.get(), N.get())
        Sround.set(round(S.get(),4))
        S11.set(round(S.get()*(1+b.get()),4))
        S12.set(round(S.get()*(1+a.get()),4))
        #Gestion Instant n
        for w in frameInstantn.winfo_children():
            w.destroy()
        Label(frameInstantn, text = "Instant n : ""{}""".format(n), font=('Courrier', 20)).place(x=250,y=0)

        for w in frameWallet.winfo_children():
            w.destroy()
        if C.get()==1:
            ActualisationC(a.get(),b.get(),r.get(),p.get(),K.get(),S.get(),N.get())
            ActualisationWalletC(a.get(),b.get(),r.get(),K.get(),N.get(),0,S.get(),p.get())
        else:
            ActualisationP(a.get(),b.get(),r.get(),p.get(),K.get(),S.get(),N.get())
            ActualisationWalletP(a.get(),b.get(),r.get(),K.get(),N.get(),0,S.get(),p.get())
        
        if N.get() == 1:
            for w in frameCall2.winfo_children():
                w.destroy()
        elif N.get() <= 0:
            N.set(0)
            for w in frameCall2.winfo_children():
                w.destroy()
            for w in frameCall1.winfo_children():
                w.destroy()

def Reset():
    global n
    n=0
    #Gestion Instant n
    for w in frameInstantn.winfo_children():
        w.destroy()
    Label(frameInstantn, text = "Instant n : ""{}""".format(n), font=('Courrier', 20)).place(x=250,y=0)

    N.set(N0.get())
    temp = S0.get()
    S.set(temp)
    Sround.set(round(temp,4))
    S11.set(round(S.get()*(1+b.get()),4))
    S12.set(round(S.get()*(1+a.get()),4))
    for w in frameWallet.winfo_children():
        w.destroy()
    for w in frameCall0.winfo_children():
        w.destroy()
    for w in frameCall1.winfo_children():
        w.destroy() 
    for w in frameCall2.winfo_children():
        w.destroy()
        

def ActiveCall():
    C.set(1)
    frameCall.config(text = 'Call')
    frameCall0.config(text = 'Call0')
    frameCall1.config(text = 'Call1')
    frameCall2.config(text = 'Call2')
    print('Call activé')

def ActivePut():
    C.set(0)
    frameCall.config(text = 'Put')
    frameCall0.config(text = 'Put0')
    frameCall1.config(text = 'Put1')
    frameCall2.config(text = 'Put2')
    print('Put activé')

#-------------------------------------------------------------------------------------------------------#
#FONCTIONS CALCULS CALL,PUT...

def fluctu1():
    S1 = S.get()
    p1 = p.get()
    a1 = a.get()
    b1 = b.get()
    c=0
    while c!=1:
        if random.random() <= p1 :
            S1= (S1 * (1+a1))
        else :
            S1 = (S1 * (1+b1))
        c+=1
    S.set(S1)
    N.set(N.get() - 1)
        
def fluctu(a,b,p,S0,n) :
    S=S0
    c=0
    while c!=n :
        if random.random() <= p :
            S= (S * (1+a))
        else :
            S = (S * (1+b))
        c+=1
    return S

def call(a,b,r,K,N,n,S0):
    p = (b-r)/(b-a)
    S = fluctu(a,b,p,S0,n)
    c=0
    for i in range(0,N-n+1,1):
        c = c + (fact(N-n)/(fact(int(i))*(fact(int(N-n-i)))))*(p**i)*((1-p)**(N-n-i))*max(S*((1+a)**i)*((1+b)**(N-n-i))-K,0)
    c = c * (1)/((1+r)**(N-n))
    return c

def calli(a,b,r,K,N,n,S):
    p = (b-r)/(b-a)
    c=0
    for i in range(0,N-n+1,1):
        c = c + (fact(N-n)/(fact(int(i))*(fact(int(N-n-i)))))*(p**i)*((1-p)**(N-n-i))*max(S*((1+a)**i)*((1+b)**(N-n-i))-K,0)
    c = c * (1)/((1+r)**(N-n))
    return c

def allCalln(a,b,r,K,N,n,S0):
    for j in range(0,n+1):
        S = S0*((1+a)**(j))*((1+b)**(n-j))
        return (round(calli(a,b,r,K,N,n,S),4),round(S,4))

def put(a,b,r,K,N,n,S0):
    return (call(a,b,r,K,N,n,S0) - S0 + K*((1+r)**(n-N)))
    
def ActualisationWalletC(a,b,r,K,N,n0,S0,p):
    global n
    if N == 0:
        print("Ouais N=0, et n",n)
        phin = Phin.get()
        phi0 = Phi0.get()
        print(S0)
        w = phi0 * (1 + r)**(n) + phin * S0
        ym = 20
        for i in range(0,3):
            if i == 0:
                Label(frameWallet, text ="Nombre d'actifs risques a detenir : ""{}""".format(round(phin,4)), font=("Courier",13)).place(x = 10, y = ym)
            if i == 1:
                Label(frameWallet, text ="Nombre d'actifs non risques a detenir : ""{}""".format(round(phi0,4)), font=("Courier",13)).place(x = 10, y = ym)
            if i == 2:
                Label(frameWallet, text ="Valeur du portefeuille: ""{}""".format(round(w,4)), font=("Courier",13)).place(x = 10, y = ym)
            ym = ym + 30
    else:
        print("N != 0 ", N,n)
        print(S0)
        print('----------------------')
        phin = (call(a,b,r,K,N-1,0,S0*(1+b)) - call(a,b,r,K,N-1,0,S0*(1+a)))/(S0*(b-a))
        Phin.set(phin)
        phi0 = (call(a,b,r,K,N-1,0,S0*(1+a))*(1+b) - call(a,b,r,K,N-1,0,S0*(1+b))*(1+a))/((b-a)*(1+r)**(n+1))
        Phi0.set(phi0)
        w = phi0 * (1 + r)**n + phin * S0
        ym = 20
        for i in range(0,3):
            if i == 0:
                Label(frameWallet, text ="Nombre d'actifs risques a detenir : ""{}""".format(round(phin,4)), font=("Courier",13)).place(x = 10, y = ym)
            if i == 1:
                Label(frameWallet, text ="Nombre d'actifs non risques a detenir : ""{}""".format(round(phi0,4)), font=("Courier",13)).place(x = 10, y = ym)
            if i == 2:
                Label(frameWallet, text ="Valeur du portefeuille: ""{}""".format(round(w,4)), font=("Courier",13)).place(x = 10, y = ym)
            ym = ym + 30

def ActualisationWalletP(a,b,r,K,N,n0,S0,p):
    global n
    if N == 0:
        phin = Phin.get()
        phi0 = Phi0.get()
        w = phi0 * (1 + r)**(n) + phin * S0
        ym = 20
        for i in range(0,3):
            if i == 0:
                Label(frameWallet, text ="Nombre d'actifs risques a detenir : ""{}""".format(round(phin,4)), font=("Courier",13)).place(x = 10, y = ym)
            if i == 1:
                Label(frameWallet, text ="Nombre d'actifs non risques a detenir : ""{}""".format(round(phi0,4)), font=("Courier",13)).place(x = 10, y = ym)
            if i == 2:
                Label(frameWallet, text ="Valeur du portefeuille: ""{}""".format(round(w,4)), font=("Courier",13)).place(x = 10, y = ym)
            ym = ym + 30
    else:
        phin = (put(a,b,r,K,N-1,0,S0*(1+b)) - put(a,b,r,K,N-1,0,S0*(1+a)))/(S0*(b-a))
        Phin.set(phin)
        phi0 = (put(a,b,r,K,N-1,0,S0*(1+a))*(1+b) - put(a,b,r,K,N-1,0,S0*(1+b))*(1+a))/((b-a)*(1+r)**(n+1))
        Phi0.set(phi0)
        w = phi0 * (1 + r)**(n) + phin * S0
        ym = 20
        for i in range(0,3):
            if i == 0:
                Label(frameWallet, text ="Nombre d'actifs risques a detenir : ""{}""".format(round(phin,4)), font=("Courier",13)).place(x = 10, y = ym)
            if i == 1:
                Label(frameWallet, text ="Nombre d'actifs non risques a detenir : ""{}""".format(round(phi0,4)), font=("Courier",13)).place(x = 10, y = ym)
            if i == 2:
                Label(frameWallet, text ="Valeur du portefeuille: ""{}""".format(round(w,4)), font=("Courier",13)).place(x = 10, y = ym)
            ym = ym + 30
#-------------------------------------------------------------------------------------------------------#
#AFFICHAGE

Window = Tk()
Window.geometry("1080x720")
Window.minsize(1080,720)
Window.maxsize(1080,720)

frameVariables = Frame(Window, width = 350, height = 255, bd = 2, highlightbackground='grey', highlightcolor = 'grey', highlightthickness='1')
frameVariables.place(x=1,y=17)
frameVariables.pack_propagate(False)

#CALL/PUT
frameCall = LabelFrame(Window, width = 700, height = 300, text = 'Call', font=('Courrier', 20), fg = 'black')
frameCall.place(x=360,y=0)
frameCall.pack_propagate(False)

frameCall0 = LabelFrame(frameCall, width = 190, height = 200, text = 'Call0', font=('Courrier', 20), fg = 'black')
frameCall0.place(x=60,y=10)
frameCall0.pack_propagate(False)

frameCall1 = LabelFrame(frameCall, width = 190, height = 200, text = 'Call1', font=('Courrier', 20), fg = 'black')
frameCall1.place(x=260, y=10)
frameCall1.pack_propagate(False)

frameCall2 = LabelFrame(frameCall, width = 190, height = 200, text = 'Call2', font=('Courrier', 20), fg = 'black')
frameCall2.place(x=460,y=10)
frameCall2.pack_propagate(False)

Button(frameCall, text = "Temps suivant", command = Suivant, font=('Courrier', 15)).place(x=220,y=220)
Button(frameCall, text = "Reset", command = Reset, font=('Courrier', 15)).place(x=400,y=220)


#-------------------------------------------------------------------------------------------------------#
#STRATEGIE DE COUVERTURE
frameWallet = LabelFrame(Window, width = 700, height = 350, text = 'Strategie de couverture', font=('Courrier', 20), fg = 'black')
frameWallet.place(x=360,y=320)
frameWallet.pack_propagate(False)

Phin = DoubleVar()
Phin.set(0)

Phi0 = DoubleVar()
Phi0.set(0)

frameInstantn = Frame(Window, width = 700, height = 50)
frameInstantn.place(x=360,y=670)
frameWallet.pack_propagate(False)

Label(frameInstantn, text = "Instant n : ""{}""".format(n), font=('Courrier', 20)).place(x=250,y=0)

#BOUTONS CALL ET PUT
frameCallPut = Frame(Window, width = 350, height = 200)
frameCallPut.place(x=0,y=275)
frameCallPut.pack_propagate(False)

ButtonCall = Button(frameCallPut, text = 'Call', command = ActiveCall, font=('Courrier', 20), width = 15).place(x=50, y=30)
ButtonPut = Button(frameCallPut, text = 'Put', command = ActivePut, font=('Courrier', 20), width = 15).place(x=50, y=100)

#ARBRE PONDERE
frameS = Frame(Window, width = 350, height = 259, bd = 2, highlightbackground='grey', highlightcolor = 'grey', highlightthickness='0.8')
frameS.place(x=1, y = 460)
frameS.pack_propagate(False)

frameArbre = Frame(frameS, width = 90, height = 130)
frameArbre.place(x=100, y = 75)
frameArbre.pack_propagate(False)
canArbre = Canvas(frameArbre)
canArbre.pack()
canArbre.create_line(0,75,90,25,fill='black', width = 3)
canArbre.create_line(0,75,90,125,fill='black', width = 3)

C = IntVar() #Savoir si on se trouve en Call ou Put, C = 1, veut dire qu'on se trouve en Call
C.set(1)

S0 = DoubleVar()
S0.set(100)
S = DoubleVar()
temp = S0.get()
S.set(temp)

a = DoubleVar() 
a.set(-0.01)
b = DoubleVar() 
b.set(0.01)
S11 = DoubleVar()
S11.set((S.get())*(1+ (b.get())))
S12 = DoubleVar()
S12.set(S.get()*(1+ (a.get())))

Sround = DoubleVar()
Sround.set(100)

Label(frameS, text = 'Sn', font=('Courrier', 20)).place(x=20,y=20)
Label(frameS, text = 'S(n+1)', font=('Courrier', 20)).place(x=210,y=20)
ValeurS0 = Label(frameS, textvariable = Sround, font=('Courrier', 20)).place(x=0,y=129)
ValeurS11 = Label(frameS, textvariable = S11, font=('Courrier', 20)).place(x=200,y=75)
ValeurS12 = Label(frameS, textvariable = S12, font=('Courrier', 20)).place(x=200,y=185)

#GESTION VARIABLES
Label(frameVariables,text = "Valeur de a (baisse):", font=("Courier",12)).place(x= 2, y=2)
entree = Entry(frameVariables, textvariable= a, width=10).place(x = 245, y = 6)

Label(frameVariables,text = "Valeur de b (hausse) :", font=("Courier",12)).place(x= 2, y=32)
entree = Entry(frameVariables, textvariable=b, width=10).place(x = 245, y = 36)

r = DoubleVar() 
r.set(0)
Label(frameVariables,text = "Valeur de r :", font=("Courier",12)).place(x= 2, y=62)
entree = Entry(frameVariables, textvariable=r, width=10).place(x = 245, y = 66)

p = DoubleVar() 
p.set(0.3)
Label(frameVariables,text = "Probablilité de baisse :", font=("Courier",12)).place(x= 2, y=92)
entree = Entry(frameVariables, textvariable=p, width=10).place(x = 245, y = 96)

K = DoubleVar() 
K.set(102)
Label(frameVariables,text = "Valeur du strike K :", font=("Courier",12)).place(x= 2, y=122)
entree = Entry(frameVariables, textvariable=K, width=10).place(x = 245, y = 126)

Label(frameVariables,text = "Valeur de S0 :", font=("Courier",12)).place(x= 2, y=152)
entree = Entry(frameVariables, textvariable=S0, width=10).place(x = 245, y = 156)


N0 = IntVar() 
N0.set(5)
N = IntVar()
temp = N0.get()
N.set(temp)
Label(frameVariables,text = "Date d'échéance :", font=("Courier",12)).place(x= 2, y=182)
entree = Entry(frameVariables, textvariable=N0, width=10).place(x = 245, y = 186)

Button(frameVariables, text="Valider",font=("Courier",12), command = valider).place(x = 130, y= 210)
