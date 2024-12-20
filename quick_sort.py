def quicksort(arr,low,high):
    if low<high:
        p = partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)
   
def partition(arr,low,high):
    
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
    
if __name__ == '__main__':

    arr = [int(x) for x in input("Enter multiple values: ").split()]
    low = 0
    high = len(arr)-1
    quick_sort(arr,low,high)
    print(arr)
