for row in range(7):
    for col in range(5):     
        if((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):    
            print("*",end="")    
        else:      
            print(end=" ")
    print()        

print("\n\n")

for row in range(7):
    for col in range(5):     
        if(col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):    
            print("*",end="")    
        else:      
            print(end=" ")
    print()

print("\n\n")

for row in range(7):
    for col in range(5):     
        if(col==0 and ( row!=0 and row!=6)) or ((row==0 or row==6) and (col>0)):    
            print("*",end="")    
        else:      
            print(end=" ")
    print()

print("\n\n")

for row in range(7):
    for col in range(5):     
        if(col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):    
            print("*",end="")    
        else:      
            print(end=" ")
    print()

print("\n\n")

for row in range(7):
    for col in range(5):     
        if (col==0) or ((row==0 or row==3 or row==6) and (col>0)):
            print("*",end="")    
        else:      
            print(end=" ")
    print()


print("\n\n")

for row in range(7):
    for col in range(5):     
        if (col==0) or ((row==0 or row==3) and (col>0)):
            print("*",end="")    
        else:      
            print(end=" ")
    print()


print("\n\n")

for row in range(7):
    for col in range(5):     
        if(col==0) or (col==4 and (row!=1 and row!=2)) or ((row==0 or row==6) and (col>0 and col<4)) or (row==3 and (col==3 or col==5)):    
            print("*",end="")    
        else:      
            print(end=" ")
    print()


print("\n\n")

for row in range(7):
    for col in range(5):     
        if col==0 or col==4 or (row==3 and (col>0 and col<4)):
            print("*",end="")    
        else:      
            print(end=" ")
    print()

 
print("\n\n")

for row in range(7):
    for col in range(5):     
        if col==2 or ((row==0 or row==6) and (col!=2)):
            print("*",end="")    
        else:      
            print(end=" ")
    print()


print("\n\n")

for row in range(7):
    for col in range(5):     
        if col==2 or (row==0 and col!=2) or (row==6 and col<2):
            print("*",end="")    
        else:      
            print(end=" ")
    print()

print("\n\n")

i=0
j=4
for row in range(7):
    for col in range(5):     
        if col==0 or (row==col+2 and col>1):
            print("*",end="")
        elif ((row==i and col==j) and col>0):
                print("*",end="")
                i=i+1
                j=j-1
        else:      
            print(end=" ")
    print()

print("\n\n")

for row in range(7):
    for col in range(5):     
        if col==0 or row==6:
            print("*",end="")    
        else:      
            print(end=" ")
    print()

print("\n\n")

for row in range(7):
    for col in range(7):     
        if (col==0 or col==6):
            print("*",end="")
        elif(row==1 and col==2) or (row==1 and col==4):
            print("*",end="")
        elif(row==2 and col==3):
            print("*",end="")
        else:      
            print(end=" ")
    print()

print("\n\n")

for row in range(7):
    for col in range(7):
        if (col==0 or col==6):
           print("*",end="")
        else:
            print(end=" ")
    print()
