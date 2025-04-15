def collatz(i):

    ncount=0
    while i!=1:
        if i % 2 == 1:
            i = 3 * i + 1
        else:
            i = i / 2
        ncount=ncount+1
    return ncount

def find_max(lst):
    if not lst:
        return None  # 빈 리스트일 경우 처리
    max_value = lst[0]
    for num in lst[1:]:
        if num > max_value:
            max_value = num
    return max_value

def top_collatz_counts(limit=101):
    max1_value = max1_n = 0
    max2_value = max2_n = 0
    max3_value = max3_n = 0

    for n in range(1, limit):
        count = 0
        i = n
        while i != 1:
            if i % 2 == 1:
                i = 3 * i + 1
            else:
                i = i / 2
            count += 1

        if count > max1_value:
            max3_value, max3_n = max2_value, max2_n
            max2_value, max2_n = max1_value, max1_n
            max1_value, max1_n = count, n
        elif count > max2_value:
            max3_value, max3_n = max2_value, max2_n
            max2_value, max2_n = count, n
        elif count > max3_value:
            max3_value, max3_n = count, n

    return {
        '1st': (max1_n, max1_value),
        '2nd': (max2_n, max2_value),
        '3rd': (max3_n, max3_value)
    }

def second_largest(lst):
    unique = list(set(lst))  # 중복 제거
    if len(unique) < 2:
        return None  # 두 번째로 큰 수가 없음
    unique.sort(reverse=True)
    return unique[1]