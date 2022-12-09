r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))

matrix = []

for i in range(r):

    # Append an empty sublist inside the list

    matrix.append([])

    for j in range(c):

        matrix[i].append(j)

# print(matrix)
counter = 1

for k in range(r+c-1):
    for j in range(k+1):
        i = k-j

        if (i < r and j < c):
            matrix[i][j] = counter
            counter += 1

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end="  ")
    print()