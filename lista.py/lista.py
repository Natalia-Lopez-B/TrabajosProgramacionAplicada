A=[2,4,6,8]
B=[3,5,7,9]

n=len(A)//2

[((A[i+1])**2 *B[2*i]) +B[n+i] for i in range(n)]