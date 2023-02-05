def larrysArray(A):
    s=0
    for i in range(len(A)):
        s+=sum(1 if A[i]>A[j] else 0 for j in range(i+1,len(A)))
    return 'YES' if s%2==0 else 'NO'
  

    
