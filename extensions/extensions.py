exten = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]

userinp = input("File name: ").casefold().strip()

count=0
for i in range(len(exten)):
    if userinp.endswith(exten[i]) == True:
        if exten[i]== "jpeg" or exten[i]=="jpg":
            print("image/jpeg")
        elif exten[i]== "png" or exten[i] == "gif":
            print(f"image/{exten[i]}")

        elif exten[i]== "pdf" or exten[i]=="zip":
            print(f"application/{exten[i]}")
        elif exten[i]=="txt":
            print("text/plain")
    else:
        count+=1
if count==7:
    print("application/octet-stream")


