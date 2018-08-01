class api:

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


    def Insertion_Sort(my_ary):
        ary = my_ary[:]
        for i in range(1, len(ary)):
            key = ary[i]
            j=i-1
            while j >=0 and key < ary[j]:
                ary[j+1] = ary[j]
                j = j-1
            ary[j+1] = key
        return ary

