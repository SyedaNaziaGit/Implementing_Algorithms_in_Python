#Time complexity= O(n*square)
#Space complexity = O(1)
def bubble_sort(elements):
    size = len(elememts)
    for k in range(size-1):
        swapped = False
        for i in range(size -1-k):
            if elememts[i] >elememts[i+1]:
                tmp =elememts[i]
                elememts[i] = elememts[i+1]
                elememts[i+1] = tmp
                swapped = True
        if not swapped:
            break
if __name__ == "__main__":
     elememts = [5,9,2,1,67,34,88,34]
     bubble_sort(elements=elememts)
     print(elememts)#op - [1, 2, 5, 9, 34, 34, 67, 88]