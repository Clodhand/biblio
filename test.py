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

# mouvement hors grille
def mov_hors_grille(pos, grille):
    row, col = pos
    if (col >= len(grille[0])) or (row >= len(grille)) or (col < 0) or (row < 0):
        return None
    
# liste des mouvement valide qui reduisent manhat

def list_move_manhat(pos, goal_pos, manhat, grille)
    list_moves =[]
    raw, col = pos
    raw_g, col_g = goal_pos
    col_right = col + 1
    pos_right = (raw, col_right)
    if mov_hors_grille(pos_right, grille) == None:
        
    manhat_new = abs ()
