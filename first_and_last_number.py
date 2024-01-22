# Check if the first and last number of a list is the same


# Function
def same_first_and_last_number(input_list):
    print("Given list:", input_list)
    first_num, last_num = input_list[0], input_list[-1]
    return first_num == last_num

numbers_one = [1, 2, 3, 4, 5]
print("Result is", same_first_and_last_number(numbers_one))

numbers_two = [6, 7, 8, 9, 6]
print("Result is", same_first_and_last_number(numbers_two))