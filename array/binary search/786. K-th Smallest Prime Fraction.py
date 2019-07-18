import math

def kthSmallestPrimeFraction(A, K):
    err = 1e-9
    def smaller(AA, lens, val):
        cnt = 0
        for i in range(1, lens):
            lo = 0
            hi = i-1
            while lo<hi:
                mid = (lo+hi)/2
                curVal = 1.0*AA[mid]/AA[i]
                if abs(curVal-val)<=err:
                    lo = mid
                    break
                elif curVal<val:
                    lo = mid+1
                else:
                    hi = mid-1

            cnt += lo
        return cnt

    lens = len(A)
    lo = 1.0/A[-1]
    hi = (A[-1]-1)/A[-1]
    while hi-lo < err:
        mid = (hi+lo)/2
        cnt = smaller(A, lens, mid)
        if cnt > K-1:
            hi = mid-1
        else:
            lo = mid+1

    for i in range(lens):
        p = int(math.ceil(A[i]*lo))
        print(p)

        if (p < A[i]) and (p in A) and (abs(p/A[i]-lo) < err):
            return [p,A[i]]

    return []

A = [1, 2, 3, 5]
K = 3
print(kthSmallestPrimeFraction(A, K))