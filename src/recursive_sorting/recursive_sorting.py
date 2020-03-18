# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a=0
    b=0

    for i in range(0, elements):
        if len(arrA) <= a:
            merged_arr[i]= arrB[b]
            b += 1   
        elif len(arrB) <= b: 
            merged_arr[i]= arrA[a]
            a += 1   
        elif arrA[a] < arrB[b]: 
            merged_arr[i]= arrA[a]
            a += 1   
        else: 
            merged_arr[i]= arrB[b]
            b += 1   
        
    # merged_arr=[]
    # while len(arrA) > 0 and len(arrB) > 0:
    #     if arrA[0] > arrB[0]:
    #         merged_arr.append(arrB[0])
    #         arrB.pop(0)
    #     else:
    #         merged_arr.append(arrA[0])
    #         arrA.pop(0)   
    # while len(arrA) > 0:
    #         merged_arr.append(arrA[0])
    #         arrA.pop(0) 
    # while len(arrB) > 0:
    #         merged_arr.append(arrB[0])
    #         arrB.pop(0)                


    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        middle_index = len(arr)//2
        left_arr= arr[:middle_index]   
        right_arr= arr[middle_index:]

        arrSortA= merge_sort(left_arr)
        arrSortB= merge_sort(right_arr)

        arr=merge(arrSortA,arrSortB)


    return arr

finalArr= [3, 5, 4, 7, 32, 6, 45, 65, 78, 97, 43, 435, 665, 98]
print(merge_sort(finalArr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
