def slidingMaximum(self, A, B):
    C = []
    for i in range(len(A)-B):
        C.append(max(A[i:i+B]))
        
        
    return C


