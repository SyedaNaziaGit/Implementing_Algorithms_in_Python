#to check performance comparision- using a decorator
#time decorator
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__+" took "+str((end-start)*1000)+"milliseconds")
        return result
    return wrapper

#brute force - Linear Search - Time complexity= O(n)
@time_it
def linear_search(numlist ,findele):
    for index,element in enumerate(numlist):
        if element == findele:
            return index
    return -1

#Binary Search - Time Complexity = O(logn)
@time_it
def binary_search(numlist,findele):
    left_index=0
    right_index = len(numlist)-1
    mid_index =0
    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        mid_ele = numlist[mid_index]
        if mid_ele == findele:
            return mid_index
        if mid_ele < findele:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

def binary_search_recursive(numlist,findele,left_index,right_index):
    if right_index < left_index:
        return -1
    mid_index = (left_index+right_index)//2
    if mid_index >= len(numlist) or mid_index <0:
        return -1
    mid_num = numlist[mid_index]
    if mid_num == findele:
        return mid_index
    if mid_num< findele:
        left_index=mid_index -1
    else:
        right_index = mid_index + 1
    return binary_search_recursive(numlist,findele,left_index,right_index)

#To Find index of all the occurances of a number from sorted list
def finding_all_occurrences(numlist,findele):
    index = binary_search(numlist,findele)
    res_indices = [index]
    #find indices in LHS
    i = index -1
    while i >0:
        if numlist[i] == findele:
            res_indices.append(i)
        else:
            break
        
        i = i -1
    #finding indices in RHS
    i = index + 1
    while i < len(numlist):
        if  numlist[i] == findele:
            res_indices.append(i)
        else:
            break
        i = i + 1
    return sorted(res_indices)

if __name__ =="__main__":
    numlist = [12,15,17,19,21,24,45,67]
    findelement = 45
    index = linear_search(numlist,findele=findelement)
    print(f"Number found at index {index} using Linear Search")#op -Number found at index 6 using Linear Search
    
    findelement = 200
    index = linear_search(numlist,findele=findelement)
    print(f"Number found at index {index} using Linear Search")#op -Number found at index -1 using Linear Search
    
    findelement = 15
    index = binary_search_recursive(numlist,findelement,0,len(numlist))
    print(f"Number found at index {index} using Binary Search with Recursion")#op -Number found at index 1 using Binary Search with Recursion
    
    rep_numlist = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    findelement = 15
    indices = finding_all_occurrences(rep_numlist,findelement)
    print(f"Indices of occurances of {rep_numlist}are {indices}")#op - Indices of occurances of [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]are [5, 6, 7]