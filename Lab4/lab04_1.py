list = [3, 4 , 2, 1, 9]

def count_sqrts(list):
    counts = {}
    for num in list:
        sqrt_num = num ** 0.5
        if sqrt_num.is_integer():
            sqrt_int = int(sqrt_num)
            counts[sqrt_int] = counts.get(sqrt_int, 0) + 1
    return counts

