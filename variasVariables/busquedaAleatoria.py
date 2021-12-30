import sympy as sp
from sympy.plotting import plot3d
import random as rnd
import pandas as pd

class BusquedaAleatoria():
    x=sp.Symbol('x')    
    y=sp.Symbol('y')   
     
    def __init__(self,fn, lower, up):
        self.fn=fn
        self.fun=sp.parse_expr(self.fn, evaluate=False)
        self.xl=lower
        self.yl=lower
        self.xu=up
        self.yu=up
        # self.xl = float(input("Digite número inferior para x: "))
        # self.xu = float(input("Digite número superior para x: "))  
        # self.yl = float(input("Digite número inferior para y: "))
        # self.yu = float(input("Digite número superior para y: "))  
        self.busquedaAleatoria(self.xl, self.xu, self.yl, self.yu)
        self.graficarFuncion() 

    f= lambda self, x_, y_: self.fun.subs({self.x:x_, self.y:y_})
    
    def busquedaAleatoria(self, xl, xu, yl, yu):
        df=pd.DataFrame(columns=['x','y','fun','maxx','maxy','f(x,y)'])
        n=1500
        
        maxFun=-1e9

        for i in range(n):
            r=rnd.random()
            x=xl+(xu-xl)*r
            y=yl+(yu-yl)*r
            
            fun=self.f(x,y)
            
            if fun> maxFun:
                maxFun=fun
                maxx =x
                maxy=y
            df=df.append({'x':x, 'y':y,'fun':fun,'maxx':maxx,'maxy':maxy,'f(x,y)':maxFun},ignore_index=True)
        print(df)
        
    def graficarFuncion(self):
        x,y=sp.symbols('x y')
        plot3d(self.fun, (x,-30, 30), (y,-30,30))

# f='y-x-2*x**2-2*x*y-y**2'        
# busqueda=busquedaAleatoria(f)
