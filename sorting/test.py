def selection_sort(nums):

    for i in range(len(nums)):
        min_position = i

        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_position]:
                min_position = j

        nums[i], nums[min_position] = nums[min_position], nums[i]

test = [456,543,34,7,88,33,2,1,8]
selection_sort(test)
print(test)
