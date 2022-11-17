def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.strip()
    if two_letter(s):
        if len_char(s):
            if mid_num(s):
                if isal_isnum(s):
                    return True
# while true:
#  if two_letter(s) and len_char(s) and mid_num(s) and isal_isnum(s):
#      return True
#  else:
#      return False
    else:
        return False




def two_letter(a):
    v = a[:2]
    try:
        v=int(v)
        return False
    except ValueError:
        return True

def len_char(l):
    if len(l) >= 2 and len(l) <= 6:
        return True
    else:
        return False

def mid_num(s):
    temp=""
    pos= 0
    count=0
    if s.isalpha():
        return True
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            temp += s[i]
            pos=i
            if temp[0] == "0":
                return False
            elif temp[0]!=0:
                for i in range(pos,len(s)):
                    count+=1
                    if s[i].isalpha()==True:
                        return False
                    else:
                        continue
                if count==len(s)-pos:
                    return True




def isal_isnum(h):
     count = 0

     for i in h:
        if i.isdigit() | i.isalpha():
            count=count + 1
        else:
            return False

     if count==len(h):
            return True





main()