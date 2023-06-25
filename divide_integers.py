def solution(dividend, divisor):


    count = 0
    sign = 1
    if (dividend < 0 and divisor < 0):
        sign = sign + 0
    if (dividend < 0 or divisor < 0):
        sign = -1
    if dividend >= 2 ** 31 - 1  and divisor == 1:
        return 2 ** 31 - 1
    if dividend >= 2 ** 31 - 1  and divisor == -1:
        return -1 * 2 ** 31
    if dividend <= -1 * 2 ** 31  and divisor == 1:
        return -1 * 2 ** 31
    if dividend <= -1 * 2 ** 31  and divisor == -1:
        return 2 ** 31 - 1
    numerator = abs(dividend)
    divider = abs(divisor)


    while numerator >= 0:
        print(numerator, count, divider)
        numerator = numerator - divider
        count = count + 1
    count = count - 1
    count = count * sign
    if count > (2 ** 31 - 1):
        return 2 ** 31 - 1
    if count < (-1 * 2 ** 31):
        return -1 * 2 ** 31
    return count

print(solution(2147483648,2))
