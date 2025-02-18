x = input("Enter a number")

print(x)
for i in x:
    if i in ['1','2','3','4','5','6','7','8','9','0','.','-']:
        print(f"{i} is a valid character for number")
    else:
        print(f"{i} is not a valid number character")

#x = int(x)