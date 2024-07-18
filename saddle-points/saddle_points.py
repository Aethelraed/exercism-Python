def saddle_points(matrix):
    if len(set(len(i) for i in matrix))>1: raise ValueError("irregular matrix")
    c,d = [[i == max(x) for i in x] for x in matrix],list(zip(*[[i == min(x) for i in x] for x in zip(*matrix)]))
    return [{"row":i+1, "column":j+1} for i in range(len(matrix)) for j in range(len(matrix[i])) if c[i][j] and d[i][j]]
    