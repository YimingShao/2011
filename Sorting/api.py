# Given an array A of n integers, sort them by repetively selecting the smallest among
# the yet unselected integers.
def Selection_Sort(my_ary):
    ary = my_ary[:]
    n = len(ary)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if ary[min] > ary[j]:
                min = j
        if min != i:
            ary[min], ary[i] = ary[i], ary[min]
    return ary

# Bubble sort is pretty slow, we don't want to use this algorithm in real problem
def Bubble_Sort(my_ary):
    ary = my_ary[:]
    for i in range(len(ary)):
        for j in range(0, len(ary)-i-1):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]
    return ary


def merge(L, R):
    res = []
    while L and R:
        if L[0] < R[0]:
            res.append(L.pop(0))
        else:
            res.append(R.pop(0))
    while L:
        res.append(L.pop(0))
    while R:
        res.append(R.pop(0))
    return res


def merge_function(ary):
    if len(ary) > 1:
        mid = (int)(len(ary)/2)
        L = mergesort(ary[:mid])
        R = mergesort(ary[mid:])
        return merge(L,R)
    return ary

def mergesort(my_ary):
    ary = my_ary[:]
    return merge_function(ary)
