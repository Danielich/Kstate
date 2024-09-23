
row0= [0,0,0]

row1= [0,0,0]
row2 = [0,0,0]

a = int(input("Enter value at row 0, column 0: "))
row0[0] = a
b = int(input("Enter value at row 0, column 1: "))
row0[1] = b
c = int(input("Enter value at row 0, column 2: "))
row0[2] = c
d = int(input("Enter value at row 1, column 0: "))
row1[0]= d

total = sum(row0)
if (row0[0] + row1[0]) < total:
    row2[0] = total - (row0[0] + row1[0])
    if (row0[2] + row2[0]) < total:
        row1[1] = total - (row0[2] + row2[0])
        if (row0[1] + row1[1]) < total: 
            row2[1] = total - (row0[1] + row1[1])
            if (row2[0] + row2[1]) < total:
                row2[2] = total - (row2[0] + row2[1])
                if (row1[0] + row1[1]) < total: 
                    row1[2] = total - (row1[0] + row1[1])
                else:
                     print("No magic squares")
            else:
                 print("No magic squares")
        else:
            print("No magic squares")
    else:
        print("No magic squares")
else:
    print("No magic squares")
print(row0)
print(row1)
print(row2)
