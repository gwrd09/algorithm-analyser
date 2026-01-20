from algorithms import insertion_sort, bubble_sort, merge_sort
from measure import generate_unsorted_list, timer, graph_efficiency

def main():
    element_count = [100, 250, 500, 1000, 5000, 10000]
    unsorted_lists = []

    insertion_times = []
    bubble_times = []
    merge_times = []
    for i in range(len(element_count)):
        unsorted_lists.append(generate_unsorted_list(element_count[i]))
        unsorted_insertion = unsorted_lists.copy()
        unsorted_bubble = unsorted_lists.copy()
        unsorted_merge = unsorted_lists.copy()

        insertion_sort_result, insertion_elapsed = timer(insertion_sort, unsorted_insertion[i])
        insertion_times.append(insertion_elapsed)

        bubble_sort_result, bubble_elapsed = timer(bubble_sort, unsorted_bubble[i])
        bubble_times.append(bubble_elapsed)

        merge_sort_result, merge_elapsed = timer(merge_sort, unsorted_merge[i])
        merge_times.append(merge_elapsed)

    graph_efficiency(element_count, insertion_times=insertion_times, bubble_times=bubble_times, merge_times=merge_times)

if __name__ == "__main__":
    main()