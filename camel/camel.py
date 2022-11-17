user_in= input("camelCase: ").strip()
new_wor= user_in[0]

for i in range(1, len(user_in)):
    if user_in[i]== user_in[i].upper():
        new_wor+="_"
        new_wor+=user_in[i].lower()
    else:
        new_wor+= user_in[i]

print(f"snake_name: {new_wor}")
