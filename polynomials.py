import numpy 
n = int(input("Enter n: "))
roots = []
for i in range(n):
    root = int(input(f"Enter root {i+1}"))
    roots.append(root)
print(numpy.poly(roots))
