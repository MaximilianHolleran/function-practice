def pascal(n):
    if n <= 0:
        return "Please provide a positive integer for the number of rows."
    
    triangle = [[1]]  

    for i in range(1, n):
        row = [1]  
        last_row = triangle[-1]
        
        for j in range(1, i):
            row.append(last_row[j-1] + last_row[j])
        
        row.append(1)  
        triangle.append(row)

    for row in triangle:
        print(" ".join(map(str, row)).center(n*2))


pascal(5)
