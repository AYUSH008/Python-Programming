#using in for check
if "s" in "Ayush":
    print("yes")
else:
    print("no")
    
#using i in for loop
for i in "AyushAshatkar":
    print(i,end=" ")
    
#print all the lis of keyword

import keyword

print("The list of keyword is: ")
print(keyword.kwlist)

#simple calculator

def addition(num1 , num2):
    return num1 + num2
def substarction(num1 , num2):
    return num1 - num2
def multiply(num1 , num2):
    return num1 * num2
def division(num1 , num2):
    return num1 / num2

print("please select operation : -\n" \
    "1. Addition \n" \
    "2. subtract\n"\
    "3. multiply\n"\
    "4. divide\n" 
    )

select = int(input("Enter Number to perform operation: "))

num1= int(input("enter 1st number : "))
num2= int(input("enter 2st number: "))

if select == 1: 
    print(num1, "+", num2, "=", 
                    addition(num1, num2)) 
  
elif select == 2: 
    print(num1, "-", num2, "=", 
                    substarction(num1, num2)) 
  
elif select == 3: 
    print(num1, "*", num2, "=", 
                    multiply(num1, num2)) 
  
elif select == 4: 
    print(num1, "/", num2, "=", 
                    division(num1, num2)) 
else: 
    print("Invalid input") 
    
 