#This function adds the two binary numbers present in its parameter
def bit_adder(k,o):
    A=0
    B=0
    C=0
    Sum=''
    x=0
    finalSum=''
    for i in range(7,-1,-1):
        A=k[i]
        B=o[i]
        carry1 = A&B
        ans1 = A^B
        carry2 = ans1&C
        fanswer = ans1^C
        fcarry = carry1|carry2
        C= fcarry
        Sum = str(fanswer) + Sum
    for i in range(0,len(Sum)):
        #if condition for removing unnecessary 0s from the final sum
        if Sum[i]=='1' or x==1 or i==len(Sum)-1:
            finalSum=finalSum+str(Sum[i])
            if Sum[i]=='1':
                x=1
    return finalSum
