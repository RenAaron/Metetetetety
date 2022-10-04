import meteo
from turtle import *

meteo.background()
penup()
speed(0)

def getNumber(stri):
    rv = ""
    skips = 0
    for x in stri:
        if(x.isdigit() or x == "-"):
            skips += 1
            rv += x
        else:
            return str(skips) + rv

def scanCommand(stri):
    n = 0
    while(n<=len(stri)-1):
        if(stri[n] == "S"):
            meteo.draw_sun()
        elif (stri[n] == "C"):
            meteo.draw_cloud()
        elif (stri[n] == "P"):
            meteo.draw_sun()
            meteo.draw_cloud()
        elif (stri[n] == "R"):
            meteo.draw_cloud()
            meteo.draw_rain()
        elif (stri[n] == "W"):
            meteo.draw_snow()
        elif (stri[n] == "A"):
            n += 1
            r = getNumber(stri[n:])[1:]
            n += int(getNumber(stri[n:])[0]) - 1
            color("red")
            pendown()
            width(2)
            circle(int(r))
            width(1)
            penup()
        elif (stri[n] == "T"):
            n += 1
            t1 = getNumber(stri[n:])[1:]
            n += int(getNumber(stri[n:])[0]) - 1
            color("white")
            begin_fill()
            meteo.draw_rectangle(24,18)
            end_fill()
            color("black")
            write(t1 + "F")
        elif(stri[n] == "G"):
            n += 1
            x1 = getNumber(stri[n:])[1:]
            n += int(getNumber(stri[n:])[0]) + 1
            y1 = getNumber(stri[n:])[1:]
            n += int(getNumber(stri[n:])[0]) - 1
            goto(int(x1),int(y1))
        n += 1


def main():
    scanCommand(input("Give meteo command: ")+"*")
    done()

if(__name__ == "__main__"):
    main()
