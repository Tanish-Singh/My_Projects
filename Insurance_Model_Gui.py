
import joblib
import pandas as pd
import numpy as np

from tkinter import *
from tkinter import messagebox


lo=joblib.load('gender.joblib') 

le=joblib.load('smoker.joblib')

ct=joblib.load('column.joblib')

sc=joblib.load('scaler.joblib')
regressor=joblib.load('regressor.joblib')
def fxn():
    
    data=pd.DataFrame({'age':[e1.get()],'gender':[e2.get()],'bmi':[e4.get()],'children':[e3.get()],'smoker':[e5.get()],'region':[e6.get()]})
    data['gender']=lo.transform(data['gender'])
    data['smoker']=le.transform(data['smoker'])
    data=ct.transform(data)
    data=sc.transform(data)
    messagebox.showinfo('Answer',regressor.predict(data))


root=Tk()
root.geometry('300x300')

Label(root,text='Age').place(x=10,y=50)
e1=Entry(root,width=10)
e1.place(x=50,y=50)


Label(root,text='Gender').place(x=10,y=100)
e2=Entry(root,width=10)
e2.place(x=50,y=100)

Label(root,text='Children').place(x=10,y=150)
e3=Entry(root,width=10)
e3.place(x=50,y=150)


Label(root,text='BMI').place(x=10,y=200)
e4=Entry(root,width=10)
e4.place(x=50,y=200)



Label(root,text='Smoker').place(x=10,y=250)
e5=Entry(root,width=10)
e5.place(x=50,y=250)


Label(root,text='Region').place(x=10,y=300)
e6=Entry(root,width=10)
e6.place(x=50,y=300)

btn=Button(root,text='Submit',command=fxn)
btn.place(x=150,y=150)


root.mainloop()
