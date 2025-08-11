    #Time complexity- O(nlogn)
def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_lists(left, right, arr)
    
def merge_two_sorted_lists(l1,l2,arr):
    len_a = len(l1)
    len_b = len(l2)
    i = j = k = 0
    while i < len_a and j < len_b:
        if l1[i] <= l2[j]:
            arr[k] = l1[i]
            i+=1
        else:
            arr[k] = l2[j]
            j+=1
        k+=1
    while i < len_a:
        arr[k] = l1[i]
        i+=1
        k+=1
    while j < len_b:
        arr[k] = l2[j]
        j+=1
        k+=1

if  __name__ == "__main__":
    #a = [5,8,12,56,100,89]
    #b = [7,9,45,51]
    #print(merge_two_sorted_lists(a,b))
    arr = [10,3,15,7,8,23,98,29]
    merge_sort(arr)
    print(arr)#op -[3, 7, 8, 10, 15, 23, 29, 98]