def quick_sort(arr,first_index,last_index):
    if first_index<last_index:
        parition_pos = partition(arr,first_index,last_index)
        quick_sort(arr,first_index,parition_pos-1)
        quick_sort(arr,parition_pos+1,last_index)
    
def partition(arr,first_index,last_index):
    
    i = first_index
    j = last_index-1
    pivot = arr[last_index]
    
    while i<j:
        while arr[i] < pivot and i<last_index:
            i+=1
            
        while arr[j] >= pivot and j>first_index:
            j-=1
            
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
            
    if arr[i] > pivot:
        arr[i],arr[last_index] = arr[last_index],arr[i]
        
    return i
    
if __name__ == '__main__':

    arr = [int(x) for x in input("Enter multiple values: ").split()]
    first = 0
    last = len(arr)-1
    quick_sort(arr,first,last)
    print(arr)
