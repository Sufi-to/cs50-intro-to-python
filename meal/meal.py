def convert(t):
    t = t.strip()
    t = t.split(":")
    o = float(t[0])
    p = float(t[1]) / 60

    return o + p

def main():
    x=convert(input("What time is it? "))
    if x>=7 and x<=8:
        print("breakfast time")
    elif x>=12 and x<=13:
        print("lunch time")
    elif x>=18 and x<=19:
        print("dinner time")

if __name__ == "__main__":
    main()