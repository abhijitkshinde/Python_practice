def merge(left,right,arr):
    i = 0
    j = 0
    k = 0
    m = len(left)
    n = len(right)
    while i<m and j<n:
        if left[i]<=right[j]:
            arr[k] = left[i]
            i = i+1
        elif right[j]<= left[i]:
            arr[k] = right[j]
            j = j+1
        k = k+1
    while i<m:
        arr[k] = left[i]
        k = k+1
        i = i+1
    while j<n:
        arr[k] = right[j]
        k = k+1
        j = j+1
    del(right)
    del(left)

def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    
    mid = n//2
    left = [0]*mid
    right = [0]*(n-mid)

    for i in range(mid):
        left[i] = arr[i]
    for j in range(mid,n):
        right[j-mid] = arr[j]
    
    merge_sort(left)
    merge_sort(right)

    merge(left,right,arr)

A = [2,9,3,1,4,5,10,22,44,98,4,2,4,0]

merge_sort(A)
print(A)