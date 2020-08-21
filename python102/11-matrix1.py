mat_1 = [[4, 5],
         [7, -3]]
mat_2 = [[7, -2],
         [3, -9]]

answer_mat = [[[],[]],
            [[],[]]]

for index_r in range(len(mat_1)):
    for index_c in range(len(mat_1[index_r])) :

        answer_mat[index_r][index_c] = mat_1[index_r][index_c] + mat_2[index_r][index_c]

print(answer_mat)
