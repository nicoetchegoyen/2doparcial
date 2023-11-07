from arbol_binario import BinaryTree
class ArbolNuevo(BinaryTree):                 ##nueva clase de arbol porque me daba error el BinaryTree
    def inorden(self):
        def inorden(root):
            if root is not None:
                inorden(root.left)
                print(root.value)
                inorden(root.right)

        inorden(self.root)


# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:"""

# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
arbol_nombre = ArbolNuevo()
arbol_numero = ArbolNuevo()
arbol_tipo = ArbolNuevo()

#datos de pokemons no fieles a la serie/juego
pokemons = [
    {'nombre': 'pikachu', 'numero': 1, 'tipo': 'electrico'},
    {'nombre': 'vaporeon', 'numero': 2, 'tipo': 'agua'},
    {'nombre': 'charmander', 'numero': 3, 'tipo': 'fuego'},
    {'nombre': 'bulbasur', 'numero': 4, 'tipo': 'agua'},
    {'nombre': 'eevy', 'numero': 5, 'tipo': 'planta'},
    {'nombre': 'jolteon', 'numero': 6, 'tipo': 'electrico'},
    {'nombre': 'lycanroc', 'numero': 7, 'tipo': 'piedra'},
    {'nombre': 'tyrantrum', 'numero': 8, 'tipo': 'acero'}    
    ]


for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})
    arbol_numero.insert_node(pokemon['numero'], {'nombre': pokemon['nombre'],'tipo': pokemon['tipo']})
    arbol_tipo.insert_node(pokemon['tipo'], {'numero': pokemon['numero'],'nombre': pokemon['nombre']})



# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
print("-----------------------------------------------------------------------------------")
print("b.datos del pokemon numero 7")
print(arbol_numero.search(7).other_values)

print("-----------------------------------------------------------------------------------")
print('busqueda por proximidad "bul"')
print(arbol_nombre.search_by_coincidence('bul'))
print("-----------------------------------------------------------------------------------")


# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
print("c.")
pos = arbol_tipo.search('agua')
if pos:
    print('TIPOS AGUA:', pos.other_values)
pos = arbol_tipo.search('fuego')
if pos:
    print('TIPOS FUEGO:', pos.other_values)
    pos = arbol_tipo.search('planta')
if pos:
    print('TIPOS PLANTA:', pos.other_values)
pos = arbol_tipo.search('electrico')
if pos:
    print('TIPOS ELECTRICO:', pos.other_values)
print("-----------------------------------------------------------------------------------")

# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
print("d. LISTADO ASCENDENTE POR NUMERO")
arbol_numero.inorden()
print("-----------------------------------------------------------------------------------")
print("LISTADO ASCENDENTE POR NOMBRE")
arbol_nombre.inorden()
print("-----------------------------------------------------------------------------------")
print("LISTADO POR NIVEL POR NOMBRE")
arbol_nombre.by_level()
print("-----------------------------------------------------------------------------------")

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
jolteon = arbol_nombre.search('jolteon')
print("INFORMACION ACERCA DE JOLTEON:", jolteon.other_values)
lycanroc = arbol_nombre.search('lycanroc')
print("INFORMACION ACERCA DE LYCANROC:", lycanroc.other_values)
tyrantrum = arbol_nombre.search('tyrantrum')
print("INFORMACION ACERCA DE TYRANTRUM:", tyrantrum.other_values)
print("-----------------------------------------------------------------------------------")

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 
print("e.CANTIDAD DE POKEMONS TIPO ELECTRICO", arbol_tipo.contar('electrico'))
print("CANTIDAD DE POKEMONS TIPO ACERO", arbol_tipo.contar('acero'))
