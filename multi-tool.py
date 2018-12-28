#! /usr/bin/env python3

# Multi-Tool Python Version 1.0

# Calculator Version 2.2
# Colors Version 10.0
# git-status Version 2.4
# Volume Version 5.0
# iTunes Version 3.0
# Piglatin Version 0.2 (Pre-Release)

# 2019 Matthew Raimondi
# www.mattraimondi.com
# www.github.com/mattraimondi

# This script is a multiple usage script.
# You can change it's function using the variable below.
# The default setting is "calc".
# Use the "lib" option if importing this script as a library for another script.
# Options are: "lib", "colors", "calc", "git-status", "volume", "piglatin", "itunes"
USAGE = "calc"

# Importable classes in this file:
# mcolors
# operations

# MIT License
#
# Copyright (c) 2019 Matthew Raimondi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sys
import subprocess
import os
import glob

from fractions import Fraction
from decimal import Decimal
from collections import Counter

def changeFunction():
    print("Please type the function you would like this script to transform to.\nOptions are: lib, colors, calc, git-status, volume, piglatin, itunes\n")
    selection = input("New Function: ")
    with open(__file__, "r+") as k:
        code = k.read()
        targetLine = code.split('\n')[20]
        lines = code.split('\n')
        lines[20] = f"USAGE = \"{selection}\""
        code = '\n'.join(lines)
        k.seek(0)
        k.write(code)


class operations:
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / b
    def square(a, b):
        return a ** b
    def root(a, b):
        return a ** (1 / b)
    def fracdec(a):
        return Fraction(Decimal(a))
    def most_common(lst):
        data = Counter(lst)
        return max(lst, key=data.get)

class mcolors:
    
    red = "\u001b[38;5;$1m"
    orange = "\u001b[38;5;$208m"
    yellow = "\u001b[38;5;$11m"
    green = "\u001b[38;5;$2m"
    blue = "\u001b[38;5;$4m"
    indigo = "\u001b[38;5;$63m"
    violet = "\u001b[38;5;$129m"
    pink = "\u001b[38;5;$13m"
    brown = "\u001b[38;5;$130m"
    white = "\u001b[38;5;$231m"
    black = "\u001b[38;5;$0m"
    
    redback = "\u001b[48;5;$1m"
    orangeback = "\u001b[48;5;$208m"
    yellowback = "\u001b[48;5;$11m"
    greenback = "\u001b[48;5;$2m"
    blueback = "\u001b[48;5;$4m"
    indigoback = "\u001b[48;5;$63m"
    violetback = "\u001b[48;5;$129m"
    pinkback = "\u001b[48;5;$13m"
    brownback = "\u001b[48;5;$130m"
    whiteback = "\u001b[48;5;$231m"
    blackback = "\u001b[48;5;$0m"
    
    reset = "\033[0m"
    clear = "\033[0m"
    
    custpink = "\u001b[38;5;$205m"
    skyblue = "\u001b[38;5;$39m"
    
    gpink = "\033[35m"
    ggreen = "\033[92m"
    gred = "\033[91m"
    
    def printcolor(number):
        if number >= 0 and number <= 256:
            sys.stdout.write(f"\u001b[38;5;${number}m")
        else:
            raise Exception("Number must be 0-256")

    def printbackcolor(number):
        if number >= 0 and number <= 256:
            sys.stdout.write(f"\u001b[48;5;${number}m")
        else:
            raise Exception("Number must be 0-256")

    def allFG():
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                sys.stdout.write(f"\u001b[38;5;{code}m {code.ljust(4)}")
                print("\u001b[0m")

    def allBG():
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                sys.stdout.write(f"\u001b[48;5;{code}m {code.ljust(4)}")
                print("\u001b[0m")

if __name__ == "__main__" and len(sys.argv) == 2:
    if sys.argv[1] == "changeFunction":
        changeFunction()

