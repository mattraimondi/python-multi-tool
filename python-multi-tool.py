#! /usr/bin/env python3

# Multi-Tool Python Version 2.0.0

# Latest Updates:
#   - I have chosen to remove any code not written by me and any extraneous code that clutters the program to improve functionality and to showcase my work alone. Therefore, the cryptography library, jpy are not longer available, but if you require them, they can still be found in older versions of the script at www.github.com/mattraimondi/python-multi-tool

# Calculator Version 2.2.0
# Colors Version 2.0.0
# git-status Version 2.4.0
# Volume Version 5.0.0
# iTunes Version 3.0.0
# Piglatin Version 1.0.0
# Numbers Game Version 1.1.0
# PCB Version 1.0.0

# Version Variables
calcVersion = "2.2.0"
volumeVersion = "5.0.0"

# 2020 Matthew Raimondi
# www.mattraimondi.com
# www.github.com/mattraimondi
# www.github.com/mattraimondi/python-multi-tool

# This script is a multiple usage script.
# You can change it's function using the variable below or by using the changeFunction option built into the script (recommended).
# The default setting is "calc".
# Use the "lib" option if importing this script as a library for another script.

funcOptions = "lib colors calc git-status volume piglatin itunes osxterm special-garbanzo numgame pcb"
USAGE = "calc"
usageLine = 38 - 2 # please make sure this is the line number of THIS LINE. Line number is shifted down one, because indices start at 0, and then down one more since the USAGE line is above this line.
changeFunctionHelpText = f"\nPlease pass the function you would like this script to transform to as arugument 2.\nOptions are: {funcOptions}\n\nIf you keep getting this message but are using the script correctly, try running as root.\nRoot permessions are sometimes needed to edit the file depending on its location.\n\nThe current usage is \"{USAGE}\"\n"

# Importable classes in this file:
#   mcolors
#   operations

# MIT License
#
# Copyright (c) 2020 Matthew Raimondi
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

def changeFunction(newFunc): # Here is the change function, used to change the use of the program.
    with open(__file__, "r+") as k:
        code = k.read()
        targetLineBefore = code.split('\n')[usageLine]
        lines = code.split('\n')
        lines[usageLine] = f"USAGE = \"{newFunc}\""
        code = '\n'.join(lines)
        k.seek(0)
        k.truncate(0)
        k.write(code)
        targetLineAfter = code.split('\n')[usageLine]
    return f"{targetLineBefore}\n{targetLineAfter}"
    quit()

class operations: # A class for putting down simple operations, to make the calculator portion of this program much simpler to read.
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

    # This is a class containing color escape codes, used for printing colors on 256-bit color terminals, but has additional codes so as to be compatible with older 16-bit color terminals.

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
            raise Exception("\aNumber must be 0-256")

    def printbackcolor(number):
        if number >= 0 and number <= 256:
            sys.stdout.write(f"\u001b[48;5;${number}m")
        else:
            raise Exception("\aNumber must be 0-256")

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

if __name__ == "__main__" and len(sys.argv) >= 2: # So, here we have the clause that initiates the change function written earlier in the program that was created to manage the changing of use of this python file.
    if sys.argv[1] == "changeFunction":
        try:
            print(changeFunction(sys.argv[2]))
            quit()
        except Exception as e:
            print(e)
            print(changeFunctionHelpText)
            quit()

