from api import api

def main():

    num_ary = [5, 2, 2, 4, 8, 9, 3, 0, 3, 11, 23, 16, 4]
    new_ary = api.Selection_Sort(num_ary)
    print(new_ary)

    new_ary = api.Bubble_Sort(num_ary)
    print(new_ary)

if __name__ == '__main__':
    main()