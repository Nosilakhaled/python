# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:05:37 2021

@author: Nosila
"""

num1=float(input("please enter the first number : "))
operator=input("please enter the operator : ")
num2=float(input("please enter the secand number : "))

def sum(num1,num2):
    return num1+num2
#----------------------------

def sub(num1,num2):
    if num1>num2:
      return num1-num2
    else:
    # return "notvalid"
     return num1-num2
#---------------------------------

def mull(num1,num2):
    return num1*num2
#----------------------------------

def div(num1,num2):
    if num2==0:
      return" notvalid divide by 0"
    else:
        return num1/num2

#----------------------------------


if operator== "+" :
    print(sum(num1,num2))
elif operator == "-":
    print(sub(num1,num2))
elif operator == "*":
    print(mull(num1,num2))
elif operator == "/":
    print(div(num1,num2))
    
else:
    print("invalid operator try again")