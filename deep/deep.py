answer = input("what is the answer for the question? ")
answer = answer.strip()
if answer == "42" or answer.casefold()=="forty-two" or answer.casefold() == "forty two":
    print("Yes")
else:
    print("No")