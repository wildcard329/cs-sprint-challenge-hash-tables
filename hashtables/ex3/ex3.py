def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    lookup = {}
    result = []
    # add every number in first array to dict
    for arr in arrays:
        for num in arr:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1
            count = lookup.get(num)
            if count == len(arrays):
                result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    arrays.append([1,2,3])
    arrays.append([1,5,7])
    arrays.append([1,3,4])

    print(intersection(arrays))
