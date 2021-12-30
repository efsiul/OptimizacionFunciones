from variasVariables.unaVariable.criterioDerivadas import CriterioDerivadas
from variasVariables.unaVariable.metodoNewton import MetodoNewton
from variasVariables.unaVariable.interpolacionCuadratica import InterpolacionCuadratica
from variasVariables.unaVariable.metodoBiseccion import MetodoBiseccion
from variasVariables.unaVariable.seccionDorada import SeccionDorada
from variasVariables.busquedaAleatoria import BusquedaAleatoria
from variasVariables.maximaInclinacionRecursion import MaximaInclinacionRecursion
from variasVariables.lagrange import Lagrange
from graphicFunction import *
import sympy as sp

def main():
    menu1= '''
              ***********************************************
              *                 MENU                        *
              *********************************************** 
              * 1- funciones con una variable               *
              * 2- funciones con dos variables              *
              * 3- Solución al Taller de Optimización       *
              * 4- Salir                                    *
              ***********************************************
              
            \n'''
    menu2= '''
            *****************************************************
            * METODOS DE SOLUCIÓN DE FUNCIONES CON UNA VARIABLE *
            *****************************************************
            *                                                   *
            *   1-Metodo Bisección                              *
            *   2-Metodo Criteriode derivadas                   *
            *   3-Metodo Interpolación Cuadratica               *
            *   4-Metodo de Newton                              *
            *   5-Metodo Sección Dorada                         *
            *   6-Graficar Función                              *  
            *   7-Cambiar función                               *
            *   8-salir del submenu                             *
            *****************************************************
            \n'''          
    menu3= '''
            *********************************************************
            * METODOS DE SOLUCIÓN DE FUNCIONES CON VARIAS VARIABLES *
            *********************************************************
            *                                                       *
            *   1-Metodo Busqueda Aleatoria                         *
            *   2-Metodo Maxima Inclinación                         *
            *   3-Metodo Lagrange                                   *
            *   4-Graficar Función                                  *
            *   5-Cambiar de función                                *
            *   6-Salir del submenu                                 *
            *********************************************************
            \n''' 
        
    menu4= '''
              *******************************************************
              *      SOLUCIÓN AL TALLER DE OPTIMIZACIÓN             *   
              ******************************************************* 
              * 1- Ejercicio 1 utilizar metodo lagrange             *
              * 2- Ejercicio 2 utilizar metodo busqueda aleatoria   *
              * 3- Ejercicio 3 utilizar metodo máxima inclinación   *
              * 4- Salir                                            *
              *******************************************************
              
            \n'''
    bandera1=True
    bandera2=True
    bandera3=True
    while True:
        print(menu1)
        opc=int(input("Seleccione una de las opciones :"))
        
        if opc==1:
            print("EVALUACIÓN DE FUNCIONES CON UNA VARIABLE \n")
            funcion=str(input("Escriba la función que desea evaluar: "))
            
            
            while bandera1:
                print(menu2)
                opc1=int(input("Seleccione la opción que desea: "))
                
                if opc1==1:
                    print("METODO DE BISECCIÓN\n")
                    MetodoBiseccion(funcion)
                    
                    
                    
                elif opc1==2:
                    print("METODO CRITERIO DE DERIVADAS\n")
                    CriterioDerivadas(funcion)
                    
                elif opc1==3:
                    print("METODO INTERPOLACIÓN CUADRATICA\n")
                    inter=InterpolacionCuadratica(funcion)
                    inter.table()
                    
                elif opc1==4:
                    print("METODO DE NEWTON\n")
                    x0 = float(input("Digite número con que empieza: "))
                    x=sp.symbols('x')
                    new=MetodoNewton(funcion,x)
                    resultado=new.metodo_newton(x0)
                    print(f"El maximo en y={resultado[1]}, cuando x={resultado[0]}")
                    new.table()
                    
                elif opc1==5:
                    print("METODO RAZÓN DORADA\n")
                    SeccionDorada(funcion)
                    
                elif opc1==6:
                    print("GRAFICANDO LA FUNCIÓN  \n")
                    grafun =graphicFunction(funcion)
                    grafun.pintar()
                    
                elif opc1==7:
                    print("ESCRIBIENDO UNA NUEVA FUNCIÓN PARA EVALUAR \n")
                    funcion=str(input("Escriba la función que desea evaluar: "))
                    
                elif opc1==8:
                    print("SALIENDO DEL SUBMENU...\n")
                    bandera1=False
                    
                else:
                    print("Opción invalida, vuelva a intentarlo \n")
                    print(menu2)
                    opc1=int(input("Seleccione la opción que desea: "))
                    
        elif opc==2:
            print("EAVLUACIÓN DE FUNCIONES CON VARIAS VARIABLES\n")
            funcion2=str(input("Escriba la función que desea evaluar: "))
            
            while bandera2:
                print(menu3)
                opc2=int(input("Seleccione la opción que desea: "))
                
                if opc2==1:
                    print("METODO DE BUSQUEDA ALEATORIA\n")
                    lower=float(input("Indique el valor inferior de la busqueda aleatoria: "))
                    uper=float(input("Indique el valor superior de la busqueda aleatoria: "))
                    bus=BusquedaAleatoria(funcion2,lower, uper)
                    
                    
                elif opc2==2:
                    print("METODO MÁXIMA INCLINACIÓN\n")
                    rex0=(float(input("Indique la posición en x: ")))
                    rey0=(float(input("Indique la posición en y: ")))
                    MaximaInclinacionRecursion(funcion2, rex0,rey0)
                    
                elif opc2==3:
                    print("METODO DE LAGRANGE\n")
                    fun2=input("ingrese la primera función: ")
                    Lagrange(fun2, funcion2)
                    
                elif opc2==4:
                    print("GRAFICANDO LA FUNCIÓN \n")
                    #grafun(funcion2)
                    print("Esta opción esta en proceso de construcción, sin embargo cada metodo tiene su grafica")
                elif opc2==5:
                    print("ESCRIBIENDO UNA NUEVA FUNCIÓN PARA EVALUAR \n")
                    funcion2=str(input("Escriba la función que desea evaluar: "))
                    
                elif opc2==6:
                    print("SALIENDO DEL SUBMENU...\n")
                    bandera2=False 
                else:
                    print("Opción invalida, vuelva a intentarlo \n")
                    print(menu3)
                    opc2=int(input("Seleccione la opción que desea: "))
            
        elif opc==3:
            fn1='3*x+5*y'
            gn1='3*x**2+y**2-4'
            fn2='4*x + 2*y + x**2 - 2*x**4 + 2*x*y -3*y**2'
            low=-2
            upp=2
            var0= 0
            while bandera3:
                print(menu4)
                opc3=int(input("Seleccione la opción deseada: "))

                if opc3==1:
                    fun = sp.parse_expr(fn1, evaluate=False)
                    gun = sp.parse_expr(gn1, evaluate=False)
                    print("las funciones f(x) y g(x) respectivamente son:")
                    sp.pprint(fun)
                    sp.pprint(gun)
                    Lagrange(fn1, gn1)
                elif opc3==2:
                    BusquedaAleatoria(fn2,low, upp)
                elif opc3==3:
                    MaximaInclinacionRecursion(fn2,var0,var0) 
                elif opc3==4:
                    print("SALIENDO DEL SUBMENU...\n")
                    bandera3=False
                else:
                    print("Opción invalida, vuelva a intentarlo \n")
                    print(menu3)
                    opc2=int(input("Seleccione la opción que desea: "))
                    
        elif opc==4:
            print("Saliendo...")
            break
        else:
            print(menu1)
            opc=input("Seleccione una de las opciones :")

if __name__ =='__main__':
    main()




