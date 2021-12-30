import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
from sympy import *


class SeccionDorada:
    
    x=sp.Symbol('x')
    
    def __init__(self, fn):
        self.fn = fn
        self.fun = sp.parse_expr(self.fn, evaluate=False)
        self.xl = float(input("Digite número inferior: "))
        self.xu = float(input("Digite número superior: "))                   
        self.evualucionPuntos(self.xl, self.xu)
    
    f=lambda self, x_: self.fun.subs(self.x, x_)

    def evualucionPuntos(self, xl, xu):
        df=pd.DataFrame(columns=['xl','xu','x1','fx1','x2','fx2','error'])
        error = 1
        tolerancia = 0.01
        while (error > tolerancia):
            
            d = 0.618033988749*(xu-xl)
            x1 = xl+d
            x2 = xu-d

            fx1 = float(self.f(x1))
            fx2 = float(self.f(x2))
            error=abs(x2-x1)
            
            df=df.append({'xl':xl, 'xu':xu,'x1':x1,'fx1':fx1,'x2':x2,'fx2':fx2,'error':error },ignore_index=True)
            #tabla = pd.DataFrame( dict(zip(i, xl,xu,x1,fx1,x2,fx2,self.error)), columns=['Iteracion','xl','xu','x1','fx1','x2','fx2','error'],index=True)
            #tabla= pd.DataFrame(dict(zip(dic)),index=True)
            # tabla.append(dic)
            if (fx2 > fx1):
                xl = xl
                xu = x1
        
            else:
                xu = xu
                xl = x2  
        print("\ La función es ")
        pprint(self.fun)
        print("\n Cuando los valores xl y xu se empiezan a emparejar la función toma valores optimos cuando fx1 y fx2 se emparejan tambien")
        print(df)
        

            



