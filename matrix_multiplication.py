rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])
    
    C = [[0]*colsB for _ in range(rowsA)]
    print(rowsB,colsA)
    if colsA != rowsB:
        return -1
    
    for i in range(rowsA):
        for j in range(colsB):
            cur_sum = 0
            for k in range(colsA):
                valA = A[i][k] 
                valB = B[k][j]
                
                if valA !=0 and valB != 0:
                    cur_sum += valA * valB
                    
            C[i][j] = cur_sum
        
    return C 
