import string
import math
a=[]
def go_on(A, R = []):
    c=0
    if len(A) > 0: 
        go_on(A[1:], R + [int(A[:1])]) # R contains the first character, A contains the Rest

        if len(A) > 1: #Check the length

            if int(A[:2]) < 80: # if Length is less than 80

                go_on(A[2:], R + [int(A[:2])]) #consider the numbers and go_on()
            else:
                a.append('NO') #NO is appended
                return # And we EXIT
    else:

        if len(R) == 8 and len(R) == len(set(R)): # If Len(A)<1 , the string is of length 8 (single digits)
            a.append(list(map(str, R)))  #Print as provided


s=input() #input here

if s.isdigit()==True: #checking for digits
    go_on(s) # pass on to go_on()

    if a.count('NO')==len(a):
        print('NO')
    else:
        for i in a:
            if i!='NO':
                print(' '.join(i)) # print out
    
else:
    print('NO')
