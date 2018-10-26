def counting_sort(A, digit, radix):
    #"A" is a list to be sorted, radix is the base of the number system, digit is the digit
    #list B the sorted list
    B = [0]*len(A)
    #list C contains the number of occurences of each digit in A 
    C = [0]*int(radix)
    
    for i in range(0, len(A)):
        value_Ai = (A[i]/radix**digit)%radix
        C[value_Ai] = C[value_Ai] +1 

    #this FOR loop changes C to show the cumulative # of digits up to that index of C
    for j in range(1,radix):
        C[j] = C[j] + C[j-1]
        #here C is modifed to have the number of elements <= i
    for m in range(len(A)-1, -1, -1):    #to count down (go through A backwards)
        value_Ai = (A[m]/radix**digit)%radix
        C[value_Ai] = C[value_Ai] -1
        B[C[value_Ai]] = A[m]

    return B