if __name__ == "__main__" and USAGE == "calc":
    
    
    helper = f"\n\tUsage: {sys.argv[0]} <option>\n\n\tOptions:\n\tbasic\n\tfracdec\n\tfibonacci\n\tinfibonacci\n\tisfibonacci\n\ttemp\n\tgpa\n\tmmmra\n\n\t\u001b[38;5;$208mCalculator Suite by Matthew Raimondi\n\t\u001b[38;5;$39mwww.github.com/mattraimondi{mcolors.reset}\n"

    basichelp = f"\n\tUsage: {sys.argv[0]} calc <n> <operation> <n>\n\n\tOperations:\n\t+  for addition\n\t-  for subtraction\n\tx  for multiplication\n\t/  for division\n\txx for power\n\t-x for root\n\n\t\u001b[38;5;$208mCalculator by Matthew Raimondi\n\t\u001b[38;5;$39mwww.github.com/mattraimondi{mcolors.reset}\n"

    fracdechelp = f"\n\tUsage: {sys.argv[0]} fracdec <n> <operation> <n>\n\n\tOperations:\n\t. for decimal into fraction (in which case, don\'t put a third number)\n\t/ for fraction into decimal\n\n\t\u001b[38;5;$208mFraction / Decimal Converter by Matthew Raimondi\n\t\u001b[38;5;$39mwww.github.com/mattraimondi{mcolors.reset}\n"

    fibohelp = f"\n\tUsage: {sys.argv[0]} fibonacci <n>\n\t{mcolors.custpink}By Matthew Raimondi\n\twww.github.com/mattraimondi{mcolors.reset}\n"

    isfibohelp = f"\n\tUsage: {sys.argv[0]} isfibonacci <n>\n\t{mcolors.custpink}By Matthew Raimondi\n\twww.github.com/mattraimondi{mcolors.reset}\n"

    temphelp = f"\n\nHelp:\n\tUsage: {sys.argv[0]} temp <option> <n>\n\nOptions:\n\tfc: convert from fahrenheit to celcius\n\tcf: convert from celcius to fahrenheit\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"

    gpahelp = f"\n\nHelp:\n\tThe GPA program can calculate your GPA.\n\n\t*For AP classes, when asked for your letter grade, you should add AP to the end of the grade.\n\tExample: A+ -> A+AP\n\t\t A -> AAP\n\t\t A- -> A-AP\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"

    mmmrahelp = f"\n\nHelp:\n\tThe MMMRA program can calculate the Mean, Meadian, Mode, Range, and Average of a set of numbers.\n\nOptions\n\tmedian\n\tmode\n\trange\n\tmean\n\taverage\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"

    calcVersion = f"{mcolors.custpink}Calculator Version 2.2{mcolors.clear}"
    
    
    if len(sys.argv) == 1:
        print(helper)
        exit(0)

    if sys.argv[1] == "basic":
        try:
            if len(sys.argv) == 5:
                astr = sys.argv[2]
                o = sys.argv[3]
                bstr = sys.argv[4]
                a = float(astr)
                b = float(bstr)
        except Exception as e:
            print(e)
            print(basichelp)
        try:
            if o == "+":
                print(operations.add(a, b))
            elif o == "-":
                print(operations.subtract(a, b))
            elif o == "x":
                print(operations.multiply(a, b))
            elif o == "/":
                print(operations.divide(a, b))
            elif o == "xx":
                print(operations.square(a, b))
            elif o == "-x":
                print(operations.root(a, b))
        except Exception as e:
            print(e)
            print(basichelp)

    elif sys.argv[1] == "fracdec":
        try:
            if len(sys.argv) == 5:
                astr = sys.argv[2]
                o = sys.argv[3]
                bstr = sys.argv[4]
                a = float(astr)
                b = float(bstr)
            elif len(sys.argv) == 4:
                astr = sys.argv[2]
                o = sys.argv[3]
                a = float(astr)
        except Exception as e:
            print(e)
            print(fracdechelp)
        try:
            if o == ".":
                print(operations.fracdec(a))
            elif o == "/":
                print(operations.divide(a, b))
        except Exception as e:
            print(e)
            print(fracdechelp)

    elif sys.argv[1] == "fibonacci":
        def Fib(n):
            a,b = 0,1
            for i in range(n):
                a,b = b, a+b
            return a
        if len(sys.argv) == 3:
            try:
                print(Fib(int(sys.argv[2])))
            except Exception as e:
                print(e)
                print(fibohelp)
        else:
            print(fibohelp)

    elif sys.argv[1] == "infibonacci":
        try:
            a=1
            b=1
            n=1
            print(a,b,end=" ")
            while(n-2):
                c=a+b
                a=b
                b=c
                print(c,end=" ")
                n=n-1
        except:
            quit()

    elif sys.argv[1] == "isfibonacci":
        def perf(a):
            p = int(a ** (1 / 2))
            return p*p == a
        def fibc(value):
            return perf(5 * (value ** 2) + 4) or perf(5 * (value ** 2) - 4)
        if len(sys.argv) == 3:
            try:
                value = int(sys.argv[2])
                if fibc(value):
                    print(f"{value} is a fibonacci number")
                else:
                    print(f"{value} is not a fibonacci number")
            except ValueError as e:
                print(e)
                print(isfibohelp)
        else:
            print(isfibohelp)

    elif sys.argv[1] == "temp":
        def cf():
            try:
                value = float(sys.argv[3])
                fahrenheit = (value * 1.8) + 32
                return fahrenheit
            except Exception as e:
                print(e)
                print(temphelp)
        def fc():
            try:
                value = float(sys.argv[3])
                celcius = (value - 32) / 1.8
                return celcius
            except Exception as e:
                print(e)
                print(temphelp)
        if len(sys.argv) == 4:
            if sys.argv[2] == "cf":
                print(cf())
            elif sys.argv[2] == "fc":
                print(fc())
            else:
                print(temphelp)
        else:
            print(temphelp)

    elif sys.argv[1] == "gpa":
        try:
            if len(sys.argv) == 3 and sys.argv[2] in "help -h".split():
                print(gpahelp)
                quit()
            else:
                letnum = {"A+":4.3,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.7,"D+":1.3,"D":1.0,"D-":0.7,"F":0.0,"A+AP":5.3,"AAP":5.0,"A-AP":4.7,"B+AP":4.3,"BAP":4.0,"B-AP":3.7,"C+AP":3.3,"CAP":3.0,"C-AP":2.7,"D+AP":2.3,"DAP":2.0,"D-AP":1.7,"FAP":0.0}
                classes = int(input("How many classes do you take: "))
                totalscores = []
                totalcredits = []
                v = 1
                for lettergrades in range(classes):
                    print(f"\nClass {v}\n")
                    lettergrade = str(input("Letter Grade: ").upper())
                    grade = letnum[lettergrade]
                    credits = int(input("Credits: "))
                    classscore = (grade * credits)
                    totalscores.append(classscore)
                    totalcredits.append(credits)
                    v += 1
                totalscoressum = sum(totalscores)
                totalcreditssum = sum(totalcredits)
                gpa = (totalscoressum / totalcreditssum)
                print(f"\nYour GPA is a {gpa}")
        except Exception as e:
            print(e)

    elif sys.argv[1] == "mmmra":
        try:
            if sys.argv[2] == "median":
                nums = list(map(int, input("Numbers: ").split()))
                middle = int(len(nums)/2)
                nums.sort()
                print(nums[middle])
            elif sys.argv[2] == "average" or sys.argv[2] == "mean":
                nums = list(map(int, input("Numbers: ").split()))
                numsum = sum(nums)
                print(numsum/len(nums))
            elif sys.argv[2] == "mode":
                nums = list(map(int, input("Numbers: ").split()))
                nums.sort()
                print(operations.most_common(nums))
            elif sys.argv[2] == "range":
                nums = list(map(int, input("Numbers: ").split()))
                nums.sort()
                print(nums[-1] - nums[0])
            else:
                print(mmmrahelp)
        except Exception as e:
            print(e)
    elif sys.argv[1] == "-v":
        print(calcVersion)
    else:
        print(helper)



