from grafo import Grafo 
from heap_min import Heap
from lista import Lista

#2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:
mi_grafo = Grafo(dirigido=False)

# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;
#a. insertar los vertices del grafo
# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO,
#  Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
mi_grafo.insert_vertice('Luke Skywalker')
mi_grafo.insert_vertice('Darth Vader')
mi_grafo.insert_vertice('Yoda')
mi_grafo.insert_vertice('Boba Fett')
mi_grafo.insert_vertice('C-3PO')
mi_grafo.insert_vertice('Leia')
mi_grafo.insert_vertice('Rey')
mi_grafo.insert_vertice('Kylo Ren')
mi_grafo.insert_vertice('Chewbacca')
mi_grafo.insert_vertice('Han Solo')
mi_grafo.insert_vertice('R2-D2')
mi_grafo.insert_vertice('BB-8')

#b. insertar las aristas del grafo
mi_grafo.insert_arist('Luke Skywalker', 'Darth Vader', 7)
mi_grafo.insert_arist('Darth Vader', 'Yoda', 7)
mi_grafo.insert_arist('Yoda', 'Boba Fett', 8)
mi_grafo.insert_arist('Boba Fett', 'C-3PO', 9)
mi_grafo.insert_arist('C-3PO', 'Leia', 10)
mi_grafo.insert_arist('Leia', 'Rey', 11)
mi_grafo.insert_arist('Rey', 'Kylo Ren', 12)
mi_grafo.insert_arist('Kylo Ren', 'Chewbacca', 13)
mi_grafo.insert_arist('Chewbacca', 'Han Solo', 14)
mi_grafo.insert_arist('Han Solo', 'R2-D2', 16)
mi_grafo.insert_arist('R2-D2', 'BB-8', 18)
mi_grafo.insert_arist('BB-8', 'Luke Skywalker', 3)
mi_grafo.insert_arist('BB-8', 'Darth Vader', 3)
mi_grafo.insert_arist('Luke Skywalker', 'Boba Fett', 4)
mi_grafo.insert_arist('Darth Vader', 'C-3PO', 2)
mi_grafo.insert_arist('Luke Skywalker', 'Yoda', 7)
mi_grafo.insert_arist('Luke Skywalker', 'Han Solo', 7)


#b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
bosque = mi_grafo.kruskal()
for arbol in bosque:
    print("---------------------------------------------------------------------------------")
    print('b.ARBOL DE EXPANSION MINIMA:')
    print(bosque)
    for nodo in arbol.split(';'):
        if 'Yoda' in nodo and '-' in nodo:
            print("Yoda aparece en el arbol de expansion minima, relacionado de la siguente manera:", nodo)
#codigo usado en clase modificado para buscar a Yoda

# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 
#me quede sin tiempo

