#! /usr/bin/env python3

# Multi-Tool Python Version 1.0.2

# Calculator Version 2.2.0
# Colors Version 2.0.0
# git-status Version 2.4.0
# Volume Version 5.0.0
# iTunes Version 3.0.0
# Piglatin Version 1.0.0-alpha.2

# 2019 Matthew Raimondi
# www.mattraimondi.com
# www.github.com/mattraimondi

# This script is a multiple usage script.
# You can change it's function using the variable below or by using the changeFunction option built into the script (recommended).
# The default setting is "calc".
# Use the "lib" option if importing this script as a library for another script.
funcOptions = "lib colors calc git-status volume piglatin itunes"
USAGE = "calc"
usageLine = 20
changeFunctionHelpText = f"\nPlease pass the function you would like this script to transform to as arugument 2.\nOptions are: {funcOptions}\n\nIf you keep getting this message but are using the script correctly, try running as root.\nRoot permessions are sometimes needed to edit the file depending on its location.\n\nThe current usage is \"{USAGE}\"\n"

# Importable classes in this file:
# mcolors
# operations
# cryptography.SHA
# cryptography.AES
# cryptography.MGF
# cryptography.HMAC
# cryptography.RSA
# cryptography.rabinmiller
# cryptography.userRandom

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
from codecs import encode
from random import SystemRandom
from math import ceil

rand = SystemRandom()

def changeFunction(newFunc):
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

