import random
from biblio import bfs

def generate_maze(hauteur, largeur, curseur, max_doublon, difficulty):
    grille =  [["#" for i in range(largeur)] for j in range(hauteur)]

    row_s = random.randint(0, hauteur - 1)
    col_s = random.randint(0, largeur - 1)
    start_pos = (row_s, col_s)
    grille[row_s][col_s] = "s"

    row_g = random.randint(0, hauteur - 1)
    col_g = random.randint(0, largeur -1)
    goal_pos = (row_g, col_g)

    manhat = abs(row_s - row_g) + abs(col_s -col_g)
    distance_max = (hauteur - 1) + (largeur - 1)
    min_distance = int(difficulty * distance_max)

    while start_pos == goal_pos or manhat < min_distance:
        row_g = random.randint(0, hauteur - 1)
        col_g = random.randint(0, largeur -1)
        goal_pos = (row_g, col_g)
        manhat = abs(row_s - row_g) + abs(col_s -col_g)

    pos = (row_s, col_s)
    grille[row_g][col_g] = "g"

    def digg_move(pos, dr, dc, grille):
        row, col = pos
        nrow = row + dr
        ncol = col + dc   
        
        # vérif limite grille
        if nrow >= len(grille) or nrow < 0 or ncol >= len(grille[nrow]) or ncol < 0 :
            return None
        return (nrow, ncol)


    def digg(pos, manhat, goal, grille):
        row, col = pos
        row_g, col_g = goal
        digg_direction = [(0, 1), (1, 0), (0, -1), (-1,0)]
        good_list = []
        bad_list = []
        

        for dr, dc in digg_direction:
            mov = digg_move(pos, dr, dc, grille)
            if mov is None :
                continue
            elif mov == goal:
                return (mov, 0)
            nrow, ncol = mov
            manhat_new = abs (nrow - row_g) + abs(ncol - col_g)
            
            if manhat_new <= manhat : 
                good_list.append((mov, manhat_new))
            else:
                bad_list.append((mov, manhat_new))   


        if good_list and bad_list :
            
            nombre = random.randint(0, 100)
            if nombre <= curseur :
                choix = random.choice(good_list)
                return choix
            else:
                choix = random.choice(bad_list)  
                return choix

        elif good_list :
            choix = random.choice(good_list)
            return choix

        elif bad_list :
            choix = random.choice(bad_list)
            return choix
        else:
            return None
    seen = {pos}
    compteur = 0
    list_main_path = []
    list_main_path.append(start_pos)
    while pos != goal_pos : 
        res = digg(pos, manhat, goal_pos, grille)
        if res is None:
            break
        pos, manhat = res
        list_main_path.append(pos)
        if pos in seen:
            compteur = compteur +1
            if compteur > max_doublon : 
                break
        seen.add(pos)
        row, col = pos
        if grille[row][col] == "s" or grille[row][col] == "g" :
            continue
        else:
            grille[row][col] = "."

    return (grille, start_pos , goal_pos)

def write_maze(grille, filename):
    with open(filename, "w") as fichier:
        for ligne in grille: 
            fichier.write("".join(ligne)+ "\n")

grille, start_pos, goal_pos = generate_maze(40, 100, 55, 200000, 0.7)

for ligne in grille:
    print("".join(ligne))

write_maze(grille, "grille.txt")

verification = bfs(start_pos, goal_pos, grille)
print(verification)