if __name__ == "__main__" and USAGE == "colors":
    
    colorfile = ""
    alist = ""
    
    colorsHelpText = f"{mcolors.reset}{mcolors.custpink}\tScript by Matthew Raimondi\n\twww.github.com/mattraimondi{mcolors.reset}\n\n\tChoose one of the following colors or\n\tspecify a number value from the chart included:\n\n\t\t{mcolors.red}Red {mcolors.orange}Orange {mcolors.yellow}Yellow {mcolors.green}Green {mcolors.blue}Blue {mcolors.indigo}Indigo {mcolors.violet}Violet\n\t\t{mcolors.pink}Pink {mcolors.brown}Brown {mcolors.white}White {mcolors.black}{mcolors.whiteback}Black{mcolors.reset}\n\n\tand then (if you want) set a backgroung using\n\tthe following colors or a number value from the preveious chart:\n\n\t\t{mcolors.white}{mcolors.redback}Redback {mcolors.orangeback}Orangeback {mcolors.yellowback}Yellowback {mcolors.greenback}Greenback {mcolors.blueback}Blueback {mcolors.indigoback}Indigoback{mcolors.reset}\n\t\t{mcolors.white}{mcolors.violetback}Violetback {mcolors.pinkback}Pinkback {mcolors.brownback}Brownback {mcolors.whiteback}{mcolors.black}Whiteback {mcolors.reset}{mcolors.blackback}{mcolors.white}Blackback{mcolors.reset}\n\n\tTo clear colors type 'Reset' instead of a color or number.\n\n\tFor a list of color numbers, use the arguments 'all' and 'allbg'\n\t\tfor text and backround colors respectively.\n\n\tExample: {sys.argv[0]} orange whiteback"
    
    if len(sys.argv) == 2:
        colorfile = (sys.argv[1])
        alist = colorfile.split(",")
    
    elif len(sys.argv) == 3:
        colorfile = (f"{sys.argv[1]},{sys.argv[2]}")
        alist = colorfile.split(",")
    
    elif len(sys.argv) == 1 or len(sys.argv) > 3:
        print(colorsHelpText)
    
    if len(sys.argv) >= 2:
        if "red" in alist:
            sys.stdout.write(mcolors.red)
        elif "orange" in alist:
            sys.stdout.write(mcolors.orange)
        elif "yellow" in alist:
            sys.stdout.write(mcolors.yellow)
        elif "green" in alist:
            sys.stdout.write(mcolors.green)
        elif "blue" in alist:
            sys.stdout.write(mcolors.blue)
        elif "indigo" in alist:
            sys.stdout.write(mcolors.indigo)
        elif "violet" in alist:
            sys.stdout.write(mcolors.violet)
        elif "pink" in alist:
            sys.stdout.write(mcolors.pink)
        elif "brown" in alist:
            sys.stdout.write(mcolors.brown)
        elif "white" in alist:
            sys.stdout.write(mcolors.white)
        elif "black" in alist:
            sys.stdout.write(mcolors.black)
        elif "reset" in alist:
            sys.stdout.write(mcolors.reset)
        elif "clear" in alist:
            sys.stdout.write(mcolors.reset)
        elif "all" in alist:
            mcolors.allFG()
        elif "allbg" in alist:
            mcolors.allBG()
        else:
            mcolors.printcolor(int(sys.argv[1]))

    if len(sys.argv) >= 3:
        if "redback" in alist:
            sys.stdout.write(mcolors.redback)
        elif "orangeback" in alist:
            sys.stdout.write(mcolors.orangeback)
        elif "yellowback" in alist:
            sys.stdout.write(mcolors.yellowback)
        elif "greenback" in alist:
            sys.stdout.write(mcolors.greenback)
        elif "blueback" in alist:
            sys.stdout.write(mcolors.blueback)
        elif "indigoback" in alist:
            sys.stdout.write(mcolors.indigoback)
        elif "violetback" in alist:
            sys.stdout.write(mcolors.violetback)
        elif "pinkback" in alist:
            sys.stdout.write(mcolors.pinkback)
        elif "brownback" in alist:
            sys.stdout.write(mcolors.brownback)
        elif "whiteback" in alist:
            sys.stdout.write(mcolors.whiteback)
        elif "blackback" in alist:
            sys.stdout.write(mcolors.blackback)
        else:
            mcolors.printbackcolor(int(sys.argv[2]))

