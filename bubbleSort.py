# write your bubble sort algorithm below
def bubble_sort(lst):
    for i in range(len(lst) - 1):
        swapped = False
        print(f"iteration: {i}")
        for j in range(len(lst) - 1):
            print(f"comparing: {lst[j]} and {lst[j + 1]}", end=" ")
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print("- swapped")
                swapped = True
            else:
                print("- not swapped")
        if not swapped:
            break
        
    return lst

if __name__ == "__main__":
    # Test your bubble sort algorithm above with the list below
    lst = [5, 4, 3, 2, 1]
    print(bubble_sort(lst))
    print("_" * 40)

    sample_list = [1, 5, 2, 6, 7]
    print(f"Unsorted list: {sample_list}")
    bubble_sort(sample_list)
    print(f"Sorted list: {sample_list}")