if __name__ == "__main__" and USAGE == "calc": # Here begins the calculator portion of the tool. There will not be many comments here, because this portion was designed to be easily read without the need for them.

    helper = f"\n\tUsage: {os.path.basename(__file__)} <option>\n\n\tOptions:\n\tbasic\n\tfracdec\n\tfibonacci\n\tinfibonacci\n\tisfibonacci\n\ttemp\n\tgpa\n\tmmmra\n\tmoleConverter\n\n\t{mcolors.orange}Calculator Suite by Matthew Raimondi\n\t{mcolors.skyblue}mwww.github.com/mattraimondi{mcolors.reset}\n"

    basichelp = f"\n\tUsage: {os.path.basename(__file__)} basic <n> <operation> <n>\n\n\tOperations:\n\t+  for addition\n\t-  for subtraction\n\tx  for multiplication\n\t/  for division\n\txx for power\n\t-x for root\n\n\t{mcolors.orange}Calculator by Matthew Raimondi\n\t{mcolors.skyblue}mwww.github.com/mattraimondi{mcolors.reset}\n"

    fracdechelp = f"\n\tUsage: {os.path.basename(__file__)} fracdec <n> <operation> <n>\n\n\tOperations:\n\t. for decimal into fraction (in which case, don\'t put a third number)\n\t/ for fraction into decimal\n\n\t{mcolors.orange}Fraction / Decimal Converter by Matthew Raimondi\n\t{mcolors.skyblue}mwww.github.com/mattraimondi{mcolors.reset}\n"

    fibohelp = f"\n\tUsage: {os.path.basename(__file__)} fibonacci <n>\n\t{mcolors.custpink}By Matthew Raimondi\n\twww.github.com/mattraimondi{mcolors.reset}\n"

    isfibohelp = f"\n\tUsage: {os.path.basename(__file__)} isfibonacci <n>\n\t{mcolors.custpink}By Matthew Raimondi\n\twww.github.com/mattraimondi{mcolors.reset}\n"

    temphelp = f"\n\nHelp:\n\tUsage: {os.path.basename(__file__)} temp <option> <n>\n\nOptions:\n\tfc: convert from fahrenheit to celcius\n\tcf: convert from celcius to fahrenheit\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"

    gpahelp = f"\n\nHelp:\n\tThe GPA program can calculate your GPA.\n\n\t*For AP classes, when asked for your letter grade, you should add AP to the end of the grade.\n\tExample: A+ -> A+AP\n\t\t A -> AAP\n\t\t A- -> A-AP\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"

    mmmrahelp = f"\n\nHelp:\n\tThe MMMRA program can calculate the Mean, Meadian, Mode, Range, and Average of a set of numbers.\n\nOptions\n\tmedian\n\tmode\n\trange\n\tmean\n\taverage\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"

    if len(sys.argv) == 1:
        print(helper)
        exit(0)

    if sys.argv[1] == "basic":
        try: # This section is for dealing with fractions, which are a pain to deal with on a CLI.
            if len(sys.argv) == 5:
                astr = sys.argv[2]
                o = sys.argv[3]
                bstr = sys.argv[4]
                a = float(astr)
                b = float(bstr)
        except Exception as e:
            print(e)
            print(basichelp)
        try: # The operational logic takes place below.
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

    elif sys.argv[1] == "fracdec": # Here we have more confusion, again related to the processing of fractional input.
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

    elif sys.argv[1] == "fibonacci": # This prints the fibonacci value of a number.
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

    elif sys.argv[1] == "infibonacci": # This is a confusing block of code, which doesn't make sense really, but is just for repeating the Fibonacci sequence indefinitely. The variable names are purposfully ambiguous.
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

    elif sys.argv[1] == "isfibonacci": # This checks to see if a number occurs in the fibonacci sequence.
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

    elif sys.argv[1] == "temp": # For converting temperatures. Check out mattraimondi.com/webdesign/project17
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

    elif sys.argv[1] == "gpa": # A GPA calculator that *actually* works.
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

    elif sys.argv[1] == "mmmra": # Useful for runnning some small data organization tasks.
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

