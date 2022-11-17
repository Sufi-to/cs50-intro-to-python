months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
            "October", "November", "December"]



try:
    user1= input("enter a date that has mm-dd-yyyy or like august 9, 1892: ")
    if user1[0].isdigit():
        user1=user1.split("/")
    elif user1[0].isalpha():
        user1=user1.split(" ")
except:
    pass
else:
    continue
