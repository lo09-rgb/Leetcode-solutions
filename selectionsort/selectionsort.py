def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current position has the minimum element
        min_index = i

        # Find the actual minimum element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example
numbers = [64, 25, 12, 22, 11]
print(selection_sort(numbers))
