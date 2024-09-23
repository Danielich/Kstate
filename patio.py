num = int(input("enter number of row and columns: "))
if num%2 !=0:
    exit(1)
rows = [[],[],[],[]]
columns = [[],[],[],[]]

for j in range(num):
    row = input("Enter the style of the row: ")
    for i in row:
        if row.count(i) > 1:
            rows[j].append(i)
        else: 
            exit(1)
    for j in range(num):
        
        columns[j].append(row[j])
for i in range(num):
    for j in columns[i]:
        if columns[i].count(j) == 1:
            exit(2)
        
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

                
            