if __name__ == "__main__" and USAGE == "git-status":

    dirs = glob.glob(f"*{os.path.sep}")
    gits = glob.glob("./*/.git")
    numgits = len(gits)

    for i in range(0, numgits):
        print(f"\n{mcolors.gpink}{gits[i]}{mcolors.clear}")
        stats = subprocess.Popen(f"cd {dirs[i]}; git status --porcelain; cd ..", shell=True, stdout=subprocess.PIPE)
        stat = str(stats.communicate()[0])
        if "M" in stat or "??" in stat:
            if "M" in stat:
                print(f"{mcolors.gred}Modified Files{mcolors.clear}")
            if "??" in stat:
                print(f"{mcolors.gred}Untracked Files{mcolors.clear}")
        else:
            print(f"{mcolors.ggreen}Clean{mcolors.clear}")

if __name__ == "__main__" and USAGE == "volume":

    helptext = f"\n{mcolors.skyblue}Volume by Matthew Raimondi\nwww.github.com/mattraimondi\n-----------------------------\nVolume Command Line Interface\n-----------------------------\nUsage: {sys.argv[0]} <option>\n\nOptions:\n\tset # = Set Volume to specified #\n\tup    = Set Volume Up 6.25\n\tdown  = Set Volume Down 6.25\n\tup1   = Set Volume Up 1\n\tdown1 = Set Volume Down 1\n\tget   = Get Volume Settings\n\tmute  = Mute Volume\n\thelp  = Show This Help Text{mcolors.clear}\n"

    versionnum = f"{mcolors.skyblue}5.0{mcolors.clear}"

    for arg in sys.argv:
        if arg == "up":
            print(f"{mcolors.skyblue}Changing Volume Level{mcolors.clear}")
            subprocess.run("osascript -e 'set volume output volume (output volume of (get volume settings) + 6.25)'", shell=True)
        elif arg == "down":
            print(f"{mcolors.skyblue}Changing Volume Level{mcolors.clear}")
            subprocess.run("osascript -e 'set volume output volume (output volume of (get volume settings) - 6.25)'", shell=True)
        elif arg == "up1":
            print(f"{mcolors.skyblue}Changing Volume Level{mcolors.clear}")
            subprocess.run("osascript -e 'set volume output volume (output volume of (get volume settings) + 1)'", shell=True)
        elif arg == "down1":
            print(f"{mcolors.skyblue}Changing Volume Level{mcolors.clear}")
            subprocess.run("osascript -e 'set volume output volume (output volume of (get volume settings) - 1)'", shell=True)
        elif arg == "get":
            print(f"{mcolors.skyblue}Getting Volume Level{mcolors.clear}")
            subprocess.run("osascript -e 'get volume settings'", shell=True)
        elif arg == "mute":
            print(f"{mcolors.skyblue}Muting{mcolors.clear}")
            subprocess.run("osascript -e 'set volume output volume 0'", shell=True)
        elif arg == "set":
            print(f"{mcolors.skyblue}Changing Volume Level{mcolors.clear}")
            subprocess.run(f"osascript -e 'set volume output volume {sys.argv[2]}'", shell=True)
        elif arg == "help":
            print(helptext)
        elif arg == "-h":
            print(helptext)
        elif arg == "-v":
            print(versionnum)
        elif len(sys.argv) == 1:
            print(helptext)

