from pyfiglet import Figlet

import sys
import random



figlet = Figlet()
f = figlet.getFonts()


if len(sys.argv)==1:
    x = input("Input: ")
    num= random.randint(0, 424)
    f = f[num]
    figlet.setFont(font=f)
    print(figlet.renderText(x))
elif len(sys.argv)==3 and (sys.argv[1]== "-f" or sys.argv[1]=="--font") and (sys.argv[2] in f):
    x = input("Input: ")
    f = sys.argv[2]
    figlet.setFont(font=f)
    print(figlet.renderText(x))
else:
    sys.exit("not accurate arguments.")