if __name__ == "__main__" and USAGE == "colors": # This is the most useless program, so you should just ingore this.

    colorfile = ""
    alist = ""

    colorsHelpText = f"{mcolors.reset}{mcolors.custpink}\tScript by Matthew Raimondi\n\twww.github.com/mattraimondi{mcolors.reset}\n\n\tChoose one of the following colors or\n\tspecify a number value from the chart included:\n\n\t\t{mcolors.red}Red {mcolors.orange}Orange {mcolors.yellow}Yellow {mcolors.green}Green {mcolors.blue}Blue {mcolors.indigo}Indigo {mcolors.violet}Violet\n\t\t{mcolors.pink}Pink {mcolors.brown}Brown {mcolors.white}White {mcolors.black}{mcolors.whiteback}Black{mcolors.reset}\n\n\tand then (if you want) set a backgroung using\n\tthe following colors or a number value from the preveious chart:\n\n\t\t{mcolors.white}{mcolors.redback}Redback {mcolors.orangeback}Orangeback {mcolors.yellowback}Yellowback {mcolors.greenback}Greenback {mcolors.blueback}Blueback {mcolors.indigoback}Indigoback{mcolors.reset}\n\t\t{mcolors.white}{mcolors.violetback}Violetback {mcolors.pinkback}Pinkback {mcolors.brownback}Brownback {mcolors.whiteback}{mcolors.black}Whiteback {mcolors.reset}{mcolors.blackback}{mcolors.white}Blackback{mcolors.reset}\n\n\tTo clear colors type 'Reset' instead of a color or number.\n\n\tFor a list of color numbers, use the arguments 'all' and 'allbg'\n\t\tfor text and backround colors respectively.\n\n\tExample: {os.path.basename(__file__)} orange whiteback"

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

if __name__ == "__main__" and USAGE == "git-status": # Something that is useful!

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

    helptext = f"\n{mcolors.skyblue}Volume by Matthew Raimondi\nwww.github.com/mattraimondi\n-----------------------------\nVolume Command Line Interface\n-----------------------------\nUsage: {os.path.basename(__file__)} <option>\n\nOptions:\n\tset # = Set Volume to specified #\n\tup    = Set Volume Up 6.25\n\tdown  = Set Volume Down 6.25\n\tup1   = Set Volume Up 1\n\tdown1 = Set Volume Down 1\n\tget   = Get Volume Settings\n\tmute  = Mute Volume\n\thelp  = Show This Help Text{mcolors.clear}\n"

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
            print(volumeVersion)
        elif len(sys.argv) == 1:
            print(helptext)

if __name__ == "__main__" and USAGE == "itunes":

    volumeHelp = f"\n{mcolors.custpink}iTunes-CLI by Matthew Raimondi\nwww.github.com/mattraimondi\n-----------------------------\niTunes Command Line Interface\n-----------------------------\nUsage {os.path.basename(__file__)} <option>\n\nOptions:\n\tstatus   = Shows iTunes' status, current artist and track.\n\tplay     = Start playing iTunes.\n\tpause    = Pause iTunes.\n\tnext     = Go to the next track.\n\tprev     = Go to the previous track.\n\tmute     = Mute iTunes' volume.\n\tunmute   = Unmute iTunes' volume.\n\tvol up   = Increase iTunes' volume by 10%\n\tvol down = Increase iTunes' volume by 10%\n\tvol #    = Set iTunes' volume to # [0-100]\n\tstop     = Stop iTunes.\n\tquit     = Quit iTunes.{mcolors.reset}\n"

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

