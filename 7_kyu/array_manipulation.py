def array_manip(arr):
    return [min([el for el in arr[i+1:] if el > arr[i]], default=-1) for i in range(len(arr))]