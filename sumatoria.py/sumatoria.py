A=[3,5,7,9]
B=[1,4,6,8]
C=[2,0,5,4]

n=len(A)

sum(((A[i]*B[i])+C[i]) for i in range(n))+n**2

