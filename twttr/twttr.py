cstr = list(input("Input: "))

vowels= ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for i in range(len(cstr)):
    if cstr[i] in vowels:
        cstr[i]= ""



print("Output: ", end="")
print("".join(cstr))

