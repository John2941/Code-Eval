# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:59:23 2015

@author: JOHNATHAN
@url - https://www.codeeval.com/open_challenges/52/
"""

import sys
import os


lines = []


        
def changeToText(_int):
    if len(_int) >= 7:
        milly(_int,pass_thru='y')
    if len(_int) in [4,5,6]:
        thousand(_int,pass_thru='y')
    if len(_int) == 3:
        hundred(_int,pass_thru='y')
    if len(_int) == 2:
        tens(_int,pass_thru='y')
    if len(_int) == 1:
        single(_int,pass_thru='y')


def milly(_int,pass_thru='n'): #len between 9 and 7 // int[:-6] returns the million numbers only
    if int(_int[:-6]) != 0:
        hundred(_int[:-6],pass_thru='n')
        sys.stdout.write("Million")
    return thousand(_int[-6:],pass_thru) ##always pass the whole remained of int when done minus the millions

def thousand(_int,pass_thru='n'):
    if int(_int[:-3]) != 0:
        if len(_int[:-3]) == 3:
            hundred(_int[:-3],pass_thru='n')
        if len(_int[:-3]) == 2:
            tens(_int[:-3],pass_thru='n')
        if len(_int[:-3]) == 1:
            single(_int[:-3],pass_thru='n') 
        sys.stdout.write("Thousand")
    hundred(_int[-3:],pass_thru)

        
def hundred(_int,pass_thru='n'):
    if int(_int) != 0:
        if _int[0] == '0' and len(_int) == 3:
            return tens(_int[-2:],pass_thru)
        if len(_int) == 2:
            return tens(_int,pass_thru)
        if len(_int) == 1:
            return single(_int[0],pass_thru)
        if len(_int) == 3:
            single(_int[0],pass_thru='n')
        sys.stdout.write("Hundred") 
        return tens(_int[-2:],pass_thru)
    return single(_int[-1],pass_thru)


def tens(_int,pass_thru='n'):
    if _int[0]  == '0':
        single(_int,pass_thru='n')
    if _int[0]  == '9':
        sys.stdout.write("Ninety")
    if _int[0]  == '8':
        sys.stdout.write("Eighty")
    if _int[0]  == '7':
        sys.stdout.write("Seventy")
    if _int[0]  == '6':
        sys.stdout.write("Sixty")
    if _int[0]  == '5':
        sys.stdout.write("Fifty")
    if _int[0]  == '4':
        sys.stdout.write("Forty")
    if _int[0]  == '3':
        sys.stdout.write("Thirty")
    if _int[0]  == '2':
        sys.stdout.write("Twenty")
    if _int[0]  == '1':
        if _int == '19':
            sys.stdout.write("Nineteen")
        if _int == '18':
            sys.stdout.write("Eighteen")
        if _int == '17':
            sys.stdout.write("Seventeen")
        if _int == '16':
            sys.stdout.write("Sixteen")
        if _int == '15':
            sys.stdout.write("Fifteen")
        if _int == '14':
            sys.stdout.write("Fourteen")
        if _int == '13':
            sys.stdout.write("Thirteen")
        if _int == '12':
            sys.stdout.write("Twelve")
        if _int == '11':
            sys.stdout.write("Eleven")
        if _int == '10':
            sys.stdout.write("Ten")
        if pass_thru == 'y':
            return finish()
    return single(_int[-1],pass_thru)

def single(_int,pass_thru='n'):
    if _int == '9':
        sys.stdout.write("Nine")
    if _int == '8':
        sys.stdout.write("Eight")
    if _int == '7':
        sys.stdout.write("Seven")
    if _int == '6':
        sys.stdout.write("Six")
    if _int == '5':
        sys.stdout.write("Five")
    if _int == '4':
        sys.stdout.write("Four")
    if _int == '3':
        sys.stdout.write("Three")
    if _int == '2':
        sys.stdout.write("Two")
    if _int == '1':
        sys.stdout.write("One")
    if pass_thru == 'y':
        return finish()
    return 


def finish():
   return sys.stdout.write("Dollars\n")


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    for one_line in input_file.readlines():#input argv file into list wihtout newline character
        if one_line != "":            
            lines.append(one_line.strip("\n"))
    for line in lines:
        if line == '0':
            sys.stdout.write("Zero")
        if int(line) >= 1000000000:
            sys.stdout.write("Number to large to convert.\n")
            continue
        changeToText(line)
        
        