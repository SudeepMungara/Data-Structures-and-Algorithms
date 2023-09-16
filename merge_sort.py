def merge_sort(arr,first_index,last_index):
    if len(arr)>1:
        mid = first_index+(last_index - first_index)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        merge_sort(left_arr,0,len(left_arr))
        merge_sort(right_arr,0,len(right_arr))
        
        i = j = k =0
        
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<=right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            elif left_arr[i]>right_arr[j]:
                arr[k] = right_arr[j]
                j+=1
            k+=1
            
        while i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        
        while j<len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
    return arr
    
if __name__ == '__main__':

    arr = [int(x) for x in input("Enter multiple values: ").split()]
    first = 0
    last = len(arr)
    print(merge_sort(arr,first,last))
