def merge_sort(arr):

    if len(arr) == 1:
        return arr

    middle = len(arr)//2
    a = arr[:middle]
    b = arr[middle:]

    if middle == 0:
        return "theres nothing here..."

    a = merge_sort(a)
    b = merge_sort(b)
    return merge(a, b)

def merge(a, b):
    c = []
    while a and b:
        if(a[0]>b[0]):
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))

    while a:
        c.append(a.pop(0))

    while b:
        c.append(b.pop(0))

    return c


