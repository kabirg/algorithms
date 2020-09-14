def selection_sort(array):

    for i in range(len(array)):
        min_position = i

        for j in range(i+1, len(array)):
            if array[j] < array[min_position]:
                min_position = j

        array[i], array[min_position] = array[min_position], array[i]

my_array = [5,7,8,9,3,1,2,7]
selection_sort(my_array)

print(my_array)
