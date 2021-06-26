# Calculator
# Imtiaz Adar

from tkinter import *
from math import sqrt
from math import pow

# setting
expression = ""
root = Tk()
app_height = 700
app_width = 500
x = 500
y = 40
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
# pic = PhotoImage(file='maths.png')
# # # root.tk.call('wm', 'iconphoto', root._w, pic)
# root.iconphoto(False, pic)
root.iconbitmap('calicon.ico')
root.title('Calculator By Imtiaz Adar')
root.configure(background='white')


# working on buttons
def button_clicked(element):
    global expression
    expression = expression + str(element)
    equation.set(expression)

def clear():
    global expression
    expression = ''
    equation.set('')

def button_equal():
    global expression
    try:
        if 'sqrt' in expression:
            ans = expression.split('sqrt')
            ans2 = ans[1]
            ans3 = sqrt(float(ans2))
            equation.set(str(ans3))
            expression = ''
        elif '^' in expression:
            res = expression.split('^')
            res1 = res[0]
            res2 = res[1]
            res3 = pow((float(res1)),(float(res2)))
            equation.set(res3)
            expression = ''
        else:
            answer = str(eval(expression))
            equation.set(answer)
            expression = ''
    except:
        equation.set('Error! Try Again')
        expression = ''

def percent():
    global expression
    ans = str(eval(expression))
    ans2 = int(ans)/100
    equation.set(str(ans2))
    expression = ''

def button_del():
    global expression
    expression = expression[0:-1]
    equation.set(expression)

def turn_on():
    button_1.configure(state=NORMAL)
    button_2.configure(state=NORMAL)
    button_3.configure(state=NORMAL)
    button_4.configure(state=NORMAL)
    button_5.configure(state=NORMAL)
    button_6.configure(state=NORMAL)
    button_7.configure(state=NORMAL)
    button_8.configure(state=NORMAL)
    button_9.configure(state=NORMAL)
    button_0.configure(state=NORMAL)
    button_eq.configure(state=NORMAL)
    button_plus.configure(state=NORMAL)
    button_mul.configure(state=NORMAL)
    button_min.configure(state=NORMAL)
    button_per.configure(state=NORMAL)
    button_dot.configure(state=NORMAL)
    button_c.configure(state=NORMAL)
    button_dell.configure(state=NORMAL)
    button_div.configure(state=NORMAL)
    button_sq.configure(state=NORMAL)
    button_r.configure(state=NORMAL)
    off.configure(state=NORMAL)
    text.configure(state=NORMAL)
    info.configure(state=NORMAL)
    name_label.configure(state=NORMAL)


def turn_off():
    button_1.configure(state=DISABLED)
    button_2.configure(state=DISABLED)
    button_3.configure(state=DISABLED)
    button_4.configure(state=DISABLED)
    button_5.configure(state=DISABLED)
    button_6.configure(state=DISABLED)
    button_7.configure(state=DISABLED)
    button_8.configure(state=DISABLED)
    button_9.configure(state=DISABLED)
    button_0.configure(state=DISABLED)
    button_eq.configure(state=DISABLED)
    button_plus.configure(state=DISABLED)
    button_mul.configure(state=DISABLED)
    button_min.configure(state=DISABLED)
    button_per.configure(state=DISABLED)
    button_dot.configure(state=DISABLED)
    button_c.configure(state=DISABLED)
    button_dell.configure(state=DISABLED)
    button_div.configure(state=DISABLED)
    button_sq.configure(state=DISABLED)
    button_r.configure(state=DISABLED)
    off.configure(state=DISABLED)
    text.configure(state=DISABLED)
    info.configure(state=DISABLED)
    name_label.configure(state=DISABLED)


equation = StringVar()

# colors
color = "#0C5C3A"
color_comm = "#404040"
color_1 = "#202020"
color_2 = "#127D61"
color_3 = "#660033"
color_4 = "#E0E0E0"
color_5 = "#FFFF00"
color_6 = "#330066"

# text field
text = Entry(root, textvariable=equation, bg=color_4, width=30, cursor='spider', borderwidth=5, font='Lucida 20 bold', justify='right', state=DISABLED)
text.bind('<Key>', lambda e: "break")
text.grid(row=0, column=0, columnspan=4, padx=20, pady=20,ipady=20)


# radio button
on = Radiobutton(root, text='ON', bg=color_2,fg='white', font=("Arial",10,"bold"), padx=22, pady=10, command=lambda:turn_on(),
                  activebackground='white', activeforeground='green', bd=4, cursor='spider')
on.place(x=285,y=117)

off = Radiobutton(root, text='OFF', bg=color_2,fg='white', font=("Arial",10,"bold"), padx=20, pady=10,
                  command=lambda:turn_off(), activebackground='white', activeforeground='green', bd=4,
                  state=DISABLED, cursor='spider')
off.place(x=380, y=117)


# setting buttons
button_7 = Button(root, text='7', padx=26,  pady=20, bg=color_comm, fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked(7))
button_7.place(x=21,y=180)

button_8 = Button(root, text='8', padx=26,  pady=20, bg=color_comm, fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked(8))
button_8.place(x=112,y=180)

button_9 = Button(root, text='9', padx=26,  pady=20, bg=color_comm, fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked(9))
button_9.place(x=203,y=180)

button_mul = Button(root, text='x', padx=28,  pady=22, bg=color_1, fg="white", state=DISABLED, font=("Arial",19,"bold"),
          activebackground=color_3, activeforeground="white",bd=2, cursor='spider', command=lambda:button_clicked('*'))
button_mul.place(x=294,y=273)

