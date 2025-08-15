nums = [1, 2, 5, 6, 11, 3, 7, 9]


def max_two_nums(nums):
    if len(nums) <= 2:
        return nums
    else:
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[0:2]


print(max_two_nums(nums))
