# Get a missing number in [ 1...100]
def getMissingNo(A):
    n=len(A)   #n=5
    total=(n+1)*(n+2)/2  #21
    sum_of_A=sum(A)   #16
    return total-sum_of_A

A = [1, 2, 3, 4, 6]
miss = getMissingNo(A)
print(miss)