if __name__ == "__main__" and USAGE == "piglatin":

    newlist = []

    def helper():
        print(f"\n\nHelp:\n\tUsage: {sys.argv[0]} <option>\n\nOptions:\n\tengpig: translate from english to piglatin\n\tpigeng: translate from piglatin to english\n\n\n\u001b[38;5;$205mBy Matthew Raimondi\nwww.github.com/mattraimondi\033[0m\n")
        quit()

    def engpig(*args):
        try:
            alist = list(args)
            
            for word in alist:
                firstletter = word[0]
                secondletter = word[1]
                thirdletter = word[2]
                if firstletter.lower() in "aeiou":
                    pigword = word + "ay"
                    newlist.append(pigword)
                elif firstletter.lower() == "c" and secondletter.lower() == "e" or secondletter.lower() == "i":
                    pigword = word[1:] + "say"
                    newlist.append(pigword)
                elif firstletter.lower() == "g" and secondletter.lower() == "e" or secondletter.lower() == "i":
                    pigword = word[1:] + "jay"
                    newlist.append(pigword)
                elif firstletter.lower() not in "aeiou" and secondletter.lower() not in "aeiou" and thirdletter.lower() not in "aeiou":
                    pigword = word[3:] + firstletter + secondletter + thirdletter + "ay"
                    newlist.append(pigword)
                elif firstletter.lower() not in "aeiou" and secondletter.lower() not in "aeiou":
                    pigword = word[2:] + firstletter + secondletter + "ay"
                    newlist.append(pigword)
                else:
                    pigword = word[1:] + firstletter + "ay"
                    newlist.append(pigword)
            return newlist
        except:
            helper()

    def pigeng(*args):
        pass

    if len(sys.argv) == 2:
        if sys.argv[1] == 'engpig':
            sentence = input("Sentence: ").lower()
            sentlist = sentence.split(" ")
            while len(newlist) < len(sentlist):
                engpig(sentence)
            newstr = " ".join(newlist)
            print(newstr)
        elif sys.argv[1] == 'pigeng':
            print("Awaiting build")
        else:
            helper()
    else:
        helper()

