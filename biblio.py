from collections import deque
# exercice de la biblio
# trouver le chemin le plus court d'un point "s"
# à un point "g"

# lire le fichier biblio
f = open('grille.txt', 'r')
contenu = f.read()
# print(repr(contenu)) voir les caractères de retour à la ligne
f.close()

# split in lines
contenu = contenu.splitlines()

# Search the initial state. mémo :  contenu[rangé][colonne] 
# et meme convention pour coordonnées
start = None
goal = None
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
    
# on génère les voisins à une case
def voisins(state, contenu):
    liste = []
    direction = [("right", 0, 1), ("down", 1, 0), ("left", 0, -1), ("up", -1, 0)]
    for action, dr, dc in direction:
        deplacement = move(state, dr, dc, contenu)
        if deplacement is not None:
            liste.append((action, deplacement))
    return  liste      

# fonction principale
def bfs(start, goal, contenu):
    frontiere = deque([start])
    seen = set()
    seen.add(start)
    parent = {}

    while frontiere:
        current = frontiere.popleft()
        if current == goal :
            node = goal
            chemin_inverse = []
            while node != start:
                parent_state, action = parent[node]
                chemin_inverse.append((action))
                node = parent_state
            actions = list(reversed(chemin_inverse))
            return actions
        
        for action, child in voisins(current, contenu):
            if child not in seen:
                seen.add(child)
                frontiere.append(child)
                parent[child] = (current, action)    
    return None 

for row in contenu:           
    print(row)  

if start is None or goal is None:
    print("Pas de case de démarrage ou pas de case goal !")
else:
    print(bfs(start, goal, contenu))









