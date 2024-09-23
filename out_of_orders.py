orders = [order for order in input("Enter sixe of your order numbers chronologically:").split()]

kioks1 = []
kioks2 = []
kioks3 = []

for order in orders:
    if int(order) >= 100 and int(order) < 200:
        kioks1.append(order)
    if int(order) >= 200 and int(order) < 300:
        kioks2.append(order)
    if int(order) >= 300 and int(order) < 400:
        kioks3.append(order)
initial = kioks1[0]
out_orders = 0 

for i in kioks1:
        if i < initial:
            out_orders += 1
        if i > initial:
            initial = i
if len(kioks2) > 0:
    initial = kioks2[0]
    for i in kioks2:
        if i < initial:
            out_orders += 1
        if i > initial:
            initial = i

if len(kioks3) > 0:
    initial = kioks3[0]
    for i in kioks3:
        if i < initial:
            out_orders += 1
        if i > initial:
            initial = i
print("Out of orders: {}".format(out_orders))