if __name__ == "__main__" and USAGE == "piglatin": # This still doesn't fully work yet...

    ending = "ay"
    vowels = ["a","e","i","o","u"]
    halfVowel = "y"

    def helper():
        print(f"\n\nHelp:\n\tUsage: {os.path.basename(__file__)} <option>\n\nOptions:\n\tengpig: translate from english to piglatin\n\tpigeng: translate from piglatin to english\n\n\n\u001b[38;5;$205mBy Matthew Raimondi\nwww.github.com/mattraimondi\033[0m\n")
        quit()

    def engpig(*args):
        alist = list(args)

        for word in alist:
            for letter in word:
                if letter not in vowels:
                    word = word[1:] + letter
                else:
                    word = word + ending
                    break

            return word

        quit()

    def pigeng(*args):
        alist = list(args)

        for word in alist:
            word = word.strip(ending)[::-1]
            for letter in word:
                if letter not in vowels:
                    word = word[1:] + letter
                else:
                    word = word[::-1]
                    break

            return word

        quit()

    if len(sys.argv) == 2:
        if sys.argv[1] == "engpig":
            sentence = input("Sentence: ").lower()
            sentlist = sentence.split(" ")
            pigwords = []
            for object in sentlist:
                pigword = engpig(object)
                pigwords.append(pigword)
            pigsentence = " ".join(pigwords)
            print(pigsentence)
        elif sys.argv[1] == "pigeng":
            sentence = input("Sentence: ").lower()
            sentlist = sentence.split(" ")
            pigwords = []
            for object in sentlist:
                pigword = pigeng(object)
                pigwords.append(pigword)
            pigsentence = " ".join(pigwords)
            print(pigsentence)
        else:
            helper()
    else:
        helper()

if __name__ == "__main__" and USAGE == "numgame": # Ported and transpiled from C-Multi-Tool
    def guessTheNumber(): # This is a simple guess the number game, which is fun to play when you are bored.
        remainingAttempts = 5
        mysteryNumber = randint(1,21)
        times = 0

        print("\nThis is a guessing game.\nA number between 0 and 20 has been randomly generated which you must guess.\n")

        for _ in range(0,4):
            print(f"\n\nCurrent Attempt: {remainingAttempts}") # Retrieve Number.
            guessedNumber = int(input("Please type a number from 0-20: ")) # Store Number.
            if guessedNumber == mysteryNumber:
                print(f"\nCongratulations! {guessedNumber} is the correct number.\n") # Correct Number.
                break
            else:
                if guessedNumber > mysteryNumber:
                    print(f"\nYour guess of {guessedNumber} is too high\n") # Too High.
                else:
                    print(f"\nYour guess of {guessedNumber} is too low\n") # Too Low.

                times += 1 # Increment
                remainingAttempts -= 1 # Decrement.

        if remainingAttempts == 0: # When you run out of attempts.
            print(f"\nThe mystery number is {mysteryNumber}\n")

    guessTheNumber()

if __name__ == "__main__" and USAGE == "pcb": # Ported and transpiled from C-Multi-Tool
    pcbHelp = f"\n\nOptions are:\n\tmoleConverter\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"
    moleHelp = f"\n\nOptions are:\n\tmolesToGrams\n\tgramsToMoles\n\tmolesToParticles\n\tparticlesToMoles\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"

    def moleConverter(): # Helpful for repetitive Chemistry homework.
        avogadrosNumber = 6.022 * (10 ** 23)

        if len(sys.argv) >= 3: # this needs a try/except clause to catch errors where letters are input instead of numbers -matt 3/9/20
            if sys.argv[2] == "molesToGrams":
                molarMass = float(input("Molar Mass: "))
                moles = float(input("# of Moles: "))
                output = molarMass * moles
                print(f"{output}\n")
            elif sys.argv[2] == "gramsToMoles":
                molarMass = float(input("Molar Mass: "))
                grams = float(input("# of Grams: "))
                output = grams / molarMass
                print(f"{output}\n")
            elif sys.argv[2] == "molesToParticles":
                moles = float(input("# of Moles: "))
                output = moles * avogadrosNumber
                print(f"{output}\n")
            elif sys.argv[2] == "particlesToMoles":
                particles = float(input("# of Particles times 10 to the 23rd power: "))
                output = (particles * (10 ** 23)) / avogadrosNumber
                print(f"{output}\n")
            else:
                print(f"{moleHelp}\n")
        else:
            print(f"{moleHelp}\n")

    if len(sys.argv) > 1:
        if sys.argv[1] == "moleConverter":
            moleConverter()
    else:
        print(pcbHelp)
