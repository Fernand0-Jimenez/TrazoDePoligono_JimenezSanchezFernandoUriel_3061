import Operaciones
import matplotlib.pyplot as plt


def menu():
    print (" Numero de lados: ",end = "")
    figura = int(input()) 
    print ("""

        1- DDA
        2- Bresenham
    """)
    algoritmo = int(input("Algoritmo: ")) 
    puntos = []
    for i in range(figura):
        puntox = int(input(f"punto x{i+1}: ")) 
        puntoy = int(input(f"punto y{i+1}: ")) 
        puntos.append([puntox,puntoy])
    puntos.append([puntos[0][0],puntos[0][1]])
    return algoritmo,puntos

def square(p,n,m):#recibe el plot, coordenada x y coordenada y
    # dibuja un cuadrado en un solo pixel de color verde
    p.plot([n+1,n+1,n,n,n+1],[m,m+1,m+1,m,m],color = "green")

if __name__ == '__main__':
    #obtenemos los datos necesarios para el programa
    algoritmo,puntos=menu()


    # listas para guardar los puntos a graficar y mostrar en consola
    coordenadas_completas_x= []
    coordenadas_completas_y= []

    # llenando con las lineas a partir de los puntos obtenidos
    for i in range(len(puntos)-1):
        if algoritmo ==1:
            x,y = Operaciones.dda(puntos[i][0],puntos[i][1],puntos[i+1][0],puntos[i+1][1])
        else:
            x,y=Operaciones.bresenham(puntos[i][0],puntos[i][1],puntos[i+1][0],puntos[i+1][1])
        coordenadas_completas_x.append(x)
        coordenadas_completas_y.append(y)
        #pinta un cuadro por cada coordenada obtenida de la linea actual de la figura
        for i in range(len(x)):
            square(plt,x[i],y[i])



    print(f"Puntos para trazos {puntos}")
    print(f"Puntos para lineas en x {coordenadas_completas_x}")
    print(f"Puntos para lineas en y {coordenadas_completas_y}")
    plt.show()