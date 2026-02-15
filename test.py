import random

def generate_maze(largeur, hauteur)
    grille =  [["#" for i in range(largeur)] for j in range(hauteur)]

    for ligne in grille:
        print("".join(ligne))



    while (row_s)
    row_s = random.randint(0, hauteur - 1)
    col_s = random.randint(0, largeur - 1)
    start_pos = (row_s, col_s)

    row_g = random.randint(0, hauteur - 1)
    col_g = random.randint(0, largeur -1)


    manhat = abs(row_s - row_g) + abs(col_s -col_g)   
    distance_max = (hauteur - 1) + (largeur - 1)
    laby_facile = 0.3*distance_max
    laby_moyen = 0.5*distance_max
    laby_dur = 0.7*distance_max