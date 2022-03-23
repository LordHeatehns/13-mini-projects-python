'''size = 2
asciiNumber = 65
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber += 1
    print(" ")'''




'''def print_pattern(n):
    for rows in range(n):
        for column in range(n):
            if ((rows == 0 or rows == n-1 ) or (column == n//2)):

               print("*" ,end=" ")
            
            else:
                print(" ",end=" ")
            
        print("")

be = print_pattern(3)'''

'''size = 5
x= "x"
for rows in range(size):
   for column in range(size):
        if(column == 0 or column == size-1 or rows ==column):
           print(x,end=" ")

        else:
            print(" ",end=" ")


   print()'''



###  H
'''size= 7

for rows in range(size):
    for column in range(size):
        if (column == 0  or column == size -1 or rows == (size/2 ) +0.5 -1  ):
            print("X",end=" ")

        else:
            print(" ",end=" ")


    print()'''





'''row = 9
col = 5


for rows in range(row):
    for column in range(col):
        if(rows == 0  or rows == row-1  or column == 0 or rows == (row/2)+0.5  -1):
            print('x',end=" ")

        else:
            print("",end=" ")

    print()'''


 


'''row = 7
col = 4


for rows in range(row):
    for column in range(row-3):
        if (column == 0  or rows == row-1):
            print("X",end=" ")
        
        else:
            print("",end=" ")

    print()'''


'''row = 5
for rows in range(row):
    for column in range(row):
        if (rows == 0  and column == row//2):
           print("x",end=" ") 
        else:
            print("",end=" ")
        
    print()'''





'''n = 9
for rows in range(n):
    for column in range(n):
        if (rows+column == n-1 and rows < n/2)   or (rows == column and rows < n/2):
            print("x",end=" ")
        
        else:
            print(" ",end=" ")

    print()'''



'''n = 9

for rows  in range(n):
    for column in range(n):
        if (rows == 0  or rows== n-1 or rows+column == n-1 ):
            #medtod2  column ==  n-rwos-1
            print('x',end=" ")
        
        else:
            print(" ",end=" ")
    print()'''


'''n= 5

for rows in range(n):
    for column in range(n):
        if ((rows +column == n-1  )  or (rows == column)):
            print('x',end=" ")
        
        else:
            print(' ',end=" ")
    
    print()'''



'''n = 7

for rows in range(n):
    for column in range(n-2):
        if (rows== 0 or rows == n-1 or  column ==0 or rows == n//2 ):
            print('E',end=" ")
        
        else:
            print(' ',end=" ")

    
    print()'''

'''n=7 


for rows in range(n):
    for column in range(n):
        if ((rows != n-1 and column ==0  or   column ==n-1 and rows != n-1 or rows == n-1 and column !=0 and column!=n-1)):
            print('U',end=" ")
        
        else:
            print(' ',end=" ")

    
    print()'''




'''n=7 
for rows in range(n):
    for column in range(n):
        if ((rows != n-1 and rows!=0 and column ==0  or   column ==n-1 and rows != n-1 and rows!=0 or rows == n-1 and column !=0 and column!=n-1 or rows ==0 and column !=0 and column!= n-1)):
            print('O',end=" ")
        
        else:
            print(' ',end=" ")

    
    print()'''


'''n = 7

for rows in range(n):
    for column in range(n):
        if (rows ==0  or column == n//2):
            print('T',end=' ')
        
        else:
            print(" ",end=" ")

    print()'''



'''n = 7

for rows in range(n):
    for column in range(n):
        if (rows ==0 and column <n-2 or column == 0 or rows == n//2 and column < n-2):
            print('T',end=' ')
        
        else:
            print(" ",end=" ")

    print()'''


'''n = 9

for rows in range(n):
    for column in range(n):
        if (column == 0 or column == n-1  or rows ==column and rows <= n//2  or column == n-rows-1 and rows <=n//2):
            print('M',end=' ')
        
        else:
            print(" ",end=" ")

    print()'''




'''n = 9

for rows in range(n):
    for column in range(n):
        if (rows + column == n-1 or rows == column and rows < n/2):
            print('Y',end=' ')
        
        else:
            print(" ",end=" ")

    print()'''




'''n = 9

for rows in range(n):
    for column in range(n):
        if (column == 0 or column == n-1  or rows ==column and rows <= n//2  or column == n-rows-1 and rows <=n//2):
            print('M',end=' ')
        
        else:
            print(" ",end=" ")

    print()'''





'''n = 9

for rows in range(n):
    for column in range(n):
        if (column == 0  or column ==n-1  or rows > n/2 and column==rows  or rows > n/2  and column == n-rows ):
            print('W',end=' ')
        
        else:
            print(" ",end=" ")

    print()'''




'''n = 7 

for rows in range(n):
    for column in range(n):
        if (column ==n-1  or column > n/2 and rows == n-1 or rows == n-2 and column == n-4):
            print('J',end=" ")
        
        else:
            print(" ",end=" ")

    print()'''






'''n = 7 

for rows in range(n):
    for column in range(n):
        if (column == 0 or rows == 0 and column < n/2 or rows == n-1 and column < n-3 or column == n//2 +1 and rows > 0  and rows < n-1):
            print('D',end=" ")
        
        else:
            print(" ",end=" ")

    print()'''

n = 11

for rows in range(n):
    for column in range(n):
        if (column == 0 or rows == 0 and column < n/2 or rows == n-1 and column < n//2 +1 or column == n//2 +1 and rows > 0  and rows < n-1 or rows == n//2 and column < n//2 +1):
            print('D',end=" ")
        
        else:
            print(" ",end=" ")

    print()





    














            
            



        


    
    