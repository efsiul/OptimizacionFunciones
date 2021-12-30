from math import *
import sympy as sp
from sympy import *
import pandas as pd

class InterpolacionCuadratica:

    x=sp.Symbol('x')
    resX=0
    resY=0
    df=pd.DataFrame(columns=['val_x0','val_x1','val_x2','result_x3','fx3','error'])

    #Definición de valores iniciales
    def __init__(self,fn):
        self.fn=fn
        self.fun=sp.parse_expr(self.fn, evaluate=False)
        self.val_x0=float(input("indique valor inicial x0 "))
        self.val_x1=float(input("indique valor inicial x1 "))
        self.val_x2=float(input("indique valor inicial x2 "))
        self.interpolacion_cuadratica(self.val_x0,self.val_x1,self.val_x2)
    
    fx=lambda self, x_: self.fun.subs(self.x, x_)

    def cuadratica(self,val_x0,val_x1,val_x2):
        x3= lambda  x0,x1,x2: ((self.fx(x0))*(x1**2 - x2**2)+self.fx(x1)*(x2**2-x0**2)+self.fx(x2)*(x0**2-x1**2))/(2*self.fx(x0)*(x1-x2)+2*self.fx(x1)*(x2-x0)+2*self.fx(x2)*(x0-x1))
        result_x3=x3(val_x0,val_x1,val_x2)
        fx3=self.fx(result_x3)
        return result_x3, fx3



    def interpolacion_cuadratica(self,val_x0,val_x1,val_x2):
        error =abs(val_x2-val_x1)
        tolerancia=0.001

        #Mientras el error sea mayor que la tolerancia
        while(error>tolerancia):
            
            result_x3,fx3=self.cuadratica(val_x0, val_x1, val_x2)
            self.df=self.df.append({'val_x0':val_x0, 'val_x1':val_x1,'val_x2':val_x2,'result_x3':result_x3,'fx3':fx3,'error':error },ignore_index=True)

            
            if (result_x3>val_x1) :
                val_x0= val_x1
                val_x1=result_x3 #ojo
                result_x3,fx3=self.cuadratica(val_x0, val_x1, val_x2)
            
                
            elif(result_x3<val_x1):
                val_x2=val_x1
                val_x1=result_x3
                
            error =abs(val_x2-val_x1)
        self.resX=result_x3
        self.resY=fx3
        return result_x3, fx3
            
    def table(self):        
        print("\n La ecuación es: ")  
        pprint(self.fun)  
        print(f"\n El punto critico lo adquiere cuando x={self.resX} entonces y={self.resY} ")
        print(self.df)
        
        
        
# f='x**5/(x-7)'
# inter=interpolacionCuadratica(f)
            

