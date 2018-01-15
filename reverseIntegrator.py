#!/usr/bin/env python3
#
# integrator
#
# Author: Timothy Baker
# Date  : September 2017
# Class : CS 517
# Assg  : Machine Assignment 1, Problem 4

import struct

# python3 defaults to double precision, emulate 32 returns
# a 32 bit float. This function must be called on every 
# variable in every operation to maintain 32 bit values
def em32(real64) :
    real32 = struct.unpack('f', struct.pack('f', real64))[0]
    return real32

# returns 32 bits worth of euler's constant in floating point format
def e() :
    return em32(2.718281828459045235360287471352662497757247093699959574966967627724076630353)

def revInt(n, N) :    
    if n == N :
        return 1
    else :
        return ((em32(1.0)/e()) + (revInt(em32(n)+ em32(1.0), em32(N)))) * em32((em32(1.0)/em32(em32(n)+em32(1.0)))) 
def main() :
            print("\n\n")
            print("\t     N=14 \t\t\t N=16 \t\t\t N=18 \t\t\t N=20")
            for i in range (0,13) :
                print("n =",i,", Yn =",revInt(em32(i), em32(14.0)), "\t" ,revInt(em32(i), em32(16.0)),"\t" ,revInt(em32(i), em32(18.0)),"\t" ,revInt(em32(i), em32(20.0)))
            print("\n\n")
 
if __name__ == "__main__":
    main()

#end of file 
