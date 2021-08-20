#This function asks an integer between 0-255 as input from the user  
def validate1():
    success = False
    while success == False:
        #Exception handling for wrong datatypes
        try:
            a= int(input("Enter the first number: "))
            print("")
            #Checking if the number is between 0-255
            if a<0 or a>255:
                print("Invalid Input. Please enter a number between 0 and 255 \n")
            else:
                success = True  
        except:
            print("")
            print("Invalid Input. Please enter a proper value. \n")
    return a
#This function asks an integer between 0-255 as input from the user  
def validate2():
    success = False
    while success == False:
        #Exception handling for wrong datatypes
        try:
            b= int(input("Enter the second number: "))
            print("")
            #Checking if the number is between 0-255
            if b<0 or b>255:
                print("Invalid Input. Please enter a number between 0 and 255 \n")
            else:
                success = True  
        except:
            print("")
            print("Invalid Input. Please enter a proper value. \n")
    return b
