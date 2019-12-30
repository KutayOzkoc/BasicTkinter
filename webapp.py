import webbrowser

import tkinter as tk


def google():
    webbrowser.open('https://www.google.com/',new = 0,autoraise=True)
def Metaloroji():
    webbrowser.open('https://www.mgm.gov.tr/',new = 0,autoraise=True)
def youtube():
    webbrowser.open('https://www.youtube.com/',new = 0,autoraise=True)
root = tk.Tk()
root.geometry('350x150')
root.title('Browser')
root.configure(background = 'pink')


btn0 = tk.Button(root,text="Google",font=('arial',10,'bold'),width = 10 ,command= google).place(x = 10,y=20)
btn1 = tk.Button(root,text="Metaloriji",font=('arial',10,'bold'),width = 10 ,command= Metaloroji).place(x = 100,y=20)
btn2 = tk.Button(root,text="You Tube",font=('arial',10,'bold'),width = 10 ,command= youtube).place(x = 10,y=50)
root.mainloop()
