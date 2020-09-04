def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    indexer = {}
    for item in range(len(weights)):
        indexer[weights[item]] = item
    print(indexer)

    for item in range(len(weights)):
        for weight in indexer:
            if length == 1:
                return None
            elif length == 2:
                if weights[0] == weights[1] and weights[0] + weights[1] == limit:
                    print((item+1,item))
                    return ((item+1, item))
                else:
                    return None
            else:
                target = limit - weights[item]
                if target in indexer:
                    print(target)
                    w = indexer.get(target)
                    print((w, item))
                    if w > item:
                        return (w, item)
                    else:
                        return(item, w)

get_indices_of_item_weights([2], 1, 5)
get_indices_of_item_weights([1], 1, 1)
get_indices_of_item_weights([2, 2], 2, 4)
get_indices_of_item_weights([2, 3], 2, 4)
get_indices_of_item_weights([2, 3, 6, 9], 4, 8)
get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)
get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7)