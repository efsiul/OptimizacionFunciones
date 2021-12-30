import numpy as np
import pandas as pd
import sympy as sp
from sympy import *


class MetodoBiseccion():
    
    x=sp.Symbol('x')
    def __init__(self, fn):
        self.fn=fn
        self.fun = sp.parse_expr(self.fn, evaluate=False)
        self.xl = float(input("Digite número inferior, debe ser diferente de 0: "))
        self.xu = float(input("Digite número superior, debe ser diferente de 0: "))                   
        self.metodo_Biseccion(self.xl, self.xu)

    f=lambda self, x_: self.fun.subs(self.x, x_)

    def metodo_Biseccion(self,xl, xu):
        df=pd.DataFrame(columns=['n','xl','xu','xr','f(xl)','f(xr)','multipliación', 'error'])
        n=50
        error=1
        xr=(xl+xu)/2
        tolerancia=0.01
        for i in range(n):
            error=abs((xl-xu)/(2**i))
            mul=(self.f(xl)*self.f(xr))
            df=df.append({'n':i,'xl':xl, 'xu':xu,'xr':xr,'f(xl)':self.f(xl),'f(xr)':self.f(xr), 'multipliación':mul, 'error':error },ignore_index=True)
            if mul<0:
                xu=xr
                xr = (xl+xu)/2
            elif mul>0:
                xl=xr
                xr = (xl+xu)/2
            else:
                break
            
        print("\n La Ecuación es: ")
        pprint(self.fun)
        print("\n Los interceptos con el eje x en la función equivalen al valor que toma finalmente xr")
        print(df)


# f='3*x**2-120*x+100'
# metodoBiseccion(f)