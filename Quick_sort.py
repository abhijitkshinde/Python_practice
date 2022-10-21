import random




def partition(A,start,end):
    p_index = start
    p_value = A[end-1]
    for i in range(start,end-1):
        if A[i] <= p_value:
            A[i], A[p_index] = A[p_index],A[i]
            p_index = p_index + 1
    
    A[p_index],A[end-1] = A[end-1],A[p_index]
    return p_index


def quick_sort(A,start,end):
    if len(A) == 1:
        return A
    
    if start<end-1:
        p_index = partition(A,start,end)
        quick_sort(A,start,p_index)
        quick_sort(A,p_index+1,end)
    return A



size = 1000
A = []

for i in range(1000):
    A.append(random.randrange(10))

print(A)
B = quick_sort(A,0,len(A))

print(B)
