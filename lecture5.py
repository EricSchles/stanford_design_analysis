import random
def quicksort(alist):
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[random.randint(0,len(alist)-1)]
        less = []
        equal = []
        greater = []
        for i in alist:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                greater.append(i)
        return quicksort(less)+equal+quicksort(greater)

arr = [elem for elem in range(0,100)]
print(quicksort(arr))
