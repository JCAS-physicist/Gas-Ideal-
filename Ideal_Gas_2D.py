from tkinter import *
from random import *


# Movimiento
def mover():
    for i in range(np):
        dx=V[i][0]*dt # cambios de posición
        dy=V[i][1]*dt
        C.move(p[i],dx,dy)
        # actualizar posiciones
        R[i][0]=R[i][0]+dx
        R[i][1]=R[i][1]+dy
        # verificar choque
        if R[i][0]>L-r or R[i][0]<r:
            V[i][0]=-V[i][0]
            
        if R[i][1]>L-r or R[i][1]<r:
            V[i][1]=-V[i][1]
    
    # movimiento 
    W.after(10,mover)
    


L=500                                                        # longitud de la caja
np=int(input("Cuántas particulas deseas? "))                 # Número de partículas
r=10                                                         # radio
dt=0.01                                                      # paso de tiempo

# Gráfico
W=Tk()
W.title('Gas Ideal')
#Ventana
C=Canvas(W, height=L, width=L, bg='black')
C.pack()
#Boton para detener
Boton=Button(W, text="Detener Simulación", command=W.destroy)
Boton.pack()
#Semilla random
seed() 

# vectores de posición y velocidad
R=[[uniform(r,L-r),uniform(r,L-r)] for i in range(np)]
V=[[uniform(-L/2,L/2),uniform(-L/2,L/2)] for i in range(np)]

# las partículas serán círculos:
#xo,y0 x1,y1
p=[C.create_oval(R[i][0]-r, R[i][1]-r, R[i][0]+r, R[i][1]+r, \
fill='red') for i in range(np)]



    
mover()
W.mainloop()
