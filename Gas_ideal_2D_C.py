from vpython import *
from random import *
from tkinter import *

np=5  #int(input("Cuántas particulas deseas tener en la simulación? "))
L = 300
thk = 0.1
s2 = 2*L - thk
s3 = 2*L + thk

#Ventana de Canavas
win=500
C=canvas(width=win, height=win)
C.range = L+15
C.title="Gas Ideal con colisiones en 2D".center(110)

wallBK = box(pos=vector(0, 0, 0), size=vector(s2, s2, thk),  color = color.gray(0.7), opacity=0.5)

t=0.0
dt=0.01
R=10
m1=1.0
m2=1.0

LL=L-0.5*thk-R

p=[]
pf=[]

for i in range(np):
    
    particles=sphere(radius=R, pos=vec(uniform(-L,L),uniform(-L,L),0), color=color.blue)

    particles.vel=vec(uniform(-L,L),uniform(-L,L),0)

    p.append(particles)
    pf.append(particles)



def sgn(x):
    if x>=0.0:
        return 1
    else:
        return -1
    
def impacto(): #Paredes
    s=sgn(particles.pos.x)
    if abs(particles.pos.x)>LL:
        particles.vel.x=-particles.vel.x
        particles.pos.x=s*abs(2*LL)-particles.pos.x
    s=sgn(particles.pos.y)
    if abs(particles.pos.y)>LL:
        particles.vel.y=-particles.vel.y
        particles.pos.y=s*abs(2*LL)-particles.pos.y
        
        
def colision():
    for i in range(np):
        for j in range(i+1,np):
            
            distance=mag(p[i].pos-p[j].pos)
            
            if distance<=(p[i].radius+p[j].radius):    
                pf1=p[j].vel   #Velocidades finales
                pf2=p[i].vel

                p[i].vel=pf1
                p[j].vel=pf2
        
while t<500:
    rate(200)  # Frames per second
    
    for particles in p:
        
        particles.pos=particles.pos+particles.vel*dt  
        
        colision()
        
        impacto()
        
    t+=dt
