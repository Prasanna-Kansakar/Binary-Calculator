#This function converts the integer given in the parameter to binary
def first_no(a):
    l=[]
    n=0
    while n<8:
        w= a%2
        a= a//2
        l.append(w)
        n+=1
    k=[]
    #Reversing the list inorder to complete the conversion
    for i in range(len(l)-1,-1,-1):
        k.append(l[i])
    return k 
#This function converts the integer given in the parameter to binary   
def second_no(b):
    m=[]
    n=0
    while n<8:
        w= b%2
        b= b//2
        m.append(w)
        n+=1
    o=[]
    #Reversing the list inorder to complete the conversion
    for i in range(len(m)-1,-1,-1):
        o.append(m[i])
    return o
    
    
