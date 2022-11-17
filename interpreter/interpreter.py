user_inp = input("Expression: ").strip()

x, y, z = user_inp.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "/":
    print(float(x) / float(z))