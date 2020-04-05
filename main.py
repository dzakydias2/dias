import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from sympy import *
import sympy as sym
import numpy as np
from scipy import optimize
from sympy.utilities.lambdify import lambdify




class Mygrid(GridLayout):
    def __init__(self, **kwargs):
        super(Mygrid, self).__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text="xkuadrat: "))
        self.x1kuadrat = TextInput(multiline=False)
        self.add_widget(self.x1kuadrat)
        
        self.add_widget(Label(text="x: "))
        self.x1 = TextInput(multiline=False)
        self.add_widget(self.x1)
        
        self.add_widget(Label(text="c: "))
        self.c1 = TextInput(multiline=False)
        self.add_widget(self.c1)
        
        self.add_widget(Label(text="ykuadrat: "))
        self.y1kuadrat = TextInput(multiline=False)
        self.add_widget(self.y1kuadrat)
        
        self.add_widget(Label(text="y: "))
        self.y1 = TextInput(multiline=False)
        self.add_widget(self.y1)
        
        self.add_widget(Label(text="c: "))
        self.cy1 = TextInput(multiline=False)
        self.add_widget(self.cy1)
        
        self.add_widget(Label(text="x*y: "))
        self.xy1= TextInput(multiline=False)
        self.add_widget(self.xy1)
        
        self.add_widget(Label(text="xkuadrat: "))
        self.x2kuadrat = TextInput(multiline=False)
        self.add_widget(self.x2kuadrat)
        
        self.add_widget(Label(text="x: "))
        self.x2 = TextInput(multiline=False)
        self.add_widget(self.x2)
        
        self.add_widget(Label(text="c: "))
        self.c2 = TextInput(multiline=False)
        self.add_widget(self.c2)

        self.add_widget(Label(text="ykuadrat: "))
        self.y2kuadrat = TextInput(multiline=False)
        self.add_widget(self.y2kuadrat)
        
        self.add_widget(Label(text="y: "))
        self.y2 = TextInput(multiline=False)
        self.add_widget(self.y2)
        
        self.add_widget(Label(text="c: "))
        self.cy2 = TextInput(multiline=False)
        self.add_widget(self.cy2)
        
        self.add_widget(Label(text="x*y: "))
        self.xy2 = TextInput(multiline=False)
        self.add_widget(self.xy2)

        

        
        self.sub = Button(text="Calculate", font_size=20)
        self.sub.bind(on_press=self.tekan)
        self.add_widget(self.sub)

    def tekan(self,instance):
        x, y,d = symbols("x y d")
        a=float(self.x1kuadrat.text)
        b=float(self.x1.text)
        c=float(self.c1.text)
        ay=float(self.y1kuadrat.text)
        by=float(self.y1.text)
        cy=float(self.cy1.text)
        ap=float(self.x2kuadrat.text)
        bp=float(self.x2.text)
        cp=float(self.c2.text)
        apy=float(self.y2kuadrat.text)
        bpy=float(self.y2.text)
        cpy=float(self.cy2.text)
        gt1=float(self.xy1.text)
        gt2=float(self.xy2.text)
        
        m=np.array([a,b,c])
        my=np.array([ay,by,cy])
        mp=np.array([ap,bp,cp])
        mpy=np.array([apy,bpy,cpy])
        f= np.array([[x**2],[x],[1]])
        f1= np.array([[y**2],[y],[1]])
        fx=np.dot(m,f)
        fy=np.dot(my,f1)
        fxp=np.dot(mp,f)
        fyp=np.dot(mpy,f1)

        palsu=fxp+fyp+gt2*x*y
        asli=fx+fy+gt1*x*y
        fakhir=asli+palsu*d
        fx1=diff(fakhir,x)
        fy1=diff(fakhir,y)
        fd1=diff(fakhir,d)
        f11=diff(fx1,x)
        f12=diff(fx1,y)
        f21=diff(fy1,x)
        f22=diff(fy1,y)

        dt=np.dot(f11,f22)-np.dot(f12,f21)
        x0=[0,0,0]

        sol = nsolve((fx1,fy1,fd1),(x,y,d),x0)
        print([round(i,3) for i in sol])
        la = lambdify([x,y],asli)
        fval = la(sol[0],sol[1])
        print(fval)
        
        self.add_widget(Label(text=str(sol)))
        self.add_widget(Label(text=str(fval)))
        if dt > 0:
            if f11> 0:
                self.add_widget(Label(text="Minimum"))
            else:
                self.add_widget(Label(text="Maksimum"))
        else:
            self.add_widget(Label(text="Saddle"))
class MyApp(App):
    def build(self):
        return Mygrid()

if __name__ == "__main__":
    MyApp().run()