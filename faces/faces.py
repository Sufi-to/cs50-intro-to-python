

def convert(s):
    x = s.split(" ")

    for i in range(len(x)):
        if x[i] == ":)":
            x[i] = "🙂"
        elif x[i] ==":(":
            x[i] = "🙁"
        i+=1

    x = " ".join(x)
    return x

def main():
    message= convert(input())
    print(message)

if __name__ == "__main__":
    main()

