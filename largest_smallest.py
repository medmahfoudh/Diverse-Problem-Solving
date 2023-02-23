def find_largest_and_smallest(numbers):
    if not numbers:
        return "The list is empty."
    else:
        smallest = largest = numbers[0] #3 , 8 , 9 , 190 , 283 , 1 , -2
        for number in numbers:
            if number < smallest:
                smallest = number
            if number > largest:
                largest = number
        return f"The largest number is {largest} and the smallest number is {smallest}."



numbers = [3 , 8 , 9 , 190 , 283 , 1 , -2] 
print(find_largest_and_smallest(numbers)) 