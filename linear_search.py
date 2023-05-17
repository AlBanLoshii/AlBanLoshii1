def linear_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1

# Prompt the user to enter a list of elements
input_list = input("Enter a list of elements separated by spaces: ")
elements = input_list.split()

# Prompt the user to enter the target element
target_element = input("Enter the target element to search: ")

# Perform linear search
result_index = linear_search(elements, target_element)

# Display the result
if result_index != -1:
    print(f"The target element {target_element} is found at index {result_index}.")
else:
    print(f"The target element {target_element} is not found in the list.")
