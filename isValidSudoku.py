def main():
    print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]))


def isValidSudoku(board):
    rows = [{} for x in range(9)]
    cols = [{} for x in range(9)]
    sqas = [{} for x in range(9)]
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col != '.':
                if col in rows[i] or col in cols[j]:
                    return False
                rows[i][col] = 1
                cols[j][col] = 2
                if i // 3 == 0 and j // 3 == 0:
                    if col in sqas[0]:
                        return False
                    else:
                        sqas[0][col] = 3
                elif i // 3 == 1 and j // 3 == 0:
                    if col in sqas[1]:
                        return False
                    else:
                        sqas[1][col] = 3
                elif i // 3 == 2 and j // 3 == 0:
                    if col in sqas[2]:
                        return False
                    else:
                        sqas[2][col] = 3
                elif i // 3 == 0 and j // 3 == 1:
                    if col in sqas[3]:
                        return False
                    else:
                        sqas[3][col] = 3
                elif i // 3 == 1 and j // 3 == 1:
                    if col in sqas[4]:
                        return False
                    else:
                        sqas[4][col] = 3
                elif i // 3 == 2 and j // 3 == 1:
                    if col in sqas[5]:
                        return False
                    else:
                        sqas[5][col] = 3
                elif i // 3 == 0 and j // 3 == 2:
                    if col in sqas[6]:
                        return False
                    else:
                        sqas[6][col] = 3
                elif i // 3 == 1 and j // 3 == 2:
                    if col in sqas[7]:
                        return False
                    else:
                        sqas[7][col] = 3
                elif i // 3 == 2 and j // 3 == 2:
                    if col in sqas[8]:
                        return False
                    else:
                        sqas[8][col] = 3
    print(rows)
    print(cols)
    print(sqas)
    return True


if __name__ == '__main__':
    main()
