def shell_sort(arr):
    size = len(arr)
    gap = size//2
    while gap > 0:
        for i in range(gap,size):
            curr_ele = arr[i]
            j = i
            while j>=gap and arr[j-gap]>curr_ele:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = curr_ele
        gap = gap // 2
        
if __name__ == '__main__':
    elements = [89,78,61,53,23,21,17,12,9,7,6,2,1]
    shell_sort(elements)
    print(elements) #op -[1, 2, 6, 7, 9, 12, 17, 21, 23, 53, 61, 78, 89]
''''
def foo(arr):
    size = len(arr)
    gap = size // 2
    gap = 3
    for i in range(gap, size):
        curr_ele = arr[i]
        j = i
        while j>=gap and arr[j-gap]>curr_ele:
            arr[j] = arr[j-gap]
            j -= gap
        arr[j] = curr_ele
'''