def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    negs = {}
    result = []
    for i in range(len(a)):
        if a[i] < 0:
            negs[a[i]] = i
        # while a[i] < 0:
        #     a.remove(a[i])
    for i in range(len(a)):
        for j in negs:
            if a[i] + j == 0:
                result.append(a[i])
        # if a[i] plus negs[counterpart] is zero, append a[i] to result
        
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
