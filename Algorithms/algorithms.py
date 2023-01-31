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
        print(unsorted_list)
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
    # Iterates through array and compares element it is at with element to the right
    # If element on left is greater than on right, the two switch
    # Process is repeated until array is sorted

    length = len(unsorted_list) - 1
    sorted = False

    while sorted == False:
        sorted = True
        for num in range(0, length):
            if unsorted_list[num] > unsorted_list[num + 1]:
                sorted = False
                unsorted_list[num], unsorted_list[num + 1] = unsorted_list[num + 1], unsorted_list[num]
    
    return unsorted_list

def selection_sort(unsorted_list):
    # Iterates through array and compares every element to minimum value (first element)
    # If an element is less than minimum, minimum = that element
    # When array has been iterated through, final minimum value is replaced with first element
    # Process is repeated until array is sorted

    minimum = unsorted_list[0]
    length = len(unsorted_list) - 1

    for elem in range(0, length):
        minimum = elem
        for num in range(elem + 1, len(unsorted_list)):
            if unsorted_list[num] < unsorted_list[minimum]:
                minimum = num
        if minimum != elem:
            unsorted_list[minimum], unsorted_list[elem] = unsorted_list[elem], unsorted_list[minimum]

    return unsorted_list

def insertion_sort(unsorted_list):

    for i in range(1, len(unsorted_list)):
        num = unsorted_list[i]
        a = i-1
        while a >= 0 and num < unsorted_list[a]:
            unsorted_list[a + 1] = unsorted_list[j]
            a -= 1
        unsorted_list[a + 1] = num
        


if __name__ == '__main__':
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2:])
    else:
        print("usage: sorter.py algorithm_name elem0 elem1 elem2...")