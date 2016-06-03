import random
def counting_sort(A,k):
    if len(A) <= 1:
        return A
    else:
        B = [0 for _ in range(len(A))]
        C = [0 for _ in range(k)]
        for j in range(0,len(A)):
            C[A[j]] += 1
        for j in range(1,k):
            C[j] += C[j-1]
        for j in range(len(A) - 1,0,-1):
            x = A[j]
            B[C[x] - 1] = x
            C[x] = C[x] - 1
        return B

print(counting_sort([random.randint(0,100) for _ in range(10)],100))
            
