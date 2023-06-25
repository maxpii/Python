def quicksort(nums):
    if len(nums) <= 1:
        return nums
    ltp = []
    gtp = []
    pivot = nums[0]
    for i in nums[1:]:
        if i < pivot:
            ltp.append(i)
        else:
            gtp.append(i)
    return quicksort(ltp) + [pivot] + quicksort(gtp)


print(quicksort([5, 62, 766, 26, 2]))
