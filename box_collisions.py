numbox = int(input("Please type in numbers or rectangles: "))
width = int(input("Enter the definite width of {} rectangles:  ".format(numbox)))
height = int(input("Enter the definite height of {} rectangles:  ".format(numbox)))
x = []
y = []
numcollision = 0
for box in range(1, numbox+1):
    xcor= int(input("Enter x cordinate of rectangle {}: ".format(box)))
    x.append(xcor)   
    ycor= int(input("Enter y cordinate of rectangle {}: ".format(box)))
    y.append(ycor)
a = 1
for i in range(len(x)):
    for i in range(len(x)-1):
        if (abs(x[0] - x[i+1])) < width and (abs(y[0] - y[i+1])) < height:
            numcollision += 1
        i +=1
        a+= 1
    x.remove(x[0])
    y.remove(y[0])

print(numcollision)




