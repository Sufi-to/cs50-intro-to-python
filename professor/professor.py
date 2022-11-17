from random import randint


def main():
    ...


def get_level():
    while True:
        level = input("Level: ")
        if x != "1" | x != "2" | x != "3":
            continue
        else:
            generate_integer(level)



def generate_integer(level):
    count = 0
    if level == "1":
        for i in range(10):
            s = randint(0, 9)
            d = randint(0, 9)
            print(f"{s} + {d} = ", end = "")
            user = int(input())
            if s + d == user :
                count+=1
                continue
            else:
                print("EEE")


if __name__ == "__main__":
    main()