suits = ''
ranks = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

colors = []
user_input = input("Enter color: ")
for i in user_input:
    colors.append(i)
for i in range(5):
    if colors[i] == "R":
        if colors[i+1] =="B":
            suits = "Diamonds"
        if colors[i+1] == "R":
            suits = "Hearts"
    if colors[i] == "B":
        if colors[i+1] == "B":
            suits = "Spades"
        if colors[i+1] == "R":
            suits = "Clubs"
    rank = 0
    if colors[i+2] == "B":
        rank +=4
    if colors[i+3] == "B":
        rank+=2
    if colors[i+4] == "B":
        rank+=1
    

    if rank== 1 and (suits== "Hearts" or suits == "Clubs") or rank == 2:
        colors += colors[i]
    else:
        if colors[i] == "B":
            colors += "R"
        if colors[i] == "R":
            colors +="B"
   
    

    print("{} of {}".format(ranks[rank], suits))
    

    

            
    




