from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title("WELCOME TO THE NUMBER SYSTEM")
root.configure(bg='yellow')


 # frame creating
frame1=LabelFrame(root,text="SQURE",padx=50,pady=50,bg='sky blue')
frame1.pack(padx=40,pady=40)
frame2=LabelFrame(root,text="..@..",padx=50,pady=50,bg='light green')
frame2.pack(padx=40,pady=40)



def error():
   root.configure(bg='red')
   messagebox.showerror('WRONG ', '...TRY IN NEXT!...')
   root.configure(bg='yellow')
   
   
   
def cheak(v,squre):
	if(v==squre):
		mai()
	else:
		error()
		mai()
def btn1(p,a,squre):
	p=p*a
	btn1=Button(frame2,text=p,width=5,height=5,bg="green",command=lambda:cheak(p,squre))
	btn1.grid(row=0,column=0)
	 
def btn2(q,a,squre):
	q=q*a
	btn2=Button(frame2,text=q,width=5,height=5,bg="green",command=lambda:cheak(q,squre))
	btn2.grid(row=0,column=1)
def btn3(r,a,squre):
	r=r*a
	btn3=Button(frame2,text=r,width=5,height=5,bg="green",command=lambda:cheak(r,squre))
	btn3.grid(row=1,column=0)
def btn4(s,a,squre):
	s=s*a
	btn4=Button(frame2,text=s,width=5,height=5,bg="green",command=lambda:cheak(s,squre))
	btn4.grid(row=1,column=1)
def mai():
 	x=int(random.randint(1,30))
 	y=int(random.randint(1,30))
 	squre=x*y
 	tex=[x,'*',y]
 	label1=Label(frame1,text=tex,width=5,height=5,bg='sky blue')
 	label1.grid(row=0,column=0)
 	a=int(random.randint(1,4))
 	if(a==1):
 		btn1(x,y,squre)
 		btn2(x-1,y,squre)
 		btn3(x+2,y,squre)
 		btn4(x+1,y,squre)
 	elif(a==2):
 		btn1(x-1,y,squre)
 		btn2(x,y,squre)
 		btn3(x+2,y,squre)
 		btn4(x+1,y,squre)
 	elif(a==3):
 		btn1(x+2,y,squre)
 		btn2(x-1,y,squre)
 		btn3(x,y,squre)
 		btn4(x+1,y,squre)
 		
 	else:
 		btn1(x+1,y,squre)
 		btn2(x-1,y,squre)
 		btn3(x+2,y,squre)
 		btn4(x,y,squre)
mai()
frame2.mainloop()
