# exercice de la biblio
# trouver le chemin le plus court d'un point s
# a un point g

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

# fonction pour voir les case autour de notre agent commençant à s
# deplacement de 1 dans chaque direction

def move_right(row, col, contenu):
    add_col = col + 1

    # dépassement de grille :
    if add_col >= len(contenu[row]):
        return None

    cell = contenu[row][add_col]

    # gestion des murs
    if cell == "#":
        return None

    # détection mouvement valide
    traversable = {'.', 's', 'g'}
    if cell.lower() in traversable:
       return (row, add_col)
    return None

def move_down(row, col, contenu):
    add_row = row + 1

    # dépassement de la grille
    if add_row >= len(contenu):
        return None

    cell = contenu[add_row][col]

    # gestion des murs
    if cell == "#":
        return None

    # détection mouvement valide
    traversable = {'.', 's', 'g'}
    if cell.lower() in traversable:
        return (add_row, col)
    return None

def move_left(row, col, contenu):
    minus_col = col -1

    # dépassement de grille
    if minus_col < 0 :
        return None

    cell = contenu[row][minus_col]

    # gestion des murs
    if cell == "#":
        return None

    # détection mouvement valide
    traversable = {'.', 's', 'g'}
    if cell.lower() in traversable:
        return (row, minus_col)
    return None

def move_up(row, col, contenu):
    minus_row = row - 1

    # dépassement de grille
    if minus_row < 0:
        return None

    cell = contenu[minus_row][col]

    # gestion des murs
    if cell =="#":
        return None

    # détection mouvement valide
    traversable = {'.', 's', 'g'}
    if cell.lower() in traversable:
        return (minus_row, col)
    return None

#bfs en pseudo :
# search convention right, down, left, up
# initial state = [start]

# on génère les voisins à une case
def voisins(state, contenu):
    row, col = state
    liste = []
    r = move_right(row, col, contenu)
    if r is not None:
        liste.append(("right", r))
    d = move_down(row, col, contenu)
    if d is not None:
        liste.append(("down", d))
    l = move_left(row, col, contenu)
    if l is not None:
        liste.append(("left", l))
    u = move_up(row, col, contenu)
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








