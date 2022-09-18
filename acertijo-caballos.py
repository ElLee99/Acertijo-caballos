# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:08:18 2022

@author: Johan Lee
"""
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



caballosorden = ""


class Caballo:
    def __init__(self, tiempo, nombre):
        self.tiempo = tiempo
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None
        
class Arbol:
    def __init__(self, tiempo, nombre):
        self.raiz = Caballo(tiempo, nombre)
     
        
    def __agregar_caballo(self, caballo, tiempo, nombre):
        if tiempo < caballo.tiempo:
            if caballo.izquierda is None:
                caballo.izquierda = Caballo(tiempo, nombre)     
            else:
                self.__agregar_caballo(caballo.izquierda, tiempo, nombre)
        else:
            if caballo.derecha is None:
                caballo.derecha = Caballo(tiempo, nombre)
            else:
                self.__agregar_caballo(caballo.derecha, tiempo, nombre)
         
    
    def __recorrido(self, caballo):
         if caballo is not None:
            self.__recorrido(caballo.izquierda)
        
            print(caballo.nombre + " = " + str(caballo.tiempo))
            #print(caballo.tiempo)
            self.__recorrido(caballo.derecha)


    def __buscar(self, nodo, tiempo):
       if nodo is None:
           return None
       if nodo.tiempo == tiempo:
           return nodo
       if tiempo < nodo.tiempo:
           return self.__buscar(nodo.izquierda, tiempo)
       else:
           return self.__buscar(nodo.derecha, tiempo)  
       
        
     
    def agregar(self, dato, nombre):
        self.__agregar_caballo(self.raiz, dato, nombre)
       # self.__agregar_caballo(self.raiz, nombre)

    def inorden(self):
        print("Imprimiendo lista en orden: ")
        self.__recorrido(self.raiz)
        print("")
        
    def buscar(self, tiempo):
        return self.__buscar(self.raiz, tiempo)
    
    

nombres = [["Juan",
"José Luis",
"José",
"María Chayo",
"Francisco"],
["Guadalupe",
"María",
"Juana",
"Antonio",
"Jesús"],
["Miguel Ángel",
"Pedro",
"Alejandro",
"Manuel",
"Margarita"],
["Marí Carmen",
"Juan Carlos",
"Roberto",
"Fernando",
"Daniel"],
["Carlos",
"Jorge",
"Ricardo",
"Miguel",
"Eduardo",
"Aisaac"]]


tabla_tiempos = np.zeros((5, 5))
dimension = tabla_tiempos.shape
for x in range(dimension[0]):
    for y in range (dimension[1]):
        tabla_tiempos[x, y] = random.randint(0,999)

print ("Listado de participantes:" )
print (nombres,'\n')

print ("Listado de 5 primeras carreras:" )
for x in range(5):
    print(" Carrera ", x + 1, nombres[x])


print("\nTiempos de cada cuaco: ")
for x in range(5):
  print(" Carrera ", x + 1, tabla_tiempos[x]) 


print("\nResultados ordenados por carrera: ")
for x in range(5):
  tabla_tiempos[x].sort() 
  print(" Carrera ", x + 1, tabla_tiempos[x]) 


print("\nCarrera entre los 5 más veloces:")
primeros= np.array([tabla_tiempos[0,0],tabla_tiempos[1,0],tabla_tiempos[2,0],tabla_tiempos[3,0],tabla_tiempos[4,0]])
print(primeros)


print("\nMatriz acomodada por velocidades:")
acomodo_final = tabla_tiempos[np.argsort(tabla_tiempos[:, 0])]
for x in range(5):
  print(acomodo_final[x]) 

print("\nCarrera por el segundo y tercer lugar:")
ultima_carrera = np.array([acomodo_final[0, 1],acomodo_final[0, 2],acomodo_final[1, 0],acomodo_final[1, 1],acomodo_final[2, 0]])
print(ultima_carrera)
ultima_carrera.sort()

print("\nResultados:")
print("Primer lugar:", int(acomodo_final[0,0]), "seg")
print("Segundo lugar:", int(ultima_carrera[0]), "seg")
print("Segundo lugar:", int(ultima_carrera[1]), "seg")
print("\n\n\n")

listafinal = np.concatenate(acomodo_final)
listafinal.sort()

carrera = Arbol(tabla_tiempos[0,0], nombres[0][0])  
for x in range(dimension[0]):
    for y in range (dimension[1]):
        if x == 0 and y == 0:
            pass
        else:
            carrera.agregar (tabla_tiempos[x,y], nombres[x][y])

carrera.inorden()


participallos = ["" for x in range(25)]
for x in range(25):
  Dato = carrera.buscar(listafinal[x])
  participallos[x] = Dato.nombre
  
  
Grafo = nx.Graph()

vertices_G = [participallos[24], participallos[23], participallos[22], participallos[21], participallos[20],participallos[19], participallos[18], 
              participallos[17], participallos[16], participallos[15], participallos[14], participallos[13], participallos[12], participallos[11], 
              participallos[10], participallos[9], participallos[8], participallos[7], participallos[6], participallos[5],participallos[4],
              participallos[3], participallos[2], participallos[1], participallos[0]]


Grafo.add_nodes_from(vertices_G)

aristas_G = [(participallos[24], participallos[23]), (participallos[23], participallos[22]), (participallos[22], participallos[21]), (participallos[21], participallos[20]),
             (participallos[20], participallos[19]), (participallos[19], participallos[18]), (participallos[18], participallos[17]), (participallos[17], participallos[16]),
             (participallos[16], participallos[15]), (participallos[15], participallos[14]), (participallos[14], participallos[13]), (participallos[13], participallos[12]),
             (participallos[12], participallos[11]), (participallos[11], participallos[10]), (participallos[10], participallos[9]), (participallos[9], participallos[8]), 
             (participallos[8], participallos[7]), (participallos[7], participallos[6]), (participallos[6], participallos[5]), (participallos[5], participallos[4]),
             (participallos[4], participallos[3]), (participallos[3], participallos[2]), (participallos[2], participallos[1]), (participallos[1], participallos[0])]

Grafo.add_edges_from(aristas_G)

ubica = {participallos[0]: (1, 21), participallos[1]: (1, 18), participallos[2]: (1, 15), participallos[3]: (1, 12), participallos[4]: (1, 9),
         participallos[5]: (1, 6), participallos[6]: (1, 3), participallos[7]: (1, 0), participallos[8]: (10, 21), participallos[9]: (10, 18), 
         participallos[10]: (10, 15), participallos[11]: (10, 12), participallos[12]: (10, 9), participallos[13]: (10, 6), participallos[14]: (10, 3),
         participallos[15]: (10, 0), participallos[16]: (20, 21), participallos[17]: (20, 18), participallos[18]: (20, 15), participallos[19]: (20, 12),
         participallos[20]: (20, 9), participallos[21]: (20, 6), participallos[22]: (20, 3), participallos[23]: (20, 0), participallos[24]: (16, 0)}



class Tupla:
    def _init_(self, x, y):
        self.x = x
        self.y = y

puntoA = Tupla()
puntoA.x = ubica[participallos[24]][0]
puntoA.y = ubica[participallos[24]][1]
puntoB = Tupla()
puntoB.x = ubica[participallos[23]][0]
puntoB.y = ubica[participallos[23]][1]
puntoC = Tupla()
puntoC.x = ubica[participallos[22]][0]
puntoC.y = ubica[participallos[22]][1]
puntoD = Tupla()
puntoD.x = ubica[participallos[21]][0]
puntoD.y = ubica[participallos[21]][1]
puntoE = Tupla()
puntoE.x = ubica[participallos[20]][0]
puntoE.y = ubica[participallos[20]][1]
puntoF = Tupla()
puntoF.x = ubica[participallos[19]][0]
puntoF.y = ubica[participallos[19]][1]
puntoG = Tupla()
puntoG.x = ubica[participallos[18]][0]
puntoG.y = ubica[participallos[18]][1]
puntoH = Tupla()
puntoH.x = ubica[participallos[17]][0]
puntoH.y = ubica[participallos[17]][1]
puntoI = Tupla()
puntoI.x = ubica[participallos[16]][0]
puntoI.y = ubica[participallos[16]][1]
puntoJ = Tupla()
puntoJ.x = ubica[participallos[15]][0]
puntoJ.y = ubica[participallos[15]][1]
puntoK = Tupla()
puntoK.x = ubica[participallos[14]][0]
puntoK.y = ubica[participallos[14]][1]
puntoL = Tupla()
puntoL.x = ubica[participallos[13]][0]
puntoL.y = ubica[participallos[13]][1]
puntoM = Tupla()
puntoM.x = ubica[participallos[12]][0]
puntoM.y = ubica[participallos[12]][1]
puntoN = Tupla()
puntoN.x = ubica[participallos[11]][0]
puntoN.y = ubica[participallos[11]][1]
puntoO = Tupla()
puntoO.x = ubica[participallos[10]][0]
puntoO.y = ubica[participallos[10]][1]
puntoP = Tupla()
puntoP.x = ubica[participallos[9]][0]
puntoP.y = ubica[participallos[9]][1]
puntoQ = Tupla()
puntoQ.x = ubica[participallos[8]][0]
puntoQ.y = ubica[participallos[8]][1]
puntoR = Tupla()
puntoR.x = ubica[participallos[7]][0]
puntoR.y = ubica[participallos[7]][1]
puntoS = Tupla()
puntoS.x = ubica[participallos[6]][0]
puntoS.y = ubica[participallos[6]][1]
puntoT = Tupla()
puntoT.x = ubica[participallos[5]][0]
puntoT.y = ubica[participallos[5]][1]
puntoU = Tupla()
puntoU.x = ubica[participallos[4]][0]
puntoU.y = ubica[participallos[4]][1]
puntoV = Tupla()
puntoV.x = ubica[participallos[3]][0]
puntoV.y = ubica[participallos[3]][1]
puntoY = Tupla()
puntoY.x = ubica[participallos[2]][0]
puntoY.y = ubica[participallos[2]][1]
puntoX = Tupla()
puntoX.x = ubica[participallos[1]][0]
puntoX.y = ubica[participallos[1]][1]
puntoZ = Tupla()
puntoZ.x = ubica[participallos[0]][0]
puntoZ.y = ubica[participallos[0]][1]


Puntos = {participallos[24]: puntoA, participallos[23]: puntoB, participallos[22]: puntoC, participallos[21]: puntoD, participallos[20]: puntoE, 
          participallos[19]: puntoF, participallos[18]: puntoG, participallos[17]: puntoH, participallos[16]: puntoI, participallos[15]: puntoJ, 
          participallos[14]: puntoK, participallos[13]: puntoL, participallos[12]: puntoM, participallos[11]: puntoN, participallos[10]: puntoO, 
          participallos[9]: puntoP, participallos[8]: puntoQ, participallos[7]: puntoR, participallos[6]: puntoS, participallos[5]: puntoT, 
          participallos[4]: puntoU, participallos[3]: puntoV, participallos[2]: puntoY, participallos[1]: puntoX, participallos[0]: puntoZ}

    
nx.draw(Grafo, pos=ubica, node_color='green', with_labels=True)
plt.show()