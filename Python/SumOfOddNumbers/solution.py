#my solution

def row_sum_odd_numbers(n):
    lst = []
    for i in range(n*(n-1), n * (n + 2)):
        if len(lst) < n and i % 2 != 0 :
            lst.append(i)
    return sum(lst)

row_sum_odd_numbers(3)

#actual solution
def row_sum_odd_numbers(n):
    return n ** 3