def coefficient(n, k) :

    res = 1

    if (k > n - k) :

        k = n - k

    for i in range(0 , k) :

        res = res * (n - i)

        res = res // (i + 1)

        list_of_lists.append(res)

    return res

list_of_lists = []

def pascal_triangle(n) :

    for line in range(0, n) :

        for i in range(0, line + 1) :

            print(coefficient(line, i)," ", end = "")

        print()
    return list_of_lists

pascal_triangle(5)
