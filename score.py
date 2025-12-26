import sys
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    name = sys.argv[1]
    array = [name] * 11
    print("Array:", array)
else:
    array = [1, 2, 3, 7, 10, 5]
    sum_of_elements = sum(array)
    avg_of_elements = sum_of_elements / len(array)
    print("Sum of elements:", sum_of_elements)