import pandas as pd
import sympy as sp
from sympy import *
from scipy import *



class MetodoNewton():
    
    resX=0
    resY=0
    
    def __init__(self,fn, var0):
        self.fn=fn
        self.var0=var0
        self.df=pd.DataFrame(columns=['x ','f(x)','df(x)','ddf(x)','error'])

        self.fun = sp.parse_expr(self.fn, evaluate=False)
        self.dx= Derivative(self.fun,self.var0).doit()
        self.dxx= Derivative(self.fun,self.var0,self.var0).doit()
        
        
        init_printing()

    f=lambda self, x_: self.fun.subs(self.var0, x_)
    fdx=lambda self, x_:self.dx.subs(self.var0, x_)
    fdxx=lambda self, x_:self.dxx.subs(self.var0, x_)
    


    def metodo_newton(self, x):
        error = 1
        tolerancia = 0.000001
        while (error > tolerancia):
            fx=self.f(x)
            dx=self.fdx(x)
            dxx=self.fdxx(x)

            
            x1=x-(dx/dxx)
            error=abs(x-x1)
            x=x1
            self.df=self.df.append({'x':x,'f(x)':fx,'df(x)':dx,'ddf(x)':dxx,'error':error },ignore_index=True)
        self.resX=x
        self.resY=fx
        return x, fx
    
    def table(self):
        print("\n La ecuación es: ")   
        pprint(self.fun)
        print(f"\n Cuando la función toma el valor de x={self.resX}, el punto optimo es y={self.resY}") 
        print(self.df) 

# h = sp.Symbol('h')
# x0 = float(input("Digite número con que empieza: "))
# f='3*h**4-5*h**3+4'
# metNew=metodoNewton(f,h)
# print(metNew.metodo_newton(x0))
# metNew.table()