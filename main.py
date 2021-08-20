#importing necessary modules 
import BinarytoDecimal
import Bitadder
import Greeting
import inputcheck
Continue = False
#Calling begining() function from Greeting module 
Greeting.beginning()
# while loop that terminates until user wants
while Continue == False:
    #Calling validate1() function from inputcheck module 
    a=inputcheck.validate1()
    #Calling validate2() function from inputcheck module 
    b=inputcheck.validate2()
    #Calling first_no function from BinarytoDecimal module 
    k= BinarytoDecimal.first_no(a)
    #Calling second_no function from BinarytoDecimal module
    o= BinarytoDecimal.second_no(b)
    #Calling bit_adder() function from Bitadder module 
    finalSum = Bitadder.bit_adder(k,o)
    print("Binary addition of the Two numbers is: ",finalSum,"\n")
    #Asking input from user in order to close the program
    g=input("Enter No to exit the Program: ")
    #if conditon to check the value of variable g
    if g.lower()=="no":
        Continue = True
    else:
        print("\n")
#Calling ending() function from Greeting module
Greeting.ending()
