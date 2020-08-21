mat_1 = [[4, 5, 10],
         [7, -3, 2],
         [4, 6, 9]]
mat_2 = [[7, -2, 3],
         [3, -9, -1],
         [4, 10, 11]]

answer_mat = [[[],[],[]],
            [[],[],[]],
            [[],[],[]]]

for index_r in range(len(mat_1)):
    for index_c in range(len(mat_1[index_r])) :

        answer_mat[index_r][index_c] = mat_1[index_r][index_c] + mat_2[index_r][index_c]

print(answer_mat)
