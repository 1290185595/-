if __name__ == "__main__":
    print("Part2.Chapter1")
    from Part2.Chapter1 import *

    for sort in [insertion_sort, merge_sort, heap_sort, quick_sort, randomized_quick_sort]:
        A = [12, 3, 41, 44, 12, 4, 14, 123]
        sort(A)
        print(A, "by", sort.__name__)

if __name__ == "__main__":
    print("Part2.Chapter2")
    from Part2.Chapter2 import *

    A = [12, 3, 41, 44, 12, 4, 14, 123]
    print(counting_sort(A), "by", counting_sort.__name__)
    A = [0.13, 0.456, 0.3, 0.567, 0.14, 0.012]
    print(bucket_sort(A), "by", bucket_sort.__name__)

if __name__ == "__main__":
    print("Part2.Chapter3")
    from Part2.Chapter3 import *

    A = [12, 3, 41, 44, 12, 4, 14, 123]
    print(randomized_select(A, 5), "by", randomized_select.__name__)
    print(bfptr_select(A, 5), "by", bfptr_select.__name__)

