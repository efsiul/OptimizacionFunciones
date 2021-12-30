import sympy as sp
from sympy.plotting import plot3d
import pandas as pd
from unaVariable import metodoNewton


class MaximaInclinacionLoop():
    
    def __init__(self,fn, x0, y0):
        self.fn=fn
        self.fun=sp.parse_expr(self.fn, evaluate=False)
        self.x0=x0
        self.y0=y0
        # self.x0=(float(input("Indique la posición en x: ")))
        # self.y0=(float(input("Indique la posición en y: ")))
        self.funcionH(self.x0, self.y0, 0)
        self.graficaMaxIn()
        
    x=sp.symbols('x')
    y=sp.symbols('y')
    h=sp.symbols('h')
    salida=[]
    lista=[]
    
    f= lambda self, x_, y_:self.fun.subs({self.x:x_,self.y:y_})
        
    def gradient(self, x, y):
        dx=sp.Derivative(self.fun,self.x,evaluate=True)
        dy=sp.Derivative(self.fun,self.y,evaluate=True)
        
        solverDx=dx.subs({self.x:x, self.y:y})
        solverDy=dy.subs({self.x:x, self.y:y})
        return solverDx, solverDy
    
    def funcionH(self, valorx, valory, iter):
        bandera=5e-10
        bandera1=5e10
                                                #Tomamos los valores de los gradientes
        while bandera!=bandera1:
            dx, dy=self.gradient(valorx, valory)
            
            x=sp.parse_expr((f'{valorx}+({dx})*h'), evaluate=False)                     #generamos la función x con la variable h    
            y=sp.parse_expr((f'{valory}+({dy})*h'), evaluate=False)                     #generamos la función y con la variable h y    
            z=round(complex(self.f(valorx, valory)).real,3)                                           #obtenemos z rredondeado con 8 decimales
            self.salida.append(z)                                                       #llenamos el arreglo salida con la variable Z    
            
            funcionG=(self.f(x,y))                                                      #obtenemos la nueva función con la reemplazando x y y con los valores de la función x y y en función de h    
            
            

            solverDg=sp.solve(funcionG)                                                 #obtenemos el valor de h, igualando la primera derivada a 0    
            funH=str(funcionG)                                                          #Volvemos la función como cadena para poderla pasar al metodo de newton y evaluar            
            
            newton=metodoNewton(funH,self.h)                                            #Instanciamos el metodo de newton para hallar el valor optimo de la funciónH
            h=newton.metodo_newton(complex(solverDg[0]).real)                           #Hallamos el valor de h y f(h) optimizados con el metodo de newton
            
            
            valorx=x.subs(self.h,h[0])                                                  #obtenemos el nuevo valol de x
            valory=y.subs(self.h,h[0])                                                  #obtenemos el nuevo valor de y
            
            dic = {'x':valorx, 'y':valory,'z':z,'h':h[0]}                               #se genera un diccionario para crear el dataset
            self.lista.append(dic)                                                      #se adiciona el diccionario a una lista
            iter+=1                                                                     #Esta variable permite controlar la salida de la recursión
            bandera=self.salida[-1]
            if iter>2:                                                                  #Es necesario que la longtud del arreglo salida sea mayor a 2, iter se encarga de ello    
                bandera1=self.salida[-2]
                if (self.salida[-1]==self.salida[-2]):                                  #Aqui es donde se decide salir de la recursión, cuando se encuentran dos valores iguales al final de la lista salida. 
                    df=pd.DataFrame(self.lista)                                        #se genera el dataframe
                    print(df,"\n")
                    #print(f"El número x {estado} es {valorx}, el número y {estado} es {valory} formando a z igual a {z}")
                    print(f"El número x optimizado es {valorx}, el número y optimizado es {valory} formando a z igual a {z}")
                    return

    def graficaMaxIn(self):
        x,y=sp.symbols('x y')
        plot3d(self.fun, (x,-30, 30), (y,-30,30))



# f='4*x + 2*y + x**2 - 2*x**4 + 2*x*y -3*y**2'
# f='2*x*y+2*y+4*x+x**2-2*x**4-y**2'
# maximaInclinacion(f,0,0)