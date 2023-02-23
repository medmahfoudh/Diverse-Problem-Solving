def find_pair(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [numbers[i], numbers[j]]
    return "No such pair exists."

numbers = [2, 7, 11, 15]
target = 9
result = find_pair(numbers, target)
print(result)  #  [2, 7]
