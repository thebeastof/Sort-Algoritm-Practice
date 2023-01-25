import sys

def main(algorithm, string_list):
    # convert every list item to int type
    unsorted_list = validate_list(string_list)
    
    if not unsorted_list:
        return
    if algorithm == "bubble":
        bubble_sort(unsorted_list)
        print(unsorted_list)
    elif algorithm == "selection":
        selection_sort(unsorted_list)
    elif algorithm == "insertion":
        insertion_sort(unsorted_list)
    else:
        print(f"can't sort using {algorithm}")

def validate_list(l):
    try:
        return [int(i) for i in l]
    except ValueError:
        print("list contains non-int element")
        return None

def bubble_sort(unsorted_list):
    length = len(unsorted_list) - 1
    sorted = False
    while sorted != True:
        sorted = True
        for num in range(0, length):
            if unsorted_list[num] > unsorted_list[num + 1]:
                sorted = False
                unsorted_list[num], unsorted_list[num + 1] = unsorted_list[num + 1], unsorted_list[num]
    
    return unsorted_list

def selection_sort(l):
    # your code here
    print(l)

def insertion_sort(l):
    # your code here
    print(l)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        # separate the algorithm name from the list elements
        main(sys.argv[1], sys.argv[2:])
    else:
        print("usage: sorter.py algorithm_name elem0 elem1 elem2...")