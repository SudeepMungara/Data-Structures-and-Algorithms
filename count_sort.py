def count_sort(arr):
    
    max_ele = max(arr)
    count_arr = [0]*(max_ele+1)
    output = [0]*len(arr)

    for val in range(0,len(arr)):
        count_arr[arr[val]]+=1
    
    for val in range(1,len(count_arr)):
        count_arr[val] = count_arr[val]+count_arr[val-1]
    
    for val in range(len(arr)-1,-1,-1):

        output[count_arr[arr[val]]-1] = arr[val]
        count_arr[arr[val]]-=1
    
    for val in range(0,len(arr)):
        arr[val] = output[val]

    return output

if __name__ == '__main__':

    arr = [int(x) for x in input("Enter multiple values: ").split()]
    print(count_sort(arr))
