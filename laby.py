import random


grille = [["#" for i in range(10)] for j in range(10)]

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
    col = col+1
    row_g, col_g = goal_pos

    if col >= len(grille[0]):
        return None
    
    if grille[row][col] == "g":
        goal_pos = (row_g, col_g)
        return (goal_pos)
    
    manhat_new = abs(row - row_g) + abs( col - col_g)

    if (manhat_new < manhat) and (grille[row][col] != "s"):
        grille[row][col] = "."
        manhat = manhat_new
        pos = (row, col)
        return (pos, manhat)
    return None

        


# on calcul manat a la position pos
# on part de pos on test +1 right
# on calcul manat_2 
# si manat_2 < manat et que (row_s, col_s + 1) != "g" et que (col_s + 1 ) < 10 :
# on ecrit un "." à la coord (row_s, col_s +1)
# elif (row_s, col_s +1) == "g" : break



for ligne in grille:
    print(''.join(ligne))







