for row in range(7):
    for col in range(7):
        if  (col==4 or row!=3 and col!=4 ) and (col==3 or row!=2):
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print() 
