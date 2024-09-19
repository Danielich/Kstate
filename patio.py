num = int(input("enter number of row and columns: "))
rows = [[],[],[],[]]
columns = [[],[],[],[]]

for j in range(num):
    row = input("Enter the style of the row: ")
    for i in row:
            rows[j].append(i)
    for j in range(num):
        columns[j].append(row[j])

for j in rows:
    for k in range(num):
        if j[0] == j[1] and j[0] == j[2]:
            print(False)
            break
        else:
            j.append(j[0])
            j.remove(j[0])
for j in columns:
    for k in range(num):
        if j[0] == j[1] and j[0] == j[2]:
            print(False)
            break
        else:
            j.append(j[0])
            j.remove(j[0])
            continue
    print(True)
    break
