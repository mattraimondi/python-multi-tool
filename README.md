# python-multi-tool
A multiple-usage script that combines most of my public python tools into an easy to manage, easy to use solution.

*This "multi-tool" should be used with python3.*

## Installation
```
$ brew install mattraimondi/formulae/python-multi-tool
```

## changeFunction
This script is a multiple usage script that is controlled by a constant named `USAGE`. This constant can be edited in the script file to change the function of the script. In addition, a more simple way would be to use the `changeFunction` function that is included in the script, which changes the value of the constant. Because this script is able to edit itself in such a way, if the script is located in a root domain such as `/bin`, it is necesary to prefix this script with a sudo call to allow the script to edit itself and change the value of `USAGE`. The default value for usage is currently `calc`

An example using this function follows:
```
$ python3 multi-tool.py changeFunction lib
USAGE = "calc"
USAGE = "lib"
```

### Calculator
* A simple calculator written in Python.
* Includes a program to convert between fractions and decimals.
* Includes a program that finds the fibonacci value to the nth number (without recursion) and a program that prints the fibonacci sequence infinetly until stopped. Additionally, there is a program which checks to see if a number n is a number in the fibonacci sequence using the property of ((5 * (n * n)) +- 4)=perfect_square.
* Includes a program which can translate celcius to fahrenheit and vice versa.
* Includes a program that can calculate your current GPA, which can be very useful.
* Includes a program that can find the Mean, Median, Mode, Range, or Average of a set of numbers.

### Colors
A python color module for creating colored text on the command line. This library can also be run as an interactive script for changing the color of text on command line interfaces in which colored output is uncommon. (Such as old computers or ones with less capable command line interfaces.)

### Volume
Lets you change the volume from within the macOS command line. Works for OS X 10.7.5 and higher.

### git-status
If you're like me, you keep your git repositories all in one folder. But when working on multiple repositories, it can become hard to remember where you left off in each one. By navigating to said folder, invoking this command will list all of your repos in the folder, and their status. **This program does not check for unpushed commits.**

### iTunes-CLI
Lets you control iTunes, to an extent, from within the macOS command line. Works for OS X 10.7.5 and higher.

### Piglatin
Now you can translate between English and pig latin using this tool. **Words containing Y as the first vowel are currently not translated to preserve integrity of the message. Words containing Y as the first consonant are unaffected.**

### PCB
Coming Soon! Basically, if there is a way to do work faster (yes, this includes homework), then I will use the most efficient method. If there is no method, I make the method. So now Physics, Chemistry, and Biology homeworks pass by faster.
