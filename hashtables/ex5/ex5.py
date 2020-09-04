# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    qu = {}
    result = []
    for q in queries:
        qu[q] = q

    for f in files:
        length = len(q)
        if f[-length:] in qu:
            result.append(f)
        length = len(q) - 1
        if f[-length:] in qu:
            result.append(f)
    print(sorted(result))
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
