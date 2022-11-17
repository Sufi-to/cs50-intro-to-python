grocery_list={}
fis=list()
while True:
    try:
        grocery_item= input().strip().upper()
        if grocery_item not in grocery_list:
            grocery_list[grocery_item]= 1

        else:
            x = grocery_list.get(grocery_item) + 1
            grocery_list[grocery_item]=x



    except EOFError:
        h=list(grocery_list)
        h.sort()


        for i in h:

            print(f"{grocery_list[i]} {i}")
        break

    else:
        continue
