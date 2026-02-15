import random

# def make_maze(largeur, hauteur, "s", "g"):
grille = [["#" for i in range(40)] for j in range(20)]
""" for ligne in grille:
    print(''.join(ligne)) """

# on pose le s
row_s = random.randint(0,19)
col_s = random.randint(0,39)
grille[row_s][col_s] = "s"

# on pose le g
row_g = row_s
col_g = col_s
while (row_g, col_g) == (row_s, col_s):
    row_g =random.randint(0,19)
    col_g = random.randint(0,39)
grille[row_g][col_g] = "g"

goal_pos = (row_g, col_g)
pos = (row_s, col_s)

manhat = abs(row_s -row_g) + abs( col_s - col_g)

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
        curseur = 90
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
while pos != goal_pos : 
    res = digg(pos, manhat, goal_pos, grille)
    if res is None:
        continue
    pos, manhat = res
    if pos in seen:
        compteur = compteur +1
        if compteur > 400 : 
            break
    seen.add(pos)
    row, col = pos
    if grille[row][col] == "s" or grille[row][col] == "g" :
        continue
    else:
        grille[row][col] = "."

for ligne in grille:
    print(''.join(ligne))        

with open("grille.txt", "w") as fichier:
    for ligne in grille:
        fichier.write("".join(ligne)+ "\n")







    







