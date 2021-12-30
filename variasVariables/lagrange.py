import sympy as sp
from sympy.plotting import plot3d
import numpy as np





class Lagrange():

    _x=np.linspace(-5,5,50)
    _y=np.linspace(-5,5,50)  
    
    def __init__(self,fn,gn):
        self.fn=fn
        self.gn=gn
        self.x=sp.symbols('x')
        self.y=sp.symbols('y')
        self.t=sp.symbols('t')
        self.L=(f"{self.fn}+t*({self.gn})")
        self.funf=sp.parse_expr(self.fn, evaluate=False)
        self.fung=sp.parse_expr(self.gn, evaluate=False)
        self.funL=sp.parse_expr(self.L, evaluate=False)
        self.lagrange()
        self.graficaFunciones()
       
        
    f=lambda self, x_,y_: self.funf.subs({self.x:x_, self.y:y_})
    g=lambda self, x_,y_: self.fung.subs({self.x:x_, self.y:y_})
    
    def lagrange(self):
        dx=self.funL.diff(self.x)
        dy=self.funL.diff(self.y)
        dt=self.funL.diff(self.t)
         
        
        resultado=sp.solve([dx,dy,dt])

        valX= [(resultado[i])[self.x] for i in range(len(resultado))]             
        valY= [(resultado[i])[self.y] for i in range(len(resultado))]             
        valT= [float((resultado[i])[self.t]) for i in range(len(resultado))]             
        puntos={f'Punto{round(i,3),round(j,3)}': self.f(i,j) for i in valX for j in valY }
        
        solucion=[{min(puntos.keys()): round(min(puntos.values()),4)},{max(puntos.keys()):round(max(puntos.values()),4)}]
        
        print("\nEcuación 1, derivada parcial con relación a x e igualando a 0")
        sp.pprint(dx)
        print("\nEcuación 2, derivada parcial con relación a y e igualando a 0")
        sp.pprint(dy)
        print("\nEcuación 3, derivada parcial con relación a t e igualando a 0")
        sp.pprint(dt)
        
        print("\nSoluciones para las variables del sistema de ecuaciones: ")
        sp.pprint(resultado)
        
        print('\nvalores para x:')
        sp.pprint(valX)
        
        print('\nvalores para y:')        
        sp.pprint(valY)
        
        print("\nConjuntos de puntos para la solución: ")
        for i in puntos:
            sp.pprint(i)   
        
        print("\nSOLUCIONES OPTIMIZADAS")
        print(f'''
              *********************************************************************
                               MINIMO: {solucion[0]}                              
                               MAXIMO: {solucion[1]}                              
              *********************************************************************
              ''')     
        
    def graficaFunciones(self):
        x,y=sp.symbols('x y')
        sp.plotting.plot3d(self.f(x,y),self.g(x,y), (x,-30, 30), (y,-30,30), show=True)


        
# f='3*x-2*y'
# g='x**2+2*y**2-1'
# lagrange(f,g)
