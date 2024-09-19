num = int(input("enter number of row and columns: "))
rows = []
columns = [[],[],[],[]]
for i in range(num):
    row = input("Enter the style of the row: ")
    rows.append(row)
    for i in range(num):
        columns[i].append(row[i])

