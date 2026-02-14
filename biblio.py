# exercice de la biblio
# trouver le chemin le plus court d'un point "s"
# à un point "g"

# lire le fichier biblio

f = open('biblio.txt', 'r')
contenu = f.read()
print(contenu)
# print(repr(contenu)) voir les caractères de retour à la ligne
f.close()

# split in lines
contenu = contenu.splitlines()
print (contenu)

# Search the initial state. mémo :  contenu[rangé][colonne] et meme convention pour coordonnées
start = None
goal = None
print(len(contenu[0]))
for row in range(len(contenu)):
    for col in range(len(contenu[row])):
        if contenu[row][col].lower() == "s":
            start = (row,col)
        if contenu[row][col].lower() == "g":
            goal = (row,col)
print("start=", start)
print("goal=", goal)

# fonction pour voir les case autour de notre agent commençant à "s"
# déplacement de 1 case dans chaque direction
def move(state, dr, dc, contenu):
    traversable = {'.', 's', 'g'}
    row, col = state
    nrow = row + dr
    ncol = col + dc
    if nrow >= len(contenu) or nrow < 0 or ncol >= len(contenu[nrow]) or ncol < 0:
        return None
    cell = contenu[nrow][ncol]
    # gestion des murs
    if cell == "#":
        return None
    # détection mouvement valide
    if cell.lower() in traversable:
        return (nrow, ncol)
    return None
    

#bfs en pseudo :
# search convention right, down, left, up
# initial state = [start]

# on génère les voisins à une case
def voisins(state, contenu):
    liste = []
    direction = [("right", 0, 1), ("down", 1, 0), ("left", 0, -1), ("up", -1, 0)]
    for action, dr, dc in direction:
        deplacement = move(state, dr, dc, contenu)
        if deplacement is not None:
            liste.append((action, deplacement))
    return  liste      


    r = move(state, 0, 1, contenu)
    if r is not None:
        liste.append(("right", r))
    d = move(state, 1, 0, contenu)
    if d is not None:
        liste.append(("down", d))
    l = move(state, 0, -1, contenu)
    if l is not None:
        liste.append(("left", l))
    u = move(state, -1, 0, contenu)
    if u is not None:
        liste.append(("up", u))
    return liste


frontiere = [start]
seen = set()
seen.add(start)
parent = {}

while frontiere:
    current = frontiere.pop(0)
    if current == goal :

        node = goal
        chemin_inverse = []
        while node != start:
            parent_state, action = parent[node]
            chemin_inverse.append((action, node))
            node = parent_state
        actions = list(reversed(chemin_inverse))
        print("Le chemin est :")
        print(actions)
        break


    for action, child in voisins(current, contenu):
        if child not in seen:
            seen.add(child)
            frontiere.append(child)
            parent[child] = (current , action)








