numList = []
# append used to data on the list
numList.append(21)
numList.append(40.8)
numList.append("Helo world")

print(numList)

# some calculation

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = num1 * num2
print("product of both numbers is ", num3)

#if else condition

if(num3 > 450):
     print("Larger number")
else:
    print("smaller number")
    
for steps in range(5):
    print(steps)
    
#importing math library
import math

def Main():
    num = float(input("Enter a number: "))
    num= math.fabs(num)
    print("Number is ", num )
    
if __name__ == "__main__":
    Main()
