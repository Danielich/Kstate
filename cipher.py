text = input("Enter your text: ")
prompt = input("Do you want to (D)ecode or (E)ncode: ")
num_letters = int(input("Enter the starting letter: "))
a_z = []
initial_a = "a"
z_a = []
initial_z = "z"
letters = []

cipher = []
for i in range(0,26):
    a_z.append(initial_a)
    initial_a = chr(ord(initial_a)+1)
for i in range(0,26):
    z_a.append(initial_z)
    initial_z = chr(ord(initial_z)-1)
for i in text:
    letters.append(i.lower())
if prompt == "E":
    for letter in letters:
        if letter in a_z:
            for i in range(a_z.index(letter)):
                a_z.append(a_z[0])
                a_z.remove(a_z[0])
        cipher.append(a_z[num_letters])
    print(cipher)

            
    
        
    
    


     
