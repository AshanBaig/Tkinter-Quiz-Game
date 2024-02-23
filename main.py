import random
from tkinter import Tk,PhotoImage,Label,Button,Frame
import time
r=Tk()
r.title('Quiz')
r.geometry('1000x560+0+0')
r.resizable(False,False)
p=PhotoImage(file='bg_Quiz.png')
l_pic=Label(r,image=p,width=996,height=577)
l_pic.pack(anchor='nw')
used50_50,usedhelp=True,True
gk_questions = [    "What is the capital \nof France?",    "Who wrote 'To Kill a \nMockingbird'?",    "Which planet is known as \nthe Red Planet?",    "What is the currency of \n Japan?",    "Who painted the Mona Lisa?",    "Which country is known as \nthe Land of the Rising Sun?",    "What is the tallest mountain \nin the world?",    "Who was the first President of \nthe United States?",    "What is the chemical symbol \nfor water?",    "What is the largest mammal \nin the world?"]
options = [    ['a. Paris', 'b. Rome', 'c. Berlin', 'd. Madrid'],
    ['a. Harper Lee', 'b. J.K. Rowling', 'c. Ernest Hemingway', 'd. Charles Dickens'],
    ['a. Venus', 'b. Mars', 'c. Jupiter', 'd. Saturn'],
    ['a. Yen', 'b. Euro', 'c. Dollar', 'd. Peso'],
    ['a. Leonardo da Vinci', 'b. Michelangelo', 'c. Pablo Picasso', 'd. Vincent van Gogh'],
    ['a. China', 'b. Japan', 'c. Australia', 'd. India'],
    ['a. Mount Kilimanjaro', 'b. Mount Everest', 'c. K2', 'd. Denali'],
    ['a. Abraham Lincoln', 'b. George Washington', 'c. Thomas Jefferson', 'd. John Adams'],
    ['a. H2O', 'b. CO2', 'c. NaCl', 'd. CaCO3'],
    ['a. Elephant', 'b. Blue whale', 'c. Giraffe', 'd. Hippopotamus']]
correct_options = ['a', 'a', 'b', 'a', 'a', 'b', 'b', 'b', 'a', 'b']
money=[1000,2000,5000,10000,250000,1000000,3200000,7200000,35000000,70000000]
reversed_money=money[::-1]
i=0
earned_money=0
select_wrong=0
s=set()    
def button():
    global b1,b2,b3,b4
    b1=Button(r,text=options[i][0],fg='white',bg='black',width=29,height=2,command=choice1)
    b1.place(x=273-44,y=390-34)
    b2=Button(r,text=options[i][1],fg='white',bg='black',width=29,height=2,command=choice2)
    b2.place(x=535-58,y=390-34)
    b3=Button(r,text=options[i][2],fg='white',bg='black',width=29,height=2,command=choice3)
    b3.place(x=273-44,y=460-44)
    b4=Button(r,text=options[i][3],fg='white',bg='black',width=29,height=2,command=choice4)
    b4.place(x=535-58,y=460-44)
def button50_50():
    global used50_50,s
    used50_50=False
    default_options=['a','b','c','d']
    default_options.remove(correct_options[i])
    while True:    
        s.update({random.choice(default_options)})
        if len(s)==2:
             break 
    for K in s:
        if K=='a':
            b1.destroy()
        elif K=='b':
            b2.destroy()
        elif K=='c':
            b3.destroy()
        elif K=='d':
            b4.destroy()     
    fun5050()
def button_help():
    #Help option
    global usedhelp,s
    usedhelp=False
    default_options=['a','b','c','d']
    default_options.remove(correct_options[i])
    #s.update({random.choice(default_options)})
    remove1=random.choice(default_options)
    if remove1=='a':
        b1.destroy()
    elif remove1=='b':    
        b2.destroy()
    elif remove1=='c':
         b3.destroy()
    elif remove1=='d':
         b4.destroy()
    funhelp()
def funquit():
    result()
def correct():
    global s,a,earned_money
    # if a==1:
    #     button()
    #     a=0
    #Help option
    # if 'a' not in s:
    #     b1.destroy()
    # elif 'b' not in s:    
    #     b2.destroy()        
    # elif 'c' not in s:
    #     b3.destroy()
    # elif 'd' not in s:
    #     b4.destroy()
    if 'a' not in s:
        b1.destroy()
    if 'b' not in s:    
        b2.destroy()     
    if 'c' not in s:
        b3.destroy()
    if 'd' not in s:
        b4.destroy()
    s=set()
    if i==3:
        earned_money=10000
    elif i==7:
        earned_money=7200000
    elif i==9:
         earned_money=70000000 
def wrong():
    global select_wrong
    select_wrong=1
    # print_money()
    r.destroy()
    r1=Tk()
    r1.title('Result')
    r1.geometry('1000x560+0+0')
    r1.resizable(False,False)
    print(1)
    p=PhotoImage(file='bg_score.png')
    l_pic=Label(r1,image=p,width=996,height=577)
    l_pic.pack(anchor='nw')
    l=Label(r1,text='opss WRONG ANSWER',bg='black',fg='white',font='Arial 30 bold').place(x=180,y=200)
    l1=Label(r1,text='Better Luck Next Time',bg='black',fg='white',font='Arial 30 bold').place(x=180,y=280)
    def exit_r1():
            exit()
    
    #b=Button(r1,text='PLAY AGAIN',bg='black',fg='white',font=('Halvetika 20 bold'),command=open('kbc.exe'),width=20,height=2)
    #b.place(x=70+52,y=290+150-20)
    b1=Button(r1,text='Exit',bg='black',fg='white',font=('Halvetika 20 bold'),command=exit_r1,width=20,height=2)
    b1.place(x=170+172+200,y=290+150-20)
    r1.mainloop()
