#Method 1 
def sort_stings1(strs):
    return sorted(strs)

#Method 2

def sort_strings2(strs):
    if len(strs) <= 1:
        return strs
    mid = len(strs) // 2
    left = sort_strings2(strs[:mid])
    right = sort_strings2(strs[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
