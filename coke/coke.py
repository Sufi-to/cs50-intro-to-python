amount_due = 50
print(f"Amount Due: {amount_due}")
while amount_due > 0:
    pay = int(input("Insert Coin: "))
    if pay == 25 or pay == 10 or pay == 5:
        if pay >50:
            print(f"Change Owed: {abs(amount_due - pay)}")
            break
        elif pay == 50:
            amount_due-=pay
            print(f"Amount Due: {amount_due}")
            break

        elif amount_due > pay:
            amount_due-=pay
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Change Owed: {abs(amount_due - pay)}")
            break

    else:
        print(f"Amount Due: {amount_due}")




