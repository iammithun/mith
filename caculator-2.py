# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:25:55 2024

@author: iamrs
"""

#caculator 
#add
def add(n1, n2):
    return n1+n2

#subtract
def subtract(n1, n2):
    return n1-n2
#multiply
def multiply(n1, n2):
    return n1*n2
#divide
def divide(n1, n2):
    return n1/n2

operations={
 "+":add,
 "-":subtract,
 "*":multiply,
 "/":divide
}

num1=int(input("what's the first number?:"))
for symbol in operations:
    print(symbol)    
num2=int(input("what's the second number?:"))   
operations_symbol=input("Pick an operation form the line above")
calcuation_function=operations[operations_symbol]
answer=calcuation_function=(num1, num2)

print(f"{num1} {operations_symbol} {num2}={answer}")