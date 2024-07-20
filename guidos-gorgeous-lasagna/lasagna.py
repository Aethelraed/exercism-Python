"""
Calc various times related to cooking lasagne
"""

EXPECTED_BAKE_TIME = 40  # 40 minutes


def bake_time_remaining(time_in_oven):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - time_in_oven


def preparation_time_in_minutes(numbers_of_layers=1):
    """Calc elapsed cooking time.

    :param number_of_layers: int how many layers of lasagne have been prepared
    :parm elapsed_bake_time: int how long the lasagne has been cooking
    :return: int sum of ccoking and preperation time

    This function takes two integers representing the number of lasagna layers      and the time already spent baking and calculates the total elapsed
    minutes        spent cooking the lasagna.

    """
    return 2 * numbers_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calc elapsed cooking time.

    :param number_of_layers: int how many layers of lasagne have been prepared
    :parm elapsed_bake_time: int how long the lasagne has been cooking
    :return: int sum of ccoking and preperation time

    This function takes two integers representing the number of lasagna layers        and the time already spent baking and calculates the total elapsed minutes        spent cooking the lasagna.

    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
