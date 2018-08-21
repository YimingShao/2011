from heapq import *


class Pair:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end
# Given an array A of n integers, sort them by repetively selecting the smallest among
# the yet unselected integers.


def Selection_Sort(my_ary):
    ary = my_ary[:]
    n = len(ary)
    for i in range(n):
        # Initialize the minimum to the first element
        min = i
        for j in range(i + 1, n):
            if ary[min] > ary[j]:

                # Find the new minimum
                min = j

        # Do swap only if the min is modified during the iteration
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


def Insertion_Sort(my_arr):
    ary = my_arr[:]
    for i in range(1, len(ary)):
        key = ary[i]
        j = i - 1
        while j >= 0 and key < ary[j]:
            ary[j + 1] = ary[j]
            j -= 1
        ary[j + 1] = key
    return ary


def Merge_Sort(my_ary):
    ary = my_ary[:]
    return merge_function(ary)

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
        L = merge_function(ary[:mid])
        R = merge_function(ary[mid:])
        return merge(L,R)
    return ary




def Heap_Sort(my_ary):
    ary = []
    for x in my_ary:
        heappush(ary, x)
    return [heappop(ary) for i in range(len(ary))]

def draw(ary,step, sign=True):
    if sign:
        print('Step {}: '.format(step))
        for x in ary:
            print(x*'||')
        print('-'*50)
        print('')
    return




def Quick_Sort(my_ary):

    ary = my_ary[:]

    # From the beginning to the end of the ary
    Quick_Sort_algrithm(ary, 0, len(ary)-1)
    return ary

def Quick_Sort_algrithm(ary, low, high):

    if low < high:

        pivot = Partition(ary, low ,high)
        print(low, high, pivot)
        # Sort the left hand side
        Quick_Sort_algrithm(ary, low, pivot-1)
        # Sort the right hand side
        Quick_Sort_algrithm(ary, pivot+1, high)


def Partition(ary, low, high):
    i = low - 1

    # pivot here we set to the last element of the ary
    pivot = ary[high]

    # Read through the ary, swap the position of elements that are less than equal to the pivot.
    for j in range(low, high):
        if ary[j] <= pivot:

            i += 1
            ary[i], ary[j] = ary[j], ary[i]

    # Put pivot at the back of the elements that they are less than equal to the pivot.
    ary[i+1], ary[high] = ary[high], ary[i+1]

    # Return the index of the previous pivot,
    # all elements in front of the pivot is less than equal to it, vice versa
    return (i+1)


def Non_recursive_Stack_Quick_Sort(my_ary):
    stack = []
    ary = my_ary[:]

    start = 0
    end = len(my_ary)-1

    stack.append(Pair(start, end))

    while len(stack):
        start = stack[len(stack)-1].getStart()
        end =stack[len(stack)-1].getEnd()

        stack.pop()

        pivot = Partition(ary, start, end)

        if pivot - 1 > start:
            stack.append(Pair(start, pivot - 1))
        if pivot + 1 < end:
            stack.append(Pair(pivot+1, end))

    return ary





def counting_sort(my_ary, max):
    max +=1
    ary = my_ary[:]
    count_ary = max*[0]

    for e in ary:
        count_ary[e]+=1

    print(count_ary)
    for i in range(1, max):
        count_ary[i] += count_ary[i-1]
    print(count_ary)

    for e in my_ary:
        ary[count_ary[e]-1] = e
        count_ary[e]-=1
    return ary
















