import random


grille = [["#" for i in range(40)] for j in range(40)]
""" for ligne in grille:
    print(''.join(ligne)) """

# on pose le s
row_s = random.randint(0,39)
col_s = random.randint(0,39)
grille[row_s][col_s] = "s"

# on pose le g
row_g = row_s
col_g = col_s
while (row_g, col_g) == (row_s, col_s):
    row_g =random.randint(0,39)
    col_g = random.randint(0,39)
grille[row_g][col_g] = "g"

goal_pos = (row_g, col_g)
pos = (row_s, col_s)

manhat = abs(row_s -row_g) + abs( col_s - col_g)

def digg_right(pos, goal_pos, manhat, grille ):
    row, col = pos
    
    col = col+1
    row_g, col_g = goal_pos
    pos = (row, col)

    # si hors grille
    if col >= len(grille[0]):
        return None
    
    manhat_new = abs(row - row_g) + abs( col - col_g)
    
    # si on est sur g
    if grille[row][col] == "g":
        return (pos, manhat_new)
    
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
    print(''.join(ligne))



""" 
    right = digg_right(pos, goal_pos, manhat, grille)
    print(right)
    if right != None:
        pos, manhat = right
        if pos == goal_pos:
            break
        continue
    down = digg_down(pos, goal_pos, manhat, grille)
    if down != None:
        pos, manhat = down
        if pos == goal_pos:
            break
        continue
    left = digg_left(pos, goal_pos, manhat, grille)   
    if left != None:
        pos, manhat = left
        if pos == goal_pos:
            break
        continue
    up = digg_up(pos, goal_pos, manhat, grille)
    if up != None:
        pos, manhat = up
        if pos == goal_pos:
            break
        continue
    print("c'est bloqué")     """



