import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd
import sympy as  sp
from sympy import * 


class graphicFunction:
    
    def __init__(self, fn):
        self.fn=fn
        #self.x_ = np.array([-2, -1, 0, 2, 4, 6])  # Creando el vector de valores de x
        self.x_= np.linspace(-30, 30, num=800)
        self.fun=sp.parse_expr(self.fn,evaluate=False)
        self.fix, self.ax = plt.subplots()


        

    def f(self,x_):
        x=sp.Symbol('x')
        y = np.fromiter( (self.fun.subs( {x:i} ) for i in x_), dtype="complex" )
        return y
    
    #Construyendo la tabla de valores
    def table(self):
        y = self.f(self.x_)
        tabla = pd.DataFrame( list(zip(self.x_, y)), columns=['x', 'f(x)'])
        print(tabla)


    #Construyendo la Gráfica
    def move_spines(self):
        """Esta funcion divide pone al eje y en el valor 
        0 de x para dividir claramente los valores positivos y
        negativos."""
        
        for spine in ["left", "bottom"]:
            self.ax.spines[spine].set_position("zero")
        
        for spine in ["right", "top"]:
            self.ax.spines[spine].set_color("none")
        return self.ax

    def pintar(self):
        #self.f= sp.symbols('self.f', cls=Function)
        self.ax = self.move_spines()
        self.ax.grid()
        self.ax.plot(self.x_, self.f(self.x_))
        plt.title(r"Grafico de $f(x)=$"+self.fn)
        plt.ylabel('f(x)')
        plt.xlabel('x')
        return plt.show()
    
    def pintar2(self):
        x = np.linspace(-20,20, num=500)
        plt.plot(x, self.f(x))
        return plt.show()
    
    def pintar3(self):
        fig = plt.figure(figsize=(8,6))
        ax3d = plt.axes(projection="3d")

        xdata = np.linspace(-3,3,100)
        ydata = np.linspace(-3,3,100)
        X,Y = np.meshgrid(xdata,ydata)
        Z = self.f(X,Y)

        ax3d = plt.axes(projection='3d')
        surf=ax3d.plot_surface(X, Y, Z, rstride=7, cstride=7, cmap="viridis")
        fig.colorbar(surf, ax=ax3d)
        ax3d.set_title('Surface Plot in Matplotlib')
        ax3d.set_xlabel('X')
        ax3d.set_ylabel('Y')
        ax3d.set_zlabel('Z')

        plt.savefig("Customized Surface Plot.png")

        return plt.show()
