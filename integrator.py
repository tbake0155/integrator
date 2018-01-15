#!/usr/bin/env python3
#
# integrator
#
# Author: Timothy Baker
# Date  : September 2017
# Class : CS 517
# Assg  : Machine Assignment 1, Problem 4

import sys
import struct

# python3 defaults to double precision, emulate 32 returns
# a 32 bit float. This function must be called on every 
# variable in every operation to maintain 32 bit values
def emulate32(real64) :
    real32 = struct.unpack('f', struct.pack('f', real64))[0]
    return real32

# returns 32 bits worth of euler's constant in floating point format
def e() :
    return emulate32(2.718281828459045235360287471352662497757247093699959574966967627724076630353)

def integrator(n) :    
    if n == 0 :
        return emulate32((emulate32(-1.0)/e())+emulate32(1.0))
    else :
        return (emulate32(n)*emulate32(integrator(emulate32(n)-emulate32(1.0)))) - emulate32(emulate32(1.0)/e()) 
def main() :
    if len(sys.argv) < 2 :
        print("error: requires an integer value for 'n'")
    else :
        n = int(sys.argv[1])
        try :
            print("\n\n")
            for i in range (0,int(n)) :
                print("n =",i,", Yn =",integrator(emulate32(i))) 
            print("\n\n")
        except :
            print("recursion limit reached")
 
if __name__ == "__main__":
    main()

#end of file 
