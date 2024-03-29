def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target: return True
        if nums[mid] == nums[left]:
            left += 1
        elif nums[mid] > nums[left]:
            if nums[mid] > target and nums[left] <= target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and nums[right] >= target:
                left = mid + 1
            else:
                right = mid - 1
    return False
nums = [1,3,1,1,1,1]
target = 3
print(search(nums, target))