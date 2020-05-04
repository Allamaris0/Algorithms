def is_prime_fast(number):
    """ Instead of testing all numbers up to n − 1,
        just check divisibility of n by numbers less than or equal to the root of n """

    if number<2:
        return False
    elif number == 2:
        return True
    else:
        n=number//number**0.5
        for factor in range(2,int(n)+1):
            if number % factor == 0:
                return False
        return True