#!/usr/bin/env python3
#
# integrator that does not force single precision
#
# Author: Timothy Baker
# Date  : September 2017
# Class : CS 517
# Assg  : Machine Assignment 1, Problem 4

import sys

# euler's constant in floating point format
def e() :
    return 2.718281828459045235360287471352662497757247093699959574966967627724076630353

def integrator(n) :    
    if n == 0 :
        return (-1.0/e())+1.0
    else :
        return (n*integrator(n- 1.0)) - (1.0/e()) 
def main() :
    if len(sys.argv) < 2 :
        print("error: requires an integer value for 'n'")
    else :
        n = int(sys.argv[1])
        try :
            print("\n\n")
            for i in range (0,int(n)) :
                print("n =",i,", Yn =",integrator(i)) 
            print("\n\n")
        except :
            print("recursion limit reached")
 
if __name__ == "__main__":
    main()

#end of file 
