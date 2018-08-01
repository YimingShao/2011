class api:

    # Given an array A of n integers, sort them by repetively selecting the smallest among
    # the yet unselected integers.
    def Selection_Sort(ary):
        n = len(ary)
        for i in range(n):
            min = i
            for j in range(i + 1, n):
                if ary[min] > ary[j]:
                    min = j
            if min != i:
                ary[min], ary[i] = ary[i], ary[min]
        return ary


    def Bubble_Sort(ary):
        for i in range(len(ary)-1):
            if ary[i] > ary[i+1]:
                ary[i],ary[i+1] = ary[i+1], ary[i]
        return ary
