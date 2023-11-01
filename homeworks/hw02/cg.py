from ucb import trace

@trace
def count_partitions(n,m):
    """ 分割数。
    >>> count_partitions(3,2)
    # 1 + 2 = 3
    # 1 + 1 + 1 = 3
    >>> 2
    """
    if n == 0:
        return 1
    if n < 0 :
        return 0
    if m == 0:
        return 0
    with_m = count_partitions(n-m,m)
    without_m = count_partitions(n,m-1)
    return with_m + without_m
