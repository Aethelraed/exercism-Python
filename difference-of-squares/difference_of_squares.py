square_of_sum = lambda number: (number * (number + 1) / 2) ** 2  # Carl Friedrich Gauß


sum_of_squares = lambda number: sum(i**2 for i in range(number + 1))


difference_of_squares = lambda number: square_of_sum(number) - sum_of_squares(number)
