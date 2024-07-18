def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1: raise ValueError("Classification is only possible for positive integers.")
    def alsum(x, reg=[1]):
        for i in range(2,x//2+1): 
            if x%i ==0: reg=reg+[i]            
        return sum(reg)
    if alsum(number)< number or number ==1 : return "deficient"
    return ["abundant","perfect"][alsum(number)== number]