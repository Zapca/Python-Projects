import tkinter as tk

root=tk.Tk()

root.title('IDK')
root.geometry('800x500')

label=tk.Label(root,text='Hello!',font=('times new roman',14,'bold'))
label.pack(pady=10)

# text=tk.Text(root,height=15,font=('times new roman',14,'bold'))
# text.pack(padx=5)

buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

btn1=tk.Button(buttonframe,text=1,font=('times new roman',14,'bold'))
btn1.grid(column=0,row=0,sticky=tk.W+tk.E)

btn1=tk.Button(buttonframe,text=2,font=('times new roman',14,'bold'))
btn1.grid(column=1,row=0,sticky=tk.W+tk.E)

btn1=tk.Button(buttonframe,text=3,font=('times new roman',14,'bold'))
btn1.grid(column=2,row=0,sticky=tk.W+tk.E)

btn1=tk.Button(buttonframe,text=4,font=('times new roman',14,'bold'))
btn1.grid(column=0,row=1,sticky=tk.W+tk.E)

btn1=tk.Button(buttonframe,text=5,font=('times new roman',14,'bold'))
btn1.grid(column=1,row=1,sticky=tk.W+tk.E)

btn1=tk.Button(buttonframe,text=6,font=('times new roman',14,'bold'))
btn1.grid(column=2,row=1,sticky=tk.W+tk.E)

btn1=tk.Button(buttonframe,text=7,font=('times new roman',14,'bold'))
btn1.grid(column=0,row=2,sticky=tk.W+tk.E)

btn1=tk.Button(buttonframe,text=8,font=('times new roman',14,'bold'))
btn1.grid(column=1,row=2,sticky=tk.W+tk.E)

btn1=tk.Button(buttonframe,text=9,font=('times new roman',14,'bold'))
btn1.grid(column=2,row=2,sticky=tk.W+tk.E)

button=tk.Button(buttonframe,text='Enter',font=('times new roman',14,'bold'))
button.grid(row=3,column=1,sticky=tk.W+tk.E,pady=10)

buttonframe.pack(fill='x')

entry=tk.Entry(root)
entry.place(x=5,y=400,height=20,width=100)

btn=tk.Button(root,text='Enter',font=('times new roman',14,'bold'))
btn.place(x=23,y=425,height=20,width=55)



root.mainloop()