def choice1():
    if correct_options[i] not in s:    
        if correct_options[i]=='a':
            correct()
        else:
            wrong()
        score()
def choice2():
    if correct_options[i] not in s:    
        if correct_options[i]=='b':
            correct()
        else:
             wrong()
        score()
def choice3():
    if correct_options[i] not in s:    
        if correct_options[i]=='c':
            correct()
        else:
             wrong()
        score()
def choice4():
    if correct_options[i] not in s:    
        if correct_options[i]=='d':
            correct()
        else:
             wrong()
        score()
def score():
        global i
        label_S=Label(r,text=f'{money[i]}',fg='white',bg='black',font='arial,8,bold')
        label_S.place(x=755,y=99)
        if i<len(gk_questions)-1:
            i+=1
            show_question()
        else:
            result()
def print_money():
    global label_money
    f1=Frame(r,bg='gray')
    for o in range(len(money)-1,-1,-1):
        label_money=Label(f1,text=money[o],font='Halvetica 13 bold',fg='white',bg='black',width=11)
        # if select_wrong==1 and o==i:
        #     label_money.config(bg='red')
        #     r.update()
        #     time.sleep(2)
        #     r.destroy()
        if i==o:
            label_money.configure(bg='yellow')
        if o==3 or o==7 or o==9:
            label_money.configure(borderwidth=10,highlightthickness=0,relief='raised')
        if earned_money==10000 and o==3:
            label_money.configure(bg='green')
        elif earned_money==7200000 and o==7:
            label_money.configure(bg='green')
        elif earned_money==70000000:
            label_money.configure(bg='green')
        label_money.pack()
    f1.place(x=722,y=173)
def show_question():
    left_frame=Frame(r,bg='black',width=2)    
    left_text=Label(left_frame,text='Kon Banega \nCrorepati',bg='black',fg='pink',font=('comfortaa 10 bold'),height=4,width=14).pack()
    left_frame.place(x=728,y=79)
    label_Q=Label(r,text=gk_questions[i],fg='white',bg='black',font='helvetica 20 bold',width=26,height=4)
    label_Q.place(x=230,y=190)
    button()
    print_money()
    if i ==0:
        fun5050()
        funhelp()
        funexit()
    r.mainloop()
def fun5050():
    global button50
    if used50_50==True:
        button50=Button(text='50/50',font='Halvetica 12 bold',bg='black',fg='pink',activebackground='green',command=button50_50,width=13,height=3)
        button50.place(x=210-1,y=86)
    else:
        button50.destroy()
def funhelp():
    global buttonHelp
    if usedhelp==True:
        buttonHelp=Button(text='Help!',font='Halvetica 12 bold',bg='black',fg='pink',activebackground='green',command=button_help,width=13,height=3)
        buttonHelp.place(x=210+174,y=86-1)
    else:
        buttonHelp.destroy()
def funexit():
    buttonQuit=Button(text='Quit',font='Halvetica 12 bold',bg='black',fg='pink',activebackground='green',command=funquit,width=13,height=3).place(x=210+166+174,y=86-1)
#func me isko config kr ke remove krna hyyy
def result():
    r.destroy()
    r1=Tk()
    r1.title('Result')
    r1.geometry('1000x560+0+0')
    r1.resizable(False,False)
    p=PhotoImage(file='bg_score.png')
    l_pic=Label(r1,image=p,width=996,height=577)
    l_pic.pack(anchor='nw')
    l=Label(text=f'Earned Money:Rs. {earned_money }',bg='black',fg='white',font='Arial 30 bold').place(x=180,y=200)
    if earned_money==0:
        l=Label(text=f'Better Luck Next Time',bg='black',fg='white',font='Arial 30 bold').place(x=180,y=280)
    elif earned_money==10000:
        l=Label(text="Best of Luck",bg='black',fg='white',font='Arial 30 bold').place(x=180,y=280) 
    elif earned_money==7200000:
        l=Label(text="Impressive",bg='black',fg='white',font='Arial 30 bold').place(x=180,y=280) 
    elif earned_money==70000000:
        l=Label(text="Congratulationsss !!",bg='black',fg='white',font='Arial 30 bold').place(x=180,y=280) 
    def exit_r1():
            r1.destroy()
    
    #b=Button(r1,text='PLAY AGAIN',bg='black',fg='white',font=('Halvetika 20 bold'),command=open('kbc.exe'),width=20,height=2)
    #b.place(x=70+52,y=290+150-20)
    b1=Button(r1,text='Exit',bg='black',fg='white',font=('Halvetika 20 bold'),command=exit_r1,width=20,height=2)
    b1.place(x=170+172+200,y=290+150-20)
    r1.mainloop()

show_question()
