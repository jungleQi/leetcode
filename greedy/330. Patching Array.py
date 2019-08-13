def minPatches(nums, n):
    padding = []
    N = len(nums)
    i, val = 0, 1
    while val <= n:
        if i>= N or val < nums[i]:
            padding.append(val)
            i += 1
            val = sum(nums[:i]) + sum(padding)
        else:
            if sum(nums[:i]) + sum(padding) < val:
                i += 1
            else:
                val += 1
        print(val,i, padding)

    return len(padding)

nums = [1,3]
n = 6
print minPatches(nums, n)
