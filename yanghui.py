

def yanghui(m, n):
    # preprocess m, n
    m = int(m)
    n = int(n)
    # validate n
    if n > m or m < 0 or n < 0:
        return "Invalid query"
    # first and last
    if n == 0 or n == m:
        return 1
    return yanghui(m - 1, n - 1) + yanghui(m - 1, n)


def generate_yh(m):
    for row in range(m + 1):
        for col in range(row + 1):
            print(yanghui(row, col), end="\t")
        print ("\n")


generate_yh(5)
