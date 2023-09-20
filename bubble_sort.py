def bubble_sort(arr):
    
    for i in range(0,len(arr)):
        for j in range(len(arr)-1,i,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
    return arr
    
if __name__ == '__main__':
    
    arr = [int(x) for x in input("Enter multiple values: ").split()]
    bubble_sort(arr)