if __name__ == "__main__" and USAGE == "itunes":
    
    volumeHelp = f"\n{mcolors.custpink}iTunes-CLI by Matthew Raimondi\nwww.github.com/mattraimondi\n-----------------------------\niTunes Command Line Interface\n-----------------------------\nUsage {sys.argv[0]} <option>\n\nOptions:\n\tstatus   = Shows iTunes' status, current artist and track.\n\tplay     = Start playing iTunes.\n\tpause    = Pause iTunes.\n\tnext     = Go to the next track.\n\tprev     = Go to the previous track.\n\tmute     = Mute iTunes' volume.\n\tunmute   = Unmute iTunes' volume.\n\tvol up   = Increase iTunes' volume by 10%\n\tvol down = Increase iTunes' volume by 10%\n\tvol #    = Set iTunes' volume to # [0-100]\n\tstop     = Stop iTunes.\n\tquit     = Quit iTunes.{mcolors.reset}\n"

    for arg in sys.argv:
        if arg == "status":
            curState = subprocess.Popen(f"osascript -e 'tell application \"iTunes\" to player state as string'", shell=True, stdout=subprocess.PIPE)
            state = str(curState.communicate()[0].decode("utf-8")).strip('\n')
            print(f"iTunes is currently {state}")
            if state == "playing":
                curArtist = subprocess.Popen(f"osascript -e 'tell application \"iTunes\" to artist of current track as string'", shell=True, stdout=subprocess.PIPE)
                curTrack = subprocess.Popen(f"osascript -e 'tell application \"iTunes\" to name of current track as string'", shell=True, stdout=subprocess.PIPE)
                artist = str(curArtist.communicate()[0].decode("utf-8")).strip('\n')
                track = str(curTrack.communicate()[0].decode("utf-8")).strip('\n')
                print(f"Current track {artist} {track}")
        elif arg == "vol":
            curVol = subprocess.Popen(f"osascript -e 'tell application \"iTunes\" to sound volume as integer'", shell=True, stdout=subprocess.PIPE)
            vol = int(curVol.communicate()[0])
            newVol = ""
            try:
                if sys.argv[2] == "up":
                    print("Volume Up...")
                    newVol = str(vol + 10)
                elif sys.argv[2] == "down":
                    print("Volume Down...")
                    newVol = str(vol - 10)
                else:
                    newVol = sys.argv[2]
                    print(f"Volume set to {newVol}")
            except IndexError:
                print("\aPlease be sure that there exists a second command line argument and that it is either \"up\", \"down\" or a number between 0-100.")
            subprocess.run(f"osascript -e 'tell application \"iTunes\" to set sound volume to {newVol}'", shell=True)
        elif arg == "mute":
            print("Muting...")
            subprocess.run("osascript -e 'tell application \"iTunes\" to set mute to true'", shell=True)
        elif arg == "unmute":
            print("Unmuting...")
            subprocess.run("osascript -e 'tell application \"iTunes\" to set mute to false'", shell=True)
        elif arg == "play":
            print("Playing...")
            subprocess.run("osascript -e 'tell application \"iTunes\" to play'", shell=True)
        elif arg == "pause":
            print("Pausing...")
            subprocess.run("osascript -e 'tell application \"iTunes\" to pause'", shell=True)
        elif arg == "next":
            print("Going to next track...")
            subprocess.run("osascript -e 'tell application \"iTunes\" to next track'", shell=True)
        elif arg == "prev":
            print("Going to previous track...")
            subprocess.run("osascript -e 'tell application \"iTunes\" to previous track'", shell=True)
        elif arg == "stop":
            print("Stopping iTunes...")
            subprocess.run("osascript -e 'tell application \"iTunes\" to stop'", shell=True)
        elif arg == "quit":
            print("Stopping iTunes...")
            subprocess.run("osascript -e 'tell application \"iTunes\" to quit'", shell=True)
        elif len(sys.argv) == 1:
            print(volumeHelp)

if __name__ == "__main__" and USAGE == "blink1-matt":

    from blink1.blink1 import Blink1

    myblink = Blink1(serial_number=u'2000D103')
    myblink.fade_to_color(1000, 'turquoise')
    myblink.close()
