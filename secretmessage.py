key = int(input("Enter the encryption key: "))
num_digit = int(input("Enter the number of digits: "))
digits =[]
keys = [0,1,2,3,4,5,6,7,8,9]
encrypted = []
decrypted = []
for i in range(num_digit):
    digit = int(input(f"Enter digit number {i+1}: "))
    digits.append(digit)
for i in digits:
    if i in keys:
        for j in range(keys.index(i)):
            keys.append(keys[0])
            keys.remove(keys[0])
        newi = keys[key%10]
        encrypted.append(newi)
        newi = 0
for i in encrypted: print(i, end="")
key2 = int(input("\nEnter the encryption key: "))
for i in encrypted:
    if i in keys:
        for j in range(keys.index(i)):
            keys.append(keys[0])
            keys.remove(keys[0])
        newi = keys[-1*key2%10]
        decrypted.append(newi)
        newi = 0
for i in decrypted: print(i, end="")