button_r = Button(root, text='√', padx=26,  pady=20, bg=color_1, fg="white", state=DISABLED, font=("lucida",20,"bold"),
          activebackground=color_3, activeforeground="white",bd=2, cursor='spider', command=lambda:button_clicked('sqrt '))
button_r.place(x=385,y=180)

button_4 = Button(root, text='4', padx=26,  pady=20, bg=color_comm, fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground=color_3, activeforeground="white", bd=2, cursor='spider', command=lambda:button_clicked(4))
button_4.place(x=21,y=274)

button_5 = Button(root, text='5', padx=26,  pady=20, bg=color_comm, fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked(5))
button_5.place(x=112,y=274)

button_6 = Button(root, text='6', padx=26,  pady=20, bg=color_comm, fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked(6))
button_6.place(x=203,y=274)

button_min = Button(root, text='-', padx=30,  pady=17, bg=color_1, fg="white", state=DISABLED, font=("calibri",21,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked('-'))
button_min.place(x=294,y=368)

button_per = Button(root, text='%', padx=26, pady=22, bg=color_1, fg="white", state=DISABLED, font=("lucida",19,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:percent())
button_per.place(x=385,y=274)

button_1 = Button(root, text='1', padx=26,  pady=20, bg=color_comm, fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked(1))
button_1.place(x=21,y=368)

button_2 = Button(root, text='2', padx=26,  pady=20, bg=color_comm, fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked(2))
button_2.place(x=112,y=368)

button_3 = Button(root, text='3', padx=26,  pady=20, bg=color_comm, fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked(3))
button_3.place(x=203,y=368)

button_div = Button(root, text='/', padx=32,  pady=22, bg=color_1, fg="white", state=DISABLED, font=("Arial",19,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked('/'))
button_div.place(x=293,y=461)

button_0 = Button(root, text='0', padx=26,  pady=20, bg=color_comm, fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked(0))
button_0.place(x=112,y=462)

button_sq = Button(root, text='^', padx=30,  pady=27, bg=color_comm, fg="white", state=DISABLED, font=("Arial",16,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked('^'))
button_sq.place(x=203,y=462)

button_dot = Button(root, text='.', padx=29,  pady=18, bg=color_comm, fg="white", state=DISABLED, font=("Arial",22,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=2, command=lambda:button_clicked('.'))
button_dot.place(x=21,y=462)

button_c = Button(root, text='C', padx=114,  pady=21, bg="#B72730", fg="white", state=DISABLED, font=("Arial",20,"bold"),
          activebackground='white', activeforeground='#B72730', cursor='spider', bd=2, command=lambda:clear())
button_c.place(x=21,y=556)

button_eq = Button(root, text='=', padx=31,  pady=116, bg=color, fg="white", state=DISABLED, font=("calibri",19,"bold"),
          activebackground='white', activeforeground=color, cursor='spider', bd=2, command=lambda:button_equal())
button_eq.place(x=384,y=368)

button_plus = Button(root, text='+', padx=29,  pady=23, bg=color_1, fg="white", state=DISABLED, font=("times new roman",19,"bold"),
          activebackground=color_3, activeforeground="white", cursor='spider', bd=1, command=lambda:button_clicked('+'))
button_plus.place(x=294,y=180)

button_dell = Button(root, text='DEL', padx=17, pady= 29, bg=color_3, fg='white', state=DISABLED, font=("times new roman",16,"bold"),
                    activebackground='white', activeforeground=color_3, cursor='spider', bd=1, command=lambda: button_del())
button_dell.place(x=293, y=556)
info = Radiobutton(root, text='INFO', bg='#4C0099', fg='white', font=("Arial",10,"bold"), padx=25, pady=2,
                  command=lambda: second_window(), activebackground='white', activeforeground='#4C0099', bd=4,
                  state=DISABLED, cursor='spider')
info.place(x=364, y=660)


# last label
name_label = Label(root, text='Calculator By Imtiaz Adar', fg='#4C0099', bg='white', state=DISABLED, font=('times new roman', 20, 'bold'))
name_label.place(x=19, y=656)
root.resizable(0, 0)


# new window
def second_window():
    s_window = Toplevel(root)
    app_height1 = 700
    app_width1 = 500
    x1 = 500
    y1 = 40
    s_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    s_window.title('Calculator By Imtiaz Adar')
    s_window.iconbitmap('calicon.ico')
    s_window.configure(background=color_3)
    s_window.resizable(0, 0)

    def button_b():
        button_e.after(1000, s_window.destroy())
    def button_ee():
        button_e.after(1, s_window.destroy())
        root.destroy()

    s = "Imtiaz Adar is a Bangladeshi Computer Programmer.\nHe is the father of this Calculator.\n Follow him on : \n" \
        "Facebook : /@imtiazaadar\nTwitter : /@imtiazaadar\nInstagram : /@imtiaz_adar\nSoundCloud : /imtiazadar\n" \
        "His Contact Info : \nPhone : +8801778-767775\nEmail : imtiaz-adar@hotmail.com"
    my_label = Label(s_window, text=s, bg='white', fg=color_3, font=('lucida', 13, 'bold'), justify='center', relief=SUNKEN)
    my_label.place(x=42, y=215)
    button = Button(s_window, text='BACK', bg=color_1, fg="white", bd=5,
                      font=("lucida", 20, "bold"),
                      activebackground="white", activeforeground=color_1, cursor='spider',
                      command=lambda: button_b())
    button.place(x=145, y=500)
    button_e = Button(s_window, text='EXIT', bd=5, bg=color_1, fg="white",
                      font=("lucida", 20, "bold"),
                      activebackground="white", padx=8, activeforeground=color_1, cursor='spider',
                      command=lambda: button_ee())
    button_e.place(x=256, y=500)
root.mainloop()