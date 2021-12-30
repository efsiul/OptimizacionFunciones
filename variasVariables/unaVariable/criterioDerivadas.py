import pandas as pd
import sympy as sp
from sympy import *
from scipy.misc import derivative
from scipy import *
import random


class CriterioDerivadas:
    x=sp.Symbol('x')                                                        #definimos x como simbolo
    absoluto=[]
    
    def __init__(self,fn):
        self.fn=fn
        self.fun = sp.parse_expr(self.fn, evaluate=False)
        
        self.criterioPrimeraDerivada()
        self.criterioSegundaDerivada()
      
        
    f=lambda self, x_: self.fun.subs(self.x, x_)
    
    def criterioPrimeraDerivada(self):
        signos=[] 
        absoluto=[]
        
        dx= Derivative(self.fun,self.x).doit()
        fdx=lambda x_: dx.subs(self.x,x_)   
        criticos=lambda x_: signos.append([x_, " positivo"]) if fdx(x_)>0 else (signos.append([x_, " negativo"]) if fdx(x_)<0  else signos.append([x_, " Es un indeterminado"]))
        
        try:
            cr1=solve(dx)
            j=0
            for i in range(len(cr1)):
                    if 1==len(cr1):
                        criticos(random.randint(int(complex(cr1[i]-100).real), int(complex(cr1[i]).real)))
                        criticos(random.randint(int(complex(cr1[i]).real), int(complex(cr1[i]+100).real)))
                        break
                    elif 2==len(cr1):
                        criticos(random.randint(int(complex(cr1[i]-100).real), int(complex(cr1[i]).real)))
                        criticos(random.uniform((complex(cr1[0]).real), (complex(cr1[1]).real)))
                        criticos(random.randint(int(complex(cr1[i]).real), int(complex(cr1[i]+100).real)))
                        break
                    else:
                        while (j<len(cr1)-1):
                            if i <= len(cr1)-1:
                                if i ==0:
                                    criticos(random.randint(int(complex(cr1[i]-100).real), int(complex(cr1[i]).real)))
                                elif i == len(cr1)-1:
                                    criticos(random.randint(int(complex(cr1[i]).real), int(complex(cr1[i]+100).real)))
                                else:
                                    criticos(random.uniform((complex(cr1[j]).real), (complex(cr1[i]).real)))
                                    j=j+1
                                i=i+1
                            else:
                                break
                        
            signos=sorted(signos)
            i=0
            j=1
            while(i<=len(cr1)-1):
                if ' positivo' in signos[i] and ' negativo' in signos[j]:
                    absoluto.append([cr1[i], 'Es maximo relativo'])
                elif ' negativo' in signos[i] and ' positivo' in signos[j]:
                    absoluto.append([cr1[i], 'Es minimo relativo'])
                i=i+1
                j=i+1
            self.absoluto=absoluto
            
            print('''\n
                  **************************************************************************************
                  ********************************* PRIMERA DERIVADA ***********************************
                  ''')
            print("\n La función es ")
            pprint(self.fun)
            print("\n La primera derivada es ")
            pprint(dx) 
            print("\n Haciendo la primera derivada 0 hallamos a")
            pprint(cr1)
            print("\n signos de la derivada en intervalos")
            pprint(signos)
            print("\n puntos relativos")
            pprint(absoluto)
        
        except NotImplementedError:
            primDeri=derivative(self.f,0, dx=1e-9)
            pprint(primDeri)
                                
    def criterioSegundaDerivada(self):
        
        x=sp.Symbol('x')                                                #definimos x como simbolo
        signos=[]
        
        dxx= Derivative(self.fun,x,x).doit()
        fdxx=lambda x_: dxx.subs(x,x_)
        puntos=lambda x_: signos.append([x_, " Es un minimo"]) if fdxx(x_)>0 else (signos.append([x_, " Es un maximo"]) if fdxx(x_)<0  else signos.append([x_, " Es un indeterminado"]))
        criticos=self.absoluto
        
        try:
            
            inflexion=solve(dxx)
            #inflexion=sorted(inflexion)
            for i in range(len(criticos)):
                puntos(float(complex(criticos[i][0]).real))
                
            print('''\n
                  **************************************************************************************
                  ********************************* SEGUNDA DERIVADA ***********************************
                  ''')
            

            
            print("\n La segunda derivada es ")
            pprint(dxx)

            print("\n Reemplazando los valores de la primmera derivada en la segunda")
            pprint( signos)
            
            print("\n Los puntos de Inflexión son: ")
            pprint(inflexion)
        except NotImplementedError:
            
            segDeri=derivative(fdxx, 0, dx=1e-9)
            pprint(segDeri)
    

    def pintar(self):
        sp.plotting.plot(self.fun, (self.x,-30,30))

        
              
    
     
# f='(x/(x-7)-1/x**2)'
# criterioDerivadas(f)