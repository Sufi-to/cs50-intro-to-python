
def main():
    temp = get_fuel()
    if temp >=99:
        print("F")
    elif temp <=1:
        print('E')
    else:
        print(f"{temp}%")


def get_fuel():
    temp=0
    while True:
        try:
            n = input("enter a fraction: ").split("/")

            s=int(n[0])
            b= int(n[1])
            if s > b:
                continue

            temp= round((s/b)*100)

        except (ZeroDivisionError, ValueError):
            pass

        else:
            return temp


main()