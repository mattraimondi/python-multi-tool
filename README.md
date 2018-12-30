# python-multi-tool
A multiple-usage script that combines most of my public python tools into an easy to manage, easy to use solution.

###### This "multi-tool" should be used with python3.

## Calculator
A simple calculator written in Python.<br>
Includes a program to convert between fractions and decimals.<br>
Includes a program that finds the fibonacci value to the nth number (without recursion) and a program that prints the fibonacci sequence infinetly until stopped. Additionally, there is a program which checks to see if a number n is a number in the fibonacci sequence using the property of ((5 * (n * n)) +- 4)=perfect_square.<br>
Includes a program which can translate celcius to fahrenheit and vice versa.<br>
Includes a program that can calculate your current GPA, which can be very useful.<br>
Includes a program that can find the Mean, Median, Mode, Range, or Average of a set of numbers.

## colors
A python color module for creating colored text on the command line.<br>
This library can also be run as an interactive script for changing the color of text on command line interfaces in which colored output is uncommon. (Such as old computers or ones with less capable command line interfaces.)

## Volume
Lets you change the volume from within the macOS command line. Works for OS X 10.6.8 and higher.

## git-status
If you're like me, you keep your git repositories all in one folder. But when working on multiple repositories, it can become hard to remember where you left off in each one. By navigating to said folder, invoking this command will list all of your repos in the folder, and their status. **This program does not check for unpushed commits.**

## iTunes-CLI
Lets you control iTunes, to an extent, from within the macOS command line. Works for OS X 10.6.8 and higher.

# Installation
```
$ brew install mattraimondi/formulae/multi-tool
```

# changeFunction
This script is a multiple usage script that is controlled by a constant named `USAGE`. This constant can be edited in the script file to change the function of the script. In addition, a more simple way would be to use the `changeFunction` function that is included in the script, which changes the value of the constant. Because this script is able to edit itself in such a way, if the script is located in a root domain such as `/bin`, it is necesary to prefix this script with a sudo call to allow the script to edit itself and change the value of `USAGE`. The default value for usage is currently `calc` <br><br>
An example using this function follows:
```
$ python3 multi-tool.py changeFunction lib
USAGE = "calc"
USAGE = "lib"
```

# Cryptograpy
Python cryptography library by <a href="https://github.com/Fitzgibbons">@Fitzgibbons</a>

## RSA
RSA is a public key cryptosystem which can be used to communicate data securely and authenticate identity. The RSA file included is capable of generating valid RSA keys and moduli, encrypting data using these keys, and finally decrypting.  
Note: This is the only class in this file that does not follow the specification exactly. The only modification is adding  7 bits instead of 8 just before encryption. This ensures that the key is never too small to encrypt the masked data.

## MGF1
This mask function utilizes SHA 256 to take in a seed and produce a mask of a given length. This is included here mostly for the RSA algorithm, which requires it for encryption.

## SHA
SHA2 (Secure Hash Algorithm) is a family cryptographic hash functions, which turn data into irreversible hashes, or seemingly random series of bits. Included are SHA-224, SHA-256, SHA-384, and SHA-512.
SHA1 is also included in this library because despite being broken in practice, it has many other less cryptographic uses.

## HMAC
HMAC, or Key Hashed Message Authentication Code, can be used to authenticate message integrity and authenticity at the same time. Requires a key, message, and the length of the message block.

## AES
The Advanced Encryption Standard is a widely used block cipher that comes in three forms, with key lengths of 128, 192, 256.

## RNG
For deterministically random numbers, use the random.SystemRandom() class with a seed upon instantiation. For non-deterministically random numbers, instantiate the same class without a seed. This will utilize the os.urandom() function, which is the most random function provided by a given operating system and is considered cryptographically secure. Once instantiated, randrange, randint, random, and other functions from the random module can be called in a cryptographically secure manner.
