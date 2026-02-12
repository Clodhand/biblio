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
manat = abs(row_s -row_g) + abs(col_s - col_g)

while pos != goal_pos:
    pos = (row_s + 1, col_s)
    add_row = row_s + 1
    manat_1 = abs(add_row - row_g) + abs(col_s - col_g)
    if manat_1 < manat:
        grille[add_row][col_s] = "."
    else:
        add_col = col_s + 1
        manat_1 = abs(row_s - row_g) + abs(add_col - col_g)
        if manat_1 < manat:
            grille[row_s][add_col] = "."




for ligne in grille:
    print(''.join(ligne))
