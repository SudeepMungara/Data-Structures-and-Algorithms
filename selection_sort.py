def selection_sort(arr):
    
    for i in range(0,len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

if __name__ == '__main__':
    
    arr = [int(x) for x in input("Enter multiple values: ").split()]
    selection_sort(arr)
    
