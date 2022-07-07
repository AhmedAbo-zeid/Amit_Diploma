# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 19:23:28 2022

@author: Ahmed_AboZeid
"""
import calc

while(1):
    Operation = input("Please enter the desired operation from (ADD , SUB , MUL , DIV) : ")
    Operand1 = int(input("Please enter the first operand : "))
    Operand2 = int(input("Please enter the second operand : "))
        
    if Operation=='ADD':
        Result = calc.Add(Operand1,Operand2)
        print(" = ",Result)
    elif Operation=='SUB':
        Result = calc.Sub(Operand1,Operand2)
        print(" = ",Result)
    elif Operation=='MUL':
        Result = calc.Mul(Operand1,Operand2)
        print(" = ",Result)
    elif Operation=='DIV':
        Result = calc.Div(Operand1,Operand2)
        print(" = ",Result)
    else:
        print("Error: Unknown operation")

    AGN = input("Would you like to try another operation? (Y/N)")
    if AGN == 'N':
        print("GoodBye!!")
        break
    elif AGN == 'Y':
        continue