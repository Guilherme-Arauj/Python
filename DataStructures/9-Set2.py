def compare_lists(initial_list, modified_list):
    initial_set = set(initial_list)
    modified_set = set(modified_list)

    unchanged = initial_set.intersection(modified_set)
    new_elements = modified_set - initial_set
    removed_elements = initial_set - modified_set

    print("Unchanged elements:", unchanged)
    print("New elements:", new_elements)
    print("Removed elements:", removed_elements)

initial_list = [1, 2, 3, 4, 5]
modified_list = [3, 4, 5, 6, 7]

compare_lists(initial_list, modified_list)