class cryptography:
    # MIT License
    #
    # Copyright (c) 2017 Fitzgibbons
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
    
    class SHA:
        #Secure Hash Algorithm 2
        try:
            range = xrange
        except Exception:
            pass
        def rightshift(a,b,w):
            return (a & ((2 ** w) - 1)) >> b
        def rightrotate(a,b,w):
            return ((a & ((2 ** w) - 1)) >> (b & (w - 1))) | ((a << (w - (b & (w - 1)))) & ((2 ** w) - 1))
        def ch(x,y,z):
            return z ^ (x & (y ^ z))
        def maj(x,y,z):
            return (x & y) ^ (x & z) ^ (y & z)
        def uppersig0(x):
            return rightrotate(x,2,32) ^ rightrotate(x,13,32) ^ rightrotate(x,22,32)
        def uppersig1(x):
            return rightrotate(x,6,32) ^ rightrotate(x,11,32) ^ rightrotate(x,25,32)
        def lowersig0(x):
            return rightrotate(x,7,32) ^ rightrotate(x,18,32) ^ rightshift(x,3,32)
        def lowersig1(x):
            return rightrotate(x,17,32) ^ rightrotate(x,19,32) ^ rightshift(x,10,32)
        def uppersig2(x):
            return rightrotate(x,28,64) ^ rightrotate(x,34,64) ^ rightrotate(x,39,64)
        def uppersig3(x):
            return rightrotate(x,14,64) ^ rightrotate(x,18,64) ^ rightrotate(x,41,64)
        def lowersig2(x):
            return rightrotate(x,1,64) ^ rightrotate(x,8,64) ^ rightshift(x,7,64)
        def lowersig3(x):
            return rightrotate(x,19,64) ^ rightrotate(x,61,64) ^ rightshift(x,6,64)
        def pad(inbits, lead):
            outbits = (inbits << 1) + 1
            while (outbits.bit_length() + lead + 64) % 512 != 0:
                outbits <<= 1
            outbits <<= 64
            outbits |= inbits.bit_length() + lead
            return outbits
        def pad2(inbits, lead):
            outbits = (inbits << 1) + 1
            while (outbits.bit_length() + lead + 128) % 1024 != 0:
                outbits <<= 1
            outbits <<= 128
            outbits |= inbits.bit_length() + lead
            return outbits
        def split(inbits):
            outarray = []
            rembits = inbits
            while rembits != 0:
                outarray += [rembits & ((2 ** 512) - 1)]
                rembits >>= 512
            return list(reversed(outarray))
        def split2(inbits):
            outarray = []
            rembits = inbits
            while rembits != 0:
                outarray += [rembits & ((2 ** 1024) - 1)]
                rembits >>= 1024
            return list(reversed(outarray))
        def SHA256(inbits, is224=False, lead=0):
            registers = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]
            if is224:
                registers = [0xc1059ed8,0x367cd507,0x3070dd17,0xf70e5939,0xffc00b31,0x68581511,0x64f98fa7,0xbefa4fa4]
            constants = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
                         0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
                         0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
                         0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
                         0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
                         0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
                         0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
                         0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
            inarray = split(pad(inbits, lead))
            for i, e in enumerate(inarray):
                messageSchedule = []
                for j in range(64):
                    messageSchedule += [0]
                    if j < 16:
                        messageSchedule[j] = (e >> (32 * (15 - j))) & ((2 ** 32) - 1)
                    else:
                        messageSchedule[j] = (lowersig1(messageSchedule[j - 2]) + messageSchedule[j - 7] + lowersig0(messageSchedule[j - 15]) + messageSchedule[j - 16]) % (2 ** 32)
                workingvars = list(registers)
                for j in range(64):
                    t1 = (workingvars[7] + uppersig1(workingvars[4]) + ch(workingvars[4],workingvars[5],workingvars[6]) + constants[j] + messageSchedule[j]) % (2 ** 32)
                    t2 = (uppersig0(workingvars[0]) + maj(workingvars[0],workingvars[1],workingvars[2])) % (2 ** 32)
                    workingvars[7] = workingvars[6]
                    workingvars[6] = workingvars[5]
                    workingvars[5] = workingvars[4]
                    workingvars[4] = (workingvars[3] + t1) % (2 ** 32)
                    workingvars[3] = workingvars[2]
                    workingvars[2] = workingvars[1]
                    workingvars[1] = workingvars[0]
                    workingvars[0] = (t1 + t2) % (2 ** 32)
                for j, e in enumerate(workingvars):
                    registers[j] = (e + registers[j]) % (2 ** 32)
            outbits = 0
            for i in registers:
                outbits <<= 32
                outbits |= i
            return outbits
        def SHA224(inbits, lead=0):
            return SHA256(inbits, True, lead) >> 32
        def SHA512(inbits, is384=False, lead=0):
            registers = [0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1, 0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b, 0x5be0cd19137e2179]
            if is384:
                registers = [0xcbbb9d5dc1059ed8, 0x629a292a367cd507, 0x9159015a3070dd17, 0x152fecd8f70e5939, 0x67332667ffc00b31, 0x8eb44a8768581511, 0xdb0c2e0d64f98fa7, 0x47b5481dbefa4fa4]
            constants = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
                         0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
                         0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
                         0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
                         0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
                         0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
                         0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
                         0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
                         0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
                         0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
                         0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
                         0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
                         0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
                         0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
                         0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
                         0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
                         0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
                         0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
                         0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
                         0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817]
            inarray = split2(pad2(inbits, lead))
            for i, e in enumerate(inarray):
                messageSchedule = []
                for j in range(80):
                    messageSchedule += [0]
                    if j < 16:
                        messageSchedule[j] = (e >> (64 * (15 - j))) & ((2 ** 64) - 1)
                    else:
                        messageSchedule[j] = (lowersig3(messageSchedule[j - 2]) + messageSchedule[j - 7] + lowersig2(messageSchedule[j - 15]) + messageSchedule[j - 16]) % (2 ** 64)
                workingvars = list(registers)
                for j in range(80):
                    t1 = (workingvars[7] + uppersig3(workingvars[4]) + ch(workingvars[4],workingvars[5],workingvars[6]) + constants[j] + messageSchedule[j]) % (2 ** 64)
                    t2 = (uppersig2(workingvars[0]) + maj(workingvars[0],workingvars[1],workingvars[2])) % (2 ** 64)
                    workingvars[7] = workingvars[6]
                    workingvars[6] = workingvars[5]
                    workingvars[5] = workingvars[4]
                    workingvars[4] = (workingvars[3] + t1) % (2 ** 64)
                    workingvars[3] = workingvars[2]
                    workingvars[2] = workingvars[1]
                    workingvars[1] = workingvars[0]
                    workingvars[0] = (t1 + t2) % (2 ** 64)
                for j, e in enumerate(workingvars):
                    registers[j] = (e + registers[j]) % (2 ** 64)
            outbits = 0
            for i in registers:
                outbits <<= 64
                outbits |= i
            return outbits
        def SHA384(inbits, lead=0):
            return SHA512(inbits, True, lead) >> 128
        def f(t,b,c,d):
            if t <= 19:
                return (b & c) | (((1 << 32) - 1 - b) & d)
            elif t <= 39:
                return b ^ c ^ d
            elif t <= 59:
                return (b & c) | (b & d) | (c & d)
            elif t <= 79:
                return b ^ c ^ d
        def k(t):
            if t <= 19:
                return 0x5A827999
            elif t <= 39:
                return 0x6ED9EBA1
            elif t <= 59:
                return 0x8F1BBCDC
            elif t <= 79:
                return 0xCA62C1D6
        def rshift(x,n):
            return (x << n) | (x >> (32 - n))
        def SHA1(inbits, lead=0):
            padded = inbits
            padded <<= 1
            padded += 1
            while (lead + padded.bit_length()) % 512 != 448:
                padded <<= 1
            padded <<= 64
            padded += lead + inbits.bit_length()
            H = [0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0]
            for i in range(padded.bit_length() // 512):
                W = []
                for j in range(16):
                    W += [(padded >> ((15 - j) * 32)) & 0xFFFFFFFF]
                for j in range(16,80):
                    W += [rshift(W[j-3]^W[j-8]^W[j-14]^W[j-16],1)]
                workingvars = list(H)
                for j in range(80):
                    temp = (rshift(workingvars[0],5) + f(j,workingvars[1],workingvars[2],workingvars[3]) + workingvars[4] + W[j] + k(j)) % (2 ** 32)
                    workingvars[4] = workingvars[3]
                    workingvars[3] = workingvars[2]
                    workingvars[2] = rshift(workingvars[1],30)
                    workingvars[1] = workingvars[0]
                    workingvars[0] = temp
                H[0] = (H[0] + workingvars[0]) % (2 ** 32)
                H[1] = (H[1] + workingvars[1]) % (2 ** 32)
                H[2] = (H[2] + workingvars[2]) % (2 ** 32)
                H[3] = (H[3] + workingvars[3]) % (2 ** 32)
                H[4] = (H[4] + workingvars[4]) % (2 ** 32)
            outbits = 0
            for i in H:
                outbits <<= 32
                outbits |= i
            return outbits

    class AES:
        #Advanced Encryption Standard
        try:
            range = xrange
        except Exception:
            pass
        xtime = lambda x: (((x << 1) ^ 0x1b) & 0xff) if (x & 0x80) else (x << 1)
        SBox = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
                [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
                [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
                [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
                [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
                [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
                [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
                [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
                [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
                [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
                [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
                [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
                [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
                [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
                [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
                [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]
        invSBox = [[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
                   [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
                   [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
                   [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
                   [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
                   [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
                   [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
                   [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
                   [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
                   [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
                   [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
                   [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
                   [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
                   [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
                   [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
                   [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]
        rcon = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
        def SubBytes(a):
            for i in range(16):
                a[i] = SBox[a[i] >> 4][a[i] & 0xf]
            return a
        def InvSubBytes(a):
            for i in range(16):
                a[i] = invSBox[a[i] >> 4][a[i] & 0xf]
            return a
        def ShiftRows(a):
            return [a[0], a[5], a[10], a[15], a[4], a[9], a[14], a[3], a[8], a[13], a[2], a[7], a[12], a[1], a[6], a[11]]
        def InvShiftRows(a):
            return [a[0], a[13], a[10], a[7], a[4], a[1], a[14], a[11], a[8], a[5], a[2], a[15], a[12], a[9], a[6], a[3]]
        def MixColumns(a):
            for i in range(4):
                b = a[0 + (i * 4):4 + (i * 4)]
                t = b[0] ^ b[1] ^ b[2] ^ b[3]
                u = b[0]
                b[0] ^= t ^ xtime(b[0] ^ b[1])
                b[1] ^= t ^ xtime(b[1] ^ b[2])
                b[2] ^= t ^ xtime(b[2] ^ b[3])
                b[3] ^= t ^ xtime(b[3] ^ u)
                a[0 + (i * 4):4 + (i * 4)] = b
            return a
        def InvMixColumns(a):
            for i in range(4):
                b = a[0 + (i * 4):4 + (i * 4)]
                u = xtime(xtime(b[0] ^ b[2]))
                v = xtime(xtime(b[1] ^ b[3]))
                b[0] ^= u
                b[1] ^= v
                b[2] ^= u
                b[3] ^= v
                a[0 + (i * 4):4 + (i * 4)] = b
            return MixColumns(a)
        def AddRoundKey(a,b):
            for i in range(4):
                for j in range(4):
                    a[j + (4 * i)] ^= (b[i] >> (8 * (3 - j))) & 0xff
            return a
        def SubWord(a):
            return (SBox[(a >> 28) & 0xf][(a >> 24) & 0xf] << 24) | (SBox[(a >> 20) & 0xf][(a >> 16) & 0xf] << 16) | (SBox[(a >> 12) & 0xf][(a >> 8) & 0xf] << 8) | (SBox[(a >> 4) & 0xf][a & 0xf])
        def RotWord(a):
            return ((a << 8) & 0xffffffff) | (a >> 24)
        def AESencryptblock(keys, numRounds, inbits):
            state = []
            for i in range(16):
                state += [(inbits >> (120 - (8 * i))) & 0xff]
            state = AddRoundKey(state, keys[0:4])
            for i in range(numRounds - 1):
                state = SubBytes(state)
                state = ShiftRows(state)
                state = MixColumns(state)
                state = AddRoundKey(state, keys[(i * 4) + 4:(i * 4) + 8])
            state = SubBytes(state)
            state = ShiftRows(state)
            state = AddRoundKey(state, keys[numRounds * 4:(numRounds * 4) + 4])
            out = 0
            for i in state:
                out <<= 8
                out += i
            return out
        def AESdecryptblock(keys, numRounds, inbits):
            state = []
            for i in range(16):
                state += [(inbits >> (120 - (8 * i))) & 0xff]
            state = AddRoundKey(state, keys[numRounds * 4:(numRounds * 4) + 4])
            state = InvShiftRows(state)
            state = InvSubBytes(state)
            for i in range(numRounds - 2,-1,-1):
                state = AddRoundKey(state, keys[(i * 4) + 4:(i * 4) + 8])
                state = InvMixColumns(state)
                state = InvShiftRows(state)
                state = InvSubBytes(state)
            state = AddRoundKey(state, keys[0:4])
            out = 0
            for i in state:
                out <<= 8
                out += i
            return out
        def AESencrypt(length, keys, inbits, lead=0):
            refrounds = {128:10,192:12,256:14}
            numRounds = refrounds.get(length, Exception())
            bytecomplete = (inbits & 1) ^ 1
            bits = 8 - ((inbits.bit_length() + lead) % 8)
            for i in range(bits):
                inbits <<= 1
                inbits += bytecomplete
            bytelength = (inbits.bit_length() + lead) // 8
            pad = 16 - (bytelength % 16)
            for i in range(pad):
                inbits <<= 8
                if pad != 16:
                    inbits += pad
            out = rand.randint(0,(2 ** 128) - 1)
            for i in range((inbits.bit_length() + lead) // 128):
                out <<= 128
                out += AESencryptblock(keys, numRounds, ((inbits >> ((inbits.bit_length() + lead) - (128 * (i + 1)))) ^ (out >> 128)) & 0xffffffffffffffffffffffffffffffff)
            return out
        def AESdecrypt(length, keys, inbits):
            refrounds = {128:10,192:12,256:14}
            numRounds = refrounds.get(length, Exception())
            lead = 128 - (inbits.bit_length() % 128) if inbits.bit_length() % 128 != 0 else 0
            out = 0
            for i in range((inbits.bit_length() + lead - 128) // 128):
                out <<= 128
                out += AESdecryptblock(keys, numRounds, (inbits >> ((inbits.bit_length() + lead) - (128 * (i + 2)))) & 0xffffffffffffffffffffffffffffffff) ^ ((inbits >> ((inbits.bit_length() + lead) - (128 * (i + 1)))) & 0xffffffffffffffffffffffffffffffff)
            lead = (-128 * (-out.bit_length() // 128)) - out.bit_length()
            if out & 0xff == 0:
                out >>= 128
            else:
                out >>= 8 * (out & 0xff)
            remove = out & 1
            while out & 1 == remove:
                out >>= 1
            return out, lead
        def getKey(length,key):
            if not (length in [128,192,256]):
                raise Exception("invalid key length")
            if length == 128:
                w = []
                for i in range(4):
                    w += [key >> (96 - (32 * i)) & 0xffffffff]
                while len(w) < 44:
                    temp = w[len(w) - 1]
                    if len(w) % 4 == 0:
                        temp = SubWord(RotWord(temp)) ^ (rcon[len(w)//4] << 24)
                    temp ^= w[len(w) - 4]
                    w += [temp]
                return w
            if length == 192:
                w = []
                for i in range(6):
                    w += [key >> (160 - (32 * i)) & 0xffffffff]
                while len(w) < 52:
                    temp = w[len(w) - 1]
                    if len(w) % 6 == 0:
                        temp = SubWord(RotWord(temp)) ^ (rcon[len(w)//6] << 24)
                    temp ^= w[len(w) - 6]
                    w += [temp]
                return w
            if length == 256:
                w = []
                for i in range(8):
                    w += [key >> (224 - (32 * i)) & 0xffffffff]
                while len(w) < 60:
                    temp = w[len(w) - 1]
                    if len(w) % 8 == 0:
                        temp = SubWord(RotWord(temp)) ^ (rcon[len(w)//8] << 24)
                    elif len(w) % 4 == 0:
                        temp = SubWord(temp)
                    temp ^= w[len(w) - 8]
                    w += [temp]
                return w

    class rabinmiller:
        def rabinMiller(num):
            if num % 2 == 0:
                return False
            s = num - 1
            t = 0
            while s % 2 == 0:
                s = s // 2
                t += 1
            for trials in range(64):
                a = rand.randrange(2, num - 1)
                v = pow(a, s, num)
                if v != 1:
                    i = 0
                    while v != (num - 1):
                        if i == t - 1:
                            return False
                        else:
                            i = i + 1
                            v = (v ** 2) % num
            return True

    class HMAC:
        #Key Hashed Message Authentication Code
        def HMAC(message, key, messagelead=0, keylead=0):
            while (keylead + key.bit_length()) % 8 != 0 and key.bit_length() != 0:
                key <<= 1
            if key.bit_length() + keylead > 512:
                keyprime = SHA256(key, lead=keylead)
            else:
                while key.bit_length() + keylead < 512 and key.bit_length() != 0:
                    key <<= 8
                keyprime = key
            concat = SHA256(((keyprime ^ 0x36363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636) << (message.bit_length() + messagelead)) + message)
            return SHA256(((keyprime ^ 0x5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c) << 256) + concat)

    class MGF:
        #Mask Generation Function
        try:
            range = xrange
        except Exception:
            pass
        def I2OSP(x, xLen):
            if x >= 256 ** xLen:
                raise Exception("Integer too large")
            nums = []
            while x:
                nums.append(x % 256)
                x >>= 8
            for i in range(xLen - len(nums)):
                nums += [0]
            outbits = 0b0
            for i in nums:
                outbits <<= 8
                outbits += i
            return outbits
        def MGF1(seed, length):
            if length > 2 ** 40:
                raise Exception("Mask length too long")
            outbits = 0b0
            for i in range(int(ceil(length / 256.0) + 1)):
                outbits <<= 256
                on = 0b0
                outbits += SHA.SHA256((seed << 32) + I2OSP(i,4))
                if outbits.bit_length() >= length:
                    break
            return outbits >> (outbits.bit_length() - length)

    class RSA:
        #RSA Public Key Cryptosystem
        try:
            range = xrange
        except Exception:
            pass
        def findModInverse(a, m):
            u1, u2, u3 = 1, 0, a
            v1, v2, v3 = 0, 1, m
            while v3 != 0:
                q = u3 // v3
                v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
            return u1 % m
        def findPrime(bits):
            num = 0b1 << ((bits) - 1)
            if num != 0b1:
                num += 1
            num2 = 0b1 << (bits)
            prime = rand.randrange(num, num2, 2)
            while not rabinmiller.rabinMiller(prime):
                prime += 2
            return prime
        def getKeys():
            prime1 = findPrime(1024)
            prime2 = findPrime(1024)
            modulus = prime1 * prime2
            totient = (prime1 - 1) * (prime2 - 1)
            publicKey = 65537
            while totient % publicKey == 0:
                prime1 = findPrime(1024)
                prime2 = findPrime(1024)
                modulus = prime1 * prime2
                totient = (prime1 - 1) * (prime2 - 1)
            privateKey = findModInverse(publicKey, totient)
            text = 1
            text <<= 2047
            cipherText = pow(text, publicKey, modulus)
            newText =  pow(cipherText, privateKey, modulus)
            if text == newText and modulus.bit_length() // 8 == 256 and privateKey.bit_length() // 8 == 256:
                return [publicKey, privateKey, modulus]
            else:
                return getKeys()
        def OS2IP(x):
            nums = []
            while x:
                nums += [x & 0xff]
                x >>= 8
            outbits = 0b0
            for i in nums:
                outbits <<= 8
                outbits += i
            return outbits
        def RSAencrypt(publicKey, modulus, message, label=0):
            if message.bit_length() > modulus.bit_length() - 528:
                raise Exception("Message too large")
            if label > 2 ** 64:
                raise Exception("Label too large")
            lhash = SHA.SHA256(label)
            while lhash.bit_length() < 256:
                lhash <<= 1
            DB = (lhash << (modulus.bit_length() - 520)) + (1 << message.bit_length()) + message
            seed = 0
            for i in range(256):
                seed <<= 1
                if rand.random() < 0.5:
                    seed += 1
            dbMask = MGF.MGF1(seed, modulus.bit_length() - 264)
            maskedDB = DB ^ dbMask
            seedMask = MGF1(maskedDB, 256)
            maskedSeed = seed ^ seedMask
            EM = (maskedSeed << 1784) + maskedDB
            m = OS2IP(EM) << 7
            c = pow(m, publicKey, modulus)
            return OS2IP(c)
        def RSAdecrypt(privateKey, modulus, message, label=0):
            if label > 2 ** 64:
                raise Exception("Label too large")
            if modulus.bit_length() < 520:
                raise Exception("Invalid modulus")
            c = OS2IP(message)
            m = pow(c, privateKey, modulus)
            EM = OS2IP(m >> 7)
            lhash = SHA.SHA256(label)
            while lhash.bit_length() < 256:
                lhash <<= 1
            maskedDB = EM & ((2 ** (modulus.bit_length() - 264)) - 1)
            EM >>= modulus.bit_length() - 264
            maskedSeed = EM & ((2 ** 256) - 1)
            EM >>= 256
            y = EM
            seedMask = MGF1(maskedDB, 256)
            seed = maskedSeed ^ seedMask
            dbMask = MGF.MGF1(seed, modulus.bit_length() - 264)
            DB = maskedDB ^ dbMask
            if DB >> (DB.bit_length() - 256) == lhash:
                DB ^= (lhash << (DB.bit_length() - 256))
                DB ^= 1 << (DB.bit_length() - 1)
                return DB
            else:
                raise Exception("Decryption Error")

    class userRandom:
        #Random Number Generator From User Input
        def getRandomFromUser():
            inNum = input("Please input a random number.\n")
            try:
                inNum = SHA.SHA512(int(inNum))
            except TypeError:
                inNum = SHA.SHA512(int((rand.random() * 10) ** (rand.random() * 13)))
            inLetters = input("Please smash your keyboard for 10 seconds. Letters only. Then press enter.\n").lower()
            numbers = []
            letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            try:
                for i, e in enumerate(inLetters):
                    numbers += [letters.index(e)]
            except ValueError:
                numbers = []
                for i in range(50):
                    numbers += [int((rand.random() * 10) ** (rand.random() * 13))]
            for i, e in enumerate(numbers):
                inNum <<= 512
                inNum += SHA.SHA512(int((SHA512(e + SHA.SHA512(e)) + e) * rand.random()))
            return SHA.SHA512(inNum)

if __name__ == "__main__" and len(sys.argv) >= 2:
    if sys.argv[1] == "changeFunction":
        try:
            print(changeFunction(sys.argv[2]))
            quit()
        except Exception as e:
            print(e)
            print(changeFunctionHelpText)
            quit()

if __name__ == "__main__" and USAGE == "calc":
    
    helper = f"\n\tUsage: {os.path.basename(__file__)} <option>\n\n\tOptions:\n\tbasic\n\tfracdec\n\tfibonacci\n\tinfibonacci\n\tisfibonacci\n\ttemp\n\tgpa\n\tmmmra\n\n\t\u001b[38;5;$208mCalculator Suite by Matthew Raimondi\n\t\u001b[38;5;$39mwww.github.com/mattraimondi{mcolors.reset}\n"

    basichelp = f"\n\tUsage: {os.path.basename(__file__)} calc <n> <operation> <n>\n\n\tOperations:\n\t+  for addition\n\t-  for subtraction\n\tx  for multiplication\n\t/  for division\n\txx for power\n\t-x for root\n\n\t\u001b[38;5;$208mCalculator by Matthew Raimondi\n\t\u001b[38;5;$39mwww.github.com/mattraimondi{mcolors.reset}\n"

    fracdechelp = f"\n\tUsage: {os.path.basename(__file__)} fracdec <n> <operation> <n>\n\n\tOperations:\n\t. for decimal into fraction (in which case, don\'t put a third number)\n\t/ for fraction into decimal\n\n\t\u001b[38;5;$208mFraction / Decimal Converter by Matthew Raimondi\n\t\u001b[38;5;$39mwww.github.com/mattraimondi{mcolors.reset}\n"

    fibohelp = f"\n\tUsage: {os.path.basename(__file__)} fibonacci <n>\n\t{mcolors.custpink}By Matthew Raimondi\n\twww.github.com/mattraimondi{mcolors.reset}\n"

    isfibohelp = f"\n\tUsage: {os.path.basename(__file__)} isfibonacci <n>\n\t{mcolors.custpink}By Matthew Raimondi\n\twww.github.com/mattraimondi{mcolors.reset}\n"

    temphelp = f"\n\nHelp:\n\tUsage: {os.path.basename(__file__)} temp <option> <n>\n\nOptions:\n\tfc: convert from fahrenheit to celcius\n\tcf: convert from celcius to fahrenheit\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"

    gpahelp = f"\n\nHelp:\n\tThe GPA program can calculate your GPA.\n\n\t*For AP classes, when asked for your letter grade, you should add AP to the end of the grade.\n\tExample: A+ -> A+AP\n\t\t A -> AAP\n\t\t A- -> A-AP\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"

    mmmrahelp = f"\n\nHelp:\n\tThe MMMRA program can calculate the Mean, Meadian, Mode, Range, and Average of a set of numbers.\n\nOptions\n\tmedian\n\tmode\n\trange\n\tmean\n\taverage\n\n\n{mcolors.custpink}By Matthew Raimondi\nwww.github.com/mattraimondi{mcolors.reset}\n"

    calcVersion = f"{mcolors.custpink}Calculator Version 2.2.0{mcolors.clear}"
    
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

    helptext = f"\n{mcolors.skyblue}Volume by Matthew Raimondi\nwww.github.com/mattraimondi\n-----------------------------\nVolume Command Line Interface\n-----------------------------\nUsage: {os.path.basename(__file__)} <option>\n\nOptions:\n\tset # = Set Volume to specified #\n\tup    = Set Volume Up 6.25\n\tdown  = Set Volume Down 6.25\n\tup1   = Set Volume Up 1\n\tdown1 = Set Volume Down 1\n\tget   = Get Volume Settings\n\tmute  = Mute Volume\n\thelp  = Show This Help Text{mcolors.clear}\n"

    versionnum = f"{mcolors.skyblue}5.0.0{mcolors.clear}"

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
        print(f"\n\nHelp:\n\tUsage: {os.path.basename(__file__)} <option>\n\nOptions:\n\tengpig: translate from english to piglatin\n\tpigeng: translate from piglatin to english\n\n\n\u001b[38;5;$205mBy Matthew Raimondi\nwww.github.com/mattraimondi\033[0m\n")
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
        if sys.argv[1] == "engpig":
            sentence = input("Sentence: ").lower()
            sentlist = sentence.split(" ")
            while len(newlist) < len(sentlist):
                engpig(sentence)
            newstr = " ".join(newlist)
            print(newstr)
        elif sys.argv[1] == "pigeng":
            print("Awaiting build")
        else:
            helper()
    else:
        helper()

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

if __name__ == "__main__" and USAGE == "blink1-matt":

    from blink1.blink1 import Blink1

    myblink = Blink1(serial_number=u'2000D103')
    myblink.fade_to_color(1000, 'turquoise')
    myblink.close()

if __name__ == "__main__" and USAGE == "matt3":
    
    letnum = {'a':805,'b':945,'c':852,'d':268,'e':674,'f':491,'g':520,'h':982,'i':256,'j':863,'k':593,'l':987,'m':764,'n':763,'o':392,'p':483,'q':238,'r':999,'s':493,'t':762,'u':193,'v':260,'w':100,'x':199,'y':872,'z':539,'.':111,'\n':222,' ':333,'\t':444,':':555,'/':666,'\\':777,'!':888,'?':123,'#':234,'=':345,'+':456,'-':567,'_':678,'(':789,')':890,'[':112,']':113,'%':114,'$':115,'@':116,'\'':117,'"':118,';':119,'<':120,'>':121,'{':122,'}':124,'*':125,',':126,'&':127,'^':128,'|':129,'`':130,'~':131,'1':926,'2':876,'3':765,'4':654,'5':543,'6':432,'7':321,'8':246,'9':135,'0':909}
    numlet = {'805':'a','945':'b','852':'c','268':'d','674':'e','491':'f','520':'g','982':'h','256':'i','863':'j','593':'k','987':'l','764':'m','763':'n','392':'o','483':'p','238':'q','999':'r','493':'s','762':'t','193':'u','260':'v','100':'w','199':'x','872':'y','539':'z','111':'.','222':'\n','333':' ','444':'\t','555':':','666':'/','777':'\\','888':'!','123':'?','234':'#','345':'=','456':'+','567':'-','678':'_','789':'(','890':')','112':'[','113':']','114':'%','115':'$','116':'@','117':'\'','118':'"','119':';','120':'<','121':'>','122':'{','124':'}','125':'*','126':',','127':'&','128':'^','129':'|','130':'`','131':'~','926':'1','876':'2','765':'3','654':'4','543':'5','432':'6','321':'7','246':'8','135':'9','909':'0'}
    def encrypt():
        with open(sys.argv[2], "r+") as e:
            message = e.read().lower()[::-1]
            rotmess = rot13(message)
            messlist = list(rotmess)
            e.seek(0)
            for letter in messlist:
                e.write(str(letnum[letter]))
    def decrypt():
        with open(sys.argv[2], "r+") as d:
            message = d.read()
            messlist = [message[i:i+3] for i in range(0, len(message), 3)][::-1]
            d.seek(0)
            d.truncate(0)
            for number in messlist:
                d.write(str(rot13(numlet[number])))
    def rot13(s):
        return encode(s, 'rot13')
    def helper():
        print(f"\n\nVersion 3.0\n\nHelp:\n\tUsage: {os.path.basename(__file__)} <option> <filename>\n\nOptions:\n\tencrypt: encrypt message\n\tdecrypt: decrypt message\n\n\n\u001b[38;5;$205mBy Matthew Raimondi\nwww.github.com/mattraimondi\033[0m\n")
        quit()
    if len(sys.argv) == 3:
        if sys.argv[1] == "encrypt":
            encrypt()
        elif sys.argv[1] == "decrypt":
            decrypt()
        elif sys.argv[1] == "erase":
            perms = input("Are you sure you would like to permanently erase this file? Y/n: ").lower()
            if perms == "y":
                with open (sys.argv[2],"r+") as j:
                    j.seek(0)
                    j.truncate(0)
            else:
                quit()
        else:
            helper()
    else:
        helper()

if __name__ == "__main__" and USAGE == "matt2":

    letnum = {'a':805,'b':945,'c':852,'d':268,'e':674,'f':491,'g':520,'h':982,'i':256,'j':863,'k':593,'l':987,'m':764,'n':763,'o':392,'p':483,'q':238,'r':999,'s':493,'t':762,'u':193,'v':260,'w':100,'x':199,'y':872,'z':539,'.':111,'\n':222,' ':333,'\t':444,':':555,'/':666,'\\':777,'!':888,'?':123,'#':234,'=':345,'+':456,'-':567,'_':678,'(':789,')':890,'[':112,']':113,'%':114,'$':115,'@':116,'\'':117,'"':118,';':119,'<':120,'>':121,'{':122,'}':124,'*':125,',':126,'&':127,'^':128,'|':129,'`':130,'~':131,'1':926,'2':876,'3':765,'4':654,'5':543,'6':432,'7':321,'8':246,'9':135,'0':909}
    numlet = {'805':'a','945':'b','852':'c','268':'d','674':'e','491':'f','520':'g','982':'h','256':'i','863':'j','593':'k','987':'l','764':'m','763':'n','392':'o','483':'p','238':'q','999':'r','493':'s','762':'t','193':'u','260':'v','100':'w','199':'x','872':'y','539':'z','111':'.','222':'\n','333':' ','444':'\t','555':':','666':'/','777':'\\','888':'!','123':'?','234':'#','345':'=','456':'+','567':'-','678':'_','789':'(','890':')','112':'[','113':']','114':'%','115':'$','116':'@','117':'\'','118':'"','119':';','120':'<','121':'>','122':'{','124':'}','125':'*','126':',','127':'&','128':'^','129':'|','130':'`','131':'~','926':'1','876':'2','765':'3','654':'4','543':'5','432':'6','321':'7','246':'8','135':'9','909':'0'}
    def encrypt():
        with open(sys.argv[2], "r+") as e:
            message = e.read().lower()[::-1]
            messlist = list(message)
            e.seek(0)
            for letter in messlist:
                e.write(str(letnum[letter]))
    def decrypt():
        with open(sys.argv[2], "r+") as d:
            message = d.read()
            messlist = [message[i:i+3] for i in range(0, len(message), 3)][::-1]
            d.seek(0)
            d.truncate(0)
            for number in messlist:
                d.write(str(numlet[number]))
    def helper():
        print(f"\n\nHelp:\n\tUsage: {os.path.basename(__file__)} <option> <filename>\n\nOptions:\n\tencrypt: encrypt message\n\tdecrypt: decrypt message\n\n\n\u001b[38;5;$205mBy Matthew Raimondi\nwww.github.com/mattraimondi\033[0m\n")
        quit()
    if len(sys.argv) == 3:
        if sys.argv[1] == "encrypt":
            encrypt()
        elif sys.argv[1] == "decrypt":
            decrypt()
        elif sys.argv[1] == "erase":
            perms = input("Are you sure you would like to permanently erase this file? Y/n: ").lower()
            if perms == "y":
                with open (sys.argv[2],"r+") as j:
                    j.seek(0)
                    j.truncate(0)
            else:
                quit()
        else:
            helper()
    else:
        helper()

if __name__ == "__main__" and USAGE == "matt1":

    letnum = {'a':805,'b':945,'c':852,'d':268,'e':674,'f':491,'g':520,'h':982,'i':256,'j':863,'k':593,'l':987,'m':764,'n':763,'o':392,'p':483,'q':238,'r':999,'s':493,'t':762,'u':193,'v':260,'w':100,'x':199,'y':872,'z':539,'.':111,'\n':222,' ':333,'\t':444,':':555,'/':666,'\\':777,'!':888,'?':123,'#':234,'=':345,'+':456,'-':567,'_':678,'(':789,')':890,'[':112,']':113,'%':114,'$':115,'@':116,'\'':117,'"':118,';':119,'<':120,'>':121,'{':122,'}':124,'*':125,',':126,'&':127,'^':128,'|':129,'`':130,'~':131,'1':926,'2':876,'3':765,'4':654,'5':543,'6':432,'7':321,'8':246,'9':135,'0':909}
    numlet = {'805':'a','945':'b','852':'c','268':'d','674':'e','491':'f','520':'g','982':'h','256':'i','863':'j','593':'k','987':'l','764':'m','763':'n','392':'o','483':'p','238':'q','999':'r','493':'s','762':'t','193':'u','260':'v','100':'w','199':'x','872':'y','539':'z','111':'.','222':'\n','333':' ','444':'\t','555':':','666':'/','777':'\\','888':'!','123':'?','234':'#','345':'=','456':'+','567':'-','678':'_','789':'(','890':')','112':'[','113':']','114':'%','115':'$','116':'@','117':'\'','118':'"','119':';','120':'<','121':'>','122':'{','124':'}','125':'*','126':',','127':'&','128':'^','129':'|','130':'`','131':'~','926':'1','876':'2','765':'3','654':'4','543':'5','432':'6','321':'7','246':'8','135':'9','909':'0'}
    def encrypt():
        with open(sys.argv[2], "r+") as e:
            message = e.read().lower()
            messlist = list(message)
            e.seek(0)
            for letter in messlist:
                e.write(str(letnum[letter]))
    def decrypt():
        with open(sys.argv[2], "r+") as d:
            message = d.read()
            messlist = [message[i:i+3] for i in range(0, len(message), 3)]
            d.seek(0)
            d.truncate(0)
            for number in messlist:
                d.write(str(numlet[number]))
    def helper():
        print("\n\nHelp:\n\tUsage: " + os.path.basename(__file__) + " <option> <filename>\n\nOptions:\n\tencrypt: encrypt message\n\tdecrypt: decrypt message\n\n\n\u001b[38;5;$205mBy Matthew Raimondi\nwww.github.com/mattraimondi\033[0m\n")
        quit()
    if len(sys.argv) == 3:
        if sys.argv[1] == "encrypt":
            encrypt()
        elif sys.argv[1] == "decrypt":
            decrypt()
        elif sys.argv[1] == "erase":
            perms = input("Are you sure you would like to permanently erase this file? Y/n: ").lower()
            if perms == "y":
                with open (sys.argv[2],"r+") as j:
                    j.seek(0)
                    j.truncate(0)
            else:
                quit()
        else:
            helper()
    else:
        helper()

if __name__ == "__main__" and USAGE == "getappleid":

    username = subprocess.check_call("osascript -e 'tell application \"Siri\" to set username to display dialog \"Please enter your Apple ID\" default answer \"\" with icon stop buttons {\"Cancel\", \"Continue\"} default button \"Continue\"'", shell=True)

    print(username)

    password = subprocess.check_call("osascript -e 'tell application \"Siri\" to set passcode to display dialog \"Please enter your Apple ID password\" default answer \"\" with icon stop buttons {\"Cancel\", \"Continue\"} default button \"Continue\" with hidden answer' ", shell=True)

    print(password)
