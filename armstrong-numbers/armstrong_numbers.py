def is_armstrong_number(number):
    h_sum = 0
    for i in str(number):
        h_sum = h_sum + int(i) ** len(str(number))
    return number == h_sum
