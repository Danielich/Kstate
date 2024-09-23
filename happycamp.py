print("‘T’ mean the statement is positive. ‘N’ means it is negative. ‘H’ means here. \n Theletters R, Y, B, G mean red, yellow, blue and green respectively. ")
user_input = input("Enter your situation: ")
user_input = user_input.replace(" ", "")
sign_bool = []
cases = []
tents= ["R", "Y", "B", "G"]
solution = []

def get_signs():
    global tent
    tent = []
    add = 0
    for i in range(4):
        tent.append(user_input[add:add+2])
        add+=2
def evaluate():
    color = ""
    global sign
    sign = ""
    for i in range(4):
        color = tents[i]
        for k in tent:
            if "N" in k:
                if "H" in k:
                    sign_bool.append(0)
                if color in k:
                    sign_bool.append(0)
                else:
                    sign_bool.append(1)
            if "T" in k:
                if "H" in k:
                    sign_bool.append(1)
                if color in k:
                    sign_bool.append(0)
                else:
                    sign_bool.append(0)
        if sum(sign_bool) == 1:
            cases.append(sign_bool)
            if sign_bool[0] == 1:
                sign = "Red"
            elif sign_bool[1] == 1:
                sign = "Yellow"
            elif sign_bool[2] ==1:
                sign = "Blue"
            elif sign_bool[3] == 1:
                sign = "Green"
            sign_bool.clear()

            if color == "R":
                solution.append("red")
            if color == "Y":
                solution.append("yellow")
            if color == "B":
                solution.append("blue")
            if color == "G":
                solution.append("green")
            
    if len(solution) > 0:
        print("Your sleeping bag is in the {0} tent. {1} sign is true !".format(solution[0],sign))
    else:
        print("No solution")

if __name__ == '__main__': 
    get_signs()
    evaluate()





