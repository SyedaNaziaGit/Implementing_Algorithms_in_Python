#insertion sort
def insertion_sort(elements):
    for i in range(len(elements)):
        curr_ele = elements[i]
        j = i -1
        while j>=0 and curr_ele<elements[j]:
            elements[j+1] = elements[j]
            j= j-1
        elements[j+1] = curr_ele
            
if __name__ == "__main__":
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)#op -[2, 7, 9, 11, 15, 28, 29]