#http://web.stanford.edu/class/cs161/

import math

def mergesort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A)//2
        return merge(mergesort(A[:mid]),mergesort(A[mid:]))

def merge(left,right):
    left_p,right_p = 0,0
    merged = []
    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            merged.append(left[left_p])
            left_p += 1
        else:
            merged.append(right[right_p])
            right_p += 1
    while left_p < len(left):
        merged.append(left[left_p])
        left_p += 1
    while right_p < len(right):
        merged.append(right[right_p])
        right_p += 1
    return merged

def brute_force_median(A):
    sorted_list = mergesort(A)
    mid = math.ceil(len(A)/2)
    return sorted_list[mid]

def median_of_medians(A,k):
    n = len(A)
    if n == 1:
        return A[0]
    groups = []
    groupings = [elem for elem in range(0,n,5)]
    groupings.remove(0)
    if groupings == []:
        groups = [A]
    else:
        for grouping in groupings:
            groups.append([A[elem] for elem in range(grouping)])
        if groupings[-1] % 5 != 0:
            groups.append([A[elem] for elem in range(groupings[-1],n)])
    medians = []
    for group in groups:
        medians.append(brute_force_median(group))
    q = median_of_medians(medians,math.ceil(len(groups)/2))
    left = [i for i in A if i < q]
    right = [i for i in A if i > q]
    if k <= len(left):
        return median_of_medians(left,k)
    elif k == len(left) +1:
        return q
    else:
        return median_of_medians(right,k-(len(left)+1))
    
print(median_of_medians([5,8,7,2,1,27,11,42,17],5))
