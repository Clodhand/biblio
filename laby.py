import random


grille = [["#" for i in range(10)] for j in range(10)]
for ligne in grille:
    print(''.join(ligne))

# on pose le s
row_s = random.randint(0,9)
col_s = random.randint(0,9)
grille[row_s][col_s] = "s"

# on pose le g
row_g = row_s
col_g = col_s
while (row_g, col_g) == (row_s, col_s):
    row_g =random.randint(0,9)
    col_g = random.randint(0,9)
grille[row_g][col_g] = "g"

goal_pos = (row_g, col_g)
pos = (row_s, col_s)

manhat = abs(row_s -row_g) + abs( col_s - col_g)

def digg_right(pos, goal_pos, manhat, grille ):
    row, col = pos
    print(pos)
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
    if (manhat_new < manhat) and (grille[row][col] != "s"):
        grille[row][col] = "."
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
    if (manhat_new < manhat) and (grille[row][col] != "s"):
        grille[row][col]= "."
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
    if (manhat_new < manhat) and (grille[row][col] != "s"):
        grille[row][col]= "."
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
    if (manhat_new < manhat) and (grille[row][col] != "s"):
        grille[row][col] = "."
        return (pos, manhat_new)
    return None

while True:
    right = digg_right(pos, goal_pos, manhat, grille)
    print(right)
    if right != None:
        pos, manhat = right
        if pos == goal_pos:
            break
    down = digg_down(pos, goal_pos, manhat, grille)
    if down != None:
        pos, manath = down
        if pos == goal_pos:
            break
    left = digg_left(pos, goal_pos, manhat, grille)   
    if left != None:
        pos, manath = left
        if pos == goal_pos:
            break
    up = digg_up(pos, goal_pos, manhat, grille)
    if up != None:
        pos, manhat = up
        if pos == goal_pos:
            break
    else:
        break    

for ligne in grille:
    print(''.join(ligne))







