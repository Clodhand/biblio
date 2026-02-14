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
        if mov is None or mov == pos :
            continue
        elif mov == goal:
            return (mov, 0)
        nrow, ncol = mov
        manhat_new = abs (nrow - row_g) + abs(ncol - col_g)
        if manhat_new <= manhat : 
            good_list.append((mov, manhat_new))
        else:
            bad_list.append((mov, manhat_new))   

    if len(good_list) != 0:






    




""" def digg_right(pos, goal_pos, manhat, grille ):
    row, col = pos
    
    col = col+1
    row_g, col_g = goal_pos
    pos = (row, col)

    # si hors grille
    if col >= len(grille[0]):
        return None
    
    manhat_new = abs(row - row_g) + abs( col - col_g)
    
   
    
    # si manhat se reduit et qu'on est pas sur "s"
    if (manhat_new <= manhat) and (grille[row][col] != "s"):
        # grille[row][col] = "."
        return (pos, manhat_new)
    return None


def digg_down(pos, goal_pos, manhat, grille):
    row, col = pos
    row = row +1
    row_g, col_g = goal_pos
    pos = (row, col)

    # si hors grille
    if row >= len(grille):
        return None
    
    manhat_new = abs(row - row_g) + abs( col - col_g)

    # si on est sur g
    if grille[row][col] == "g":
        return (pos , manhat_new)
    
    # si manhat se reduit et qu'on est pas sur "s"
    if (manhat_new <= manhat) and (grille[row][col] != "s"):
        # grille[row][col]= "."
        return (pos, manhat_new)
    return None

def digg_left(pos, goal_pos, manhat, grille):
    row, col = pos
    col = col - 1
    row_g, col_g = goal_pos
    pos = (row, col)

    # si hors grille
    if col < 0:
        return None

    manhat_new = abs(row - row_g) + abs( col - col_g) 

    # si on est sur g
    if grille[row][col] == "g":
        return (pos, manhat_new)

    # si manhat se reduit et qu'on est pas sur "s"
    if (manhat_new <= manhat) and (grille[row][col] != "s"):
        # grille[row][col]= "."
        return (pos, manhat_new)
    return None
    
def digg_up(pos, goal_pos,manhat, grille):
    row, col = pos
    row = row - 1
    row_g, col_g = goal_pos
    pos = (row, col)

    # si hors grille
    if row < 0:
        return None
    
    manhat_new = abs(row - row_g) + abs( col - col_g) 
   
    # si on est sur g
    if grille[row][col] == "g" :
        return (pos, manhat_new)
    
    # si manhat se reduit et qu'on est pas "s"
    if (manhat_new <= manhat) and (grille[row][col] != "s"):
        # grille[row][col] = "."
        return (pos, manhat_new)
    return None

while True:
    list_mov = []
    right = digg_right(pos, goal_pos, manhat, grille) 
    if right != None :
        list_mov.append(right)

    down = digg_down(pos, goal_pos, manhat, grille)  
    if down != None:
        list_mov.append(down)

    left = digg_left(pos, goal_pos, manhat, grille)
    if left != None:
        list_mov.append(left)    

    up = digg_up(pos, goal_pos, manhat, grille)
    if up != None:
        list_mov.append(up)
        # print(list_mov)
    if not list_mov:
        break    
    found = False
    for element in list_mov:
        if goal_pos == element[0]:
            print("goal trouvé :", goal_pos)
            found = True
            
    if found == True:
        pos = goal_pos
        break
    
    choix_mov = random.choice(list_mov)
    pos, manhat = choix_mov
    row, col = pos

    if (grille[row][col] != "s") and (grille[row][col] != "g"):
        grille[row][col] = "."
    
for ligne in grille:
    print(''.join(ligne)) """



