user1 = input("Grettings: ")
user1 = user1.strip()
user1 = user1.casefold()


if user1.startswith("hello")== True:
    print("$0")
elif user1.startswith("h") == True and user1.startswith("hello")==False:
    print("$20")
else:
    print("$100")
