def do(arr):
    m = {}
    for elem in range(1, len(arr)):
        m[arr[elem]['abbr']] = arr[elem]['name']
    return m
