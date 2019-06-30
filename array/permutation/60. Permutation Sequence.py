import os

def getPermutation(n, k):
    nums = [i + 1 for i in range(n)]
    facbs = {}
    for i in range(n):
        if i == 0:
            facbs[i] = 1
        else:
            facbs[i] = facbs[i - 1] * i

    ret = []
    for i in range(1, n + 1):
        if k == 1:
            ret += nums
            break
        idx = int((k - 1) / facbs[n - i])
        ret += nums[idx],
        del nums[idx]

        k = k % facbs[n - i]

    strret = [str(i) for i in ret]
    return "".join(strret)

print(getPermutation(3,3))