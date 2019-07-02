def searchInsert(nums, target):
    left, right = 0, len(nums)-1
    mid = -1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            break
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    if mid == -1 or nums[mid] != target:
        return [-1,-1]

    #min idx
    minIdx = mid
    while left <= minIdx:
        curmid = (left+minIdx)//2
        if nums[curmid] == target and minIdx != curmid:
            minIdx = curmid
        else:
            left = curmid+1

    #max idx
    maxIdx = mid
    while maxIdx <= right:
        curmid = (maxIdx+right)//2+(maxIdx+right)%2
        if nums[curmid] == target and maxIdx != curmid:
            maxIdx = curmid
        else:
            right = curmid-1
    return [minIdx, maxIdx]

nums = []
target = 7
print(searchInsert(nums, target))