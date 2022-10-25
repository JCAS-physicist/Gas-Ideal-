from vpython import *
from random import *
from tkinter import *


np=6  #int(input("Cuántas particulas deseas tener en la simulación? "))
L=20
t=0.0
dt=0.01
R=2.5


thk=0.1
s2=2*L - thk
s3=2*L + thk
LL=L-0.5*thk-R


win=500
C=canvas(width=win, height=win)
C.range = L+20
C.title="Gas Ideal con colisiones en 3D mejorado".center(110)


gray=color.gray(0.7)
boxbottom = curve(color=gray, radius=thk)
boxbottom.append([vector(-L,-L,-L), vector(-L,-L,L), vector(L,-L,L), vector(L,-L,-L), vector(-L,-L,-L)])
boxtop = curve(color=gray, radius=thk)
boxtop.append([vector(-L,L,-L), vector(-L,L,L), vector(L,L,L), vector(L,L,-L), vector(-L,L,-L)])
vert1 = curve(color=gray, radius=thk)
vert2 = curve(color=gray, radius=thk)
vert3 = curve(color=gray, radius=thk)
vert4 = curve(color=gray, radius=thk)
vert1.append([vector(-L,-L,-L), vector(-L,L,-L)])
vert2.append([vector(-L,-L,L), vector(-L,L,L)])
vert3.append([vector(L,-L,L), vector(L,L,L)])
vert4.append([vector(L,-L,-L), vector(L,L,-L)])


p=[]
pf=[]

for i in range(np):
    
    particles=sphere(radius=R, pos=vec(uniform(-L,L),uniform(-L,L),uniform(-L,L)), color=color.red)

    particles.vel=vec(uniform(-L,L),uniform(-L,L),uniform(-L,L))

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
    s=sgn(particles.pos.z)
    if abs(particles.pos.z)>LL:
        particles.vel.z=-particles.vel.z
        particles.pos.z=s*abs(2*LL)-particles.pos.z
        
        
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
